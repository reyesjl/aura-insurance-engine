<!-- PLACEHODLER FOR PAGE -->
<template>
  <NavBar />
  <!-- Background Image Banner -->
  <div
    class="w-full h-[100vh] bg-cover bg-center object-cover relative"
    :style="{ backgroundImage: `url(${bannerImage})` }"
    aria-label="Family in a field"
  >
    <!-- Down Icon in bottom right -->
    <ScrollButton> [SCROLL] </ScrollButton>
  </div>

  <!-- About Section -->
  <Section mode="light">
    <div class="flex flex-col gap-7 md:gap-none md:flex-row mt-10">
      <div class="w-full md:w-1/2">
        <div class="text-4xl md:text-3xl font-semibold w-full">
          Creating technology that’s helping real insurance agents close faster and work smarter.
        </div>
      </div>
      <div class="w-full md:w-1/2 flex flex-col text-2xl gap-5 mt-10 md:mt-0">
        <div>
          We’re not another bloated SaaS startup. We build lean, focused tools that actually get
          used—designed for speed, usability, and outcomes. If you care more about real-world impact
          than vanity metrics, you’ll feel right at home here.
        </div>
      </div>
    </div>
  </Section>

  <!--  Section -->
  <Section mode="beige">
    <div class="flex flex-col gap-7 md:gap-none md:flex-row mt-10">
      <div class="w-full md:w-1/2">
        <div class="text-4xl md:text-3xl font-semibold w-full">Who We Are</div>
      </div>
      <div class="w-full md:w-1/2 flex flex-col text-2xl gap-5 mt-10 md:mt-0">
        <div>
          We believe the best tools come from firsthand experience. That’s why our team blends
          product minds with real insurance veterans who know what it takes to close deals and stay
          organized. Meet the people bringing clarity to the chaos.
        </div>
      </div>
    </div>
    <div class="mt-20 md:mt-50 flex flex-col gap-10 md:flex-row">
      <div class="flex flex-col font-bold w-full md:w-1/3 gap-2">
        <div class="text-2xl">@Jacob</div>
        <div>Chief Executive Officer</div>
        <div class="font-normal">
          Licensed agent with deep frontline experience turning daily inefficiencies into scalable
          solutions.
        </div>
      </div>
      <div class="flex flex-col font-bold w-full md:w-1/3 gap-2">
        <div class="text-2xl">@Kevin</div>
        <div>Chief Strategy Officer</div>
        <div class="font-normal">
          Business operator with a sharp eye for systems, sales, and where the market's headed.
        </div>
      </div>
      <div class="flex flex-col font-bold w-full md:w-1/3 gap-2">
        <div class="text-2xl">@Jose</div>
        <div>Chief Technology Officer</div>
        <div class="font-normal">
          Full-stack engineer and product lead focused on speed, simplicity, and good design.
        </div>
      </div>
    </div>
  </Section>

  <FootBar />
</template>

<script setup lang="ts">
import NavBar from '@/components/NavBar.vue'
import bannerImage from '@/assets/dc-bg.jpg'
import Section from '@/components/Section.vue'
import FootBar from '@/components/FootBar.vue'
import ScrollButton from '@/components/ScrollButton.vue'
</script>

<style scoped></style>
