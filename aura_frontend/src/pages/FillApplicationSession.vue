<template>
  <NavBar />
  <div class="page-spacer bg-black"></div>

  <Section mode="light" padding="small">
    <div class="text-4xl md:text-5xl font-semibold leading-tight mb-12">
      Fill Application Session
    </div>

    <div v-if="!session" class="max-w-2xl">
      <div class="p-8 bg-yellow-100 border border-yellow-400 text-yellow-700 rounded-lg">
        <div class="text-lg font-semibold mb-4">Session Not Found</div>
        <div class="text-base leading-relaxed mb-6">
          No application session data found. Please navigate to this page through the proper
          workflow.
        </div>
        <router-link
          to="/"
          class="px-6 py-3 bg-black text-white hover:bg-gray-700 duration-300 rounded-lg text-base font-semibold"
        >
          Return to Home
        </router-link>
      </div>
    </div>

    <div v-else class="max-w-2xl">
      <div class="text-xl leading-relaxed mb-8">
        Complete your application session by filling out the required information.
      </div>

      <!-- Application Form Placeholder -->
      <div class="p-8 bg-gray-100 rounded-lg">
        <div class="text-lg font-semibold mb-4">Application Form</div>
        <div class="text-base opacity-80">Form implementation coming soon...</div>
      </div>
    </div>
  </Section>

  <FootBar />
</template>

<script setup lang="ts">
import FootBar from '@/components/FootBar.vue'
import NavBar from '@/components/NavBar.vue'
import Section from '@/components/Section.vue'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const session = ref(window.history.state?.session)

onMounted(() => {
  // If session is not present (e.g. direct navigation), redirect to auth page
  if (!session.value) {
    // If you can't get a token, redirect to a safe page
    router.replace({ name: 'Home' }) // or a custom error page
  }
})
</script>

<style scoped></style>
