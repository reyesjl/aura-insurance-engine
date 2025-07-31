<template>
  <NavBar />
  <div class="page-spacer bg-black"></div>
  <Breadcrumbs />

  <Section mode="light" padding="small">
    <div class="text-4xl md:text-5xl font-semibold leading-tight mb-12">Create New Question</div>

    <div class="max-w-2xl">
      <div class="text-xl leading-relaxed mb-8">
        Add a new question to your insurance application templates. Questions will be available for
        use across different carriers and coverage types.
      </div>

      <!-- Question Form Placeholder -->
      <div class="p-8 bg-gray-100 rounded-lg">
        <div class="text-lg font-semibold mb-4">Question Form</div>
        <div class="text-base opacity-80">Form implementation coming soon...</div>
      </div>
    </div>
  </Section>

  <FootBar />
</template>

<script setup lang="ts">
import Breadcrumbs from '@/components/Breadcrumbs.vue'
import FootBar from '@/components/FootBar.vue'
import NavBar from '@/components/NavBar.vue'
import Section from '@/components/Section.vue'
</script>

<style scoped></style>
