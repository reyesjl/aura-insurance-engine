export interface ApplicationTemplate {
  id: number
  name: string
  agent?: number // User ID, optional
  insurance_type: number // InsuranceType ID
  carriers: number[] // Array of Carrier IDs
  coverages: number[] // Array of CoverageLine IDs
  created_at: string // ISO date string
}
