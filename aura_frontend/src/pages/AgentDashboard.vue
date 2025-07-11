<template>
  <NavBar />
  <div class="page-spacer bg-black"></div>
  <Breadcrumbs />

  <Section mode="light" padding="small" class="min-h-screen">
    <div class="text-4xl md:text-5xl font-bold mb-5">
      Welcome back, {{ user?.username || 'Agent' }}
    </div>

    <!-- Show different content based on agent status -->
    <div
      v-if="!userStore.isAgent"
      class="mb-6 p-4 bg-yellow-100 border border-yellow-400 text-yellow-700 rounded"
    >
      <p class="font-semibold">Account Pending Agent Approval</p>
      <p>Your account is being reviewed for agent access. Please contact support for assistance.</p>
    </div>

    <!-- Tiles -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-2">
      <button
        @click="navigateToCreateApplication"
        @keydown.enter="navigateToCreateApplication"
        @keydown.space.prevent="navigateToCreateApplication"
        class="flex flex-col gap-5 duration-200 bg-gray-200 hover:bg-black hover:text-white focus:bg-black focus:text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 p-10 text-left"
        aria-label="Start a new insurance application"
      >
        <div class="text-2xl">+ New App</div>
        <div class="tile-description">Start a new insurance application</div>
      </button>
      
      <button
        @click="navigateToApplicationSessions"
        @keydown.enter="navigateToApplicationSessions"
        @keydown.space.prevent="navigateToApplicationSessions"
        class="flex flex-col gap-5 duration-200 bg-gray-200 hover:bg-black hover:text-white focus:bg-black focus:text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 p-10 text-left"
        aria-label="View active application sessions"
      >
        <div class="text-2xl">My Sessions</div>
        <div class="tile-description">View active application sessions</div>
      </button>
      
      <button
        @click="navigateToQuestions"
        @keydown.enter="navigateToQuestions"
        @keydown.space.prevent="navigateToQuestions"
        class="flex flex-col gap-5 duration-200 bg-gray-200 hover:bg-black hover:text-white focus:bg-black focus:text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 p-10 text-left"
        aria-label="View and manage your questions"
      >
        <div class="text-2xl">Questions</div>
        <div class="tile-description">View and manage your questions</div>
      </button>
      
      <button
        @click="handleLogout"
        @keydown.enter="handleLogout"
        @keydown.space.prevent="handleLogout"
        class="flex flex-col gap-5 duration-200 bg-gray-200 hover:bg-black hover:text-white focus:bg-black focus:text-white focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 p-10 text-left"
        aria-label="Logout of your account"
      >
        <div class="text-2xl">Logout</div>
        <div class="tile-description">Logout of your account</div>
      </button>
    </div>
  </Section>

  <FootBar />
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user.ts'
import NavBar from '@/components/NavBar.vue'
import FootBar from '@/components/FootBar.vue'
import Section from '@/components/Section.vue'
import Breadcrumbs from '@/components/Breadcrumbs.vue'

const userStore = useUserStore()
const router = useRouter()
const { user } = userStore

const handleLogout = async () => {
  try {
    await userStore.logout()
    router.push('/')
  } catch (error) {
    console.error('Logout failed:', error)
    router.push('/') // Redirect anyway
  }
}

const navigateToCreateApplication = () => {
  router.push('/applications/create')
}

const navigateToApplicationSessions = () => {
  router.push('/applications')
}

const navigateToQuestions = () => {
  router.push('/questions')
}

// Protect the route - redirect if not logged in, but allow non-agents
onMounted(() => {
  if (!userStore.isLoggedIn) {
    router.push('/auth/login')
  }
  // Remove the isAgent check - let logged in users access the dashboard
  // They'll just see limited functionality if they're not agents
})
</script>
