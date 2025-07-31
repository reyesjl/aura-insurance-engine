<template>
  <NavBar />
  <div class="page-spacer bg-black"></div>
  <Breadcrumbs />

  <Section mode="light" padding="small">
    <div class="flex flex-col md:flex-row justify-between md:items-center gap-8 mb-12">
      <div class="flex flex-col gap-3">
        <div class="text-4xl md:text-5xl font-semibold leading-tight">Questions</div>
        <div class="text-base opacity-80">
          Showing {{ startIndex }}–{{ endIndex }} of {{ questionsResponse?.count || 0 }} questions
        </div>
      </div>
      <input
        id="searchQuestionText"
        type="text"
        placeholder="Type question here..."
        class="p-4 border-b border-gray-300 bg-gray-100 w-full md:w-1/3 rounded-lg text-base focus:ring-2 focus:ring-blue-500"
        v-model="searchText"
      />
    </div>

    <div class="border-t border-gray-200 flex flex-col">
      <div v-if="loading" class="p-6 text-base opacity-80">Loading...</div>
      <div v-else-if="error" class="p-6 text-red-600 text-base">{{ error }}</div>
      <div
        v-else-if="!questions.length"
        class="flex flex-col justify-center items-center p-8 gap-4"
      >
        <div class="text-base opacity-80">No questions found.</div>
        <router-link
          to="/questions/create"
          class="text-lg underline underline-offset-4 hover:underline-offset-6 transition-all font-semibold"
          >+ Create question</router-link
        >
      </div>
      <div v-else>
        <div>
          <div
            v-for="question in questions"
            :key="question.id"
            class="question p-6 border-b border-gray-200 flex flex-col md:flex-row md:items-stretch gap-4 hover:bg-black hover:text-white duration-200 cursor-pointer rounded-lg"
            :class="{ 'bg-beige-200': selectedQuestionIds.includes(question.id) }"
            @click="toggleQuestionSelection(question.id)"
          >
            <div class="flex mt-2 md:mt-0 justify-end md:justify-start">
              <!-- Custom Checkbox -->
              <div
                class="border-2 border-black h-4 w-4 mr-2 flex items-center justify-center"
                :class="{ 'bg-black': selectedQuestionIds.includes(question.id) }"
              ></div>
            </div>

            <!-- Question text -->
            <p
              class="text-lg font-semibold min-w-0 w-full md:w-auto md:flex-1 md:max-w-[75%] leading-relaxed"
            >
              {{ question.text }}
            </p>

            <!-- Coverages -->
            <div class="flex flex-wrap gap-2 w-full md:w-[160px] flex-shrink-0">
              <InsuranceTypeBox
                v-for="coverage in question.coverages"
                :key="coverage.id"
                :coverage="coverage"
              />
            </div>

            <!-- Carriers -->
            <div class="text-base opacity-80 w-full md:w-[160px] flex-shrink-0">
              <template v-if="question.carriers && question.carriers.length">
                <span class="hidden md:flex flex-wrap gap-2">
                  <span v-for="carrier in question.carriers" :key="carrier.id">{{
                    carrier.name
                  }}</span>
                </span>
                <span class="md:hidden">
                  {{ question.carriers.map((carrier) => carrier.name).join(', ') }}
                </span>
              </template>
            </div>
          </div>
        </div>

        <div class="flex justify-between items-center mt-8 pt-6 border-t border-gray-200">
          <button
            @click="goToPreviousPage"
            :disabled="!questionsResponse?.previous"
            class="underline underline-offset-2 disabled:opacity-50"
          >
            Previous
          </button>
          {{ currentPage }} / {{ Math.ceil((questionsResponse?.count ?? 0) / pageSize) || 1 }}
          <button
            @click="goToNextPage"
            :disabled="!questionsResponse?.next"
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
import { fetchQuestions, type QuestionsResponse } from '@/api/questions'
import Breadcrumbs from '@/components/Breadcrumbs.vue'
import InsuranceTypeBox from '@/components/InsuranceTypeBox.vue'
import NavBar from '@/components/NavBar.vue'
import Section from '@/components/Section.vue'
import type { Question } from '@/types'
import { computed, onMounted, ref, watch } from 'vue'

const selectedQuestionId = ref<number | null>(null)
const selectedQuestionIds = ref<number[]>([])

const questionsResponse = ref<QuestionsResponse | null>(null)
const questions = ref<Question[]>([])
const loading = ref(false)
const error = ref<string | null>(null)
const currentPage = ref(1)
const searchText = ref('')

onMounted(() => {
  loadQuestions()
})

const loadQuestions = async (page = 1, search = '') => {
  loading.value = true
  error.value = null
  try {
    const params: Record<string, any> = { page }
    if (search) params.search = search
    const response = await fetchQuestions(params)
    questionsResponse.value = response
    questions.value = response.results
    currentPage.value = page
  } catch (err) {
    error.value = 'Failed to fetch questions'
  } finally {
    loading.value = false
  }
}

const goToNextPage = () => {
  if (questionsResponse.value?.next) {
    loadQuestions(currentPage.value + 1, searchText.value)
  }
}

const goToPreviousPage = () => {
  if (questionsResponse.value?.previous && currentPage.value > 1) {
    loadQuestions(currentPage.value - 1, searchText.value)
  }
}

let searchTimeout: ReturnType<typeof setTimeout> | null = null
watch(searchText, (newVal) => {
  if (searchTimeout) clearTimeout(searchTimeout)
  searchTimeout = setTimeout(() => {
    loadQuestions(1, newVal)
  }, 500)
})

const pageSize = computed(() => questions.value.length || 10)
const startIndex = computed(() =>
  questions.value.length ? (currentPage.value - 1) * pageSize.value + 1 : 0,
)
const endIndex = computed(() =>
  questions.value.length ? startIndex.value + questions.value.length - 1 : 0,
)

// Toggle selection for a question
const toggleQuestionSelection = (id: number) => {
  const idx = selectedQuestionIds.value.indexOf(id)
  if (idx === -1) {
    selectedQuestionIds.value.push(id)
  } else {
    selectedQuestionIds.value.splice(idx, 1)
  }
}
</script>
<style scoped>
/* You can add more custom styles here if needed */
</style>
