export interface CoverageLine {
  id: number
  name: string
  abbreviation?: string
  insurance_types: number[] // Array of InsuranceType IDs
}
