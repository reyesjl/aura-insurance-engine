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
      <div class="text-5xl font-semibold">MCP Server with Automated Agents</div>
      <div class="text-2xl">
        Beyond intake—our Model Context Protocol server takes your completed applications and
        automatically fills carrier portals across the industry. No more manual data entry, no more
        portal juggling. From ApplicationSession to carrier quotes in minutes, not hours.
      </div>
      <div class="flex flex-col gap-5">
        <div class="text-xl">
          <strong>Automated Portal Integration:</strong> Seamlessly connect with major carriers and
          submit applications directly from your AURA workflow.
        </div>
        <div class="text-xl">
          <strong>Real-time Quote Retrieval:</strong> Automated agents fetch quotes and post them
          back to your dashboard for instant comparison.
        </div>
        <div class="text-xl">
          <strong>End-to-End Automation:</strong> From ApplicationAnswer collection to carrier
          submission—streamline your entire workflow.
        </div>
      </div>
      <div class="flex flex-col gap-2">
        <router-link class="text-2xl w-fit underline underline-offset-6" to="/auth/register">
          Experience automated carrier integration.
        </router-link>
      </div>
    </div>
  </ImageSection>

  <!-- AI-Powered Carrier Recommendations Section -->
  <Section mode="dark" padding="large">
    <div class="flex flex-col gap-5 md:gap-none md:flex-row text-white">
      <div class="w-full md:w-1/2">
        <div class="text-4xl md:text-5xl font-semibold w-full">
          AI-Powered Carrier Recommendations
        </div>
      </div>
      <div class="w-full md:w-1/2 flex flex-col text-2xl gap-10 mt-10 md:mt-0">
        <div>
          Stop guessing which carriers to approach. Our AI analyzes quotes, carrier context, and
          market conditions to provide intelligent recommendations—automating the agent's
          decision-making process with data-driven insights.
        </div>
      </div>
    </div>

    <div class="grid md:grid-cols-2 gap-10 mt-15 text-white">
      <div class="flex flex-col gap-5">
        <div class="text-3xl font-semibold">Intelligent Analysis</div>
        <div class="text-xl">
          Advanced algorithms analyze carrier performance, quote competitiveness, and coverage
          quality to rank your best options automatically.
        </div>
      </div>
      <div class="flex flex-col gap-5">
        <div class="text-3xl font-semibold">Contextual Insights</div>
        <div class="text-xl">
          Beyond price comparison—understand carrier appetite, underwriting preferences, and market
          positioning for each submission.
        </div>
      </div>
      <div class="flex flex-col gap-5">
        <div class="text-3xl font-semibold">Automated Workflow</div>
        <div class="text-xl">
          From ApplicationSession completion to carrier recommendations—let AI handle the analysis
          while you focus on client relationships.
        </div>
      </div>
      <div class="flex flex-col gap-5">
        <div class="text-3xl font-semibold">Market Intelligence</div>
        <div class="text-xl">
          Leverage real-time market data and carrier trends to make informed decisions with
          confidence backed by comprehensive analytics.
        </div>
      </div>
    </div>

    <div class="mt-15 text-center">
      <router-link
        class="text-2xl bg-blue-600 hover:bg-blue-700 px-8 py-4 rounded-lg transition-colors duration-200 inline-block text-white no-underline"
        to="/auth/register"
      >
        Discover AI-Powered Recommendations
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
