import type { TemplateQuestionSnapshot } from './TemplateQuestionSnapshot'

export interface ApplicationAnswer {
  id: number
  session: number // ApplicationSession ID
  question_snapshot: TemplateQuestionSnapshot
  answer: string
}
