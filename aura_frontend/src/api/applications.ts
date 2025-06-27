import { api } from './apiClient'
import type { InsuranceType, Carrier, CoverageLine, ApplicationSession } from '@/types'

// API Response interfaces
// (these sometimes can differ from our internal types)
// just business specific and what is needed upfront.
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

class ApplicationsAPI {
  // Get all insurance types
  async getInsuranceTypes(): Promise<InsuranceType[]> {
    // API returns direct array, not paginated response
    return api.get<InsuranceType[]>('/insurance-types/')
  }

  // Get carriers organized by coverage lines for a specific insurance type
  async getCarriersByCoverage(insuranceTypeId: number): Promise<CarriersByCoverageResponse> {
    return api.get<CarriersByCoverageResponse>(
      `/carriers-by-coverage/?insurance_type_id=${insuranceTypeId}`,
    )
  }

  // Preview questions that would be included for given selections
  async previewQuestions(
    insuranceTypeId: number,
    carrierIds: number[],
    coverageIds: number[],
  ): Promise<PreviewQuestionsResponse> {
    const params = new URLSearchParams({
      insurance_type_id: insuranceTypeId.toString(),
      carrier_ids: carrierIds.join(','),
      coverage_ids: coverageIds.join(','),
    })

    return api.get<PreviewQuestionsResponse>(`/preview-questions/?${params}`)
  }

  // Create a new application session
  async createApplicationSession(
    data: CreateApplicationSessionRequest,
  ): Promise<CreateApplicationSessionResponse> {
    return api.post<CreateApplicationSessionResponse>('/create-application-session/', data)
  }

  // Get all application sessions (from the viewset)
  async getApplicationSessions(): Promise<ApplicationSession[]> {
    // The API returns a direct array, not a paginated response
    return api.get<ApplicationSession[]>('/application-sessions/')
  }

  // Get a specific application session
  async getApplicationSession(id: number): Promise<ApplicationSession> {
    return api.get<ApplicationSession>(`/application-sessions/${id}/`)
  }
}

export const applicationsAPI = new ApplicationsAPI()
