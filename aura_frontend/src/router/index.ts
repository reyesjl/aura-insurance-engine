import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import AgentDashboard from '../pages/AgentDashboard.vue'
import Home from '../pages/Home.vue'
import About from '../pages/About.vue'
import SessionList from '../pages/SessionList.vue'

const routes: Array<RouteRecordRaw> = [
  { path: '/', name: 'Home', component: Home },
  { path: '/about', name: 'About', component: About },
  { path: '/sessions', name: 'SessionList', component: SessionList },
  { path: '/agent', name: 'AgentDashboard', component: AgentDashboard },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
