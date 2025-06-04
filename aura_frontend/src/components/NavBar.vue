<template>
  <div
    :class="[
      'fixed w-full top-0 flex justify-between transition-colors duration-300 z-9999',
      isScrolled
        ? 'bg-beige-200 text-black border-b border-black'
        : 'bg-transparent text-white border-b border-white',
      isHidden && isScrolled ? '-translate-y-full' : 'translate-y-0',
      'transition-transform duration-300',
    ]"
  >
    <div
      :class="[
        'p-10 md:p-8 w-fit font-bold font-scp flex flex-grow-1 md:flex-grow-0 items-center align-center duration-300',
        isScrolled
          ? 'border-r border-black hover:bg-gray-200 hover:text-black'
          : 'border-r border-white hover:bg-gray-400 hover:text-black',
      ]"
    >
      <router-link class="min-h-[37px]" to="/">
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
        'px-10 w-fit text-lg hidden md:flex flex-grow align-center items-center gap-8',
        isScrolled ? 'border-r border-black' : 'border-r border-white',
      ]"
    >
      <router-link
        to="/"
        :class="['hover:underline underline-offset-6', isScrolled ? 'text-black' : 'text-white']"
        >Home</router-link
      >
      <router-link
        to="/personal"
        :class="['hover:underline underline-offset-6', isScrolled ? 'text-black' : 'text-white']"
        >Personal</router-link
      >
      <router-link
        to="/commercial"
        :class="['hover:underline underline-offset-6', isScrolled ? 'text-black' : 'text-white']"
        >Commercial</router-link
      >
      <router-link
        to="/about"
        :class="['hover:underline underline-offset-6', isScrolled ? 'text-black' : 'text-white']"
        >About Us</router-link
      >
    </div>
    <div class="md:flex align-center items-center px-10 hidden text-lg">
      <a
        href="https://forms.gle/9T3hno3iGvyiuWGd7"
        target="_blank"
        rel="noopener"
        :class="['hover:underline underline-offset-6', isScrolled ? 'text-black' : 'text-white']"
        >Leave Feedback</a
      >
    </div>
    <div
      :class="[
        'text-lg bg-black text-white flex align-center items-center px-10 duration-300 hover:bg-white hover:text-black',
        isScrolled ? 'border-l border-black' : 'border-l border-white',
      ]"
    >
      <router-link to="/"><button>Menu</button></router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const isScrolled = ref(false)
const isHidden = ref(false)
let lastScrollY = window.scrollY

const handleScroll = () => {
  const currentY = window.scrollY
  const prevScrolled = isScrolled.value
  isScrolled.value = currentY > 10

  if (!isScrolled.value) {
    isHidden.value = false
  } else {
    // Only allow hiding if already in scrolled state before this event AND scrolled at least 300px
    if (prevScrolled && currentY > lastScrollY && !isHidden.value && currentY > 300) {
      isHidden.value = true
    } else if (currentY < lastScrollY && isHidden.value) {
      isHidden.value = false
    }
  }
  lastScrollY = currentY
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
