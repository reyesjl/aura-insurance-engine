<template>
  <NavBar />
  <!-- Background Image Banner -->
  <div
    class="w-full h-[100vh] bg-cover bg-center object-cover"
    :style="{ backgroundImage: `url(${bannerImage})` }"
    aria-label="Family in a field"
  >
    
  </div>
  <!-- Landing Content -->
  <div class="container nav-spacer mx-auto py-12 space-y-6">
    <h1 class="text-3xl font-bold">Welcome to the pre-alpha version 0.0.1</h1>

    <p class="text-base">
      Aura Solutions is building a better way to collect insurance application data. One form.
      Multiple carriers. No duplicate work.
    </p>

    <div class="space-y-4">
      <h2 class="text-lg font-semibold">How it works:</h2>
      <ol class="list-decimal list-inside space-y-2">
        <li>Create an application by selecting carriers and coverage lines.</li>
        <li>Send the generated form link to the insured to complete once.</li>
        <li>Track progress and download carrier-specific output instantly.</li>
      </ol>
    </div>

    <div class="text-sm text-gray-400 space-y-2 border-t pt-6">
      <p>
        This is an early build. Please test it and share feedback — your input directly influences
        the final product.
      </p>
      <p>Agents who contribute during pre-release will receive perks in the production version.</p>
      <p>Thank you for your time and insight.</p>
      <p>
        <a
          href="https://forms.gle/9T3hno3iGvyiuWGd7"
          target="_blank"
          rel="noopener"
          class="text-blue-400 underline hover:text-blue-600"
          >Leave feedback here</a
        >
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import NavBar from '@/components/NavBar.vue'
import bannerImage from '@/assets/juliane-bg.jpg'
</script>

<style scoped></style>
