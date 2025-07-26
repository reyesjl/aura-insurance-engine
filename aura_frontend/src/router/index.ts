/*
 * Aura Insurance Engine – Proprietary Software
 *
 * Copyright © 2025 Jose Reyes (GitHub: @reyesjl). All rights reserved.
 *
 * This software was developed solely by Jose Reyes – full-stack engineer and designer.
 * It is a modern insurance submission platform built to streamline the intake
 * and processing of insurance applications.
 *
 * This code is proprietary and confidential. Unauthorized use, reproduction,
 * distribution, or modification is strictly prohibited.
 *
 * Project repository: https://github.com/reyesjl/aura-insurance-engine
 * DeepWiki: https://app.devin.ai/wiki/reyesjl/aura-insurance-engine
 */

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
import Questions from '@/pages/Questions.vue'
import CreateQuestion from '@/pages/CreateQuestion.vue'
import AuthApplicationSession from '@/pages/AuthApplicationSession.vue'
import FillApplicationSession from '@/pages/FillApplicationSession.vue'

const routes: Array<RouteRecordRaw> = [
  { path: '/', name: 'Home', component: Home },
  { path: '/about', name: 'About', component: About },
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
