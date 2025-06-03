<template>
  <div
    class="absolute right-[5rem] md:right-100 w-12 h-12 z-10 cursor-default text-white letter-spacing-2 text-xl flex justify-center items-center rounded-full bg-black/50 hover:bg-black/70 transition-all duration-300 blink-cursor"
    :style="{ bottom: computedBottom + 'px', opacity: computedOpacity }"
    @click="$emit('click')"
  >
    <slot>[SCROLL DOWN]</slot>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue'

const baseBottom = 200 // px, initial bottom offset
const maxOffset = 500 // px, how much it can move up
const computedBottom = ref(baseBottom)
const computedOpacity = ref(1)

function handleScroll() {
  const scrollY = window.scrollY || window.pageYOffset
  computedBottom.value = baseBottom + Math.min(scrollY, maxOffset)
  // Fade out as you scroll down: fully visible at top, gone at 500px
  computedOpacity.value = Math.max(0, 1 - Math.min(scrollY, maxOffset) / maxOffset)
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})
onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
@keyframes blink {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0.3;
  }
}
.blink-cursor {
  animation: blink 1.2s steps(1) infinite;
}
</style>
