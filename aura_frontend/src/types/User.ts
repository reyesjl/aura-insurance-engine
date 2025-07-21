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
