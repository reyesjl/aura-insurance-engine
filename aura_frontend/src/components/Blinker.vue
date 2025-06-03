<template>
  <div
    class="fixed left-1/2 top-1/2 z-20 flex justify-center items-center"
    :style="{ transform: 'translate(-50%, -50%)', opacity: computedOpacity }"
    @click="$emit('click')"
  >
    <div
      class="w-20 h-20 aspect-square rounded-full bg-black/50 hover:bg-black/70 transition-all duration-300 blink-cursor flex items-center justify-center"
    ></div>
    <div
      class="absolute flex items-center justify-center w-20 h-20 pointer-events-none select-none text-nowrap text-white md:text-xl"
    >
      <slot>[BLINKER]</slot>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const maxOffset = 500 // px, how much it can move up before fully faded
const computedOpacity = ref(1)

function handleScroll() {
  const scrollY = window.scrollY || window.pageYOffset
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
