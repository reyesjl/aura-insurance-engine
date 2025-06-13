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
