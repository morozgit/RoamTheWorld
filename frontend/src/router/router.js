import { createRouter, createWebHistory } from 'vue-router';
import LocationsPage from '@/views/LocationsPage.vue';
import TracksPage from '@/views/TracksPage.vue';
import TrackDetail from '@/views/TrackDetail.vue';


const routes = [
  { path: '/', name: 'Home', component: LocationsPage },
  { path: '/locations', name: 'Locations', component: LocationsPage },
  { path: '/location/:location_id', name: 'TracksPage', component: TracksPage },
  { path: '/track/:track_id', name: 'TrackDetail', component: TrackDetail },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
