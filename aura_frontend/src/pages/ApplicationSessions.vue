<template>
  <!-- Sessions List -->
  <Section mode="light">
    <h1 class="text-2xl font-bold">My Sessions</h1>
    <div v-if="loading" class="text-gray-600">Loading sessions...</div>
    <div v-else-if="error" class="text-red-600">{{ error }}</div>
    <div v-else-if="!sessions || sessions.length === 0" class="text-gray-600">
      <p>No application sessions found.</p>
      <router-link to="/applications/create" class="text-lg text-black underline underline-offset-5">
        Create your first application
      </router-link>
    </div>
    <div v-else class="space-y-4">
      <div
        v-for="session in sessions"
        :key="session.id"
        class="p-4 border hover:bg-gray-50 cursor-pointer"
        @click="viewSession(session.id)"
      >
        <div class="flex items-center justify-between">
          <div>
            <h3 class="font-semibold text-lg">{{ session.name || 'Untitled Application' }}</h3>
            <p class="text-sm text-gray-600">Token: {{ session.token }}</p>
            <p class="text-sm text-gray-500">Created: {{ formatDate(session.created_at) }}</p>
          </div>

          <div class="text-right">
            <span
              class="inline-block px-3 py-1 rounded-full text-sm font-medium"
              :class="getStatusClass(session.status)"
            >
              {{ session.status }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </Section>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Section from '@/components/Section.vue'
import { applicationsAPI } from '@/api/applications'
import type { ApplicationSession } from '@/types'

const router = useRouter()

// State - Initialize as empty array to prevent undefined errors
const sessions = ref<ApplicationSession[]>([])
const loading = ref(false)
const error = ref('')

// Methods
const loadSessions = async () => {
  loading.value = true
  error.value = ''
  try {
    sessions.value = await applicationsAPI.getApplicationSessions()
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to load sessions'
    console.error('Error loading sessions:', err)
  } finally {
    loading.value = false
  }
}

const viewSession = (sessionId: number) => {
  router.push(`/applications/${sessionId}`)
}

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  })
}

const getStatusClass = (status: string) => {
  switch (status) {
    case 'pending':
      return 'bg-yellow-100 text-yellow-800'
    case 'completed':
      return 'bg-green-100 text-green-800'
    case 'error':
      return 'bg-red-100 text-red-800'
    default:
      return 'bg-gray-100 text-gray-800'
  }
}

// Initialize
onMounted(() => {
  loadSessions()
})
</script>

<style scoped>
/* Add any custom styles here */
</style>
