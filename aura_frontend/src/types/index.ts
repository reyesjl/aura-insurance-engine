// Match: User model
export interface User {
  id: number
  username: string
  email: string
  first_name: string
  last_name: string
  is_agent: boolean
  agent_name?: string
  agency?: string
  phone_number?: string
  level: number
  xp: number
  // Future: achievements when implemented
}

// Match: InsuranceType model
export interface InsuranceType {
  id: number
  key: string
  label: string
}

// Match: Carrier model
export interface Carrier {
  id: number
  name: string
  insurance_types: number[] // Array of InsuranceType IDs
}

// Match: CoverageLine model
export interface CoverageLine {
  id: number
  name: string
  abbreviation?: string
  insurance_types: number[] // Array of InsuranceType IDs
}

// Match: Question model
export interface Question {
  id: number
  text: string
  carriers: number[] // Array of Carrier IDs
  coverages: number[] // Array of CoverageLine IDs
  insurance_types: number[] // Array of InsuranceType IDs
}

// Match: ApplicationTemplate model
export interface ApplicationTemplate {
  id: number
  name: string
  agent?: number // User ID, optional
  insurance_type: number // InsuranceType ID
  carriers: number[] // Array of Carrier IDs
  coverages: number[] // Array of CoverageLine IDs
  created_at: string // ISO date string
}

// Match: TemplateQuestionSnapshot model
export interface TemplateQuestionSnapshot {
  id: number
  template: number // ApplicationTemplate ID
  original_question: number // Question ID
  question_text: string
}

// Match: ApplicationSession model
export interface ApplicationSession {
  id: number
  template: number // ApplicationTemplate ID
  agent?: number // User ID, optional
  token: string // UUID
  name?: string
  created_at: string // ISO date string
  status: 'pending' | 'completed' | 'error'
}

// Match: ApplicationAnswer model
export interface ApplicationAnswer {
  id: number
  session: number // ApplicationSession ID
  question_snapshot: number // TemplateQuestionSnapshot ID
  answer: string
}

// Match: Submission model
export interface Submission {
  id: number
  session: number // ApplicationSession ID (OneToOne relationship)
  submitted_at: string // ISO date string
}
