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
        <div class="mt-2 text-gray-700">
          <span v-if="getAnswerForSnapshot(snapshot.id)">
            {{ getAnswerForSnapshot(snapshot.id)?.answer }}
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
