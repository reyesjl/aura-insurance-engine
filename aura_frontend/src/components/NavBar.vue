<template>
  <div class="fixed w-full top-0 border-b-1 border-white flex">
    <div
      class="p-10 md:p-8 w-fit text-2xl font-bold font-scp flex items-center align-center"
    >
      <img
        src="@/assets/aura_logo_light.svg"
        alt="Aura Logo"
        class="mr-5 min-w-[100px] max-w-[100px] md:max-w-[120px]"
      />
    </div>
    <div class="border-x-1 border-white px-10 w-fit flex flex-grow align-center items-center gap-8">
      <router-link to="/" class="text-white hover:underline underline-offset-6"> Home </router-link>
      <router-link to="/agent" class="text-white hover:underline underline-offset-6">
        Personal
      </router-link>
      <router-link to="/sessions" class="text-white hover:underline underline-offset-6">
        Commercial
      </router-link>
      <router-link to="/" class="text-white hover:underline underline-offset-6">
        About Us
      </router-link>
    </div>
    <div class="flex align-center items-center px-10">
        <a href="#" class="text-white hover:underline underline-offset-6">Leave Feedback</a>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped></style>
