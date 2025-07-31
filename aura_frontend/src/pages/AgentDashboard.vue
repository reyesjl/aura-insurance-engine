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
        @click="userStore.isAgent ? navigateToCreateApplication : null"
        @keydown.enter="userStore.isAgent ? navigateToCreateApplication : null"
        @keydown.space.prevent="userStore.isAgent ? navigateToCreateApplication : null"
        :class="{
          'flex flex-col gap-5 duration-200 p-10 text-left focus:outline-none focus:ring-2 focus:ring-offset-2': true,
          'bg-gray-200 hover:bg-black hover:text-white focus:bg-black focus:text-white focus:ring-blue-500 cursor-pointer':
            userStore.isAgent,
          'bg-red-100 text-red-400 cursor-not-allowed hover:bg-red-200 focus:ring-red-300':
            !userStore.isAgent,
        }"
        :aria-label="
          userStore.isAgent ? 'Start a new insurance application' : 'Agent access required'
        "
        :disabled="!userStore.isAgent"
      >
        <div class="text-2xl">+ New App</div>
        <div class="tile-description">
          {{ userStore.isAgent ? 'Start a new insurance application' : 'Agent access required' }}
        </div>
      </button>

      <button
        @click="userStore.isAgent ? navigateToApplicationSessions : null"
        @keydown.enter="userStore.isAgent ? navigateToApplicationSessions : null"
        @keydown.space.prevent="userStore.isAgent ? navigateToApplicationSessions : null"
        :class="{
          'flex flex-col gap-5 duration-200 p-10 text-left focus:outline-none focus:ring-2 focus:ring-offset-2': true,
          'bg-gray-200 hover:bg-black hover:text-white focus:bg-black focus:text-white focus:ring-blue-500 cursor-pointer':
            userStore.isAgent,
          'bg-red-100 text-red-400 cursor-not-allowed hover:bg-red-200 focus:ring-red-300':
            !userStore.isAgent,
        }"
        :aria-label="
          userStore.isAgent ? 'View active application sessions' : 'Agent access required'
        "
        :disabled="!userStore.isAgent"
      >
        <div class="text-2xl">My Sessions</div>
        <div class="tile-description">
          {{ userStore.isAgent ? 'View active application sessions' : 'Agent access required' }}
        </div>
      </button>

      <button
        @click="userStore.isAgent ? navigateToQuestions : null"
        @keydown.enter="userStore.isAgent ? navigateToQuestions : null"
        @keydown.space.prevent="userStore.isAgent ? navigateToQuestions : null"
        :class="{
          'flex flex-col gap-5 duration-200 p-10 text-left focus:outline-none focus:ring-2 focus:ring-offset-2': true,
          'bg-gray-200 hover:bg-black hover:text-white focus:bg-black focus:text-white focus:ring-blue-500 cursor-pointer':
            userStore.isAgent,
          'bg-red-100 text-red-400 cursor-not-allowed hover:bg-red-200 focus:ring-red-300':
            !userStore.isAgent,
        }"
        :aria-label="userStore.isAgent ? 'View and manage your questions' : 'Agent access required'"
        :disabled="!userStore.isAgent"
      >
        <div class="text-2xl">Questions</div>
        <div class="tile-description">
          {{ userStore.isAgent ? 'View and manage your questions' : 'Agent access required' }}
        </div>
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
import Breadcrumbs from '@/components/Breadcrumbs.vue'
import FootBar from '@/components/FootBar.vue'
import NavBar from '@/components/NavBar.vue'
import Section from '@/components/Section.vue'
import { useUserStore } from '@/stores/user.ts'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

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
