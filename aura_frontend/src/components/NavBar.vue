<template>
  <div
    ref="navbarRef"
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
        'p-4 md:p-6 w-fit font-bold font-scp flex flex-grow-1 md:flex-grow-0 items-center align-center duration-300',
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
        'px-10 w-fit text-lg hidden lg:flex flex-grow align-center items-center gap-8',
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
      @click="toggleMenu"
      :class="[
        'text-lg bg-black text-white flex align-center items-center px-10 duration-300 hover:bg-white hover:text-black',
        isScrolled ? 'border-l border-black' : 'border-l border-white',
      ]"
    >
      <button>Menu</button>
    </div>
  </div>

  <!-- Toggable menu -->
  <transition name="slide-menu">
    <div
      v-if="menuOpen"
      class="bg-black text-white w-full fixed z-999"
      :style="{ top: `var(--navbar-height)` }"
    >
      <div class="container">
        <ul class="flex list-none m-0 p-0 py-10 flex-col text-2xl md:text-4xl">
          <li class="py-5 border-b-1">
            <router-link to="/">Home</router-link>
          </li>
          <li class="py-5 border-b-1">
            <router-link to="/personal">Personal</router-link>
          </li>
          <li class="py-5 border-b-1">
            <router-link to="/commercial">Commercial</router-link>
          </li>
          <li class="py-5 border-b-1">
            <router-link to="/about">About Us</router-link>
          </li>
          <li class="py-5 border-b-1">
            <a href="https://forms.gle/9T3hno3iGvyiuWGd7" target="_blank" rel="noopener"
              >Leave Feedback</a
            >
          </li>
        </ul>
      </div>
    </div>
  </transition>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, nextTick } from 'vue'

const navbarRef = ref<HTMLElement | null>(null)
const isScrolled = ref(false)
const isHidden = ref(false)
let lastScrollY = window.scrollY

const menuOpen = ref(false)

const setNavbarHeight = () => {
  if (navbarRef.value) {
    const height = navbarRef.value.offsetHeight
    document.documentElement.style.setProperty('--navbar-height', `${height}px`)
  }
  console.log(
    'Navbar height set to:',
    document.documentElement.style.getPropertyValue('--navbar-height'),
  )
}

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
}

const handleScroll = () => {
  const currentY = window.scrollY
  const prevScrolled = isScrolled.value
  isScrolled.value = currentY > 10

  if (!isScrolled.value) {
    isHidden.value = false
  } else {
    if (prevScrolled && currentY > lastScrollY && !isHidden.value && currentY > 300) {
      isHidden.value = true
    } else if (currentY < lastScrollY && isHidden.value) {
      isHidden.value = false
    }
  }
  lastScrollY = currentY
  menuOpen.value = false
}

onMounted(() => {
  setNavbarHeight()
  window.addEventListener('resize', setNavbarHeight)
  window.addEventListener('scroll', handleScroll)
  nextTick(setNavbarHeight)
})

onUnmounted(() => {
  window.removeEventListener('resize', setNavbarHeight)
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.slide-menu-enter-active,
.slide-menu-leave-active {
  transition:
    transform 0.9s cubic-bezier(0.4, 0, 0.2, 1),
    opacity 0.5s;
}

.slide-menu-enter-from,
.slide-menu-leave-to {
  transform: translateX(100%);
  opacity: 0;
}
.slide-menu-enter-to,
.slide-menu-leave-from {
  transform: translateX(0);
  opacity: 1;
}
</style>
