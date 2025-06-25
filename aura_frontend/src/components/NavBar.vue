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
        isScrolled ? 'hover:bg-gray-200 hover:text-black' : 'hover:bg-gray-400 hover:text-black',
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
        to="/about"
        :class="['hover:underline underline-offset-6', isScrolled ? 'text-black' : 'text-white']"
        >About Us</router-link
      >
      <a
        href="https://forms.gle/9T3hno3iGvyiuWGd7"
        target="_blank"
        rel="noopener"
        :class="['hover:underline underline-offset-6', isScrolled ? 'text-black' : 'text-white']"
        >Feedback</a
      >
    </div>
    <div
      v-if="!userStore.isLoggedIn"
      class="md:flex align-center items-center px-10 hidden text-lg"
    >
      <!-- <a
          href="https://forms.gle/9T3hno3iGvyiuWGd7"
          target="_blank"
          rel="noopener"
          :class="['hover:underline underline-offset-6', isScrolled ? 'text-black' : 'text-white']"
          >Leave Feedback</a
        > -->
      <router-link
        to="/agent"
        :class="['hover:underline underline-offset-6', isScrolled ? 'text-black' : 'text-white']"
        >Login/Signup</router-link
      >
    </div>
    <div
      @click="toggleMenu"
      :class="[
        'text-lg bg-black text-white flex align-center items-center px-10 duration-300 hover:bg-white hover:text-black cursor-pointer',
        isScrolled ? 'border-l border-black' : 'border-l border-white',
      ]"
    >
      <!-- Replace button with hamburger icon -->
      <div class="hamburger-menu" :class="{ active: menuOpen }">
        <span class="hamburger-line"></span>
        <span class="hamburger-line"></span>
        <span class="hamburger-line"></span>
      </div>
    </div>
    <div
      v-if="userStore.isLoggedIn"
      @click="navToAgent"
      :class="[
        'text-lg bg-black text-white flex align-center items-center px-4 md:px-10 duration-300 hover:bg-white hover:text-black',
        isScrolled ? 'border-l border-black' : 'border-l border-white',
      ]"
    >
      <router-link to="/agent" class="flex align-center items-center">
        <span>MyAgent</span>
      </router-link>
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
          <li class="py-5 border-b-1 text-right md:text-left">
            <router-link to="/">Home</router-link>
          </li>
          <li class="py-5 border-b-1 text-right md:text-left">
            <router-link to="/about">About Us</router-link>
          </li>
          <li v-if="!userStore.isLoggedIn" class="py-5 border-b-1 text-right md:text-left">
            <router-link to="/auth/login">Login/Signup</router-link>
          </li>
          <li class="py-5 border-b-1 text-right md:text-left">
            <a href="https://forms.gle/9T3hno3iGvyiuWGd7" target="_blank" rel="noopener"
              >Feedback</a
            >
          </li>
          <li v-if="userStore.isLoggedIn" class="py-5 border-b-1 text-right md:text-left">
            <button
              @click="handleLogout"
              :class="[
                'hover:underline underline-offset-6 text-sm',
                isScrolled ? 'text-black' : 'text-white',
              ]"
            >
              Logout
            </button>
          </li>
        </ul>
      </div>
    </div>
  </transition>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()

const navbarRef = ref<HTMLElement | null>(null)
const isScrolled = ref(false)
const isHidden = ref(false)
let lastScrollY = window.scrollY

const menuOpen = ref(false)

const handleLogout = async () => {
  try {
    await userStore.logout()
    menuOpen.value = false
    router.push('/')
  } catch (error) {
    console.error('Logout failed:', error)
    router.push('/') // Redirect anyway
  }
}

const setNavbarHeight = () => {
  if (navbarRef.value) {
    const height = navbarRef.value.offsetHeight
    document.documentElement.style.setProperty('--navbar-height', `${height}px`)
  }
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

const navToAgent = () => {
  router.push('/agent')
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

/* Hamburger menu styles */
.hamburger-menu {
  display: flex;
  flex-direction: column;
  width: 24px;
  height: 18px;
  justify-content: space-between;
  cursor: pointer;
}

.hamburger-line {
  width: 100%;
  height: 2px;
  background-color: currentColor;
  transition: all 0.3s ease;
  transform-origin: center;
}

.hamburger-menu.active .hamburger-line:nth-child(1) {
  transform: rotate(45deg) translate(6px, 6px);
}

.hamburger-menu.active .hamburger-line:nth-child(2) {
  opacity: 0;
}

.hamburger-menu.active .hamburger-line:nth-child(3) {
  transform: rotate(-45deg) translate(6px, -6px);
}

/* Hover effect for the hamburger container */
.hamburger-menu:hover .hamburger-line {
  background-color: white;
}
</style>
