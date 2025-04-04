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
        <p>
  Ce graphique montre l'évolution annuelle du nombre d'attaques terroristes dans le monde. Après une hausse marquée entre 1989 et 1994 (environ 5 000 attaques), on observe une diminution progressive jusqu’à un creux en 2001. Ce point bas coïncide paradoxalement avec l’année des attentats du 11 septembre, qui ont marqué un tournant majeur dans la lutte antiterroriste mondiale. À partir de 2004, une reprise des violences est visible, culminant entre 2014 et 2015 avec plus de 10 000 attaques annuelles. Cette période correspond à l’expansion du groupe État Islamique (Daesh), qui a semé la terreur en Irak, en Syrie, et au-delà. L’attaque de la ville de Sinjar, le siège de Kobané, ou encore les attentats de Paris en 2015 ont marqué les mémoires. Depuis 2016, une légère décrue s’observe, mais le niveau reste élevé. Ce graphique ne se limite pas à des chiffres : il raconte une histoire d’instabilités, de conflits géopolitiques et de tragédies humaines.
</p>

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
       <p>
  Cette carte mondiale présente la répartition des attaques terroristes par type et par région. Chaque couleur représente une zone géographique, révélant des foyers intenses de violence. L’Asie du Sud (notamment l’Afghanistan et le Pakistan), le Moyen-Orient, l’Afrique du Nord et l’Afrique subsaharienne ressortent comme les zones les plus touchées. Cette densité reflète des contextes historiques lourds : guerres civiles, instabilités gouvernementales, présence de groupes djihadistes ou séparatistes. À titre d’exemple, la ville de Bagdad a connu des vagues successives d’attentats à la voiture piégée entre 2006 et 2010. Au Nigeria, Boko Haram a ravagé des villages entiers, comme lors de l’enlèvement de plus de 200 lycéennes à Chibok en 2014. Cette carte ne montre pas seulement où les attaques ont eu lieu, mais elle dessine une cartographie de la souffrance humaine, de la peur et de la résilience dans des territoires profondément marqués.
</p>

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
    <p>
  Cette carte en dégradé de rouge illustre le bilan humain des attaques terroristes, avec l’Irak en tête, dépassant les 50 000 morts. Ce pays a été le théâtre de conflits majeurs depuis 2003, avec l’invasion américaine, la guerre civile et la montée en puissance de Daesh. L’Afghanistan, deuxième sur la liste, porte également les stigmates de décennies de guerre, de l’intervention soviétique aux Talibans. Le Pakistan, la Syrie, le Nigeria ou encore l’Inde présentent aussi des bilans élevés. Ces chiffres rappellent que le terrorisme n’est pas seulement un enjeu sécuritaire : c’est une tragédie humaine. Dans les rues de Mossoul, des familles entières ont péri sous les bombes. À Kaboul, des écoliers ont été tués lors d'attentats ciblés. Cette carte est une carte du deuil, une mémoire visuelle des endroits où des vies ont été fauchées, souvent dans l’indifférence du monde.
</p>

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
<p>
  Ce graphique classe les types d’attaques terroristes selon leur fréquence. Les attentats à la bombe ou par explosion arrivent largement en tête, avec plus de 57 000 incidents. Ces méthodes sont souvent utilisées pour frapper des lieux publics, des marchés, ou des transports — des cibles symboliques et densément peuplées. Les assauts armés et les assassinats suivent, soulignant l’aspect ciblé de certaines opérations, notamment contre des figures politiques ou militaires. Le recours à l’enlèvement et aux attaques d’infrastructures traduit aussi une volonté de déstabiliser l’autorité et de semer le chaos. L’histoire récente regorge d’exemples marquants : l’attentat du métro de Madrid en 2004, les attaques coordonnées à Bombay en 2008, ou encore l’explosion meurtrière à Kaboul en 2017. Derrière chaque barre de ce graphique, ce sont des vies bouleversées, des familles détruites, et des sociétés entières plongées dans l’incertitude.
</p>

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
