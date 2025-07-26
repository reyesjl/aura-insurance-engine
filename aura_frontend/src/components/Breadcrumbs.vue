/*
 * Aura Insurance Engine – Proprietary Software
 *
 * Copyright © 2025 Jose Reyes (GitHub: @reyesjl). All rights reserved.
 *
 * This software was developed solely by Jose Reyes – full-stack engineer and designer.
 * Jacob Powers contributed as the licensed insurance agent for the project.
 * It is a modern insurance submission platform built to streamline the intake
 * and processing of insurance applications.
 *
 * This code is proprietary and confidential. Unauthorized use, reproduction,
 * distribution, or modification is strictly prohibited.
 *
 * Project repository: https://github.com/reyesjl/aura-insurance-engine
 * DeepWiki: https://app.devin.ai/wiki/reyesjl/aura-insurance-engine
 */

<template>
    <Section mode="light" padding="none">
        <nav class="breadcrumb text-sm text-gray-500 py-4">
            <span v-for="(crumb, index) in breadcrumbs" :key="index">
            <router-link 
                v-if="crumb.to && index < breadcrumbs.length - 1"
                :to="crumb.to"
                class="text-gray-500 hover:text-gray-800 hover:underline"
            >
                {{ crumb.text }}
            </router-link>
            <span v-else class="text-black font-medium">
                {{ crumb.text }}
            </span>
            <span v-if="index < breadcrumbs.length - 1" class="mx-2">/</span>
            </span>
        </nav>
  </Section>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import Section from './Section.vue'

interface Breadcrumb {
  text: string
  to?: string
}

const route = useRoute()

const breadcrumbs = computed((): Breadcrumb[] => {
  const crumbs: Breadcrumb[] = [{ text: 'Home', to: '/' }]
  
  // Generate breadcrumbs based on current route
  switch (route.name) {
    case 'About':
      crumbs.push({ text: 'About' })
      break
    case 'Register':
      crumbs.push({ text: 'Auth', to: '/auth/login' }, { text: 'Register' })
      break
    case 'Login':
      crumbs.push({ text: 'Auth', to: '/auth/login' }, { text: 'Login' })
      break
    case 'ResetPassword':
      crumbs.push({ text: 'Auth', to: '/auth/login' }, { text: 'Reset Password' })
      break
    case 'Agent':
      crumbs.push({ text: 'MyAgent' })
      break
    case 'Questions':
      crumbs.push({ text: 'MyAgent', to: '/agent' }, { text: 'Questions' })
      break
    case 'ApplicationSessions':
      crumbs.push({ text: 'MyAgent', to: '/agent' }, { text: 'Applications' })
      break
    case 'CreateApplicationSession':
      crumbs.push(
        { text: 'MyAgent', to: '/agent' },
        { text: 'Applications', to: '/applications' },
        { text: 'Create' }
      )
      break
    case 'ApplicationSessionDetail':
      crumbs.push(
        { text: 'Agent', to: '/agent' },
        { text: 'Applications', to: '/applications' },
        { text: 'Session' }
      )
      break
    default:
      // For unknown routes, try to build from path segments
      const pathSegments = route.path.split('/').filter(segment => segment)
      pathSegments.forEach((segment, index) => {
        const path = '/' + pathSegments.slice(0, index + 1).join('/')
        const isLast = index === pathSegments.length - 1
        crumbs.push({
          text: segment.charAt(0).toUpperCase() + segment.slice(1),
          to: isLast ? undefined : path
        })
      })
  }
  
  return crumbs
})
</script>