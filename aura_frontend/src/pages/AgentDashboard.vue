<template>
  <NavBar />
  <div class="container mx-auto">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
      <!-- Left Column: Selections and Actions -->
      <div class="space-y-6">
        <!-- Carrier Selection -->
        <div>
          <label class="block font-bold font-helvetica">Select Carriers</label>
          <div class="mt-2">
            <div v-for="carrier in carriers" :key="carrier.id" class="flex items-center space-x-10">
              <input
                type="checkbox"
                :id="'carrier-' + carrier.id"
                :value="carrier.id"
                v-model="selectedCarriers"
                class="form-checkbox"
              />
              <label class="mx-2" :for="'carrier-' + carrier.id">
                {{ carrier.name }}
              </label>
            </div>
          </div>
        </div>

        <!-- Coverage Selection -->
        <div>
          <label class="block font-bold font-helvetica">Select Coverages</label>
          <div class="mt-2">
            <div
              v-for="coverage in coverages"
              :key="coverage.id"
              class="flex items-center space-x-2"
            >
              <input
                type="checkbox"
                :id="'coverage-' + coverage.id"
                :value="coverage.id"
                v-model="selectedCoverages"
                class="form-checkbox"
              />
              <label class="mx-2" :for="'coverage-' + coverage.id">
                {{ coverage.name }}
              </label>
            </div>
          </div>
        </div>

        <!-- Create Session Button -->
        <button
          class="transition-[.3ms] px-4 py-2 border-1 border-white bg-black text-white hover:bg-white hover:text-black"
          @click="handleCreateSession"
          :disabled="isLoading"
        >
          <span v-if="isLoading">...</span>
          <span v-else>Create Session +</span>
        </button>

        <!-- Generated Link -->
        <div v-if="generatedLink" class="mt-8">
          <p class="font-helvetica font-bold mb-2">Aura Public Link</p>
          <a :href="generatedLink" class="text-yellow-500 underline" target="_blank">
            {{ generatedLink }}
          </a>
        </div>
      </div>

      <!-- Right Column: Preview Questions -->
      <div class="questions-container p-4 pb-1 min-h-[300px]">
        <div v-if="questions.length">
          <div class="flex items-center justify-between mb-2">
            <h2 class="font-semibold">Preview Questions [{{ questions.length }}]</h2>
            <span v-if="lastPreviewRequestAt" class="flex items-center text-xs text-gray-400 gap-1">
              <svg class="w-3 h-3 mr-1 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                <circle cx="10" cy="10" r="10" />
              </svg>
              <div class="flex items-center gap-1">
                <span>Last updated: </span>
                {{ formatTimestamp(lastPreviewRequestAt) }}
              </div>
            </span>
          </div>
          <ul class="list-none p-0">
            <li class="mb-2 text-gray-400" v-for="q in questions" :key="q.id">{{ q.text }}</li>
          </ul>
        </div>
        <div v-else>
          <p class="text-gray-500">
            No questions to preview. Please select carriers and coverages.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import NavBar from '@/components/NavBar.vue'
import { fetchCarriers, fetchCoverageLines, createSession, previewQuestions } from '@/api/sessions'
import type { Carrier, CoverageLine, Question } from '@/types'

const carriers = ref<Carrier[]>([])
const coverages = ref<CoverageLine[]>([])

const selectedCarriers = ref<number[]>([])
const selectedCoverages = ref<number[]>([])
const generatedLink = ref<string>('')

// handle submit button state
const isLoading = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

const questions = ref<Question[]>([])
const lastPreviewRequestAt = ref<Date | null>(null)

function updatePreviewTimestamp() {
  lastPreviewRequestAt.value = new Date()
}

onMounted(async () => {
  carriers.value = await fetchCarriers()
  coverages.value = await fetchCoverageLines()

  try {
    questions.value = await previewQuestions(selectedCarriers.value, selectedCoverages.value)
    updatePreviewTimestamp()
  } catch (e) {
    questions.value = []
  }
})

// Watch for changes and update questions
watch([selectedCarriers, selectedCoverages], async () => {
  isLoading.value = true
  try {
    questions.value = await previewQuestions(selectedCarriers.value, selectedCoverages.value)
    updatePreviewTimestamp()
    isLoading.value = false
  } catch (e) {
    questions.value = []
    isLoading.value = false
  } finally {
    isLoading.value = false
  }
})

async function handleCreateSession() {
  isLoading.value = true
  try {
    const token = await createSession(selectedCarriers.value, selectedCoverages.value)
    if (token) {
      generatedLink.value = `http://127.0.0.1:8000/api/v1/fill/${token}`
    } else {
      generatedLink.value = ''
      errorMessage.value = 'No token was returned form API'
    }
  } catch (error) {
    errorMessage.value = 'Failed to create session. Please try again.'
    console.error(error)
  } finally {
    isLoading.value = false
  }
}

// Format helper for timestamp
function formatTimestamp(date: Date | null) {
  if (!date) return ''
  return date.toLocaleTimeString()
}
</script>

<style scoped>
.questions-container {
  border: 1px solid white;
  overflow-y: auto;
  max-height: 500px;
}
</style>
