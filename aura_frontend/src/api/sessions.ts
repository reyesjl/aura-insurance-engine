import type { Carrier, CoverageLine, Question } from '@/types'

const API_VERSION = import.meta.env.VITE_API_VERSION
const BASE_URL = `${import.meta.env.VITE_API_BASE}${API_VERSION}`

// Helper function to handle API responses
async function handleResponse<T>(res: Response, key?: string): Promise<T> {
  if (!res.ok) {
    const errorMessage = await res.text()
    throw new Error(`API Error: ${res.status} - ${errorMessage}`)
  }
  const json = await res.json()
  return key ? (json[key] as T) : (json as T)
}

// Fetch carriers
export async function fetchCarriers(): Promise<Carrier[]> {
  try {
    const res = await fetch(`${BASE_URL}/carriers/`)
    return await handleResponse<Carrier[]>(res, 'carriers')
  } catch (error) {
    console.error('Error fetching carriers:', error)
    throw error
  }
}

// Fetch coverage lines
export async function fetchCoverageLines(): Promise<CoverageLine[]> {
  try {
    const res = await fetch(`${BASE_URL}/coverages/`)
    return await handleResponse<CoverageLine[]>(res, 'coverages')
  } catch (error) {
    console.error('Error fetching coverage lines:', error)
    throw error
  }
}

// Create session
export async function createSession(
  carrierIds: number[],
  coverageIds: number[]
): Promise<{ token: string }> {
  try {
    const res = await fetch(`${BASE_URL}/create-session/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        carriers: carrierIds,
        coverages: coverageIds,
      }),
    })
    return await handleResponse<{ token: string }>(res, 'token')
  } catch (error) {
    console.error('Error creating session:', error)
    throw error
  }
}

// Preview Questions
export async function previewQuestions(
  carrierIds: number[],
  coverageIds: number[],
): Promise<Question[]> {
  try {
    const res = await fetch(`${BASE_URL}/preview-questions/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        carriers: carrierIds,
        coverages: coverageIds,
      }),
    })
    return await handleResponse<Question[]>(res, 'questions')
  } catch (error) {
    console.error('Error previewing questions:', error)
    throw error
  }
}