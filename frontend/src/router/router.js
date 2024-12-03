import { createRouter, createWebHistory } from 'vue-router';
import LocationsPage from '@/views/LocationsPage.vue';


const routes = [
  { path: '/', name: 'Home', component: LocationsPage },
  { path: '/locations', name: 'Locations', component: LocationsPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
