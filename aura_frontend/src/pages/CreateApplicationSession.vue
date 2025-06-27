<template>
  <!-- Step 1: Insurance Type Selection -->
  <Section v-if="currentStep === 1" mode="light">
    <div class="flex items-center justify-between mb-10">
      <h2 class="text-2xl font-bold">Select Type</h2>
      <button @click="navigateToDashboard" class="px-4 py-2 bg-black text-white hover:bg-gray-500 duration-300">
        Cancel
      </button>
    </div>
    <div v-if="loading" class="text-gray-600">Loading insurance types...</div>
    <div v-else-if="error" class="text-red-600">{{ error }}</div>
    <div v-else class="space-y-3">
      <div
        v-for="type in insuranceTypes"
        :key="type.id"
        class="p-4 border cursor-pointer hover:bg-black hover:text-white duration-300"
        :class="{ 'bg-black text-white border-black': selectedInsuranceType?.id === type.id }"
        @click="selectInsuranceType(type)"
      >
        <h3>{{ type.label }}</h3>
      </div>
    </div>
  </Section>

  <!-- Step 2: Carrier Selection by Coverage -->
  <Section v-if="currentStep === 2" mode="light">
    <div class="flex items-center justify-between mb-10">
      <h2 class="text-2xl font-bold">Select Carriers</h2>
      <button @click="goBack" class="px-4 py-2 bg-black text-white hover:bg-gray-500 duration-300">
        Back
      </button>
    </div>

    <div v-if="loadingCarriers" class="text-gray-600">Loading carriers...</div>
    <div v-else-if="carriersError" class="text-red-600">{{ carriersError }}</div>
    <div v-else class="space-y-6 flex flex-col gap-10">
      <div v-for="coverageLine in carriersByCoverage" :key="coverageLine.coverage.id">
        <div class="flex gap-2 items-center mb-10">
          <InsuranceTypeBox :coverage="coverageLine.coverage" />
          <h3 class="text-lg font-semibold">
            {{ coverageLine.coverage.name }}
          </h3>
        </div>

        <div class="grid grid-cols-2 lg:grid-cols-3">
          <div
            v-for="carrier in coverageLine.carriers"
            :key="carrier.id"
            class="p-3 cursor-pointer hover:bg-black hover:text-white duration-300"
            :class="{
              'bg-black text-white': isCarrierSelected(
                coverageLine.coverage.id,
                carrier.id,
              ),
              'bg-gray-100': !isCarrierSelected(coverageLine.coverage.id, carrier.id),
            }"
            @click="toggleCarrier(coverageLine.coverage.id, carrier.id)"
          >
            <div class="font-medium">{{ carrier.name }}</div>
          </div>
        </div>
      </div>

      <button
        :disabled="!hasSelections"
        @click="nextStep"
        class="p-10 w-full bg-green-600 text-white hover:bg-green-700 disabled:bg-gray-400 duration-300"
      >
        Preview Questions
      </button>
    </div>
  </Section>

  <!-- Step 3: Question Preview -->
  <Section v-if="currentStep === 3" mode="light">
    <div class="flex items-center justify-between mb-10">
      <h2 class="text-2xl font-bold">Questions Preview</h2>
      <button @click="goBack" class="px-4 py-2 bg-black text-white hover:bg-gray-500 duration-300">
        Back
      </button>
    </div>

    <div v-if="loadingPreview" class="text-gray-500">Loading questions preview...</div>
    <div v-else-if="previewError" class="text-red-600">{{ previewError }}</div>
    <div v-else>
      <div class="mb-10">
        <input
          v-model="sessionName"
          id="sessionName"
          type="text"
          class="w-full p-3 border-b bg-gray-100 focus:ring-2 focus:ring-blue-500"
          placeholder="Enter application name"
        />

        <div class="mt-5">
          <button
            @click="createApplication"
            :disabled="!sessionName.trim() || creatingSession"
            class="p-10 w-full bg-green-600 text-white hover:bg-green-700 disabled:bg-gray-400 duration-300"
          >
            {{ creatingSession ? 'Creating...' : 'Create Application' }}
          </button>
        </div>
      </div>

      <div class="mb-10 flex flex-col gap-5 md:max-w-1/3 w-full">
        <div class="flex justify-between border-b items-baseline">
          <div class="label">Question Count</div>
          <div class="value"><span class="text-4xl">{{ questionPreview?.questions_count || 0 }}</span> ques</div>
        </div>
        
        <div class="flex justify-between border-b items-baseline">
          <div class="label">Estimated Burden</div>
          <div class="value"><span class="text-4xl">{{ estimatedTime || 0 }}</span> mins</div>
        </div>
      </div>

      <div class="flex flex-col">
        <div
          v-for="question in questionPreview?.questions"
          :key="question.id"
          class="border-b-1 p-3 flex flex-col md:flex-row md:items-stretch gap-2 md:gap-4"
        >
          <!-- Question text -->
          <p class="font-semibold min-w-0 w-full md:w-auto md:flex-1 md:max-w-[75%]">
            {{ question.text }}
          </p>

          <!-- Coverages -->
          <div
            class="flex flex-wrap gap-1 w-full md:w-[160px] flex-shrink-0"
          >
            <InsuranceTypeBox
              v-for="coverage in question.coverages"
              :key="coverage.name"
              :coverage="coverage"
            />
          </div>

          <!-- Carriers -->
          <div
            class="text-sm text-gray-600 w-full md:w-[160px] flex-shrink-0"
          >
            <template v-if="question.carriers && question.carriers.length">
              <span class="hidden md:flex flex-wrap gap-2">
                <span v-for="carrier in question.carriers" :key="carrier">{{ carrier }}</span>
              </span>
              <span class="md:hidden">
                {{ question.carriers.join(', ') }}
              </span>
            </template>
          </div>
        </div>
      </div>
    </div>
  </Section>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import NavBar from '@/components/NavBar.vue'
import Section from '@/components/Section.vue'
import InsuranceTypeBox from '@/components/InsuranceTypeBox.vue'
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
// Time estimation constants
const timePerQuestion = 15 // seconds per question (you can adjust this)

// Computed properties
const hasSelections = computed(() => {
  return Object.values(selectedCarriers.value).some((carriers) => carriers.length > 0)
})

const estimatedTime = computed(() => {
  const totalQuestions = questionPreview.value?.questions_count || 0
  const totalSeconds = totalQuestions * timePerQuestion
  const minutes = Math.ceil(totalSeconds / 60)
  
  return minutes
})

// Methods

const navigateToDashboard = () => {
  router.push('/agent')
}

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
      coverageIds,
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
        carrier_ids: carrierIds,
      }))

    const response = await applicationsAPI.createApplicationSession({
      insurance_type_id: selectedInsuranceType.value.id,
      session_name: sessionName.value.trim(),
      selections,
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
