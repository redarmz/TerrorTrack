<template>
    <div class="container py-5">
      <!-- Contexte -->
      <h2 class="section-title">Contexte</h2>
      <p>
        Dans un contexte où les actes de terrorisme représentent une menace mondiale croissante, l'analyse des données joue un rôle crucial pour mieux comprendre les tendances, les facteurs de risque et les modes opératoires des groupes terroristes.
        Grâce aux avancées technologiques et aux bases de données ouvertes, il est possible d’identifier des schémas, de prédire des menaces potentielles et d'améliorer les stratégies de prévention et de réponse aux attaques.
      </p>
  
      <!-- Objectifs -->
      <h2 class="section-title">Objectifs</h2>
      <ul>
        <li>Collecter, nettoyer et organiser les données issues de la Global Terrorism Database (GTD).</li>
        <li>Réaliser des analyses descriptives pour identifier les tendances temporelles et géographiques du terrorisme.</li>
        <li>Développer des modèles prédictifs pour anticiper les risques et mieux comprendre les modes opératoires des groupes terroristes.</li>
        <li>Fournir des visualisations interactives pour aider les analystes et décideurs à interpréter les données plus efficacement.</li>
      </ul>
  
      <!-- Solution -->
      <h2 class="section-title">Solution</h2>
      <p>
        Pour répondre aux problématiques et atteindre les objectifs fixés, le projet s’articule autour des étapes suivantes :
      </p>
      <ol>
        <li><strong>Exploration et préparation des données :</strong> Extraction, nettoyage et normalisation des informations pour garantir leur qualité et leur cohérence.</li>
        <li><strong>Analyse des données :</strong> Identification des tendances, des facteurs influents et des zones les plus touchées par le terrorisme.</li>
        <li><strong>Modélisation prédictive :</strong> Utilisation de techniques de machine learning pour anticiper les risques et évaluer les stratégies de lutte contre le terrorisme.</li>
        <li><strong>Interprétation des résultats :</strong> Production de rapports et visualisations pour une meilleure compréhension des données et une prise de décision éclairée.</li>
      </ol>
  
      <!-- Données Utilisées -->
      <h2 class="section-title">Données Utilisées</h2>
      <p>
        Les données utilisées pour ce projet proviennent de la Global Terrorism Database (GTD), une base de données publique qui recense plus de 180 000 attentats terroristes à travers le monde entre 1990 et 2017.
      </p>
      <ul>
        <li>📅 Dates et lieux des attentats</li>
        <li>🎯 Types d'attaques et cibles visées</li>
        <li>👥 Groupes terroristes impliqués</li>
        <li>🚨 Méthodes et armes utilisées</li>
        <li>📊 Nombre de victimes et dégâts matériels</li>
      </ul>
      <p>
        L’exploitation de ces données permet de mieux comprendre les tendances du terrorisme, d’identifier des **schémas récurrents** et d’élaborer des stratégies de prévention plus efficaces.
      </p>
      <p>
        🔗 En savoir plus sur la GTD : <a href="https://www.start.umd.edu/data-tools/GTD" target="_blank">Global Terrorism Database</a>
      </p>
    </div>
</template>
  
<script setup lang="ts">
</script>

<style scoped>
/* ---- Style des titres de sections ---- */
.section-title {
  font-size: 1.75rem;
  font-weight: bold;
  margin-top: 40px;
  margin-bottom: 20px;
  border-left: 4px solid #ff0707;
  padding-left: 10px;
  color: #042075;
}
</style>
