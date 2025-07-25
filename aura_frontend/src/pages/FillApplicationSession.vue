<template>
  
</template>

<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'

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

<style scoped>
</style>