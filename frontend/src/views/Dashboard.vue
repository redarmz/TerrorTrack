<template>
  <div class="container py-5">

    <!-- 🎯 INTRODUCTION -->
    <div class="intro-block">
      <h2 class="highlighted-title">📌 BIENVENUE SUR LE TABLEAU DE BORD TERRORTRACK</h2>
      <p class="intro-text">
        Explorez des statistiques interactives sur les attaques terroristes à travers le monde.
        Grâce aux graphiques ci-dessous, identifiez les tendances, les régions les plus affectées,
        les types d’attaques utilisés, les groupes responsables et bien plus encore.
      </p>
    </div>

    <h1 class="title">📊 Dashboard TerrorTrack</h1>
    <p class="intro">Visualisations interactives sur les attaques terroristes à travers le monde.</p>

    <!-- Graphique 1 -->
    <div class="graph-section">
      <h2>1. Évolution annuelle du nombre d’attaques</h2>
      <div class="iframe-wrapper">
        <iframe src="/plotly/graph_1.html" width="100%" height="600" frameborder="0"></iframe>
      </div>
      <div class="analysis-box">
        <h3>Analyse</h3>
        <p>Ceci est le commentaire pour le graphique 1. Tu pourras parler ici de la hausse ou baisse des attaques dans le temps.</p>
      </div>
    </div>

    <!-- Graphique 2 -->
    <div class="graph-section">
      <h2>2. Répartition des attaques par type (avec slider)</h2>
      <div class="iframe-wrapper">
        <iframe src="/plotly/graph_2.html" width="100%" height="600" frameborder="0"></iframe>
      </div>
      <div class="analysis-box">
        <h3>Analyse</h3>
        <p>Ici, tu peux décrire les types d’attaques les plus fréquents ou leur évolution au fil des années.</p>
      </div>
    </div>

    <!-- Graphique 3 -->
    <div class="graph-section">
      <h2>3. Cartographie des attaques par région</h2>
      <div class="iframe-wrapper">
        <iframe src="/plotly/graph_3.html" width="100%" height="600" frameborder="0"></iframe>
      </div>
      <div class="analysis-box">
        <h3>Analyse</h3>
        <p>Analyse ici la concentration des attaques dans certaines régions du monde, avec un focus géographique.</p>
      </div>
    </div>

    <!-- Graphique 4 -->
    <div class="graph-section">
      <h2>4. Types d’attaques selon les régions</h2>
      <div class="iframe-wrapper">
        <iframe src="/plotly/graph_4.html" width="100%" height="600" frameborder="0"></iframe>
      </div>
      <div class="analysis-box">
        <h3>Analyse</h3>
        <p>Ce graphe te permet d'expliquer les différences régionales dans les types d’attaques utilisés.</p>
      </div>
    </div>

    <!-- Graphique 5 -->
    <div class="graph-section">
      <h2>5. Groupes terroristes les plus actifs (liste déroulante)</h2>
      <div class="iframe-wrapper">
        <iframe src="/plotly/graph_5.html" width="100%" height="600" frameborder="0"></iframe>
      </div>
      <div class="analysis-box">
        <h3>Analyse</h3>
        <p>Ici tu peux parler des groupes responsables des attaques, leur récurrence, et leur répartition géographique.</p>
      </div>
    </div>

    <!-- Graphique 6 -->
    <div class="graph-section">
      <h2>6. Carte des pays les plus touchés</h2>
      <div class="iframe-wrapper">
        <iframe src="/plotly/graph_6.html" width="100%" height="600" frameborder="0"></iframe>
      </div>
      <div class="analysis-box">
        <h3>Analyse</h3>
        <p>Commenter ici les pays les plus touchés par les attaques : pourquoi eux ? Conflits ? Instabilité ?</p>
      </div>
    </div>

    <!-- Graphique 7 -->
    <div class="graph-section">
      <h2>7. Chronologie des groupes actifs par pays</h2>
      <div class="iframe-wrapper">
        <iframe src="/plotly/graph_7.html" width="100%" height="600" frameborder="0"></iframe>
      </div>
      <div class="analysis-box">
        <h3>Analyse</h3>
        <p>Tu peux détailler ici les périodes d’activité des groupes et l’apparition de nouveaux acteurs.</p>
      </div>
    </div>

    <!-- Graphique 8 -->
    <div class="graph-section">
      <h2>8. Répartition des attaques par région (camembert)</h2>
      <div class="iframe-wrapper">
        <iframe src="/plotly/graph_8.html" width="100%" height="600" frameborder="0"></iframe>
      </div>
      <div class="analysis-box">
        <h3>Analyse</h3>
        <p>Une analyse globale des régions les plus impactées avec leur pourcentage du total.</p>
      </div>
    </div>

    <!-- Graphique 9 -->
    <div class="graph-section">
      <h2>9. Nombre de morts par type d’arme</h2>
      <div class="iframe-wrapper">
        <iframe src="/plotly/graph_9.html" width="100%" height="600" frameborder="0"></iframe>
      </div>
      <div class="analysis-box">
        <h3>Analyse</h3>
        <p>Quels types d’armes sont les plus meurtriers ? Ce graphique sert à répondre à cette question.</p>
      </div>
    </div>

    <!-- Graphique 10 -->
    <div class="graph-section">
      <h2>10. Timeline des attaques les plus meurtrières</h2>
      <div class="iframe-wrapper">
        <iframe src="/plotly/graph_10.html" width="100%" height="600" frameborder="0"></iframe>
      </div>
      <div class="analysis-box">
        <h3>Analyse</h3>
        <p>Analyse les pics de mortalité, les années marquantes et les pays associés aux pires événements.</p>
      </div>
    </div>

    <!-- 🧩 CONCLUSION -->
    <div class="intro-block mt-5">
      <h2 class="highlighted-title">🧠 CONCLUSION GÉNÉRALE</h2>
      <p class="intro-text">
        Cette analyse permet de mieux comprendre les dynamiques du terrorisme mondial.
        En combinant cartes, timelines, répartitions par type ou par groupe, nous avons construit une vision claire
        des phénomènes à travers le temps. Ce tableau de bord peut alimenter des réflexions stratégiques,
        scientifiques ou politiques.
      </p>
    </div>

  </div>

