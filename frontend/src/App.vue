<template>
  <div>
    <!-- Barre de navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark">
      <div class="container">
        <router-link class="navbar-brand" to="/">TerrorTrack</router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Basculer la navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <router-link class="nav-link" to="/">Accueil</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/modules">Modules</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/dashboard">Dashboard</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Zone où s'affichent les pages dynamiques -->
    <router-view></router-view>

    <!-- Pied de page -->
    <footer class="footer text-white py-3 text-center">
      <div class="container">
        <small>© 2025 TerrorTrack - Tous droits réservés</small>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
/* ---- Couleurs et style navbar ---- */
.navbar {
  background-color: #042075 !important;
}

/* ---- Pied de page ---- */
.footer {
  background-color: #042075;
  border-top: 4px solid #ff0707;
}
</style>
