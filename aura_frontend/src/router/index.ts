import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import AgentDashboard from '../pages/AgentDashboard.vue'

const routes: Array<RouteRecordRaw> = [
  { path: '/', redirect: '/agent' },
  { path: '/agent', name: 'AgentDashboard', component: AgentDashboard }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router

