<template>
  <NavBar />
  <div class="page-spacer bg-black"></div>
  <Breadcrumbs />

  <Section mode="light" padding="small">
    <div class="flex flex-col md:flex-row justify-between md:items-center md:gap-0 gap-5">
      <div class="flex flex-col">
        <div class="text-5xl font-bold">Applications</div>
        <div class="text-gray-600 text-sm">
          Showing {{ startIndex }}–{{ endIndex }} of {{ applicationsResponse?.count || 0 }} applications
        </div>
      </div>
    </div>

    <div class="mt-10 border-t-1 flex flex-col">
      <div v-if="loading" class="p-4 text-gray-600">Loading...</div>
      <div v-else-if="error" class="p-4 text-red-600">{{ error }}</div>
      <div v-else-if="!sessions.length" class="flex flex-col justify-center items-center p-4">
        <div class="text-gray-600">No applications found.</div>
        <router-link to="/applications/create" class="mt-2 underline underline-offset-2 font-semibold">
          + Create application
        </router-link>
      </div>
      <div v-else>
        <div>
          <div
            v-for="session in sessions"
            :key="session.id"
            class="p-2 py-3 border-b-1 flex flex-col md:flex-row md:items-stretch gap-2 md:gap-4 hover:bg-black hover:text-white duration-200 cursor-pointer"
            @click="viewSession(session.id)"
          >
            <!-- Application Name -->
            <p class="font-semibold min-w-0 w-full md:w-auto md:flex-1 md:max-w-[75%]">
              {{ session.name || 'Untitled Application' }}
            </p>
            <!-- Created Date -->
            <div class="text-sm text-gray-600 w-full md:w-[160px] flex-shrink-0">
              {{ formatDate(session.created_at) }}
            </div>
            <!-- Status -->
            <div class="text-right w-full md:w-[120px] flex-shrink-0">
              <span
                class="inline-block px-3 py-1 rounded-full text-sm font-medium"
                :class="getStatusClass(session.status)"
              >
                {{ session.status }}
              </span>
            </div>
          </div>
        </div>

        <!-- Pagination Controls -->
        <div class="flex justify-between items-center mt-4">
          <button
            @click="goToPreviousPage"
            :disabled="!applicationsResponse?.previous || currentPage === 1"
            class="underline underline-offset-2 disabled:opacity-50"
          >
            Previous
          </button>
          {{ currentPage }} / {{ Math.ceil(applicationsResponse?.count / pageSize) || 1 }}
          <button
            @click="goToNextPage"
            :disabled="!applicationsResponse?.next"
            class="underline underline-offset-2 disabled:opacity-50"
          >
            Next
          </button>
        </div>
      </div>
    </div>
  </Section>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import Breadcrumbs from '@/components/Breadcrumbs.vue'
import NavBar from '@/components/NavBar.vue'
import Section from '@/components/Section.vue'
import { useRouter } from 'vue-router'
import type { ApplicationSession } from '@/types'
import { fetchApplicationSessions, type ApplicationSessionsResponse } from '@/api/applications'

const router = useRouter()
const applicationsResponse = ref<ApplicationSessionsResponse | null>(null)
const sessions = ref<ApplicationSession[]>([])
const loading = ref(false)
const error = ref('')
const currentPage = ref(1)

const loadSessions = async (page = 1) => {
  loading.value = true
  error.value = ''
  try {
    const response = await fetchApplicationSessions({ page })
    applicationsResponse.value = response
    sessions.value = response.results
    currentPage.value = page
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to load applications'
  } finally {
    loading.value = false
  }
}

const goToNextPage = () => {
  if (applicationsResponse.value?.next) {
    loadSessions(currentPage.value + 1)
  }
}

const goToPreviousPage = () => {
  if (applicationsResponse.value?.previous && currentPage.value > 1) {
    loadSessions(currentPage.value - 1)
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
      return 'bg-gray-200 text-gray-800'
  }
}

const pageSize = computed(() => sessions.value.length || 10)
const startIndex = computed(() => (sessions.value.length ? (currentPage.value - 1) * pageSize.value + 1 : 0))
const endIndex = computed(() => (sessions.value.length ? startIndex.value + sessions.value.length - 1 : 0))

onMounted(() => loadSessions())
</script>
<style scoped>
/* Add any custom styles here if needed */
</style>
