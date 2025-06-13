<template>
  <NavBar />
  <div class="container mx-auto max-w-md page-spacer">
    <div class="content">
      <h2 class="text-2xl mb-6">Sign Up</h2>
      <form>
        <input placeholder="Username" class="input mb-4 w-full" required />
        <input placeholder="Email" class="input mb-4 w-full" type="email" />
        <input placeholder="Password" class="input mb-4 w-full" type="password" required />
        <button type="submit" class="btn w-full">Register</button>
        <div class="text-red-500 mt-2">error</div>
        <div class="text-green-500 mt-2">success</div>
      </form>
    </div>
  </div>
  <FootBar />
</template>

<script setup lang="ts">
import NavBar from '@/components/NavBar.vue'
import bannerImage from '@/assets/family-bg.jpg'
import FootBar from '@/components/FootBar.vue'
</script>

<style scoped></style>
