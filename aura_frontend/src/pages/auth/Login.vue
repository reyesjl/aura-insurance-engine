<template>
  <NavBar />
  <ImageSection
    :image="loginBanner"
    overlay
    overlayClass="bg-black/20"
    aria-label="Descriptive alt text"
  >
    <div class="wrapper-sm">
      <div class="text-4xl md:text-5xl font-bold text-white mb-10">Welcome back, Agent.</div>
      <div class="text-white mb-10">
        <form @submit.prevent="handleLogin" class="flex flex-col gap-5">
          <!-- Error message display -->
          <div
            v-if="errorMessage"
            class="p-3 bg-red-500/80 backdrop-blur-sm border border-red-400 text-white text-sm rounded"
          >
            {{ errorMessage }}
          </div>

          <input
            placeholder="Email or Username"
            v-model="email"
            type="text"
            @input="clearError"
            class="p-2 backdrop-blur-sm bg-black/20 mb-4 border-b-1 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />

          <input
            placeholder="Password"
            v-model="password"
            type="password"
            @input="clearError"
            class="p-2 backdrop-blur-sm bg-black/20 mb-4 border-b-1 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />

          <button
            type="submit"
            :disabled="isLoading"
            class="p-8 bg-black text-white font-bold hover:bg-gray-800 transition duration-300 disabled:opacity-50"
          >
            {{ isLoading ? 'Logging in...' : 'Login' }}
          </button>
        </form>
      </div>
      <div class="flex justify-between text-xs uppercase text-white">
        <div>
          <router-link to="/auth/register">New Account?</router-link>
        </div>
        <div>
          <router-link to="/auth/reset-password">Forgot Password?</router-link>
        </div>
      </div>
    </div>
  </ImageSection>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import NavBar from '@/components/NavBar.vue'
import loginBanner from '@/assets/mountains-bg.jpg'
import ImageSection from '@/components/ImageSection.vue'

const router = useRouter()
const userStore = useUserStore()
const email = ref('')
const password = ref('')
const errorMessage = ref('')
const isLoading = ref(false)

async function handleLogin() {
  // Clear previous error
  errorMessage.value = ''
  isLoading.value = true

  try {
    await userStore.login(email.value.toLowerCase(), password.value)
    router.push('/agent')
  } catch (error: any) {
    console.error('Login failed:', error)
    errorMessage.value =
      error.message || 'Login failed. Please check your credentials and try again.'
  } finally {
    isLoading.value = false
  }
}

// Clear error when user starts typing
function clearError() {
  if (errorMessage.value) {
    errorMessage.value = ''
  }
}

// Protect the route - redirect if already logged in
onMounted(() => {
  if (userStore.isLoggedIn) {
    router.push('/agent')
  }
})
</script>

<style scoped>
input::placeholder {
  color: #c0c0c0;
  letter-spacing: 0.05em;
  font-size: 0.875rem;
}
</style>
