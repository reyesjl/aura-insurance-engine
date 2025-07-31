<template>
  <NavBar />
  <ImageSection
    :image="feedbackBanner"
    overlay
    overlayClass="bg-black/20"
    aria-label="Feedback form background"
  >
    <div class="wrapper-sm">
      <div class="text-4xl md:text-5xl font-bold text-white mb-10">Share Your Feedback</div>
      <div class="text-white mb-10">
        <form @submit.prevent="handleSubmit" class="flex flex-col gap-5">
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

          <!-- Feedback content field with validation -->
          <div class="flex flex-col">
            <textarea
              placeholder="Tell us what you think..."
              v-model="feedbackContent"
              rows="6"
              @input="clearFieldError('feedbackContent')"
              :class="[
                'p-2 backdrop-blur-sm bg-black/20 mb-2 border-b-1 focus:outline-none focus:ring-2 resize-vertical',
                validationErrors.feedbackContent
                  ? 'border-red-400 focus:ring-red-500'
                  : 'border-gray-300 focus:ring-blue-500',
              ]"
            />
            <div
              v-if="validationErrors.feedbackContent"
              class="text-red-300 font-semibold text-xs mb-2 bg-black/50 p-1 w-fit"
            >
              {{ validationErrors.feedbackContent }}
            </div>
          </div>

          <button
            type="submit"
            :disabled="isLoading"
            class="p-8 bg-black text-white font-bold hover:bg-gray-800 transition duration-300 disabled:opacity-50"
          >
            {{ isLoading ? 'Submitting...' : 'Submit Feedback' }}
          </button>
        </form>
      </div>
      <div class="flex justify-center text-xs uppercase text-white">
        <div>
          <router-link to="/">Back to Home</router-link>
        </div>
      </div>
    </div>
  </ImageSection>
</template>

<script setup lang="ts">
import { submitFeedback } from '@/api/feedback'
import feedbackBanner from '@/assets/staircase-bg.jpg'
import ImageSection from '@/components/ImageSection.vue'
import NavBar from '@/components/NavBar.vue'
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const email = ref('')
const feedbackContent = ref('')
const errorMessage = ref('')
const successMessage = ref('')
const isLoading = ref(false)

// Validation errors object
const validationErrors = reactive({
  email: '',
  feedbackContent: '',
})

// Clear individual field errors
const clearFieldError = (field: string) => {
  validationErrors[field as keyof typeof validationErrors] = ''
  errorMessage.value = ''
}

// Clear all validation errors
const clearAllErrors = () => {
  Object.keys(validationErrors).forEach((key) => {
    validationErrors[key as keyof typeof validationErrors] = ''
  })
  errorMessage.value = ''
  successMessage.value = ''
}

// Validate form data
const validateForm = () => {
  clearAllErrors()
  let isValid = true

  // Email validation
  if (!email.value.trim()) {
    validationErrors.email = 'Email is required'
    isValid = false
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
    validationErrors.email = 'Please enter a valid email address'
    isValid = false
  }

  // Feedback content validation
  if (!feedbackContent.value.trim()) {
    validationErrors.feedbackContent = 'Feedback content is required'
    isValid = false
  } else if (feedbackContent.value.trim().length < 10) {
    validationErrors.feedbackContent = 'Feedback must be at least 10 characters long'
    isValid = false
  }

  return isValid
}

// Handle form submission
const handleSubmit = async () => {
  if (!validateForm()) {
    return
  }

  isLoading.value = true
  clearAllErrors()

  try {
    await submitFeedback({
      email: email.value.trim(),
      content: feedbackContent.value.trim(),
    })

    successMessage.value = 'Thank you for your feedback! We appreciate your input.'

    // Clear form after successful submission
    email.value = ''
    feedbackContent.value = ''

    // Optionally redirect after a delay
    setTimeout(() => {
      router.push('/')
    }, 3000)
  } catch (error) {
    console.error('Feedback submission error:', error)
    errorMessage.value =
      error instanceof Error ? error.message : 'Failed to submit feedback. Please try again.'
  } finally {
    isLoading.value = false
  }
}
</script>
