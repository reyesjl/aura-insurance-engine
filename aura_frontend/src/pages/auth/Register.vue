<template>
  <NavBar />
  <ImageSection
    :image="registerBanner"
    overlay
    overlayClass="bg-black/20"
    aria-label="Descriptive alt text"
  >
    <div class="wrapper-sm">
      <div class="text-4xl md:text-5xl font-bold text-white mb-10">Welcome, new Agent.</div>
      <div class="text-white mb-10">
        <form @submit.prevent="handleRegister" class="flex flex-col gap-5">
          <!-- Error message display -->
          <div 
            v-if="errorMessage" 
            class="p-3 bg-red-500/80 backdrop-blur-sm border border-red-400 text-white text-sm rounded"
          >
            {{ errorMessage }}
          </div>

          <!-- Success message display -->
          <div 
            v-if="successMessage" 
            class="p-3 bg-green-500/80 backdrop-blur-sm border border-green-400 text-white text-sm rounded"
          >
            {{ successMessage }}
          </div>

          <input
            placeholder="Email"
            v-model="email"
            type="email"
            required
            @input="clearMessages"
            class="p-2 backdrop-blur-sm bg-black/20 mb-4 border-b-1 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />

          <input
            placeholder="Username"
            v-model="username"
            type="text"
            @input="clearMessages"
            class="p-2 backdrop-blur-sm bg-black/20 mb-4 border-b-1 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />

          <input
            placeholder="Password"
            v-model="password"
            type="password"
            required
            @input="clearMessages"
            class="p-2 backdrop-blur-sm bg-black/20 mb-4 border-b-1 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />

          <input
            placeholder="Confirm Password"
            v-model="confirmPassword"
            type="password"
            required
            @input="clearMessages"
            class="p-2 backdrop-blur-sm bg-black/20 mb-4 border-b-1 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />

          <button
            type="submit"
            :disabled="isLoading"
            class="p-8 bg-black text-white font-bold hover:bg-gray-800 transition duration-300 disabled:opacity-50"
          >
            {{ isLoading ? 'Registering...' : 'Register' }}
          </button>
        </form>
      </div>
      <div class="flex justify-between text-xs uppercase text-white">
        <div>
          <router-link to="/auth/login">Have an Account?</router-link>
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
import registerBanner from '@/assets/industry-bg.jpg'
import ImageSection from '@/components/ImageSection.vue'

const router = useRouter()
const userStore = useUserStore()

const email = ref('')
const username = ref('')
const password = ref('')
const confirmPassword = ref('')
const errorMessage = ref('')
const successMessage = ref('')
const isLoading = ref(false)

async function handleRegister() {
  errorMessage.value = ''
  successMessage.value = ''
  isLoading.value = true

  // Client-side validation
  if (!email.value.trim()) {
    errorMessage.value = 'Email is required'
    return
  }

  if (!username.value.trim()) {
    errorMessage.value = 'Username is required'
    return
  }

  if (!password.value.trim()) {
    errorMessage.value = 'Password is required'
    return
  }

  if (!confirmPassword.value.trim()) {
    errorMessage.value = 'Confirm password is required'
    return
  }

  if (password.value !== confirmPassword.value) {
    errorMessage.value = 'Passwords do not match'
    return
  }

  try {
    await userStore.register(email.value.toLowerCase(), username.value.toLowerCase(), password.value, confirmPassword.value)
    successMessage.value = 'Registration successful! Redirecting...'
    
    // Redirect to agent dashboard after brief delay
    setTimeout(() => {
      router.push('/agent')
    }, 1500)
    
  } catch (error: any) {
    console.error('Registration failed:', error)
    errorMessage.value = error.message || 'Registration failed. Please try again.'
  } finally {
    isLoading.value = false
  }
}

function clearMessages() {
  errorMessage.value = ''
  successMessage.value = ''
  isLoading.value = false
}

// Protect the route - redirect if not logged in or not an agent
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
