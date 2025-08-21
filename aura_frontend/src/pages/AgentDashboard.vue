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
      <!-- New Application Tile -->
      <RouterLink
        v-if="userStore.isAgent"
        to="/applications/create"
        class="flex flex-col gap-6 duration-200 p-8 text-left focus:outline-none focus:ring-2 focus:ring-offset-2 rounded-lg bg-gray-200 hover:bg-black hover:text-white focus:bg-black focus:text-white focus:ring-blue-500 cursor-pointer"
        aria-label="Start a new insurance application"
      >
        <div class="text-lg font-semibold">+ New App</div>
        <div class="text-base opacity-80 leading-relaxed">Start a new insurance application</div>
      </RouterLink>
      <div
        v-else
        class="flex flex-col gap-6 duration-200 p-8 text-left focus:outline-none focus:ring-2 focus:ring-offset-2 rounded-lg bg-red-100 text-red-400 cursor-not-allowed hover:bg-red-200 focus:ring-red-300"
        aria-label="Agent access required"
        aria-disabled="true"
        tabindex="-1"
      >
        <div class="text-lg font-semibold">+ New App</div>
        <div class="text-base opacity-80 leading-relaxed">Agent access required</div>
      </div>

      <!-- Sessions Tile -->
      <RouterLink
        v-if="userStore.isAgent"
        to="/applications"
        class="flex flex-col gap-6 duration-200 p-8 text-left focus:outline-none focus:ring-2 focus:ring-offset-2 rounded-lg bg-gray-200 hover:bg-black hover:text-white focus:bg-black focus:text-white focus:ring-blue-500 cursor-pointer"
        aria-label="View active application sessions"
      >
        <div class="text-lg font-semibold">My Sessions</div>
        <div class="text-base opacity-80 leading-relaxed">View active application sessions</div>
      </RouterLink>
      <div
        v-else
        class="flex flex-col gap-6 duration-200 p-8 text-left focus:outline-none focus:ring-2 focus:ring-offset-2 rounded-lg bg-red-100 text-red-400 cursor-not-allowed hover:bg-red-200 focus:ring-red-300"
        aria-label="Agent access required"
        aria-disabled="true"
        tabindex="-1"
      >
        <div class="text-lg font-semibold">My Sessions</div>
        <div class="text-base opacity-80 leading-relaxed">Agent access required</div>
      </div>

      <!-- Questions Tile -->
      <RouterLink
        v-if="userStore.isAgent"
        to="/questions"
        class="flex flex-col gap-6 duration-200 p-8 text-left focus:outline-none focus:ring-2 focus:ring-offset-2 rounded-lg bg-gray-200 hover:bg-black hover:text-white focus:bg-black focus:text-white focus:ring-blue-500 cursor-pointer"
        aria-label="View and manage your questions"
      >
        <div class="text-lg font-semibold">Questions</div>
        <div class="text-base opacity-80 leading-relaxed">View and manage your questions</div>
      </RouterLink>
      <div
        v-else
        class="flex flex-col gap-6 duration-200 p-8 text-left focus:outline-none focus:ring-2 focus:ring-offset-2 rounded-lg bg-red-100 text-red-400 cursor-not-allowed hover:bg-red-200 focus:ring-red-300"
        aria-label="Agent access required"
        aria-disabled="true"
        tabindex="-1"
      >
        <div class="text-lg font-semibold">Questions</div>
        <div class="text-base opacity-80 leading-relaxed">Agent access required</div>
      </div>

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
import { RouterLink, useRouter } from 'vue-router'

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

// navigation handled via <RouterLink> for agent-only tiles

// Protect the route - redirect if not logged in, but allow non-agents
onMounted(() => {
  if (!userStore.isLoggedIn) {
    router.push('/auth/login')
  }
  // Remove the isAgent check - let logged in users access the dashboard
  // They'll just see limited functionality if they're not agents
})
</script>
