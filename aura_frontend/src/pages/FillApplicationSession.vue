/* * Aura Insurance Engine – Proprietary Software * * Copyright © 2025 Jose Reyes (GitHub:
@reyesjl). All rights reserved. * * This software was developed solely by Jose Reyes – full-stack
engineer and designer. * Jacob Powers contributed as the licensed insurance agent for the project. *
It is a modern insurance submission platform built to streamline the intake * and processing of
insurance applications. * * This code is proprietary and confidential. Unauthorized use,
reproduction, * distribution, or modification is strictly prohibited. * * Project repository:
https://github.com/reyesjl/aura-insurance-engine * DeepWiki:
https://app.devin.ai/wiki/reyesjl/aura-insurance-engine */

<template></template>

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

<style scoped></style>
