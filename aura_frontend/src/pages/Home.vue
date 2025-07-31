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
  <Section mode="light" padding="large">
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
  <Section id="UMSI" mode="beige" padding="large">
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

  <!-- MCP Server with Automated Agents Section -->
  <ImageSection
    :image="mcpBanner"
    overlay
    overlayClass="bg-blue-900/50 backdrop-blur-xs"
    aria-label="Modern server infrastructure"
  >
    <div class="flex flex-col gap-15 text-white md:w-2/3">
      <div class="flex flex-col gap-3">
        <div class="text-5xl font-semibold">AURA Bridge</div>
        <div class="text-xl italic opacity-90">Powered by MCP Servers</div>
      </div>
      <div class="text-2xl leading-relaxed">
        From completed application to carrier portal—automatically. AURA Bridge handles the heavy
        lifting after intake, pushing submissions directly into carrier portals across the industry.
        No more copy-pasting, no more tab juggling. Just seamless automation that gets you quotes in
        minutes—not hours.
      </div>
      <div class="grid md:grid-cols-1 gap-6">
        <div class="flex flex-col gap-2">
          <div class="text-xl font-semibold">Seamless Portal Integration</div>
          <div class="text-lg opacity-90">
            Automatically syncs with major carriers from your existing AURA workflow.
          </div>
        </div>
        <div class="flex flex-col gap-2">
          <div class="text-xl font-semibold">Real-Time Quote Retrieval</div>
          <div class="text-lg opacity-90">
            Fetches quotes instantly and returns them to your dashboard.
          </div>
        </div>
        <div class="flex flex-col gap-2">
          <div class="text-xl font-semibold">End-to-End Submission Automation</div>
          <div class="text-lg opacity-90">
            From application to carrier confirmation—fully automated.
          </div>
        </div>
      </div>
      <div class="flex flex-col gap-2">
        <router-link class="text-xl w-fit underline underline-offset-4" to="/auth/register">
          Experience automated carrier integration with AURA Bridge.
        </router-link>
      </div>
    </div>
  </ImageSection>

  <!-- AI-Powered Carrier Recommendations Section -->
  <Section mode="dark" padding="large">
    <div class="flex flex-col gap-5 md:gap-none md:flex-row text-white">
      <div class="w-full md:w-1/2">
        <div class="flex flex-col gap-3">
          <div class="text-4xl md:text-5xl font-semibold">AURA Insight</div>
          <div class="text-xl italic opacity-90">Powered by AI Analytics</div>
        </div>
      </div>
      <div class="w-full md:w-1/2 flex flex-col text-2xl gap-10 mt-10 md:mt-0">
        <div class="leading-relaxed">
          Smarter carrier selection, built into your workflow. AURA Insight removes the guesswork.
          By analyzing submissions, coverage context, and market dynamics, it surfaces the most
          aligned carriers—so you focus on advising, not digging through rate sheets.
        </div>
      </div>
    </div>

    <div class="grid md:grid-cols-2 gap-10 mt-15 text-white">
      <div class="flex flex-col gap-3">
        <div class="text-2xl font-semibold">Context-Aware Matching</div>
        <div class="text-lg opacity-90">
          Understand carrier appetite, underwriting posture, and alignment.
        </div>
      </div>
      <div class="flex flex-col gap-3">
        <div class="text-2xl font-semibold">Competitive Scoring</div>
        <div class="text-lg opacity-90">
          Ranks carriers based on performance, price competitiveness, and fit.
        </div>
      </div>
      <div class="flex flex-col gap-3">
        <div class="text-2xl font-semibold">Integrated Workflow Intelligence</div>
        <div class="text-lg opacity-90">
          Activates the moment an ApplicationSession is completed.
        </div>
      </div>
      <div class="flex flex-col gap-3">
        <div class="text-2xl font-semibold">Market Data + Decision Support</div>
        <div class="text-lg opacity-90">
          Uses trends and live data to guide carrier prioritization.
        </div>
      </div>
    </div>

    <div class="mt-15 text-center">
      <router-link
        class="text-xl bg-blue-600 hover:bg-blue-700 px-8 py-4 rounded-lg transition-colors duration-200 inline-block text-white no-underline"
        to="/auth/register"
      >
        Act with clarity—powered by AURA Insight.
      </router-link>
    </div>
  </Section>

  <!-- Footer -->
  <FootBar />
</template>

<script setup lang="ts">
import mcpBanner from '@/assets/dc-bg.jpg'
import bannerImage from '@/assets/juliane-bg.jpg'
import rebuildBanner from '@/assets/staircase-bg.jpg'
import AuraSteps from '@/components/AuraSteps.vue'
import FootBar from '@/components/FootBar.vue'
import ImageSection from '@/components/ImageSection.vue'
import NavBar from '@/components/NavBar.vue'
import ScrollButton from '@/components/ScrollButton.vue'
import Section from '@/components/Section.vue'
</script>

<style scoped></style>
