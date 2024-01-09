import { createRouter, createWebHistory } from 'vue-router';
import Ping from '../components/Ping.vue';
import ToDos from "@/components/ToDos.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
      {
      path: '/',
      name: 'Books',
      component: ToDos,
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
  ]
});

export default router;

