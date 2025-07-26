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
 */

import { Orbit } from './orbit'
import type { Question } from '@/types'

export interface QuestionsResponse {
  count: number
  next: string | null
  previous: string | null
  results: Question[]
}

// Fetch all questions (paginated)
export function fetchQuestions(params?: Record<string, any>) {
  return Orbit.get<QuestionsResponse>('/questions/', { params })
}

// Fetch a single question by ID
export function fetchQuestion(id: number) {
  return Orbit.get<Question>(`/questions/${id}/`)
}

// Create a new question
export function createQuestion(data: Partial<Question>) {
  return Orbit.post<Question>('/questions/', data)
}

// Update an existing question
export function updateQuestion(id: number, data: Partial<Question>) {
  return Orbit.put<Question>(`/questions/${id}/`, data)
}

// Delete a question
export function deleteQuestion(id: number) {
  return Orbit.delete(`/questions/${id}/`)
}
