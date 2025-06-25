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

          <!-- Email/Username field with validation -->
          <div class="flex flex-col">
            <input
              placeholder="Email or Username"
              v-model="loginField"
              type="text"
              @input="clearFieldError('loginField')"
              :class="[
                'p-2 backdrop-blur-sm bg-black/20 mb-2 border-b-1 focus:outline-none focus:ring-2',
                validationErrors.loginField
                  ? 'border-red-400 focus:ring-red-500'
                  : 'border-gray-300 focus:ring-blue-500',
              ]"
            />
            <div
              v-if="validationErrors.loginField"
              class="text-red-300 font-semibold text-xs mb-2 bg-black/50 p-1 w-fit"
            >
              {{ validationErrors.loginField }}
            </div>
          </div>

          <!-- Password field with validation -->
          <div class="flex flex-col">
            <input
              placeholder="Password"
              v-model="password"
              type="password"
              @input="clearFieldError('password')"
              :class="[
                'p-2 backdrop-blur-sm bg-black/20 mb-2 border-b-1 focus:outline-none focus:ring-2',
                validationErrors.password
                  ? 'border-red-400 focus:ring-red-500'
                  : 'border-gray-300 focus:ring-blue-500',
              ]"
            />
            <div
              v-if="validationErrors.password"
              class="text-red-300 font-semibold text-xs mb-2 bg-black/50 p-1 w-fit"
            >
              {{ validationErrors.password }}
            </div>
          </div>

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
import { ref, onMounted, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { loginSchema, type LoginFormData } from '@/schemas/auth.schema'
import NavBar from '@/components/NavBar.vue'
import loginBanner from '@/assets/mountains-bg.jpg'
import ImageSection from '@/components/ImageSection.vue'

const router = useRouter()
const userStore = useUserStore()
const loginField = ref('')
const password = ref('')
const errorMessage = ref('')
const isLoading = ref(false)

// Validation errors state
const validationErrors = reactive<Partial<Record<keyof LoginFormData, string>>>({})

// Clear validation errors
function clearFieldError(field: keyof LoginFormData) {
  if (validationErrors[field]) {
    delete validationErrors[field]
  }
  // Also clear general error message when user starts typing
  if (errorMessage.value) {
    errorMessage.value = ''
  }
}

function clearAllErrors() {
  Object.keys(validationErrors).forEach((key) => {
    delete validationErrors[key as keyof LoginFormData]
  })
  errorMessage.value = ''
}

async function handleLogin() {
  // Clear all previous errors
  clearAllErrors()

  // Validate form data
  const formData = {
    loginField: loginField.value.trim(),
    password: password.value,
  }

  const validation = loginSchema.safeParse(formData)

  if (!validation.success) {
    // Handle validation errors
    validation.error.errors.forEach((error) => {
      const field = error.path[0] as keyof LoginFormData
      validationErrors[field] = error.message
    })
    return
  }

  // Proceed with login if validation passes
  isLoading.value = true

  try {
    await userStore.login(validation.data.loginField.toLowerCase(), validation.data.password)
    router.push('/agent')
  } catch (error: any) {
    console.error('Login failed:', error)
    errorMessage.value =
      error.message || 'Login failed. Please check your credentials and try again.'
  } finally {
    isLoading.value = false
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
