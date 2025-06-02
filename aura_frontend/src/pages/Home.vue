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
  <div class="container content md:max-w-3/4 mx-auto py-30 mb-[100px]">
    <div class="text-3xl md:text-4xl">Our Mission</div>
    <div class="flex flex-col gap-5 md:gap-none md:flex-row mt-10">
      <div class="w-full md:w-1/2">
        <div class="text-4xl md:text-5xl font-semibold w-full">Transforming insurance processing with advanced software.</div>
      </div>
      <div class="w-full md:w-1/2 flex flex-col text-2xl gap-10 mt-10 md:mt-0">
        <div>The insurance world has changed. How we process needs to change too.</div>
        <div>Insurance submissions are fractured and slow. To fix that, we put technology ahead of tradition—streamlining intake across carriers and lines to give agents and underwriters a unified, real-time advantage.</div>
      </div>
    </div>
  </div>

  <div
    class="w-full bg-cover bg-center object-cover pb-[100px] min-h-[100vh]"
    :style="{ backgroundImage: `url(${highriseBanner})` }"
    aria-label="Highrise buildings low angle shot looking up at the sky"
  >
  <div class="container content mx-auto py-20">
    <div class="flex flex-col gap-20 text-white">
      <div class="text-3xl">Rebuild the Backbone</div>
      <div class="text-2xl">The insurance industry runs on legacy systems that slow down progress and obscure insight. Agents and carriers are forced to work around the problem, not through it. But quoting, binding, and underwriting across multiple lines and carriers doesn’t have to be fractured. It’s time to rebuild the digital backbone of insurance—with tools that unify intake, speed decisions, and bring the whole market forward. See how we’re reshaping insurance infrastructure—and how you can be part of it.</div>
    </div>
  </div>

  </div>
</template>

<script setup lang="ts">
import NavBar from '@/components/NavBar.vue'
import bannerImage from '@/assets/juliane-bg.jpg'
import highriseBanner from '@/assets/highrise-bg.jpg'
</script>

<style scoped></style>
