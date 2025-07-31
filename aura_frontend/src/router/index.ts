import AgentDashboard from '@/pages/AgentDashboard.vue'
import ApplicationSessions from '@/pages/ApplicationSessions.vue'
import Login from '@/pages/auth/Login.vue'
import Register from '@/pages/auth/Register.vue'
import ResetPassword from '@/pages/auth/ResetPassword.vue'
import AuthApplicationSession from '@/pages/AuthApplicationSession.vue'
import CreateApplicationSession from '@/pages/CreateApplicationSession.vue'
import CreateQuestion from '@/pages/CreateQuestion.vue'
import FillApplicationSession from '@/pages/FillApplicationSession.vue'
import Questions from '@/pages/Questions.vue'
import ViewApplicationSession from '@/pages/ViewApplicationSession.vue'
import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import About from '../pages/About.vue'
import Feedback from '../pages/Feedback.vue'
import Home from '../pages/Home.vue'
import License from '../pages/License.vue'
import TermsOfService from '../pages/TermsOfService.vue'

const routes: Array<RouteRecordRaw> = [
  { path: '/', name: 'Home', component: Home },
  { path: '/about', name: 'About', component: About },
  { path: '/feedback', name: 'Feedback', component: Feedback },
  { path: '/license', name: 'License', component: License },
  { path: '/terms-of-service', name: 'TermsOfService', component: TermsOfService },
  { path: '/auth/register', name: 'Register', component: Register },
  { path: '/auth/login', name: 'Login', component: Login },
  { path: '/auth/reset-password', name: 'ResetPassword', component: ResetPassword },
  { path: '/agent', name: 'Agent', component: AgentDashboard },
  { path: '/questions', name: 'Questions', component: Questions },
  { path: '/questions/create', name: 'CreateQuestion', component: CreateQuestion },

  { path: '/applications', name: 'ApplicationSessions', component: ApplicationSessions },
  {
    path: '/applications/create',
    name: 'CreateApplicationSession',
    component: CreateApplicationSession,
  },
  {
    path: '/applications/:id',
    name: 'ApplicationSessionDetail',
    component: ViewApplicationSession,
    props: true,
  },
  {
    path: '/applications/auth/:token',
    name: 'AuthApplicationSession',
    component: AuthApplicationSession,
  },
  {
    path: '/applications/fill/:id',
    name: 'FillApplicationSession',
    component: FillApplicationSession,
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
