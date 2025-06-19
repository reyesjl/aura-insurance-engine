<template>
  <NavBar />
  <ImageSection
    :image="resetBanner"
    overlay
    overlayClass="bg-black/20"
    aria-label="Descriptive alt text"
  >
    <div class="wrapper-sm">
      <div class="text-4xl md:text-5xl font-bold text-white mb-10">Reset Password</div>
      <div class="text-white mb-10">
        <form @submit.prevent="handleResetPassword" class="flex flex-col gap-5">
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

          <button
            type="submit"
            :disabled="isLoading || !!successMessage"
            class="p-8 bg-black text-white font-bold hover:bg-gray-800 transition duration-300 disabled:opacity-50"
          >
            {{ isLoading ? 'Sending...' : 'Send Reset Link' }}
          </button>

          <div v-if="successMessage" class="text-center text-sm">
            <p>The password for all accounts is: <strong>******</strong></p>
          </div>
        </form>
      </div>
      <div class="flex justify-between text-xs uppercase text-white">
        <div>
          <router-link to="/auth/login">Back to Login</router-link>
        </div>
        <div>
          <router-link to="/auth/register">New Account?</router-link>
        </div>
      </div>
    </div>
  </ImageSection>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'
import NavBar from '@/components/NavBar.vue'
import resetBanner from '@/assets/factory-bg.jpg'
import ImageSection from '@/components/ImageSection.vue'

const userStore = useUserStore()

const email = ref('')
const errorMessage = ref('')
const successMessage = ref('')
const isLoading = ref(false)

async function handleResetPassword() {
  errorMessage.value = ''
  successMessage.value = ''
  isLoading.value = true

  try {
    const result = await userStore.resetPassword(email.value)
    successMessage.value = result.message
  } catch (error: any) {
    console.error('Password reset failed:', error)
    errorMessage.value = error.message || 'Password reset failed. Please try again.'
  } finally {
    isLoading.value = false
  }
}

function clearMessages() {
  errorMessage.value = ''
  successMessage.value = ''
}
</script>

<style scoped>
input::placeholder {
  color: #c0c0c0;
  letter-spacing: 0.05em;
  font-size: 0.875rem;
}
</style>
