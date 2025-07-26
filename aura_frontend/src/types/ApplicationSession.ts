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

export interface ApplicationSession {
  id: number
  template: number // ApplicationTemplate ID
  agent?: number // User ID, optional
  token: string // UUID
  name?: string
  insured_email?: string // Optional email for the insured
  created_at: string // ISO date string
  status: 'pending' | 'completed' | 'error'
}
