<!-- PLACEHODLER FOR PAGE -->
<template>
  <NavBar />
  <!-- Background Image Banner -->
  <div
    class="w-full h-[100vh] bg-cover bg-center object-cover relative"
    :style="{ backgroundImage: `url(${bannerImage})` }"
    aria-label="Family in a field"
  >
    <!-- Blinker Notice -->
    <Blinker> [COMING SOON] </Blinker>
  </div>
</template>

<script setup lang="ts">
import NavBar from '@/components/NavBar.vue'
import bannerImage from '@/assets/family-bg.jpg'
import Blinker from '@/components/Blinker.vue'
</script>

<style scoped></style>
