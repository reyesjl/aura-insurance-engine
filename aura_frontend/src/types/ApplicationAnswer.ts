export interface ApplicationAnswer {
  id: number
  session: number // ApplicationSession ID
  question_snapshot: number // TemplateQuestionSnapshot ID
  answer: string
}
