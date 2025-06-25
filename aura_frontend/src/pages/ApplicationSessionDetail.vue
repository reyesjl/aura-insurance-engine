<template>
  <Section mode="dark">
    <router-link
      to="/applications"
      class="text-white underline underline-offset-4 mb-4 inline-block"
    >
      Back
    </router-link>
    <h1 class="text-2xl font-bold">Application Details</h1>
    <p>View and manage this insurance application session.</p>
  </Section>

  <Section mode="light">
    <div v-if="loading" class="text-gray-600">Loading application details...</div>
    <div v-else-if="error" class="text-red-600 p-4 bg-red-50 border border-red-200 rounded">
      {{ error }}
    </div>
    <div v-else-if="session" class="space-y-6">
      <!-- Session Overview -->
      <div class="bg-white p-6 border rounded-lg">
        <h2 class="text-xl font-semibold mb-4">Session Overview</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="text-sm font-medium text-gray-600">Session Name</label>
            <p class="text-lg">{{ session.name || 'Unnamed Session' }}</p>
          </div>
          <div>
            <label class="text-sm font-medium text-gray-600">Status</label>
            <span
              class="inline-block px-3 py-1 text-sm rounded-full"
              :class="getStatusClass(session.status)"
            >
              {{ session.status.charAt(0).toUpperCase() + session.status.slice(1) }}
            </span>
          </div>
          <div>
            <label class="text-sm font-medium text-gray-600">Created</label>
            <p>{{ formatDate(session.created_at) }}</p>
          </div>
          <div>
            <label class="text-sm font-medium text-gray-600">Session ID</label>
            <p>{{ session.id }}</p>
          </div>
          <div>
            <label class="text-sm font-medium text-gray-600">Template ID</label>
            <p>{{ session.template }}</p>
          </div>
          <div>
            <label class="text-sm font-medium text-gray-600">Token</label>
            <p class="font-mono text-sm break-all">{{ session.token }}</p>
          </div>
        </div>
      </div>

      <!-- Template Information -->
      <div class="bg-white p-6 border rounded-lg" v-if="templateData">
        <h2 class="text-xl font-semibold mb-4">Template Information</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="text-sm font-medium text-gray-600">Template Name</label>
            <p>{{ templateData.name }}</p>
          </div>
          <div>
            <label class="text-sm font-medium text-gray-600">Insurance Type</label>
            <p>{{ templateData.insurance_type?.label || 'N/A' }}</p>
          </div>
        </div>

        <!-- Carriers -->
        <div class="mt-4" v-if="templateData.carriers && templateData.carriers.length > 0">
          <label class="text-sm font-medium text-gray-600">Selected Carriers</label>
          <div class="flex flex-wrap gap-2 mt-2">
            <span
              v-for="carrier in templateData.carriers"
              :key="carrier.id"
              class="px-3 py-1 bg-blue-100 text-blue-800 text-sm rounded-full"
            >
              {{ carrier.name }}
            </span>
          </div>
        </div>

        <!-- Coverages -->
        <div class="mt-4" v-if="templateData.coverages && templateData.coverages.length > 0">
          <label class="text-sm font-medium text-gray-600">Coverage Lines</label>
          <div class="flex flex-wrap gap-2 mt-2">
            <span
              v-for="coverage in templateData.coverages"
              :key="coverage.id"
              class="px-3 py-1 bg-green-100 text-green-800 text-sm rounded-full"
            >
              {{ coverage.name }} ({{ coverage.abbreviation }})
            </span>
          </div>
        </div>
      </div>

      <!-- Questions Summary -->
      <div class="bg-white p-6 border rounded-lg" v-if="templateData?.question_snapshots">
        <h2 class="text-xl font-semibold mb-4">
          Questions ({{ templateData.question_snapshots.length }})
        </h2>
        <div class="space-y-3">
          <div
            v-for="(question, index) in templateData.question_snapshots"
            :key="question.id"
            class="p-4 border border-gray-200 rounded"
          >
            <div class="flex items-start justify-between">
              <div class="flex-1">
                <span class="text-sm font-medium text-gray-500">Question {{ index + 1 }}</span>
                <p class="mt-1">{{ question.question_text }}</p>
              </div>
              <div class="ml-4 text-sm text-gray-500">ID: {{ question.id }}</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Actions -->
      <div class="bg-white p-6 border rounded-lg">
        <h2 class="text-xl font-semibold mb-4">Actions</h2>
        <div class="flex flex-wrap gap-3">
          <button
            v-if="session.status === 'pending'"
            class="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700"
          >
            Start Application
          </button>
          <button class="px-4 py-2 bg-gray-600 text-white rounded hover:bg-gray-700">
            Export Data
          </button>
          <button
            v-if="session.status !== 'completed'"
            class="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
          >
            Delete Session
          </button>
        </div>
      </div>
    </div>
  </Section>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import Section from '@/components/Section.vue'
import { applicationsAPI } from '@/api/applications'
import type { ApplicationSession } from '@/types'

// Define props (in case sessionId is passed as prop)
const props = defineProps<{
  sessionId?: string | number
}>()

const route = useRoute()

// Get session ID from props or route params
const sessionId = computed(() => {
  if (props.sessionId) {
    return typeof props.sessionId === 'string' ? parseInt(props.sessionId) : props.sessionId
  }
  return parseInt(route.params.id as string)
})

const session = ref<ApplicationSession | null>(null)
const templateData = ref<any>(null) // We'll need to fetch template data separately
const loading = ref(false)
const error = ref('')

const loadSession = async () => {
  const id = sessionId.value

  if (!id || isNaN(id)) {
    error.value = 'Invalid session ID'
    return
  }

  loading.value = true
  error.value = ''

  try {
    session.value = await applicationsAPI.getApplicationSession(id)
    // Note: You may need to fetch template data separately if needed
    // templateData.value = await applicationsAPI.getApplicationTemplate(session.value.template)
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to load application session'
    console.error('Failed to load session:', err)
  } finally {
    loading.value = false
  }
}

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
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

onMounted(() => {
  loadSession()
})
</script>

<style scoped>
/* Add any custom styles here */
</style>
