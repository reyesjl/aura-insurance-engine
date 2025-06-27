<template>
  <div
    class="w-fit h-fit border border-black text-center font-medium flex items-center align-center justify-center"
    :class="[
      getInsuranceTypeClass(coverage.abbreviation),
      getSizeClass(size)
    ]"
    :aria-label="coverage.name"
    :title="coverage.name"
  >
    {{ coverage.abbreviation }}
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  coverage: {
    name: string
    abbreviation: string
  }
  size?: 'xs' | 'sm' | 'md' | 'lg'
}>()

const size = props.size || 'xs'

const getInsuranceTypeClass = (abbreviation: string): string => {
  const colorClasses: Record<string, string> = {
    'GL': 'bg-black text-white',
    'WC': 'bg-orange-500 text-white',
    'E&O': 'bg-red-500 text-white',
    'CYB': 'bg-purple-500 text-white',
    'AUTO': 'bg-blue-500 text-white',
    'UMB': 'bg-yellow-500 text-black'
  }
  return colorClasses[abbreviation] || 'bg-gray-500'
}

const getSizeClass = (size: 'xs' | 'sm' | 'md' | 'lg'): string => {
  switch (size) {
    case 'xs':
      return 'p-0.5 text-[0.6rem] min-w-[1.2rem] min-h-[1.2rem]'
    case 'sm':
      return 'p-1 text-xs min-w-[2rem] min-h-[2rem]'
    case 'lg':
      return 'p-6 text-2xl min-w-[5rem] min-h-[5rem]'
    case 'md':
    default:
      return 'p-4 text-base min-w-[3rem] min-h-[3rem]'
  }
}
</script>