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
    Ce graphique retrace l’évolution du nombre d’attaques terroristes enregistrées chaque année dans le monde, de 1990 à 2018. Il permet de visualiser les grandes dynamiques du terrorisme mondial à travers les décennies.
  </p>
  <p>
    On observe un premier pic dans les années 1990, atteignant environ 5 000 attaques, suivi d’une baisse importante vers l’an 2000. À partir de 2005, une hausse constante s’amorce, culminant en 2014-2015 avec plus de 10 000 attaques par an. Après cette période, une décroissance modérée est observable.
  </p>
  <p>
    Cette évolution peut s’expliquer par plusieurs facteurs : la fin de la Guerre froide a entraîné une reconfiguration des conflits, tandis que l’invasion de l’Irak en 2003 et le Printemps arabe en 2011 ont catalysé l’émergence de groupes extrémistes puissants tels que Daesh. Le pic de 2014-2015 coïncide avec l’établissement du pseudo-califat de Daesh et ses actions violentes en Irak, Syrie et au-delà.
  </p>
  <p>
    En 2015, la France est frappée de plein fouet par une série d’attentats coordonnés à Paris (Bataclan, Stade de France), illustrant la montée en puissance d’un terrorisme transnational. Ce contexte mondial de peur s’inscrit dans les données de ce graphique.
  </p>
  <p>
    À Mossoul en 2014, un enseignant a poursuivi ses cours sous la menace de Daesh pour préserver l’instruction des enfants. Il fut exécuté quelques semaines plus tard. Ce sacrifice symbolise l’humanité écrasée derrière chaque pic statistique.
  </p>
  <p>
    En conclusion, ce graphique met en lumière l’impact des conflits géopolitiques majeurs sur la fréquence des attaques. Il rappelle que le terrorisme s’inscrit dans l’histoire mondiale et affecte autant les États que les individus.
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
    Cette carte interactive représente la répartition mondiale des attaques terroristes par type, avec un code couleur correspondant à chaque région. Elle permet d’identifier les zones géographiques les plus affectées par les violences extrémistes.
  </p>
  <p>
    On distingue nettement des foyers de très forte activité en Asie du Sud (Afghanistan, Pakistan, Inde), au Moyen-Orient (Irak, Syrie), en Afrique subsaharienne (Nigeria, Mali) et en Amérique latine (Colombie, Pérou). L’Europe, l’Asie du Sud-Est et l’Amérique du Nord affichent également des points d’intensité, mais plus localisés.
  </p>
  <p>
    Cette répartition peut s’expliquer par la présence de conflits armés prolongés, de mouvements séparatistes actifs, et de contextes politiques instables. Le type d’attaque varie selon les régions : attentats à la bombe au Moyen-Orient, enlèvements en Afrique, guérilla en Amérique du Sud.
  </p>
  <p>
    À Maiduguri (Nigéria), épicentre des activités de Boko Haram, les marchés et écoles sont régulièrement la cible d’explosions. La ville apparaît comme un point rouge sur la carte, symbole d’un conflit qui mêle religion, pauvreté et insécurité.
  </p>
  <p>
    Une fillette de 10 ans fut utilisée comme kamikaze en 2014 à Kano, au Nigéria. Cette tragédie illustre cruellement un point de données sur la carte. Derrière chaque couleur, des vies bouleversées.
  </p>
  <p>
    Cette carte offre une lecture immédiate des grandes zones de tension terroriste à travers le monde. Elle rappelle que le terrorisme, loin d’être uniforme, se manifeste selon les spécificités culturelles et géopolitiques de chaque région.
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
    Cette carte du monde en dégradé de rouge représente les pays ayant enregistré le plus grand nombre de morts liés à des attaques terroristes. Plus la couleur est foncée, plus le nombre de victimes est élevé.
  </p>
  <p>
    L’Irak apparaît comme le pays le plus endeuillé, suivi de l’Afghanistan, du Pakistan, de la Syrie, du Nigeria et de l’Inde. Ces pays ont tous été confrontés à des conflits internes, à la présence de groupes djihadistes puissants ou à des tensions ethniques et politiques majeures.
  </p>
  <p>
    Le nombre élevé de morts est souvent corrélé à des attaques de grande ampleur dans des zones densément peuplées, à l’instar de Mossoul, Kaboul ou Maiduguri. Les conflits asymétriques, où les civils sont les premières cibles, y sont fréquents.
  </p>
  <p>
    À Kaboul, en 2017, une attaque au camion piégé a tué plus de 150 personnes dans le quartier diplomatique. Cet événement marque l’un des attentats les plus meurtriers de l’histoire récente de l’Afghanistan.
  </p>
  <p>
    Chaque teinte rouge sur cette carte représente des milliers de familles endeuillées. Des rues détruites, des marchés calcinés, des écoles vides. C’est une cartographie du deuil mondial.
  </p>
  <p>
    Ce graphique permet de visualiser la répartition géographique de la souffrance humaine liée au terrorisme, et rappelle la nécessité d’un engagement international pour stabiliser ces régions.
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
    Ce graphique classe les types d’attaques terroristes selon leur fréquence. Il donne un aperçu global des tactiques privilégiées par les groupes armés à travers le monde.
  </p>
  <p>
    Les attentats à la bombe (explosions) dominent largement, avec plus de 57 000 incidents, suivis par les assauts armés (25 000), les assassinats, les prises d’otages et les attaques contre les infrastructures. D’autres formes comme les détournements d’avion ou les armes chimiques sont beaucoup plus rares.
  </p>
  <p>
    Ces tendances reflètent une préférence pour les méthodes accessibles, peu coûteuses, et susceptibles de provoquer un impact médiatique fort. Les explosions dans les lieux publics visent souvent à semer la panique de manière indiscriminée.
  </p>
  <p>
    En Irak, entre 2005 et 2010, les attentats à la voiture piégée étaient presque quotidiens à Bagdad. Le marché d’Al-Karada a été ciblé en 2016 par un camion piégé, tuant plus de 300 personnes en une nuit.
  </p>
  <p>
    Derrière chaque barre du graphique se cache une réalité humaine : des familles détruites, des enfants blessés, des traumatismes collectifs. Une statistique qui parle, mais ne crie pas la douleur qu’elle contient.
  </p>
  <p>
    Ce graphique souligne que le terrorisme moderne s’appuie majoritairement sur des tactiques simples, brutales et efficaces. Pour les contrer, il faut comprendre ces logiques opérationnelles et anticiper les vulnérabilités potentielles.
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
  <p>
    Ce graphique en camembert montre la répartition des attaques suicides selon les grandes régions du monde. Il met en lumière la concentration géographique de cette méthode d’attaque, particulièrement radicale et meurtrière.
  </p>
  <p>
    Le Moyen-Orient et l’Afrique du Nord concentrent la majorité des attaques suicides, suivis de près par l’Asie du Sud. L’Afrique subsaharienne, l’Asie de l’Est et l’Europe apparaissent de façon plus marginale. Cette concentration dans certaines zones reflète des contextes où l’idéologie religieuse extrême et les conflits prolongés favorisent le recours au martyre comme outil militaire.
  </p>
  <p>
    Les attaques suicides sont souvent perçues comme l’arme du désespoir, mais aussi comme un choix stratégique visant un impact psychologique maximal. Elles requièrent une préparation idéologique et logistique spécifique, souvent orchestrée par des groupes comme Al-Qaïda, Daesh ou les Talibans.
  </p>
  <p>
    L’attentat suicide de 2005 à Amman (Jordanie), ayant visé trois hôtels internationaux et causé plus de 60 morts, est un exemple marquant. De jeunes recrues y ont été envoyées pour se faire exploser, à la suite d’un endoctrinement intense.
  </p>
  <p>
    Une femme nigériane, forcée par Boko Haram à porter une ceinture explosive, a sauvé des dizaines de personnes en désobéissant à ses bourreaux, quittant le lieu visé avant l’explosion. Son acte de courage fait écho à un contrepoids discret dans ce type d’attaque.
  </p>
  <p>
    Ce graphique rappelle que l’usage du corps humain comme arme de guerre est une stratégie extrême, largement conditionnée par les idéologies et conflits régionaux. Il interpelle sur le caractère profondément humain – et tragique – de chaque donnée affichée.
  </p>
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
  <p>
    Ce graphique en boîte (boxplot) compare le nombre de morts générés par différents types d’armes utilisées lors d’attaques terroristes. Il permet de visualiser la létalité médiane et les extrêmes liés à chaque catégorie d’arme.
  </p>
  <p>
    Les armes à feu et les explosifs ressortent comme les plus meurtrières, avec une large dispersion du nombre de morts par attaque. Les véhicules, les armes incendiaires, les armes chimiques et biologiques présentent également des pics élevés, bien qu’utilisées moins fréquemment.
  </p>
  <p>
    Ces résultats s’expliquent par la facilité d'accès aux armes à feu dans certaines régions, la puissance destructrice des explosifs improvisés (IED), et l’effet de surprise des attaques au véhicule-bélier, particulièrement en zone urbaine dense.
  </p>
  <p>
    L’attentat à la voiture piégée à Kaboul en 2017 (plus de 150 morts) ou celui de Nice en 2016 (86 morts au camion) illustrent la violence potentielle de ces armes. Même les attaques chimiques, bien que rares, peuvent avoir un effet catastrophique, comme celle au gaz sarin à Tokyo en 1995.
  </p>
  <p>
    Un attentat avorté en Allemagne en 2018 visait à répandre un poison biologique dans un métro, mais fut déjoué à temps. Cette tentative illustre les risques émergents d’attaques atypiques.
  </p>
  <p>
    Ce graphique offre un éclairage précis sur la dangerosité relative des moyens employés par les groupes terroristes. Il souligne que la prévention doit intégrer tous les scénarios, même les plus rares, car leurs conséquences peuvent être dramatiques.
  </p>
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
  <p>
    Ce graphique en treemap hiérarchique illustre la répartition des types de cibles visées par les attaques terroristes dans le monde. Il classe ces cibles en grandes catégories (civils, forces militaires, gouvernements, infrastructures...) et montre leur fréquence respective.
  </p>
  <p>
    Les civils et leurs biens ("Private Citizens & Property") sont les cibles les plus fréquentes, loin devant les institutions militaires ou gouvernementales. Viennent ensuite la police, les entités commerciales (banques, entreprises), les infrastructures de transport ou d’énergie.
  </p>
  <p>
    Cette tendance révèle une volonté claire de frapper les populations civiles, souvent dans les lieux du quotidien (marchés, places, transports publics), pour semer la terreur et déstabiliser le tissu social.
  </p>
  <p>
    À Bagdad, les attaques contre les marchés bondés sont devenues tristement routinières au fil des années 2000. En 2016, un attentat dans un centre commercial d’Al-Karrada a fait plus de 300 morts, ciblant des civils en pleine fête du Ramadan.
  </p>
  <p>
    L’histoire d’un conducteur de bus de Nairobi, qui a protégé ses passagers musulmans et chrétiens d’une attaque des Shebab en refusant de les trier, incarne la résistance humaine dans un monde où les civils sont en première ligne.
  </p>
  <p>
    Ce graphique met en évidence que le terrorisme vise souvent les plus vulnérables. Il nous rappelle que derrière chaque statistique, il y a des victimes innocentes et des sociétés traumatisées, ciblées dans ce qu’elles ont de plus quotidien.
  </p>
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
  <p>
    Ce graphique interactif classe les groupes terroristes les plus actifs par région du monde, selon la sélection effectuée via un menu déroulant. Il permet d’analyser la diversité des organisations extrémistes en fonction des contextes géographiques.
  </p>
  <p>
    En Amérique du Sud, les FARC et le Sentier lumineux sont prédominants, incarnant une guérilla marxiste prolongée. En Asie du Sud, les Talibans et Lashkar-e-Taiba dominent, tandis que Daesh et Al-Qaïda apparaissent nettement au Moyen-Orient. En Afrique, Boko Haram est l’un des plus meurtriers. Chaque région a ainsi ses propres dynamiques idéologiques, historiques et militaires.
  </p>
  <p>
    Ces groupes émergent souvent dans des contextes d'inégalités sociales, de vide institutionnel, ou de conflits prolongés. Leurs stratégies varient : guérilla rurale, attentats-suicides urbains, enlèvements, etc.
  </p>
  <p>
    En 2014, Boko Haram enlève plus de 200 lycéennes à Chibok, Nigeria. Ce drame mondialement médiatisé est l’œuvre du groupe le plus actif d’Afrique cette année-là. Dans les Andes, le Sentier lumineux a tué des dizaines de paysans dans les années 80 pour asseoir son autorité.
  </p>
  <p>
    Ce graphique ne montre pas que des noms : il expose les mouvements qui ont façonné des décennies de peur et d’insécurité, dans des contextes bien distincts. Il offre une vue comparative rare sur le terrorisme mondial.
  </p>
  <p>
    L’interactivité permet de mieux comprendre les logiques régionales du terrorisme, et souligne que la lutte contre ces groupes nécessite des approches localisées, adaptées aux réalités de chaque terrain.
  </p>
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
  <p>
    Ce graphique empilé compare le nombre d’attaques terroristes réussies (en vert) et échouées (en rouge) de 1990 à 2017. Il permet d’évaluer non seulement la fréquence des attaques, mais aussi l’efficacité des dispositifs de prévention et de neutralisation.
  </p>
  <p>
    Les attaques réussies restent largement majoritaires, représentant la quasi-totalité des cas. Une hausse globale est visible à partir de 2005, avec un pic en 2014-2015, période correspondant à l’apogée de l’État Islamique. Les tentatives échouées augmentent légèrement dans les années 2010.
  </p>
  <p>
    Cette évolution s’explique par la montée en puissance de groupes organisés, la multiplication des cellules autonomes et une meilleure coordination logistique. L’augmentation des échecs peut témoigner d’un renforcement des services de renseignement et de la coopération internationale.
  </p>
  <p>
    En France, l’attentat de l’église de Villejuif (2015) a été évité de justesse grâce à une interpellation fortuite. À New York, en 2010, un attentat à la voiture piégée sur Times Square a échoué suite à l’intervention d’un vendeur de rue qui a alerté la police.
  </p>
  <p>
    Ces histoires montrent que derrière chaque attaque évitée, il y a souvent une vigilance humaine, un hasard heureux ou un renseignement bien exploité. Le rouge sur ce graphique, bien que discret, représente des vies sauvées.
  </p>
  <p>
    Ce graphique incite à poursuivre les efforts de prévention, tout en rappelant que malgré les dispositifs de sécurité, le risque reste structurellement élevé lorsque les tensions géopolitiques et idéologiques perdurent.
  </p>
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
  <p>
    Ce graphique interactif recense les attaques terroristes ayant causé au moins 20 morts, en les répartissant dans le temps et selon les régions du monde. Grâce à un filtre par région, l’utilisateur peut analyser les événements les plus violents à l’échelle globale.
  </p>
  <p>
    L’Afrique subsaharienne, le Moyen-Orient, l’Asie du Sud et l’Amérique latine affichent plusieurs pics d’intensité, souvent liés à des conflits prolongés ou à des vagues extrémistes localisées. Des événements majeurs sont aussi visibles en Europe ou en Asie du Sud-Est.
  </p>
  <p>
    Ces attaques de grande ampleur sont souvent le fruit de stratégies de terreur massives, comme les attentats-suicides multiples, les embuscades contre des forces armées ou les massacres dans des lieux de culte ou de rassemblement.
  </p>
  <p>
    En Irak, une explosion dans un marché bondé à Al-Karrada a tué plus de 300 personnes en une nuit. Au Nigeria, Boko Haram a perpétré en 2015 une attaque contre le village de Baga, faisant jusqu’à 2 000 morts. Ce sont des points extrêmes de ce nuage de données.
  </p>
  <p>
    En Colombie, dans les années 90, les FARC ont bombardé des postes de police et des villages entiers, causant des dizaines de morts. Même en Europe, les attentats de Madrid (2004) ou Paris (2015) s’inscrivent dans cette catégorie.
  </p>
  <p>
    Ce graphique montre que la violence extrême du terrorisme touche tous les continents et qu’elle n’est pas l’apanage d’une région. Il invite à une vigilance globale et à une lecture comparée des causes profondes de cette radicalité meurtrière.
  </p>
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
