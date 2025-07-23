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
        <div
          class="bg-orange-600 text-black text-2xl font-medium h-full flex items-end justify-start pl-2"
          :style="{ width: progressPercent + '%' }"
        >
          {{ answers.length }}
        </div>
        <div class="absolute right-2 text-2xl text-white">
          {{ Math.round((answers.length / questionSnapshots.length) * 100) }}%
        </div>
      </div>
    </div>

    <!-- Access token -->
    <div>
      <div class="text-sm uppercase mt-5">Access Token</div>
      <div class="flex items-center gap-2">
        <div>{{ obfuscatedToken }}</div>
        <button
          class="text-xs bg-gray-200 hover:bg-gray-300 p-1"
          @click="copyToClipboard(session?.token)"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M11 17H7C5.61667 17 4.4375 16.5125 3.4625 15.5375C2.4875 14.5625 2 13.3833 2 12C2 10.6167 2.4875 9.4375 3.4625 8.4625C4.4375 7.4875 5.61667 7 7 7H11V9H7C6.16667 9 5.45833 9.29167 4.875 9.875C4.29167 10.4583 4 11.1667 4 12C4 12.8333 4.29167 13.5417 4.875 14.125C5.45833 14.7083 6.16667 15 7 15H11V17ZM8 13V11H16V13H8ZM13 17V15H17C17.8333 15 18.5417 14.7083 19.125 14.125C19.7083 13.5417 20 12.8333 20 12C20 11.1667 19.7083 10.4583 19.125 9.875C18.5417 9.29167 17.8333 9 17 9H13V7H17C18.3833 7 19.5625 7.4875 20.5375 8.4625C21.5125 9.4375 22 10.6167 22 12C22 13.3833 21.5125 14.5625 20.5375 15.5375C19.5625 16.5125 18.3833 17 17 17H13Z" fill="#1D1B20"/>
          </svg>
        </button>
        <button
          class="text-xs bg-gray-200 hover:bg-gray-300 p-1"
          @click="rollToken"
        >
          <svg width="20" height="20" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M46 8V20M46 20H34M46 20L36.74 11.28C33.9812 8.51948 30.4 6.73037 26.5359 6.18229C22.6719 5.6342 18.7343 6.35683 15.3167 8.24128C11.8991 10.1257 9.18649 13.0699 7.58772 16.6301C5.98895 20.1904 5.59061 24.1738 6.45272 27.9801C7.31484 31.7864 9.3907 35.2095 12.3675 37.7333C15.3443 40.2572 19.0608 41.7453 22.9568 41.9732C26.8529 42.2011 30.7175 41.1566 33.9683 38.997C37.2191 36.8374 39.6799 33.6798 40.98 30" stroke="#1E1E1E" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>

        </button>
        <transition name="fade">
          <span
            v-if="copiedId === session?.token"
            class="ml-2 bg-black text-white text-xs p-1"
            style="vertical-align: middle;"
          >
            Copied to clipboard
          </span>
        </transition>
      </div>
    </div>


    <div v-if="loading" class="my-8 text-center text-gray-400">Loading...</div>
    <div v-else>
      <div v-for="snapshot in questionSnapshots" :key="snapshot.id" class="my-10 border-b pb-4 relative">
        <div class="font-semibold">{{ snapshot.question_text }}</div>
        <div class="mt-2 text-gray-700 relative flex items-center">
          <span v-if="getAnswerForSnapshot(snapshot.id)">
            {{ getAnswerForSnapshot(snapshot.id)?.answer }}
            <span class="inline-block align-middle ml-2">
              <button
                class="text-xs bg-gray-200 hover:bg-gray-300 p-1"
                @click="copyToClipboard(getAnswerForSnapshot(snapshot.id)?.answer, snapshot.id)"
                title="Copy to clipboard"
                style="vertical-align: middle;"
              >
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M11 17H7C5.61667 17 4.4375 16.5125 3.4625 15.5375C2.4875 14.5625 2 13.3833 2 12C2 10.6167 2.4875 9.4375 3.4625 8.4625C4.4375 7.4875 5.61667 7 7 7H11V9H7C6.16667 9 5.45833 9.29167 4.875 9.875C4.29167 10.4583 4 11.1667 4 12C4 12.8333 4.29167 13.5417 4.875 14.125C5.45833 14.7083 6.16667 15 7 15H11V17ZM8 13V11H16V13H8ZM13 17V15H17C17.8333 15 18.5417 14.7083 19.125 14.125C19.7083 13.5417 20 12.8333 20 12C20 11.1667 19.7083 10.4583 19.125 9.875C18.5417 9.29167 17.8333 9 17 9H13V7H17C18.3833 7 19.5625 7.4875 20.5375 8.4625C21.5125 9.4375 22 10.6167 22 12C22 13.3833 21.5125 14.5625 20.5375 15.5375C19.5625 16.5125 18.3833 17 17 17H13Z" fill="#1D1B20"/>
                </svg>
              </button>
              <transition name="fade">
                <span
                  v-if="copiedId === snapshot.id"
                  class="ml-2 bg-black text-white text-xs p-1"
                  style="vertical-align: middle;"
                >
                  Copied to clipboard
                </span>
              </transition>
            </span>
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

const copiedId = ref<string | number | null>(null)
let copyTimeout: ReturnType<typeof setTimeout> | null = null

const tokenRefreshed = ref(false)
let refreshTimeout: ReturnType<typeof setTimeout> | null = null

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

function copyToClipboard(text?: string, id?: number | string) {
  if (!text) return
  navigator.clipboard.writeText(text)
  copiedId.value = id ?? text
  if (copyTimeout) clearTimeout(copyTimeout)
  copyTimeout = setTimeout(() => {
    copiedId.value = null
  }, 1500)
}

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

const progressPercent = computed(() => {
  if (questionSnapshots.value.length === 0) return 0
  return (answers.value.length / questionSnapshots.value.length) * 100
})

const obfuscatedToken = computed(() => {
  const token = session.value?.token || ''
  if (copiedId.value === token) return token
  if (token.length <= 12) return token // Not enough to obfuscate middle 8
  const start = token.slice(0, 4)
  const end = token.slice(-4)
  return `${start}********${end}`
})

function rollToken() {
  // Proper UUID v4 generator
  const uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c: string) => {
    const r = crypto.getRandomValues(new Uint8Array(1))[0] % 16
    const v = c === 'x' ? r : (r & 0x3 | 0x8)
    return v.toString(16)
  })
  console.log('Rolled new token:', uuid)
  tokenRefreshed.value = true
  if (refreshTimeout) clearTimeout(refreshTimeout)
  refreshTimeout = setTimeout(() => {
    tokenRefreshed.value = false
  }, 1500)
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>
