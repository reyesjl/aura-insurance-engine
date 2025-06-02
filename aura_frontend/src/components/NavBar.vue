<template>
  <div
    :class="[
      'fixed w-full top-0 flex transition-colors duration-300',
      isScrolled
        ? 'bg-[#FAF3E3] text-black border-b border-black'
        : 'bg-transparent text-white border-b border-white'
    ]"
  >
    <div
      :class="[
        'p-10 md:p-8 w-fit text-2xl font-bold font-scp flex items-center align-center duration-300',
        isScrolled
          ? 'border-r border-black hover:bg-gray-200 hover:text-black'
          : 'border-r border-white hover:bg-gray-400 hover:text-black'
      ]"
    >

      <router-link to="/">
        <img
          v-if="!isScrolled"
          src="@/assets/aura_logo_light.svg"
          alt="Aura Logo"
          class="mr-5 min-w-[100px] max-w-[100px] md:max-w-[120px]"
        />
        <img
          v-else
          src="@/assets/aura_logo_dark.svg"
          alt="Aura Logo"
          class="mr-5 min-w-[100px] max-w-[100px] md:max-w-[120px]"
        />
      </router-link>
    </div>
    <div
      :class="[
        'px-10 w-fit flex flex-grow align-center items-center gap-8',
        isScrolled ? 'border-r border-black' : 'border-r border-white'
      ]"
    >
      <router-link
        to="/"
        :class="['hover:underline underline-offset-6', isScrolled ? 'text-black' : 'text-white']"
      >Home</router-link>
      <router-link
        to="/agent"
        :class="['hover:underline underline-offset-6', isScrolled ? 'text-black' : 'text-white']"
      >Personal</router-link>
      <router-link
        to="/sessions"
        :class="['hover:underline underline-offset-6', isScrolled ? 'text-black' : 'text-white']"
      >Commercial</router-link>
      <router-link
        to="/about"
        :class="['hover:underline underline-offset-6', isScrolled ? 'text-black' : 'text-white']"
      >About Us</router-link>
    </div>
    <div class="flex align-center items-center px-10">
      <a
        href="https://forms.gle/9T3hno3iGvyiuWGd7"
        target="_blank"
        rel="noopener"
        :class="['hover:underline underline-offset-6', isScrolled ? 'text-black' : 'text-white']"
      >Leave Feedback</a>
    </div>
    <div
    :class="['bg-black text-white flex align-center items-center px-10 duration-300 hover:bg-white hover:text-black', 
      isScrolled ? 'border-l border-black' : 'border-l border-white'
    ]">
      <router-link to="/about"><button>Menu</button></router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const isScrolled = ref(false)

const handleScroll = () => {
  isScrolled.value = window.scrollY > 10
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
/* No extra styles needed, all handled by Tailwind */
</style>
