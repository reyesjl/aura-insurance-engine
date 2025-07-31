export interface FeedbackData {
  email: string
  content: string
}

export interface FeedbackResponse {
  id: number
  email: string
  content: string
  created_at: string
  status: string
}

export const submitFeedback = async (feedbackData: FeedbackData): Promise<FeedbackResponse> => {
  //   return await api.post<FeedbackResponse>('/feedback/', feedbackData)
  console.log('Submitting feedback:', feedbackData)
  // Temporary mock response to satisfy return type
  return {
    id: 1,
    email: feedbackData.email,
    content: feedbackData.content,
    created_at: new Date().toISOString(),
    status: 'submitted',
  }
}