</template>

<script setup lang="ts">
// pas de logique JS ici pour le moment, on est full statique avec les iframes
</script>

<style scoped>
 
/* Pour que la container flotte au-dessus avec une ombre légère */
.container {
  background-color: #ffffff;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.04);
}

.container {
  max-width: 1200px;
  margin: auto;
  padding: 2rem;
}
.title {
  font-size: 2.5rem;
  text-align: center;
  margin-bottom: 0.5rem;
}
.intro {
  text-align: center;
  font-size: 1.1rem;
  margin-bottom: 2rem;
  color: #555;
}
.graph-section {
  background-color: #ffffff;
  padding: 2rem;
  margin-bottom: 3rem;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.graph-section h2 {
  font-size: 1.4rem;
  margin-bottom: 1rem;
}
.iframe-wrapper {
  border-radius: 6px;
  overflow: hidden;
}
.analysis-box {
  margin-top: 1.5rem;
  background-color: rgba(216, 148, 148, 0.302);
  border-left: 4px solid #076aff;
  padding: 1rem 1.5rem;
  border-radius: 6px;
}
.analysis-box h3 {
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
  color: #333;
}
.analysis-box p {
  font-size: 0.95rem;
  color: #444;
}
.intro-block {
  background-color: #ffffff;
  padding: 2rem;
  margin-bottom: 3rem;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.06);
  text-align: center;
}
.highlighted-title {
  font-weight: bold;
  color: #e0a800;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}
.intro-text {
  font-size: 1rem;
  color: #444;
  line-height: 1.6;
}
</style>
