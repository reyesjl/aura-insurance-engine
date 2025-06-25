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

          <!-- Email field with validation -->
          <div class="flex flex-col">
            <input
              placeholder="Email"
              v-model="email"
              type="email"
              @input="clearFieldError('email')"
              :class="[
                'p-2 backdrop-blur-sm bg-black/20 mb-2 border-b-1 focus:outline-none focus:ring-2',
                validationErrors.email
                  ? 'border-red-400 focus:ring-red-500'
                  : 'border-gray-300 focus:ring-blue-500',
              ]"
            />
            <div
              v-if="validationErrors.email"
              class="text-red-300 font-semibold text-xs mb-2 bg-black/50 p-1 w-fit"
            >
              {{ validationErrors.email }}
            </div>
          </div>

          <!-- Username field with validation -->
          <div class="flex flex-col">
            <input
              placeholder="Username"
              v-model="username"
              type="text"
              @input="clearFieldError('username')"
              :class="[
                'p-2 backdrop-blur-sm bg-black/20 mb-2 border-b-1 focus:outline-none focus:ring-2',
                validationErrors.username
                  ? 'border-red-400 focus:ring-red-500'
                  : 'border-gray-300 focus:ring-blue-500',
              ]"
            />
            <div
              v-if="validationErrors.username"
              class="text-red-300 font-semibold text-xs mb-2 bg-black/50 p-1 w-fit"
            >
              {{ validationErrors.username }}
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

          <!-- Confirm Password field with validation -->
          <div class="flex flex-col">
            <input
              placeholder="Confirm Password"
              v-model="confirmPassword"
              type="password"
              @input="clearFieldError('confirmPassword')"
              :class="[
                'p-2 backdrop-blur-sm bg-black/20 mb-2 border-b-1 focus:outline-none focus:ring-2',
                validationErrors.confirmPassword
                  ? 'border-red-400 focus:ring-red-500'
                  : 'border-gray-300 focus:ring-blue-500',
              ]"
            />
            <div
              v-if="validationErrors.confirmPassword"
              class="text-red-300 font-semibold text-xs mb-2 bg-black/50 p-1 w-fit"
            >
              {{ validationErrors.confirmPassword }}
            </div>
          </div>

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
import { ref, onMounted, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { registerSchema, type RegisterFormData } from '@/schemas/auth.schema'
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

// Validation errors state
const validationErrors = reactive<Partial<Record<keyof RegisterFormData, string>>>({})

// Clear validation errors
function clearFieldError(field: keyof RegisterFormData) {
  if (validationErrors[field]) {
    delete validationErrors[field]
  }
  // Also clear general error message when user starts typing
  if (errorMessage.value) {
    errorMessage.value = ''
  }
  if (successMessage.value) {
    successMessage.value = ''
  }
}

function clearAllErrors() {
  Object.keys(validationErrors).forEach((key) => {
    delete validationErrors[key as keyof RegisterFormData]
  })
  errorMessage.value = ''
  successMessage.value = ''
}

async function handleRegister() {
  // Clear all previous errors
  clearAllErrors()

  // Validate form data
  const formData = {
    email: email.value.trim(),
    username: username.value.trim(),
    password: password.value,
    confirmPassword: confirmPassword.value,
  }

  const validation = registerSchema.safeParse(formData)

  if (!validation.success) {
    // Handle validation errors
    validation.error.errors.forEach((error) => {
      const field = error.path[0] as keyof RegisterFormData
      validationErrors[field] = error.message
    })
    return
  }

  // Proceed with registration if validation passes
  isLoading.value = true

  try {
    await userStore.register(
      validation.data.email,
      validation.data.username,
      validation.data.password,
      validation.data.confirmPassword,
    )
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
