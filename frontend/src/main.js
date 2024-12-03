import './assets/main.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from './router/router.js';
import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
});

console.log('Base URL:', import.meta.env.VITE_API_URL);

export default axiosInstance;

createApp(App).use(router).mount('#app');
