export interface ApplicationSession {
  id: number
  template: number // ApplicationTemplate ID
  agent?: number // User ID, optional
  token: string // UUID
  name?: string
  insured_email?: string // Optional email for the insured
  created_at: string // ISO date string
  status: 'pending' | 'completed' | 'error'
}
