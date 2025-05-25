<template>
  <div class="container mx-auto p-6 space-y-6">
    <h1 class="text-2xl font-bold">Agent Dashboard</h1>
    <p>Create → Track → Complete</p>

    <!-- Carrier Selection -->
    <div>
      <label class="block font-medium">Select Carriers</label>
      <div class="mt-4">
        <div
          v-for="carrier in carriers"
          :key="carrier.id"
          class="flex items-center space-x-10"
        >
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
      <label class="block font-medium">Select Coverages</label>
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

    <!-- Preview Questions Section -->
    <div v-if="questions.length" class="mt-6">
      <h2 class="font-semibold">Preview Questions</h2>
      <ul class="list-disc ml-6">
        <li v-for="q in questions" :key="q.id">{{ q.text }}</li>
      </ul>
    </div>

    <!-- Create Session Button -->
    <button
      class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      @click="handleCreateSession"
    >
      Create Session
    </button>

    <!-- Generated Link -->
    <div v-if="generatedLink" class="mt-4">
      <p class="font-semibold">Form Link:</p>
      <a :href="generatedLink" class="text-blue-600 underline" target="_blank">
        {{ generatedLink }}
      </a>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { fetchCarriers, fetchCoverageLines, createSession, previewQuestions } from '@/api/sessions'
import type { Carrier, CoverageLine, Question } from '@/types'

const carriers = ref<Carrier[]>([])
const coverages = ref<CoverageLine[]>([])

const selectedCarriers = ref<number[]>([])
const selectedCoverages = ref<number[]>([])
const generatedLink = ref<string>('')

const questions = ref<Question[]>([])

onMounted(async () => {
  carriers.value = await fetchCarriers()
  coverages.value = await fetchCoverageLines()
})

// Watch for changes and update questions
watch([selectedCarriers, selectedCoverages], async () => {
  if (selectedCarriers.value.length || selectedCoverages.value.length) {
    try {
      questions.value = await previewQuestions(selectedCarriers.value, selectedCoverages.value)
    } catch (e) {
      questions.value = []
    }
  } else {
    questions.value = []
  }
})

async function handleCreateSession() {
  try {
    const token = await createSession(selectedCarriers.value, selectedCoverages.value)
    if (token) {
      generatedLink.value = `http://127.0.0.1:8000/api/v1/fill/${token}`
    } else {
      generatedLink.value = ''
      alert('No token returned from API')
    }
  } catch (error) {
    alert('Failed to create session')
    console.error(error)
  }
}
</script>