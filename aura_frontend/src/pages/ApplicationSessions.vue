<template>
  <NavBar />
  <div class="page-spacer bg-black"></div>
  <Breadcrumbs />

  <Section mode="light" padding="small">
    <div class="flex flex-col md:flex-row justify-between md:items-center gap-8 mb-12">
      <div class="flex flex-col gap-3">
        <div class="text-4xl md:text-5xl font-semibold leading-tight">Applications</div>
        <div class="text-base opacity-80">
          Showing {{ startIndex }}–{{ endIndex }} of
          {{ applicationsResponse?.count || 0 }} applications
        </div>
      </div>
    </div>

    <div class="border-t border-gray-200 flex flex-col">
      <div v-if="loading" class="p-6 text-base opacity-80">Loading...</div>
      <div v-else-if="error" class="p-6 text-red-600 text-base">{{ error }}</div>
      <div v-else-if="!sessions.length" class="flex flex-col justify-center items-center p-8 gap-4">
        <div class="text-base opacity-80">No applications found.</div>
        <router-link
          to="/applications/create"
          class="text-lg underline underline-offset-4 hover:underline-offset-6 transition-all font-semibold"
        >
          + Create application
        </router-link>
      </div>
      <div v-else>
        <div>
          <div
            v-for="session in sessions"
            :key="session.id"
            class="p-6 border-b border-gray-200 flex flex-col md:flex-row md:items-stretch gap-4 hover:bg-black hover:text-white duration-200 cursor-pointer rounded-lg"
            @click="viewSession(session.id)"
          >
            <!-- Application Name -->
            <p
              class="text-lg font-semibold min-w-0 w-full md:w-auto md:flex-1 md:max-w-[75%] leading-relaxed"
            >
              {{ session.name || 'Untitled Application' }}
            </p>
            <!-- Created Date -->
            <div class="text-base opacity-80 w-full md:w-[160px] flex-shrink-0">
              {{ formatDate(session.created_at) }}
            </div>
            <!-- Status -->
            <div class="text-right w-full md:w-[120px] flex-shrink-0">
              <span
                class="inline-block px-4 py-2 rounded-full text-sm font-medium"
                :class="getStatusClass(session.status)"
              >
                {{ session.status }}
              </span>
            </div>
          </div>
        </div>

        <!-- Pagination Controls -->
        <div class="flex justify-between items-center mt-8 pt-6 border-t border-gray-200">
          <button
            @click="goToPreviousPage"
            :disabled="!applicationsResponse?.previous || currentPage === 1"
            class="text-lg underline underline-offset-4 hover:underline-offset-6 transition-all disabled:opacity-50"
          >
            Previous
          </button>
          <span class="text-base opacity-80">
            {{ currentPage }} / {{ Math.ceil((applicationsResponse?.count ?? 0) / pageSize) || 1 }}
          </span>
          <button
            @click="goToNextPage"
            :disabled="!applicationsResponse?.next"
            class="text-lg underline underline-offset-4 hover:underline-offset-6 transition-all disabled:opacity-50"
          >
            Next
          </button>
        </div>
      </div>
    </div>
  </Section>
</template>

<script setup lang="ts">
import { fetchApplicationSessions, type ApplicationSessionsResponse } from '@/api/applications'
import Breadcrumbs from '@/components/Breadcrumbs.vue'
import NavBar from '@/components/NavBar.vue'
import Section from '@/components/Section.vue'
import type { ApplicationSession } from '@/types'
import { computed, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

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
const startIndex = computed(() =>
  sessions.value.length ? (currentPage.value - 1) * pageSize.value + 1 : 0,
)
const endIndex = computed(() =>
  sessions.value.length ? startIndex.value + sessions.value.length - 1 : 0,
)

onMounted(() => loadSessions())
</script>
<style scoped>
/* Add any custom styles here if needed */
</style>
