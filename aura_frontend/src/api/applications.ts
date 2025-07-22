import { Orbit } from './orbit'
import type { ApplicationSession, InsuranceType, Carrier, CoverageLine } from '@/types'

export interface ApplicationSessionsResponse {
  count: number
  next: string | null
  previous: string | null
  results: ApplicationSession[]
}

export interface CarriersByCoverageResponse {
  insurance_type: InsuranceType
  coverage_lines: Array<{
    coverage: {
      id: number
      name: string
      abbreviation: string
    }
    carriers: Array<{
      id: number
      name: string
    }>
  }>
}

export interface PreviewQuestionsResponse {
  questions_count: number
  questions: Array<{
    id: number
    text: string
    carriers: string[]
    coverages: Array<{
      name: string
      abbreviation: string
    }>
  }>
}

export interface CreateApplicationSessionRequest {
  insurance_type_id: number
  session_name: string
  insured_email?: string
  selections: Array<{
    coverage_id: number
    carrier_ids: number[]
  }>
}

export interface CreateApplicationSessionResponse {
  session: ApplicationSession
  template_id: number
  questions_count: number
  message: string
}

// Fetch all application sessions (paginated)
export function fetchApplicationSessions(params?: Record<string, any>) {
  return Orbit.get<ApplicationSessionsResponse>(
    '/application-sessions/',
    { params }
  )
}

// Fetch a single application session by ID
export function fetchApplicationSession(id: number) {
  return Orbit.get<ApplicationSession>(`/application-sessions/${id}/`)
}

// Create a new application session
export function createApplicationSession(data: CreateApplicationSessionRequest) {
  return Orbit.post<CreateApplicationSessionResponse>('/create-application-session/', data)
}

// Get all insurance types
export function fetchInsuranceTypes() {
  return Orbit.get<InsuranceType[]>('/insurance-types/')
}

// Get carriers organized by coverage lines for a specific insurance type
export function fetchCarriersByCoverage(insuranceTypeId: number) {
  return Orbit.get<CarriersByCoverageResponse>(
    `/carriers-by-coverage/?insurance_type_id=${insuranceTypeId}`
  )
}

// Preview questions for given selections
export function previewQuestions(
  insuranceTypeId: number,
  carrierIds: number[],
  coverageIds: number[]
) {
  const params = new URLSearchParams({
    insurance_type_id: insuranceTypeId.toString(),
    carrier_ids: carrierIds.join(','),
    coverage_ids: coverageIds.join(','),
  })
  return Orbit.get<PreviewQuestionsResponse>(`/preview-questions/?${params}`)
}
