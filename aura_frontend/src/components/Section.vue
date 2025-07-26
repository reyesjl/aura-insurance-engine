/*
 * Aura Insurance Engine – Proprietary Software
 *
 * Copyright © 2025 Jose Reyes (GitHub: @reyesjl). All rights reserved.
 *
 * This software was developed solely by Jose Reyes – full-stack engineer and designer.
 * Jacob Powers contributed as the licensed insurance agent for the project.
 * It is a modern insurance submission platform built to streamline the intake
 * and processing of insurance applications.
 *
 * This code is proprietary and confidential. Unauthorized use, reproduction,
 * distribution, or modification is strictly prohibited.
 *
 * Project repository: https://github.com/reyesjl/aura-insurance-engine
 * DeepWiki: https://app.devin.ai/wiki/reyesjl/aura-insurance-engine
 */

<template>
  <section :class="[modeClass, textClass, paddingClass]">
    <div class="container">
      <slot />
    </div>
  </section>
</template>

<script setup lang="ts">
const props = defineProps<{
  mode?: 'light' | 'dark' | 'beige'
  padding?: 'none' | 'small' | 'medium' | 'large' | 'xl'
}>()

const modeClass =
  props.mode === 'dark' ? 'bg-black' : props.mode === 'beige' ? 'bg-beige-200' : 'bg-white'

const textClass = props.mode === 'dark' ? 'text-white' : 'text-black'

const paddingClass = (() => {
  switch (props.padding) {
    case 'none':
      return 'py-0'
    case 'small':
      return 'py-8'
    case 'medium':
      return 'py-16'
    case 'large':
      return 'py-20'
    case 'xl':
      return 'py-32'
    default:
      return 'py-16' // Default maintains roughly the same padding as content class (100px ≈ 25 * 0.25rem)
  }
})()
</script>
