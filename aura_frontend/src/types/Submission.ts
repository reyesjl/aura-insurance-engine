export interface Submission {
  id: number
  session: number // ApplicationSession ID (OneToOne relationship)
  submitted_at: string // ISO date string
}
