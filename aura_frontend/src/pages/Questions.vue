<template>
<NavBar />
<div class="page-spacer bg-black"></div>
<Breadcrumbs />

<Section mode="light" padding="small">
  <div class="flex flex-col md:flex-row justify-between md:items-center md:gap-0 gap-5">
    <div class="flex flex-col">
      <div class="text-5xl font-bold">Questions</div>
      <div class="text-gray-600 text-sm">
        Showing {{ startIndex }}–{{ endIndex }} of {{ questionsResponse?.count || 0 }} questions
      </div>
    </div>
    <input
      id="searchQuestionText"
      type="text"
      placeholder="Type question here..."
      class="p-4 border-b-1 bg-gray-100 w-full md:w-1/3"
      v-model="searchText"
    />
  </div>

  <div class="mt-10 border-t-1 flex flex-col">
    <div v-if="loading" class="p-4 text-gray-600">Loading...</div>
    <div v-else-if="error" class="p-4 text-red-600">{{ error }}</div>
    <div v-else-if="!questions.length" class="flex flex-col justify-center items-center p-4">
      <div class="text-gray-600">No questions found.</div>
      <router-link to="/questions/create" class="mt-2 underline underline-offset-2 font-semibold">+ Create question</router-link>
    </div>
    <div v-else>
     <div>
        <div
          v-for="question in questions"
          :key="question.id"
          class="question p-2 py-3 border-b-1 flex flex-col md:flex-row md:items-stretch gap-2 md:gap-4 hover:bg-black hover:text-white duration-200"
        >
          <!-- Question text -->
          <p class="font-semibold min-w-0 w-full md:w-auto md:flex-1 md:max-w-[75%]">
            {{ question.text }}
          </p>

          <!-- Coverages -->
          <div class="flex flex-wrap gap-1 w-full md:w-[160px] flex-shrink-0">
            <InsuranceTypeBox
              v-for="coverage in question.coverages"
              :key="coverage.id"
              :coverage="coverage"
            />
          </div>

          <!-- Carriers -->
          <div
            class="text-sm text-gray-600 w-full md:w-[160px] flex-shrink-0"
          >
            <template v-if="question.carriers && question.carriers.length">
              <span class="hidden md:flex flex-wrap gap-2">
                <span v-for="carrier in question.carriers" :key="carrier.id">{{ carrier.name }}</span>
              </span>
              <span class="md:hidden">
                {{ question.carriers.map(carrier => carrier.name).join(', ') }}
              </span>
            </template>
          </div>
        </div>
     </div>
        
      <div class="flex justify-between mt-10 text-sm mx-auto md:w-3/4 font-semibold">
        <button
          @click="goToPreviousPage"
          :disabled="!questionsResponse?.previous"
          class="underline underline-offset-2 disabled:opacity-50"
        >
          Previous
        </button>
        {{ currentPage }} / {{ Math.ceil(questionsResponse?.count / pageSize) || 1 }}
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
import { ref, onMounted, watch, computed } from 'vue';
import Breadcrumbs from '@/components/Breadcrumbs.vue';
import NavBar from '@/components/NavBar.vue';
import Section from '@/components/Section.vue';
import InsuranceTypeBox from '@/components/InsuranceTypeBox.vue';
import type { Question } from '@/types';
import { fetchQuestions, type QuestionsResponse } from '@/api/questions';

const questionsResponse = ref<QuestionsResponse | null>(null);
const questions = ref<Question[]>([]);
const loading = ref(false);
const error = ref<string | null>(null);
const currentPage = ref(1);
const searchText = ref('');

onMounted(() => {
  loadQuestions();
});

const loadQuestions = async (page = 1, search = '') => {
  loading.value = true;
  error.value = null;
  try {
    const params: Record<string, any> = { page };
    if (search) params.search = search;
    const response = await fetchQuestions(params);
    questionsResponse.value = response;
    questions.value = response.results;
    currentPage.value = page;
  } catch (err) {
    error.value = 'Failed to fetch questions';
  } finally {
    loading.value = false;
  }
}

const goToNextPage = () => {
  if (questionsResponse.value?.next) {
    loadQuestions(currentPage.value + 1, searchText.value);
  }
}

const goToPreviousPage = () => {
  if (questionsResponse.value?.previous && currentPage.value > 1) {
    loadQuestions(currentPage.value - 1, searchText.value);
  }
}


let searchTimeout: ReturnType<typeof setTimeout> | null = null;
watch(searchText, (newVal) => {
  if (searchTimeout) clearTimeout(searchTimeout);
  searchTimeout = setTimeout(() => {
    loadQuestions(1, newVal);
  }, 500);
});

const pageSize = computed(() => questions.value.length || 10);
const startIndex = computed(() => (questions.value.length ? (currentPage.value - 1) * pageSize.value + 1 : 0));
const endIndex = computed(() => (questions.value.length ? startIndex.value + questions.value.length - 1 : 0));
</script>
<style scoped>
/* You can add more custom styles here if needed */
</style>