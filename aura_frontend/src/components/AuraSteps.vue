<template>
  <div class="mt-10">
    <div class="container bg-white">
      <div v-if="active === 'Types'" class="py-20">
        <div class="md:w-1/2">
          <div class="text-2xl font-bold">Select a Type</div>
          <div class="divider h-[2px] bg-black my-5"></div>
          <div class="text-xl">
            Commercial or personal—start once, and we structure the entire submission around your
            chosen risk. Every detail smartly aligned from the first click.
          </div>
        </div>
      </div>
      <div v-else-if="active === 'Carriers'" class="py-20">
        <div class="md:w-1/2">
          <div class="text-2xl font-bold">Select the Carriers</div>
          <div class="divider h-[2px] bg-black my-5"></div>
          <div class="text-xl">
            Pull from your existing markets instantly. No more duplicating work—route submissions
            across carriers from a single intake, with logic that adjusts to each one.
          </div>
        </div>
      </div>
      <div v-else-if="active === 'Lines'" class="py-20">
        <div class="md:w-1/2">
          <div class="text-2xl font-bold">Select any Coverage</div>
          <div class="divider h-[2px] bg-black my-5"></div>
          <div class="text-xl">
            Mix and match lines—GL, Auto, Property, Cyber, and more. One intake, infinite
            configurations. Every coverage question dynamically included for complete clarity.
          </div>
        </div>
      </div>
    </div>
    <div class="flex flex-nowrap items-center bg-black border-gray-500 border-1 overflow-x-auto">
      <div
        :class="[
          'p-4 md:p-10 text-sm text-center duration-300 flex-grow-0 md:text-base w-1/3 min-w-[33%] text-nowrap font-bold md:border-r-1 md:border-white cursor-pointer',
          active === 'Types'
            ? 'hover:bg-gray-300 bg-gray-300 text-black'
            : 'hover:bg-gray-900 text-white',
        ]"
        @click="handleClick('Types')"
      >
        Types
      </div>
      <div
        :class="[
          'p-4 md:p-10 text-sm text-center duration-300 md:text-base w-1/3 min-w-[33%] text-nowrap font-bold md:border-r-1 md:border-white cursor-pointer',
          active === 'Carriers' ? 'bg-gray-300 text-black' : 'hover:bg-gray-900 text-white',
        ]"
        @click="handleClick('Carriers')"
      >
        Carriers
      </div>
      <div
        :class="[
          'p-4 md:p-10 text-sm text-center duration-300 md:text-base w-1/3 min-w-[33%] text-nowrap font-bold cursor-pointer',
          active === 'Lines' ? 'bg-gray-300 text-black' : 'hover:bg-gray-900 text-white',
        ]"
        @click="handleClick('Lines')"
      >
        Lines
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const active = ref('Types')

function handleClick(feature: string) {
  active.value = feature
}
</script>

<style scoped></style>
