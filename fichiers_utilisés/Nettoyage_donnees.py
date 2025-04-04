import pandas as pd

# Spécifier le chemin du fichier
file_path = r"C:\Users\redar\Desktop\Script Python TT\donnees\globalterrorismdb_0718dist.csv"

# Charger le fichier CSV
df = pd.read_csv(file_path, encoding='latin1', sep=None, engine='python')  # Modifier le séparateur si nécessaire

# Colonnes à conserver même avec plus de 100 000 lignes vides
colonnes_a_conserver = ['nperps', 'claimed']

# Vérifier les colonnes et supprimer celles qui ont plus de 100 000 lignes vides (sauf les colonnes spécifiées)
colonnes_a_supprimer = [
    col for col in df.columns 
    if col not in colonnes_a_conserver and df[col].isna().sum() > 100000
]
df = df.drop(columns=colonnes_a_supprimer)

# Traitement des colonnes spécifiques

# 1. Supprimer les lignes avec un mois égal à 0 dans la colonne 'imonth'
df = df[df['imonth'] != 0]

# 2. Supprimer les lignes avec un jour égal à 0 dans la colonne 'iday'
df = df[df['iday'] != 0]

# 3. Supprimer les lignes avec une année inférieure à 1990
df = df[df['iyear'] >= 1990]

# 4. Supprimer les lignes vides dans les colonnes 'attacktype1', 'attacktype1_txt', 'targtype1', 'targtype1_txt'
colonnes_a_nettoyer = ['attacktype1', 'attacktype1_txt', 'targtype1', 'targtype1_txt']
for col in colonnes_a_nettoyer:
    df = df[~df[col].isna()]

# 5. Supprimer les colonnes inutiles : INT_LOG, INT_IDEO, INT_MISC, INT_ANY, crit1, crit2, crit3
colonnes_a_supprimer = ['INT_LOG', 'INT_IDEO', 'INT_MISC', 'INT_ANY', 'crit1', 'crit2', 'crit3']
df = df.drop(columns=[col for col in colonnes_a_supprimer if col in df.columns])

# 6. Remplacer les valeurs négatives et vides dans 'nperps' par -9
df['nperps'] = df['nperps'].apply(lambda x: -9 if pd.isna(x) or x < 0 else x)

# 7. Remplacer les valeurs vides dans 'claimed' par -9
df.loc[:, 'claimed'] = df['claimed'].fillna(-9)

# 8. Remplacer les valeurs vides dans 'weaptype1' par 13
df.loc[:, 'weaptype1'] = df['weaptype1'].fillna(13)


# 9. Remplacer les valeurs vides dans 'weaptype1_txt' par 'Unknown'
df.loc[:, 'weaptype1_txt'] = df['weaptype1_txt'].fillna('Unknown')

# Enregistrer le fichier Excel mis à jour
df.to_excel("fichier_filtre_et_nettoye.xlsx", index=False)

print("Nettoyage et traitement des colonnes terminé avec succès.")