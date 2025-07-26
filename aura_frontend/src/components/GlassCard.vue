/* * Aura Insurance Engine – Proprietary Software * * Copyright © 2025 Jose Reyes (GitHub:
@reyesjl). All rights reserved. * * This software was developed solely by Jose Reyes – full-stack
engineer and designer. * Jacob Powers contributed as the licensed insurance agent for the project. *
It is a modern insurance submission platform built to streamline the intake * and processing of
insurance applications. * * This code is proprietary and confidential. Unauthorized use,
reproduction, * distribution, or modification is strictly prohibited. * * Project repository:
https://github.com/reyesjl/aura-insurance-engine * DeepWiki:
https://app.devin.ai/wiki/reyesjl/aura-insurance-engine */

<template>
  <div
    class="bg-gradient-to-br from-white/40 via-white/10 to-blue-200/30 shadow-2xl backdrop-blur-[6px] border border-white/30 p-8 relative overflow-hidden"
  >
    <!-- Optional: Decorative glassy highlights -->
    <div
      class="absolute left-6 top-6 w-1/3 h-1/3 rounded-full bg-white/40 blur-lg opacity-40 pointer-events-none"
    ></div>
    <div
      class="absolute right-8 bottom-8 w-1/4 h-1/4 rounded-full bg-white/30 blur-md opacity-30 pointer-events-none"
    ></div>
    <!-- Slot for card content -->
    <slot />
  </div>
</template>

<script setup lang="ts">
// No JS needed for this effect
</script>
