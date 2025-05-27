<template>
    <!-- Navigation Bar -->
    <div class="bg-black border-b-1 border-white flex">
        <div class="border-r-1 border-white p-6 px-10 w-fit text-2xl font-bold">
            AURA SOLUTIONS
        </div>
        <div class="border-r-1 border-white p-6 px-10 w-fit flex align-center items-center gap-8 text-sm">
            <router-link to="/" class="text-white hover:underline underline-offset-6">
                Home
            </router-link>
             <router-link to="/agent" class="text-white hover:underline underline-offset-6">
                Create
            </router-link>
             <router-link to="/sessions" class="text-white hover:underline underline-offset-6">
                Track
            </router-link>
        </div>
    </div>
    
    <!-- Landing Content -->
  <div class="container mx-auto py-12 space-y-6">
    <h1 class="text-3xl font-bold">Welcome to the pre-alpha version 0.0.1</h1>

    <p class="text-base">
      Aura Solutions is building a better way to collect insurance application data.
      One form. Multiple carriers. No duplicate work.
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
        This is an early build. Please test it and share feedback — your input directly influences the final product.
      </p>
      <p>
        Agents who contribute during pre-release will receive perks in the production version.
      </p>
      <p>
        Thank you for your time and insight.
      </p>
      <p>
        <a href="https://forms.gle/9T3hno3iGvyiuWGd7" target="_blank" rel="noopener" class="text-blue-400 underline hover:text-blue-600">Leave feedback here</a>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped></style>