import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/login.vue';
import UserCrud from '../components/UserCrud.vue';

const routes = [
  { path: '/', component: Login },
  { 
    path: '/users', 
    component: UserCrud,
    beforeEnter: (to, from, next) => {
      const isAuthenticated = localStorage.getItem('authenticated');
      if (isAuthenticated) {
        next();  // Si el usuario está autenticado, permite el acceso.
      } else {
        next('/');  // Si no está autenticado, redirige al login.
      }
    }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
