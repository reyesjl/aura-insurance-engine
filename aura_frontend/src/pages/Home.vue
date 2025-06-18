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

  <!-- Our Mission Section -->
  <Section mode="light">
    <div class="text-3xl md:text-4xl">Our Mission</div>
    <div class="flex flex-col gap-5 md:gap-none md:flex-row mt-10">
      <div class="w-full md:w-1/2">
        <div class="text-4xl md:text-5xl font-semibold w-full">
          Transforming insurance processing with advanced software.
        </div>
      </div>
      <div class="w-full md:w-1/2 flex flex-col text-2xl gap-5 mt-10 md:mt-0">
        <div>The insurance world has changed. How we process needs to change too.</div>
        <div>
          Insurance submissions are fractured and slow. To fix that, we put technology ahead of
          tradition—streamlining intake across carriers and lines to give agents and underwriters a
          unified, real-time advantage.
        </div>
      </div>
    </div>
  </Section>

  <!-- Rebuild the Backbone Section -->
  <ImageSection
    :image="rebuildBanner"
    overlay
    overlayClass="bg-black/40 backdrop-blur-xs"
    aria-label="Descriptive alt text"
  >
    <div class="flex flex-col gap-15 text-white md:w-1/2">
      <div class="text-5xl font-semibold">Rebuild the Backbone</div>
      <div class="text-2xl">
        Insurance runs on outdated infrastructure. Agents juggle portals. Carriers chase clarity.
        It’s time for a connected system—one that unifies intake and accelerates decisions across
        every line and carrier. See how we’re rebuilding the core of insurance—and how you can be
        part of it.
      </div>
      <div class="flex flex-col gap-2">
        <a class="text-2xl w-fit underline underline-offset-6" href="#UMSI"
          >Upgrade your intake process with UMSI.</a
        >
        <router-link class="text-2xl w-fit underline underline-offset-6" to="/auth/register">
          Get started with a free aura account.
        </router-link>
      </div>
    </div>
  </ImageSection>

  <!-- Unified Intelligence Section -->
  <Section id="UMSI" mode="beige">
    <div class="flex flex-col gap-5 md:gap-none md:flex-row">
      <div class="w-full md:w-1/2">
        <div class="text-4xl md:text-5xl font-semibold w-full">
          Unified Multi-line Submission Intelligence
        </div>
      </div>
      <div class="w-full md:w-1/2 flex flex-col text-2xl gap-10 mt-10 md:mt-0">
        <div>
          A single smart intake, powered by our AURA engine, that generates dynamic reports for
          every carrier—merging all questions and coverage lines into one seamless experience for
          agents, carriers, and the insured.
        </div>
      </div>
    </div>

    <AuraSteps />
  </Section>

  <!-- Footer -->
  <FootBar />
</template>

<script setup lang="ts">
import NavBar from '@/components/NavBar.vue'
import FootBar from '@/components/FootBar.vue'
import AuraSteps from '@/components/AuraSteps.vue'
import bannerImage from '@/assets/juliane-bg.jpg'
import rebuildBanner from '@/assets/staircase-bg.jpg'
import ScrollButton from '@/components/ScrollButton.vue'
import Section from '@/components/Section.vue'
import ImageSection from '@/components/ImageSection.vue'
</script>

<style scoped></style>
