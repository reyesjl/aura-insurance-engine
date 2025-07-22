import type { InsuranceType } from './InsuranceType'

export interface CoverageLine {
  id: number
  name: string
  abbreviation?: string
  insurance_types: InsuranceType[]
}
