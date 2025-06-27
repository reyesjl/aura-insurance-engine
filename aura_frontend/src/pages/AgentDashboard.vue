<template>
  <NavBar />
  <div class="page-spacer bg-black"></div>

  <Section mode="light">
    <div class="text-4xl md:text-5xl font-bold mb-10">
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

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="p-6 border border-gray-300">
        <h3 class="text-xl font-bold mb-4">Create Application</h3>
        <p class="mb-4">Start a new insurance application</p>
        <button
          @click="navigateToCreateApplication"
          :disabled="!userStore.isAgent"
          class="bg-black text-white px-4 py-2 hover:bg-gray-800 disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
          Get Started
        </button>
      </div>

      <div class="p-6 border border-gray-300">
        <h3 class="text-xl font-bold mb-4">My Sessions</h3>
        <p class="mb-4">View active application sessions</p>
        <button
          @click="navigateToApplicationSessions"
          :disabled="!userStore.isAgent"
          class="bg-black text-white px-4 py-2 hover:bg-gray-800 disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
          View Sessions
        </button>
      </div>

      <div class="p-6 border border-gray-300">
        <h3 class="text-xl font-bold mb-4">Site Carriers</h3>
        <p class="mb-4">View and manage carriers</p>
        <button
          :disabled="!userStore.isAgent"
          class="bg-black text-white px-4 py-2 hover:bg-gray-800 disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
          View Carriers
        </button>
      </div>

      <div class="p-6 border border-gray-300">
        <h3 class="text-xl font-bold mb-4">Site Coverages</h3>
        <p class="mb-4">View and manage coverages</p>
        <button
          :disabled="!userStore.isAgent"
          class="bg-black text-white px-4 py-2 hover:bg-gray-800 disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
          View Coverages
        </button>
      </div>

      <div class="p-6 border border-gray-300">
        <h3 class="text-xl font-bold mb-4">Profile</h3>
        <p class="mb-4">Manage your profile</p>
        <button class="bg-black text-white px-4 py-2 hover:bg-gray-800">Edit Profile</button>
      </div>
      <div class="p-6 border border-gray-300">
        <h3 class="text-xl font-bold mb-4">Logout</h3>
        <p class="mb-4">Logout of your profile</p>
        <button @click="handleLogout" class="bg-black text-white px-4 py-2 hover:bg-gray-800">
          Logout
        </button>
      </div>
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

// Protect the route - redirect if not logged in, but allow non-agents
onMounted(() => {
  if (!userStore.isLoggedIn) {
    router.push('/auth/login')
  }
  // Remove the isAgent check - let logged in users access the dashboard
  // They'll just see limited functionality if they're not agents
})
</script>
