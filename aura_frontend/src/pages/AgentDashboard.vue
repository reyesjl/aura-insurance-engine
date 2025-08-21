<template>
  <NavBar />
  <div class="page-spacer bg-black"></div>
  <Breadcrumbs />

  <Section mode="light" padding="small" class="min-h-screen">
    <div class="text-4xl md:text-5xl font-semibold leading-tight mb-12">
      Welcome back, {{ user?.username || 'Agent' }}
    </div>

    <!-- Show different content based on agent status -->
    <div
      v-if="!userStore.isAgent"
      class="mb-8 p-6 bg-yellow-100 border border-yellow-400 text-yellow-700 rounded-lg"
    >
      <p class="text-lg font-semibold mb-2">Account Pending Agent Approval</p>
      <p class="text-base leading-relaxed">
        Your account is being reviewed for agent access. Please contact support for assistance.
      </p>
    </div>

    <!-- Tiles -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <button
        @click="navigateToCreateApplication"
        @keydown.enter="navigateToCreateApplication"
        @keydown.space.prevent="navigateToCreateApplication"
        :class="{
          'flex flex-col gap-6 duration-200 p-8 text-left focus:outline-none focus:ring-2 focus:ring-offset-2 rounded-lg': true,
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
        <div class="text-lg font-semibold">+ New App</div>
        <div class="text-base opacity-80 leading-relaxed">
          {{ userStore.isAgent ? 'Start a new insurance application' : 'Agent access required' }}
        </div>
      </button>

      <button
        @click="navigateToApplicationSessions"
        @keydown.enter="navigateToApplicationSessions"
        @keydown.space.prevent="navigateToApplicationSessions"
        :class="{
          'flex flex-col gap-6 duration-200 p-8 text-left focus:outline-none focus:ring-2 focus:ring-offset-2 rounded-lg': true,
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
        <div class="text-lg font-semibold">My Sessions</div>
        <div class="text-base opacity-80 leading-relaxed">
          {{ userStore.isAgent ? 'View active application sessions' : 'Agent access required' }}
        </div>
      </button>

      <button
        @click="navigateToQuestions"
        @keydown.enter="navigateToQuestions"
        @keydown.space.prevent="navigateToQuestions"
        :class="{
          'flex flex-col gap-6 duration-200 p-8 text-left focus:outline-none focus:ring-2 focus:ring-offset-2 rounded-lg': true,
          'bg-gray-200 hover:bg-black hover:text-white focus:bg-black focus:text-white focus:ring-blue-500 cursor-pointer':
            userStore.isAgent,
          'bg-red-100 text-red-400 cursor-not-allowed hover:bg-red-200 focus:ring-red-300':
            !userStore.isAgent,
        }"
        :aria-label="userStore.isAgent ? 'View and manage your questions' : 'Agent access required'"
        :disabled="!userStore.isAgent"
      >
        <div class="text-lg font-semibold">Questions</div>
        <div class="text-base opacity-80 leading-relaxed">
          {{ userStore.isAgent ? 'View and manage your questions' : 'Agent access required' }}
        </div>
      </button>

      <button
        @click="handleLogout"
        @keydown.enter="handleLogout"
        @keydown.space.prevent="handleLogout"
        class="flex flex-col gap-6 duration-200 bg-gray-200 hover:bg-black hover:text-white focus:bg-black focus:text-white focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 p-8 text-left rounded-lg"
        aria-label="Logout of your account"
      >
        <div class="text-lg font-semibold">Logout</div>
        <div class="text-base opacity-80 leading-relaxed">Logout of your account</div>
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
  if (!userStore.isAgent) return
  router.push('/applications/create')
}

const navigateToApplicationSessions = () => {
  if (!userStore.isAgent) return
  router.push('/applications')
}

const navigateToQuestions = () => {
  if (!userStore.isAgent) return
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
