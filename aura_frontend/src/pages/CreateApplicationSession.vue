<template>
  <Section mode="dark">
    <router-link to="/agent" class="text-white underline underline-offset-5 mb-4">
      Back
    </router-link>
    <h1 class="text-2xl font-bold">Create Application</h1>
    <p>Start a new insurance application.</p>
  </Section>

  <!-- Step 1: Insurance Type Selection -->
  <Section v-if="currentStep === 1" mode="light">
    <h2 class="text-xl font-bold mb-4">Step 1: Insurance Type</h2>
    <div v-if="loading" class="text-gray-600">Loading insurance types...</div>
    <div v-else-if="error" class="text-red-600">{{ error }}</div>
    <div v-else class="space-y-3">
      <div v-for="type in insuranceTypes" :key="type.id" 
           class="p-4 border cursor-pointer hover:bg-gray-100"
           :class="{ 'bg-black text-white border-black': selectedInsuranceType?.id === type.id }"
           @click="selectInsuranceType(type)">
        <h3 class="font-semibold">{{ type.label }}</h3>
        <p class="text-sm" :class="selectedInsuranceType?.id === type.id ? 'text-gray-300' : 'text-gray-600'">{{ type.key }}</p>
      </div>
    </div>
  </Section>

  <!-- Step 2: Carrier Selection by Coverage -->
  <Section v-if="currentStep === 2" mode="light">
    <div class="flex items-center justify-between mb-4">
      <h2 class="text-xl font-bold">Step 2: Select Carriers</h2>
      <button @click="goBack" class="px-4 py-2 bg-gray-500 text-white hover:bg-gray-600">
        Back
      </button>
    </div>
    
    <div v-if="loadingCarriers" class="text-gray-600">Loading carriers...</div>
    <div v-else-if="carriersError" class="text-red-600">{{ carriersError }}</div>
    <div v-else class="space-y-6">
      <div v-for="coverageLine in carriersByCoverage" :key="coverageLine.coverage.id">
        <h3 class="text-lg font-semibold mb-3">
          {{ coverageLine.coverage.name }} ({{ coverageLine.coverage.abbreviation }})
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
          <div v-for="carrier in coverageLine.carriers" :key="carrier.id"
               class="p-3 border cursor-pointer hover:bg-black hover:text-white"
               :class="{ 'bg-black text-white border-black': isCarrierSelected(coverageLine.coverage.id, carrier.id) }"
               @click="toggleCarrier(coverageLine.coverage.id, carrier.id)">
            <div class="font-medium">{{ carrier.name }}</div>
          </div>
        </div>
      </div>
      
      <button v-if="hasSelections" 
              @click="nextStep" 
              class="px-6 py-2 bg-blue-600 text-white hover:bg-blue-699">
        Preview Questions
      </button>
    </div>
  </Section>

  <!-- Step 3: Question Preview -->
  <Section v-if="currentStep === 3" mode="light">
    <div class="flex items-center justify-between mb-4">
      <h2 class="text-xl font-bold">Question Preview</h2>
      <button @click="goBack" class="px-4 py-2 bg-gray-500 text-white hover:bg-gray-600">
        Back
      </button>
    </div>
    
    <div v-if="loadingPreview" class="text-gray-600">Loading questions preview...</div>
    <div v-else-if="previewError" class="text-red-600">{{ previewError }}</div>
    <div v-else>
      <div class="mb-4">
        <p class="text-lg">Total Questions: <strong>{{ questionPreview?.questions_count || 0 }}</strong></p>
      </div>
      
      <div class="space-y-3 mb-6">
        <div v-for="question in questionPreview?.questions" :key="question.id"
             class="p-4 border bg-white">
          <p class="font-medium">{{ question.text }}</p>
          <div class="mt-2 text-sm text-gray-600">
            <span class="mr-4">Carriers: {{ question.carriers.join(', ') }}</span>
            <span>Coverages: {{ question.coverages.join(', ') }}</span>
          </div>
        </div>
      </div>
      
      <div class="mb-4">
        <label for="sessionName" class="block text-sm font-medium text-gray-700 mb-2">
          Application Name
        </label>
        <input v-model="sessionName" 
               id="sessionName"
               type="text" 
               class="w-full p-3 border focus:ring-2 focus:ring-blue-500"
               placeholder="Enter application name">
      </div>
      
      <button @click="createApplication" 
              :disabled="!sessionName.trim() || creatingSession"
              class="px-6 py-2 bg-green-600 text-white hover:bg-green-700 disabled:bg-gray-400">
        {{ creatingSession ? 'Creating...' : 'Create Application' }}
      </button>
    </div>
  </Section>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Section from '@/components/Section.vue'
import { applicationsAPI } from '@/api/applications'
import type { CarriersByCoverageResponse, PreviewQuestionsResponse } from '@/api/applications'
import type { InsuranceType } from '@/types'

const router = useRouter()

