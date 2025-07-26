/* * Aura Insurance Engine – Proprietary Software * * Copyright © 2025 Jose Reyes (GitHub:
@reyesjl). All rights reserved. * * This software was developed solely by Jose Reyes – full-stack
engineer and designer. * Jacob Powers contributed as the licensed insurance agent for the project. *
It is a modern insurance submission platform built to streamline the intake * and processing of
insurance applications. * * This code is proprietary and confidential. Unauthorized use,
reproduction, * distribution, or modification is strictly prohibited. * * Project repository:
https://github.com/reyesjl/aura-insurance-engine * DeepWiki:
https://app.devin.ai/wiki/reyesjl/aura-insurance-engine */

<template>
  <div
    class="w-fit h-fit border border-black text-center font-medium flex items-center align-center justify-center"
    :class="[getInsuranceTypeClass(coverage.abbreviation), getSizeClass(size)]"
    :aria-label="coverage.name"
    :title="coverage.name"
  >
    {{ coverage.abbreviation || 'N/A' }}
  </div>
</template>

<script setup lang="ts">
import type { CoverageLine } from '@/types'

const props = defineProps<{
  coverage: CoverageLine
  size?: 'xs' | 'sm' | 'md' | 'lg'
}>()

const size = props.size || 'xs'

const getInsuranceTypeClass = (abbreviation?: string): string => {
  const colorClasses: Record<string, string> = {
    GL: 'bg-black text-white',
    WC: 'bg-orange-500 text-white',
    'E&O': 'bg-red-500 text-white',
    CYB: 'bg-purple-500 text-white',
    AUTO: 'bg-blue-500 text-white',
    UMB: 'bg-yellow-500 text-black',
  }
  return abbreviation ? colorClasses[abbreviation] || 'bg-gray-500' : 'bg-gray-500'
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
