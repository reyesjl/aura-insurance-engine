/*
 * Aura Insurance Engine – Proprietary Software
 *
 * Copyright © 2025 Jose Reyes (GitHub: @reyesjl). All rights reserved.
 *
 * This software was developed solely by Jose Reyes – full-stack engineer and designer.
 * Jacob Powers contributed as the licensed insurance agent for the project.
 * It is a modern insurance submission platform built to streamline the intake
 * and processing of insurance applications.
 *
 * This code is proprietary and confidential. Unauthorized use, reproduction,
 * distribution, or modification is strictly prohibited.
 *
 * Project repository: https://github.com/reyesjl/aura-insurance-engine
 * DeepWiki: https://app.devin.ai/wiki/reyesjl/aura-insurance-engine
 */

/** Generic paginated response type for API endpoints that use pagination.
 * Use as: PaginatedResponse<Question>, PaginatedResponse<User>, etc.
 *
 * Note: based on Django REST Framework's pagination structure.
 */
export interface PaginatedResponse<T> {
  count: number
  next?: string
  previous?: string
  results: T[]
}
