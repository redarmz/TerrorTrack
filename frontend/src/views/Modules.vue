<template>
  <div class="container py-5">
    <h1 class="mb-4 text-center">
       Prédiction d’un attentat mortel
    </h1>

    <form @submit.prevent="lancerPrediction" class="bg-white shadow rounded p-4" style="max-width: 700px; margin: auto;">

      <!-- Pays -->
      <div class="mb-3">
        <label class="form-label">Pays</label>
        <input
          type="text"
          class="form-control"
          v-model="form.country_txt"
          placeholder="Commencez à taper un pays..."
          list="paysList"
        />
        <datalist id="paysList">
          <option v-for="p in allCountries" :key="p" :value="p">{{ p }}</option>
        </datalist>
      </div>

      <!-- Année -->
      <div class="mb-3">
        <label class="form-label">Année</label>
        <input type="number" class="form-control" v-model="form.iyear" placeholder="Ex: 2015" />
      </div>

      <!-- Région -->
      <div class="mb-3">
        <label class="form-label">Bloc géopolitique</label>
        <select v-model="form.region_txt" class="form-select">
          <option disabled value="">Sélectionnez une région</option>
          <option v-for="r in regionList" :key="r" :value="r">{{ r }}</option>
        </select>
      </div>

      <!-- Champs Oui / Non / Ne sais pas -->
      <div v-for="(label, field) in choixOuiNon" :key="field" class="mb-3">
        <label class="form-label">{{ label }}</label><br />
        <div class="form-check form-check-inline" v-for="(val, idx) in optionsOuiNon" :key="idx">
          <input class="form-check-input" type="radio" :name="field" :value="val.value" v-model="form[field]" />
          <label class="form-check-label">{{ val.label }}</label>
        </div>
      </div>

      <!-- Bouton -->
      <div class="text-center mt-4">
        <button type="submit" class="btn btn-primary px-4"> Lancer la prédiction</button>
      </div>
    </form>

    <div class="mt-5 text-center" v-if="result">
  <h4>Résultat :</h4>

  <!-- BARRE DE POURCENTAGE -->
  <div class="progress" style="height: 30px; max-width: 400px; margin: auto;">
    <div
      class="progress-bar"
      role="progressbar"
      :style="{ width: (result.probabilite * 100).toFixed(0) + '%'}"
      :class="result.prediction === 1 ? 'bg-danger' : 'bg-success'"
    >
      {{ (result.probabilite * 100).toFixed(2) }} %
    </div>
  </div>

  <p class="mt-3">
    <strong>Classe prédite :</strong>
    <span :class="result.prediction === 1 ? 'text-danger fw-bold' : 'text-success fw-bold'">
      {{ result.prediction === 1 ? 'Victimes probables' : 'Pas de victimes attendues' }}
    </span>
  </p>
</div>
  </div>
</template>

<script setup lang="ts">
//import { ref } from 'vue'
import axios from 'axios'
import { ref, onMounted } from 'vue'

onMounted(async () => {
  try {
    await axios.get("http://localhost:8000/api/test", { withCredentials: true });
    console.log("CSRF cookie récupéré ✅");
  } catch (err) {
    console.error("Erreur init CSRF :", err);
  }
});
// === Formulaire
const form = ref({
  country_txt: '',
  iyear: '',
  region_txt: '',
  en_guerre: null,
  groupes_active: null,
  est_democratie: null,
  revenu_faible: null,
})

// === Labels + options
const choixOuiNon = {
  en_guerre: 'En guerre actuellement ?',
  groupes_active: 'Groupes armés actifs ?',
  est_democratie: 'Pays démocratique ?',
  revenu_faible: 'Pays en développement ?',
}

const optionsOuiNon = [
  { label: 'Oui', value: 1 },
  { label: 'Non', value: 0 },
  { label: 'Je ne sais pas', value: null },
]

// === Pays
const allCountries = [
  "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan",
  "Bangladesh", "Belarus", "Belgium", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Bulgaria",
  "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia",
  "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Dominican Republic", "Ecuador", "Egypt",
  "El Salvador", "Eritrea", "Estonia", "Ethiopia", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana",
  "Greece", "Guatemala", "Guinea", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",
  "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
  "Lebanon", "Liberia", "Libya", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Mali", "Malta", "Mauritania",
  "Mauritius", "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nepal",
  "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "Norway", "Oman", "Pakistan", "Palestine",
  "Panama", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saudi Arabia",
  "Senegal", "Serbia", "Singapore", "Slovakia", "Slovenia", "Somalia", "South Africa", "South Korea", "Spain", "Sri Lanka",
  "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tunisia",
  "Turkey", "Turkmenistan", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan",
  "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

// === Régions
const regionList = [
  "Middle East & North Africa", "Western Europe", "Sub-Saharan Africa",
  "South Asia", "North America", "East Asia", "Southeast Asia",
  "Eastern Europe", "Central America & Caribbean", "Australasia & Oceania", "Central Asia", "Other"
]

// === Résultat
const result = ref(null)
function getCookie(name: string) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop()?.split(';').shift();
}


const lancerPrediction = async () => {
  try {
    const guerre = form.value.en_guerre ?? 0.5
    const groupes = form.value.groupes_active ?? 0.5
    const democratie = form.value.est_democratie ?? 0.5
    const revenu = form.value.revenu_faible ?? 0.5

    const instabilite = 0.4 * guerre + 0.4 * groupes + Math.random() * 0.2

    const payload = {
      country_txt: form.value.country_txt,
      iyear: form.value.iyear,
      region_txt: form.value.region_txt,
      en_guerre: guerre,
      groupes_active: groupes,
      est_democratie: democratie,
      revenu_faible: revenu,
      indice_instabilite: parseFloat(instabilite.toFixed(3))
    }

    const csrftoken = getCookie('csrftoken')
    const response = await axios.post('http://localhost:8000/api/predict/', payload, {
      headers: { 'X-CSRFToken': csrftoken },
      withCredentials: true
    })

    result.value = response.data

    // Réinitialiser le formulaire
    form.value = {
      country_txt: '',
      iyear: '',
      region_txt: '',
      en_guerre: null,
      groupes_active: null,
      est_democratie: null,
      revenu_faible: null
    }

  } catch (error) {
    console.error("Erreur lors de la prédiction :", error)
  }
}
</script>

<style scoped>
body, .form-label, input, select {
  font-family: 'Inter', sans-serif;
}
input[type="text"], input[type="number"], .form-select {
  font-size: 16px;
}
</style>
