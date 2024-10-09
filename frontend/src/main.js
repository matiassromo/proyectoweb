import { createApp } from 'vue';
import App from './App.vue';
import router from './router/router';  // Asegúrate que la ruta sea correcta

createApp(App).use(router).mount('#app');
