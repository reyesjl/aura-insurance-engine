<!-- About Page -->
<template>
  <NavBar />
  <!-- Background Image Banner -->
  <div
    class="w-full h-[100vh] bg-cover bg-center object-cover relative"
    :style="{ backgroundImage: `url(${bannerImage})` }"
    aria-label="About AURA team"
  >
    <!-- Down Icon in bottom right -->
    <ScrollButton> [SCROLL] </ScrollButton>
  </div>

  <!-- About Section -->
  <Section mode="light" padding="large">
    <div class="flex flex-col gap-8 md:gap-16 md:flex-row">
      <div class="w-full md:w-1/2">
        <div class="text-4xl md:text-5xl font-semibold leading-tight">
          Creating technology that's helping real insurance agents close faster and work smarter.
        </div>
      </div>
      <div class="w-full md:w-1/2 flex flex-col gap-6">
        <div class="text-xl leading-relaxed">
          We're not another bloated SaaS startup. We build lean, focused tools that actually get
          used—designed for speed, usability, and outcomes. If you care more about real-world impact
          than vanity metrics, you'll feel right at home here.
        </div>
      </div>
    </div>
  </Section>

  <!-- Who We Are Section -->
  <Section mode="beige" padding="large">
    <div class="flex flex-col gap-8 md:gap-16 md:flex-row mb-16">
      <div class="w-full md:w-1/2">
        <div class="text-4xl md:text-5xl font-semibold leading-tight">Who We Are</div>
      </div>
      <div class="w-full md:w-1/2 flex flex-col gap-6">
        <div class="text-xl leading-relaxed">
          We believe the best tools come from firsthand experience. That's why our team blends
          product minds with real insurance veterans who know what it takes to close deals and stay
          organized. Meet the people bringing clarity to the chaos.
        </div>
      </div>
    </div>

    <!-- Team Grid -->
    <div class="grid md:grid-cols-3 gap-8">
      <div class="flex flex-col gap-4">
        <div class="text-lg font-semibold">@Jacob</div>
        <div class="text-base font-medium">Chief Executive Officer</div>
        <div class="text-base opacity-80 leading-relaxed">
          Licensed agent with deep frontline experience turning daily inefficiencies into scalable
          solutions.
        </div>
      </div>
      <div class="flex flex-col gap-4">
        <div class="text-lg font-semibold">@Kevin</div>
        <div class="text-base font-medium">Chief Strategy Officer</div>
        <div class="text-base opacity-80 leading-relaxed">
          Business operator with a sharp eye for systems, sales, and where the market's headed.
        </div>
      </div>
      <div class="flex flex-col gap-4">
        <div class="text-lg font-semibold">@Jose</div>
        <div class="text-base font-medium">Chief Technology Officer</div>
        <div class="text-base opacity-80 leading-relaxed">
          Full-stack engineer and product lead focused on speed, simplicity, and good design.
        </div>
      </div>
    </div>
  </Section>

  <FootBar />
</template>

<script setup lang="ts">
import bannerImage from '@/assets/dc-bg.jpg'
import FootBar from '@/components/FootBar.vue'
import NavBar from '@/components/NavBar.vue'
import ScrollButton from '@/components/ScrollButton.vue'
import Section from '@/components/Section.vue'
</script>

<style scoped></style>
