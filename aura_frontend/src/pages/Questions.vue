<template>
<NavBar />
<div class="page-spacer bg-black"></div>
<Breadcrumbs />

<Section mode="light" padding="small">
  <div class="flex flex-col md:flex-row justify-between md:items-center md:gap-0 gap-5">
    <div class="flex flex-col">
      <div class="text-5xl font-bold">Questions</div>
      <div class="text-gray-600 text-sm">{{ questions.length }} of {{ questionsResponse?.count || 0 }} questions shown</div>
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
      <router-link to="/applications/create" class="mt-2 underline underline-offset-2 font-semibold">+ Create question</router-link>
    </div>
    <div v-else>
     <div>
        <div
          v-for="question in questions"
          :key="question.id"
          class="question p-2 py-3 border-b-1 hover:bg-black hover:text-white duration-200"
        >
          {{ question.text }}
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
import { ref, onMounted, watch } from 'vue';
import Breadcrumbs from '@/components/Breadcrumbs.vue';
import NavBar from '@/components/NavBar.vue';
import Section from '@/components/Section.vue';
import type { Question, InsuranceType } from '@/types';
import { applicationsAPI } from '@/api/applications'
import { fetchQuestions, type QuestionsResponse } from '@/api/questions';

const questionsResponse = ref<QuestionsResponse | null>(null);
const questions = ref<Question[]>([]);
const loading = ref(false);
const error = ref<string | null>(null);
const currentPage = ref(1);
const searchText = ref('');

const insuranceTypes = ref<InsuranceType[]>([]);
const selectedInsuranceType = ref('');

onMounted(() => {
  loadQuestions();
  loadInsuranceTypes();
});

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
</script>
<style scoped>
/* You can add more custom styles here if needed */
</style>