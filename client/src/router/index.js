import { createRouter, createWebHistory } from 'vue-router';
import Students from '../components/Students.vue'
import Absences from '../components/Absences.vue'
import Ping from '../components/Ping.vue';

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Students',
      component: Students,
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
    {
      path: '/absences',
      name: 'Absences',
      component: Absences
    },
  ]
});

export default router;
