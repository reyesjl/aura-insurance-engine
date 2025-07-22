import type { Carrier } from './Carrier'
import type { CoverageLine } from './CoverageLine'
import type { InsuranceType } from './InsuranceType'

export interface Question {
  id: number
  text: string
  carriers: Carrier[]
  coverages: CoverageLine[]
  insurance_types: InsuranceType[]
}
