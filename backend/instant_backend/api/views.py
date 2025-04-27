from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import joblib
import os
import numpy as np
import pandas as pd

# Chemins
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "modeles", "modele6_mlp_plus.pkl")
columns_path = os.path.join(BASE_DIR, "modeles", "model_rf_columns.pkl")
kmeans_path = os.path.join(BASE_DIR, "modeles", "kmeans.pkl")
pca_path = os.path.join(BASE_DIR, "modeles", "pca.pkl")

# Chargements
model = joblib.load(model_path)
expected_columns = joblib.load(columns_path)
kmeans = joblib.load(kmeans_path)
pca = joblib.load(pca_path)

def test_api(request):
    return JsonResponse({"status": "ok"})

@csrf_exempt
def predict_risk(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            en_guerre = float(data.get("en_guerre", 0.5))
            groupes = float(data.get("groupes_active", 0.5))
            est_democratie = float(data.get("est_democratie", 0.5))
            revenu_faible = float(data.get("revenu_faible", 0.5))
            instabilite = float(data.get("indice_instabilite", 0.5))
            region = data.get("region_txt", "Other")
            pays = data.get("country_txt", "Autres")
            cible = data.get("targtype1_txt", "Civils")

            # Simplification du pays
            top_pays = ['Afghanistan', 'Iraq', 'Pakistan', 'India', 'United States', 'Somalia', 'Nigeria', 'Israel', 'Yemen', 'Philippines']
            pays_simplifie = pays if pays in top_pays else "Autres"

            # Préparation du row
            row = {
                "indice_instabilite": instabilite,
                "revenu_faible": revenu_faible,
                "est_democratie": est_democratie,
            }

            # Ajout des colonnes encodées
            for col in expected_columns:
                if col.startswith("region_txt_"):
                    row[col] = 1 if col == f"region_txt_{region}" else 0
                elif col.startswith("pays_simplifie_"):
                    row[col] = 1 if col == f"pays_simplifie_{pays_simplifie}" else 0
                elif col.startswith("targtype1_txt_"):
                    row[col] = 1 if col == f"targtype1_txt_{cible}" else 0

            # Construction DataFrame
            df_pred = pd.DataFrame([row])

            # Réarrangement pour KMeans : uniquement jusqu'à 'indice_instabilite'
            base_cols = [c for c in expected_columns if c not in ["cluster", "pca_1", "pca_2"]]
            X_for_kmeans = df_pred[base_cols].values

            # Ajout du cluster
            cluster = kmeans.predict(X_for_kmeans)
            df_pred["cluster"] = cluster

            # Application PCA
            pca_input = np.concatenate([X_for_kmeans, cluster.reshape(-1, 1)], axis=1)
            pca_features = pca.transform(pca_input)
            df_pred["pca_1"] = pca_features[:, 0]
            df_pred["pca_2"] = pca_features[:, 1]

            # Prédiction
            df_pred = df_pred[expected_columns]
            prob = model.predict_proba(df_pred)[0, 1]
            classe = model.predict(df_pred)[0]

            return JsonResponse({
                "prediction": int(classe),
                "probabilite": round(prob, 3)
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Méthode non autorisée"}, status=405)
