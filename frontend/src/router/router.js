import { createRouter, createWebHistory } from 'vue-router';
import LocationsPage from '@/views/LocationsPage.vue';
import TracksPage from '@/views/TracksPage.vue';


const routes = [
  { path: '/', name: 'Home', component: LocationsPage },
  { path: '/locations', name: 'Locations', component: LocationsPage },
  { path: '/tracks/:location_id', name: 'TracksPage', component: TracksPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