// Step management
const currentStep = ref(1)
const maxStep = 3

// Step 1: Insurance Type Selection
const insuranceTypes = ref<InsuranceType[]>([])
const selectedInsuranceType = ref<InsuranceType | null>(null)
const loading = ref(false)
const error = ref('')

// Step 2: Carrier Selection
const carriersByCoverage = ref<CarriersByCoverageResponse['coverage_lines']>([])
const selectedCarriers = ref<Record<number, number[]>>({}) // coverage_id -> carrier_ids[]
const loadingCarriers = ref(false)
const carriersError = ref('')

// Step 3: Question Preview
const questionPreview = ref<PreviewQuestionsResponse | null>(null)
const sessionName = ref('')
const loadingPreview = ref(false)
const previewError = ref('')
const creatingSession = ref(false)

// Computed properties
const hasSelections = computed(() => {
  return Object.values(selectedCarriers.value).some(carriers => carriers.length > 0)
})

// Methods
const goBack = () => {
  if (currentStep.value > 1) {
    currentStep.value--
  }
}

const nextStep = () => {
  if (currentStep.value < maxStep) {
    currentStep.value++
    if (currentStep.value === 3) {
      loadQuestionPreview()
    }
  }
}

const selectInsuranceType = async (type: InsuranceType) => {
  selectedInsuranceType.value = type
  await loadCarriersByCoverage(type.id)
  nextStep()
}

const toggleCarrier = (coverageId: number, carrierId: number) => {
  if (!selectedCarriers.value[coverageId]) {
    selectedCarriers.value[coverageId] = []
  }
  
  const carriers = selectedCarriers.value[coverageId]
  const index = carriers.indexOf(carrierId)
  
  if (index > -1) {
    carriers.splice(index, 1)
  } else {
    carriers.push(carrierId)
  }
}

const isCarrierSelected = (coverageId: number, carrierId: number) => {
  return selectedCarriers.value[coverageId]?.includes(carrierId) || false
}

// API calls
const loadInsuranceTypes = async () => {
  loading.value = true
  error.value = ''
  try {
    insuranceTypes.value = await applicationsAPI.getInsuranceTypes()
    console.log('Loaded insurance types:', insuranceTypes.value)
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to load insurance types'
  } finally {
    loading.value = false
  }
}

const loadCarriersByCoverage = async (insuranceTypeId: number) => {
  loadingCarriers.value = true
  carriersError.value = ''
  try {
    const response = await applicationsAPI.getCarriersByCoverage(insuranceTypeId)
    carriersByCoverage.value = response.coverage_lines
    // Reset selections when changing insurance type
    selectedCarriers.value = {}
  } catch (err) {
    carriersError.value = err instanceof Error ? err.message : 'Failed to load carriers'
  } finally {
    loadingCarriers.value = false
  }
}

const loadQuestionPreview = async () => {
  if (!selectedInsuranceType.value) return
  
  loadingPreview.value = true
  previewError.value = ''
  
  try {
    // Collect all selected carrier IDs and coverage IDs
    const allCarrierIds: number[] = []
    const coverageIds: number[] = []
    
    Object.entries(selectedCarriers.value).forEach(([coverageId, carrierIds]) => {
      if (carrierIds.length > 0) {
        coverageIds.push(parseInt(coverageId))
        allCarrierIds.push(...carrierIds)
      }
    })
    
    if (allCarrierIds.length === 0 || coverageIds.length === 0) {
      previewError.value = 'Please select at least one carrier'
      return
    }
    
    questionPreview.value = await applicationsAPI.previewQuestions(
      selectedInsuranceType.value.id,
      allCarrierIds,
      coverageIds
    )
  } catch (err) {
    previewError.value = err instanceof Error ? err.message : 'Failed to load question preview'
  } finally {
    loadingPreview.value = false
  }
}

const createApplication = async () => {
  if (!selectedInsuranceType.value || !sessionName.value.trim()) return
  
  creatingSession.value = true
  
  try {
    // Format selections for API
    const selections = Object.entries(selectedCarriers.value)
      .filter(([, carrierIds]) => carrierIds.length > 0)
      .map(([coverageId, carrierIds]) => ({
        coverage_id: parseInt(coverageId),
        carrier_ids: carrierIds
      }))
    
    const response = await applicationsAPI.createApplicationSession({
      insurance_type_id: selectedInsuranceType.value.id,
      session_name: sessionName.value.trim(),
      selections
    })
    
    // Redirect to the created application session
    router.push(`/applications/${response.session.id}`)
  } catch (err) {
    const errorMessage = err instanceof Error ? err.message : 'Failed to create application'
    alert(errorMessage) // You might want to use a proper notification system
  } finally {
    creatingSession.value = false
  }
}

// Initialize
onMounted(() => {
  loadInsuranceTypes()
})
</script>

<style scoped>
/* Add any custom styles here */
</style>