import Vue from 'vue';
import VueRouter from 'vue-router';
import CurrentTime from '../components/CurrentTime.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/get_new_time',
    name: 'CurrentTime',
    component: CurrentTime,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
