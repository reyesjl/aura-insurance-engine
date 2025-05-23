<template>
  <div class="container mx-auto p-6 space-y-6">
    <h1 class="text-2xl font-bold">Agent Dashboard</h1>
    <p>Create → Track → Complete</p>

    <!-- Carrier Selection -->
    <div>
      <label class="block font-medium">Select Carriers:</label>
      <div class="space-y-2">
        <div
          v-for="carrier in carriers"
          :key="carrier.id"
          class="flex items-center space-x-2"
        >
          <input
            type="checkbox"
            :id="'carrier-' + carrier.id"
            :value="carrier.id"
            v-model="selectedCarriers"
            class="form-checkbox"
          />
          <label :for="'carrier-' + carrier.id">
            {{ carrier.name }}
          </label>
        </div>
      </div>
    </div>

    <!-- Coverage Selection -->
    <div>
      <label class="block font-medium">Select Coverages:</label>
      <div class="space-y-2">
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
          <label :for="'coverage-' + coverage.id">
            {{ coverage.name }}
          </label>
        </div>
      </div>
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
import { ref, onMounted } from 'vue'
import { fetchCarriers, fetchCoverageLines, createSession } from '@/api/sessions'
import type { Carrier, CoverageLine } from '@/types'

const carriers = ref<Carrier[]>([])
const coverages = ref<CoverageLine[]>([])

const selectedCarriers = ref<number[]>([])
const selectedCoverages = ref<number[]>([])
const generatedLink = ref<string>('')

onMounted(async () => {
  carriers.value = await fetchCarriers()
  coverages.value = await fetchCoverageLines()
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