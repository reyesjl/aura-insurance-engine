import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import Home from '../pages/Home.vue'
import About from '../pages/About.vue'
import Register from '@/pages/auth/Register.vue'
import Login from '@/pages/auth/Login.vue'
import ResetPassword from '@/pages/auth/ResetPassword.vue'
import AgentDashboard from '@/pages/AgentDashboard.vue'
import CreateApplicationSession from '@/pages/CreateApplicationSession.vue'
import ApplicationSessions from '@/pages/ApplicationSessions.vue'
import ViewApplicationSession from '@/pages/ViewApplicationSession.vue'

const routes: Array<RouteRecordRaw> = [
  { path: '/', name: 'Home', component: Home },
  { path: '/about', name: 'About', component: About },
  { path: '/auth/register', name: 'Register', component: Register },
  { path: '/auth/login', name: 'Login', component: Login },
  { path: '/auth/reset-password', name: 'ResetPassword', component: ResetPassword },
  { path: '/agent', name: 'Agent', component: AgentDashboard },

  { path: '/applications', name: 'ApplicationSessions', component: ApplicationSessions },
  {
    path: '/applications/create',
    name: 'CreateApplicationSession',
    component: CreateApplicationSession,
  },
  {
    path: '/applications/:sessionId',
    name: 'ApplicationSessionDetail',
    component: ViewApplicationSession,
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
