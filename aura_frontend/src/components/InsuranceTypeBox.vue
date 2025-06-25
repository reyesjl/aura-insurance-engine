<template>
  <div class="p-4 w-fit border border-black text-center font-medium text-white flex items-center align-center justify-center"
       :class="getInsuranceTypeClass(insuranceType)">
    {{ insuranceType }}
  </div>
</template>

<script setup lang="ts">
defineProps<{
  insuranceType: string
}>()

const getInsuranceTypeClass = (abbreviation: string): string => {
  const colorClasses: Record<string, string> = {
    'GL': 'bg-black',
    'WC': 'bg-orange-500',
    'E&O': 'bg-red-500',
    'CYB': 'bg-purple-500',
    'AUTO': 'bg-blue-500',
    'UMB': 'bg-yellow-500 text-black' // Yellow with black text for better contrast
  }
  
  return colorClasses[abbreviation] || 'bg-gray-500'
}
</script>