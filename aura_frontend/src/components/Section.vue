<template>
  <section :class="['content', modeClass, textClass]">
    <div class="container">
      <slot />
    </div>
  </section>
</template>

<script setup lang="ts">
const props = defineProps<{
  mode?: 'light' | 'dark' | 'beige'
}>()

const modeClass =
  props.mode === 'dark' ? 'bg-black' : props.mode === 'beige' ? 'bg-beige-200' : 'bg-white'

const textClass = props.mode === 'dark' ? 'text-white' : 'text-black'
</script>
