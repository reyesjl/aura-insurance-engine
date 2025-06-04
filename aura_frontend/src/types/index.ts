// Match: Carrier model
export interface Carrier {
  id: number
  name: string
}

// Match: CoverageLine model
export interface CoverageLine {
  id: number
  name: string
}

// Match: Question model
export interface Question {
  id: number
  text: string
  carriers: number[]
  coverages: number[]
}

// Match: ApplicationSession model
export interface ApplicationSession {
  id: number
  token: string // UUID
  created_at: string // ISO date string from Django
  carriers: number[]
  coverages: number[]
  status: 'pending' | 'completed' | 'error'
}

// Match: Submission model
export interface Submission {
  id: number
  session: number // session ID or token-based link
  answers: Record<string, any> // or more specific shape if you define it
  submitted_at: string
}
