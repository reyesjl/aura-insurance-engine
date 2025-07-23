<template>
  <Breadcrumbs />
  <Section>

    <div class="flex justify-between mb-2">
      <div v-if="session" class="text-4xl md:max-w-2/3">{{ session?.name }}</div>
      <div :class="statusClass">{{ session?.status }}</div>
    </div>

    <div class="text-gray-400">Insured: {{ session?.insured_email }}</div>
    <div v-if="session" class="text-gray-400 mb-5">Created: {{ session.created_at.slice(0, 10) }}</div>
    
    <div class="mt-5 md:w-1/2">
      <div class="text-sm uppercase">Progress</div>
      <div class="flex items-end w-full h-12 bg-neutral-900 overflow-hidden relative">
        <div class="bg-orange-600 text-black text-2xl font-medium h-full flex items-end justify-start pl-2" style="width: 5%;">
          {{ answers.length }}
        </div>
        <div class="absolute right-2 text-2xl text-white">
          {{ Math.round((answers.length / questionSnapshots.length) * 100) }}%
        </div>
      </div>
    </div>

    <div v-if="loading" class="my-8 text-center text-gray-400">Loading...</div>
    <div v-else>
      <div v-for="snapshot in questionSnapshots" :key="snapshot.id" class="my-10 border-b pb-4">
        <div class="font-semibold">{{ snapshot.question_text }}</div>
        <div class="mt-2 text-gray-700 relative">
          <span v-if="getAnswerForSnapshot(snapshot.id)">
            {{ getAnswerForSnapshot(snapshot.id)?.answer }}
            <button
              class="absolute top-0 right-0 text-xs bg-gray-200 hover:bg-gray-300 px-2 py-1 ml-2"
              @click="copyToClipboard(getAnswerForSnapshot(snapshot.id)?.answer)"
              title="Copy to clipboard"
            >
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M11.5 22C9.96667 22 8.66667 21.4667 7.6 20.4C6.53333 19.3333 6 18.0333 6 16.5V6C6 4.9 6.39167 3.95833 7.175 3.175C7.95833 2.39167 8.9 2 10 2C11.1 2 12.0417 2.39167 12.825 3.175C13.6083 3.95833 14 4.9 14 6V15.5C14 16.2 13.7583 16.7917 13.275 17.275C12.7917 17.7583 12.2 18 11.5 18C10.8 18 10.2083 17.7583 9.725 17.275C9.24167 16.7917 9 16.2 9 15.5V6H10.5V15.5C10.5 15.7833 10.5958 16.0208 10.7875 16.2125C10.9792 16.4042 11.2167 16.5 11.5 16.5C11.7833 16.5 12.0208 16.4042 12.2125 16.2125C12.4042 16.0208 12.5 15.7833 12.5 15.5V6C12.5 5.3 12.2583 4.70833 11.775 4.225C11.2917 3.74167 10.7 3.5 10 3.5C9.3 3.5 8.70833 3.74167 8.225 4.225C7.74167 4.70833 7.5 5.3 7.5 6V16.5C7.5 17.6 7.89167 18.5417 8.675 19.325C9.45833 20.1083 10.4 20.5 11.5 20.5C12.6 20.5 13.5417 20.1083 14.325 19.325C15.1083 18.5417 15.5 17.6 15.5 16.5V6H17V16.5C17 18.0333 16.4667 19.3333 15.4 20.4C14.3333 21.4667 13.0333 22 11.5 22Z" fill="#1D1B20"/>
</svg>

            </button>
          </span>
          <span v-else class="italic text-gray-400">No answer yet</span>
        </div>
      </div>
    </div>
  </Section>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import Section from '@/components/Section.vue'
import Breadcrumbs from '@/components/Breadcrumbs.vue'
import { fetchApplicationSessionDetails } from '@/api/applications'

const route = useRoute()
const sessionId = Number(route.params.id)

const loading = ref(true)
const session = ref<any>(null)
const questionSnapshots = ref<any[]>([])
const answers = ref<any[]>([])

onMounted(async () => {
  loading.value = true
  try {
    const resp = await fetchApplicationSessionDetails(sessionId)
    session.value = resp.session
    questionSnapshots.value = resp.question_snapshots
    answers.value = resp.answers
  } finally {
    loading.value = false
  }
})

function getAnswerForSnapshot(snapshotId: number) {
  return answers.value.find(a => a.question_snapshot.id === snapshotId)
}

const statusClass = computed(() =>
  session.value?.status === 'completed'
    ? 'text-green-600'
    : session.value?.status === 'pending'
      ? 'text-yellow-600'
      : 'text-red-600'
)
</script>

<style scoped>
/* Add any custom styles here */
</style>
