import { createRouter, createWebHistory } from 'vue-router';
import Home from './views/Home.vue';        // Créez ce fichier si nécessaire
import Modules from './views/Modules.vue';
import Dashboard from './views/Dashboard.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home, 
  },
  {
    path: '/modules',
    name: 'Modules',
    component: Modules,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
