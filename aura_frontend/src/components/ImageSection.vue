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
