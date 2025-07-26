/* * Aura Insurance Engine – Proprietary Software * * Copyright © 2025 Jose Reyes (GitHub:
@reyesjl). All rights reserved. * * This software was developed solely by Jose Reyes – full-stack
engineer and designer. * Jacob Powers contributed as the licensed insurance agent for the project. *
It is a modern insurance submission platform built to streamline the intake * and processing of
insurance applications. * * This code is proprietary and confidential. Unauthorized use,
reproduction, * distribution, or modification is strictly prohibited. * * Project repository:
https://github.com/reyesjl/aura-insurance-engine * DeepWiki:
https://app.devin.ai/wiki/reyesjl/aura-insurance-engine */

<template>
  <section
    class="content relative w-full min-h-[100vh] bg-cover bg-center flex items-center"
    :style="{ backgroundImage: `url(${image})` }"
    :aria-label="ariaLabel"
  >
    <div v-if="overlay" class="absolute inset-0" :class="overlayClass" aria-hidden="true"></div>
    <div class="container relative z-10">
      <slot />
    </div>
  </section>
</template>

<script setup lang="ts">
const props = defineProps<{
  image: string
  overlay?: boolean
  overlayClass?: string
  ariaLabel?: string
}>()
</script>
