export interface Question {
  id: number
  text: string
  carriers: number[]  // Array of Carrier IDs
  coverages: number[] // Array of CoverageLine IDs
  insurance_types: number[] // Array of InsuranceType IDs
}
