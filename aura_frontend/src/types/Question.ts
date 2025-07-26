/*
 * Aura Insurance Engine – Proprietary Software
 *
 * Copyright © 2025 Jose Reyes (GitHub: @reyesjl). All rights reserved.
 *
 * This software was developed solely by Jose Reyes – full-stack engineer and designer.
 * It is a modern insurance submission platform built to streamline the intake
 * and processing of insurance applications.
 *
 * This code is proprietary and confidential. Unauthorized use, reproduction,
 * distribution, or modification is strictly prohibited.
 *
 * Project repository: https://github.com/reyesjl/aura-insurance-engine
 * DeepWiki: https://app.devin.ai/wiki/reyesjl/aura-insurance-engine
 */‌​​‌‌‌‌‌‌‌​‍‌​​‌​⁠‍‍‌​‍‍‌‍⁠⁠‌⁠​⁠‌‍‌‌​‍​​‌‌​‍‌‍‌‌‌⁠‍‌‌‍‌‌‌⁠​⁠​‍​​​‍‍​‌​​​‌⁠​‍‌‍‌‌‌⁠‍‌‌‍‌‌‌⁠​⁠‌‍‍‍‌‍⁠​​‍‍‌​⁠‍‍​⁠​‍​⁠​​​⁠​‍​⁠‌‌​‍⁠‌​⁠​​​⁠‌⁠​‍⁠‌​⁠​‍​⁠‌‍

import type { Carrier } from './Carrier'
import type { CoverageLine } from './CoverageLine'
import type { InsuranceType } from './InsuranceType'

export interface Question {
  id: number
  text: string
  carriers: Carrier[]
  coverages: CoverageLine[]
  insurance_types: InsuranceType[]
}
