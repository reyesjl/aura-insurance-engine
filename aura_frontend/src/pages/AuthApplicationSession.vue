<template>
  <div class="min-h-screen flex flex-col items-center justify-center">
    <div class="bg-gray-100 p-10 w-full max-w-md">
      <div v-if="loading" class="text-center text-gray-500">Loading...</div>
      <div v-else>
        <div v-if="!tokenValid" class="text-center">
          <div class="flex items-center justify-center mb-5">
            <svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M14 22V14C14 11.3478 15.0536 8.8043 16.9289 6.92893C18.8043 5.05357 21.3478 4 24 4C26.6522 4 29.1957 5.05357 31.0711 6.92893C32.9464 8.8043 34 11.3478 34 14V22M10 22H38C40.2091 22 42 23.7909 42 26V40C42 42.2091 40.2091 44 38 44H10C7.79086 44 6 42.2091 6 40V26C6 23.7909 7.79086 22 10 22Z" stroke="#1E1E1E" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>

          <div class="text-3xl font-bold mb-8">Access Denied</div>
          <div>Please check your access token and try again.</div>
          {{ error }}
        </div>
        <div v-else>
          <div class="text-3xl font-bold mb-8 text-center">Authenticate</div>
          <div class="mb-6 text-center">
            <div class="text-xs uppercase text-gray-500 mb-1">Access Token</div>
            <div class="font-mono text-sm bg-gray-100 text-black break-all">{{ token }}</div>
          </div>
          <form @submit.prevent="handleSubmit" class="flex flex-col gap-5">
            <div class="flex flex-col">
              <input
                placeholder="Enter your email"
                v-model="email"
                type="email"
                @input="clearError"
                :class="[
                  'p-2 backdrop-blur-sm bg-black/20 mb-2 border-b-1 focus:outline-none focus:ring-2',
                  error ? 'border-red-400 focus:ring-red-500' : 'border-gray-300 focus:ring-blue-500',
                ]"
                required
              />
              <div v-if="error" class="text-red-300 font-semibold text-xs mb-2 bg-black/50 p-1 w-fit">
                {{ error }}
              </div>
            </div>
            <button
              type="submit"
              class="p-8 bg-black text-white font-bold hover:bg-gray-800 transition duration-300 disabled:opacity-50"
            >
              Continue
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import Breadcrumbs from '@/components/Breadcrumbs.vue'
import { verifyApplicationToken, authenticateApplicationSession } from '@/api/applications'
import router from '@/router'
import { id } from 'zod/v4/locales'

const route = useRoute()
const token = route.params.token as string || ''

const email = ref('')
const error = ref('')
const tokenValid = ref(false)
const loading = ref(true)

function clearError() {
  error.value = ''
}

async function handleSubmit() {
  if (!email.value.trim()) {
    error.value = 'Email is required'
    return
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())) {
    error.value = 'Please enter a valid email address'
    return
  }
  try {
    const resp = await authenticateApplicationSession(token, email.value.trim())
    console.log('Authentication successful:', resp)
    console.log(JSON.stringify(resp.session))
    router.push({
      name: 'FillApplicationSession',
      params: { id: resp.session.id },
      state: { session: JSON.stringify(resp.session) }
    })
  } catch (err: any) {
    error.value = err.message || 'Authentication failed'
  }
}

onMounted(async () => {
  loading.value = true
  try {
    const resp = await verifyApplicationToken(token)
    tokenValid.value = resp.exists
    if (!tokenValid.value) {
      error.value = 'Application does not exist or has expired.'
    }
  } catch (err) {
    error.value = 'Application does not exist or has expired.'
    tokenValid.value = false
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
</style>