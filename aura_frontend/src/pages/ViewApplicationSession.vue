<template>
  <Section title="Application Session Details" :loading="loading" :error="error">
    <div v-if="session">
      <h2 class="text-xl font-semibold mb-4">Session ID: {{ session.id }}</h2>
      <p><strong>Created At:</strong> {{ formatDate(session.created_at) }}</p>
      <p><strong>Status:</strong> <span :class="getStatusClass(session.status)">{{ session.status }}</span></p>
      <p><strong>Template:</strong> {{ session.template }}</p>

      <!-- Add more fields as necessary -->
    </div>
  </Section>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import Section from '@/components/Section.vue'
import { fetchApplicationSession } from '@/api/applications'
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
    session.value = await fetchApplicationSession(id)
    // Note: You may need to fetch template data separately if needed
    // templateData.value = await fetchApplicationTemplate(session.value.template)
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
      return 'bg-gray-200 text-gray-800'
  }
}

onMounted(() => {
  loadSession()
})
</script>

<style scoped>
/* Add any custom styles here */
</style>
