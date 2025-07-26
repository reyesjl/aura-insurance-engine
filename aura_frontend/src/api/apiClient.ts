/*
 * Aura Insurance Engine – Proprietary Software
 *
 * Copyright © 2025 Jose Reyes (GitHub: @reyesjl). All rights reserved.
 *
 * This software was developed solely by Jose Reyes – full-stack engineer and designer.
 * Jacob Powers contributed as the licensed insurance agent for the project.
 * It is a modern insurance submission platform built to streamline the intake
 * and processing of insurance applications.
 *
 * This code is proprietary and confidential. Unauthorized use, reproduction,
 * distribution, or modification is strictly prohibited.
 *
 * Project repository: https://github.com/reyesjl/aura-insurance-engine
 * DeepWiki: https://app.devin.ai/wiki/reyesjl/aura-insurance-engine
 */

// In production, API_BASE should be empty (same origin)
// In development, it should be http://localhost:8000
const API_BASE =
  import.meta.env.VITE_API_BASE || (import.meta.env.PROD ? '' : 'http://localhost:8000')
const API_VERSION = import.meta.env.VITE_API_VERSION || '/api'
const BASE_URL = `${API_BASE}${API_VERSION}`

class ApiClient {
  private getAuthHeaders(): HeadersInit {
    const token = localStorage.getItem('access_token')
    return {
      'Content-Type': 'application/json',
      ...(token && { Authorization: `Bearer ${token}` }),
    }
  }

  async get<T>(endpoint: string): Promise<T> {
    const response = await fetch(`${BASE_URL}${endpoint}`, {
      method: 'GET',
      headers: this.getAuthHeaders(),
    })

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.error || data.detail || 'Request failed')
    }

    return data
  }

  async post<T>(endpoint: string, body: any): Promise<T> {
    const response = await fetch(`${BASE_URL}${endpoint}`, {
      method: 'POST',
      headers: this.getAuthHeaders(),
      body: JSON.stringify(body),
    })

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.error || data.detail || 'Request failed')
    }

    return data
  }

  async put<T>(endpoint: string, body: any): Promise<T> {
    const response = await fetch(`${BASE_URL}${endpoint}`, {
      method: 'PUT',
      headers: this.getAuthHeaders(),
      body: JSON.stringify(body),
    })

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.error || data.detail || 'Request failed')
    }

    return data
  }

  async delete<T>(endpoint: string): Promise<T> {
    const response = await fetch(`${BASE_URL}${endpoint}`, {
      method: 'DELETE',
      headers: this.getAuthHeaders(),
    })

    // Some DELETE requests return no content
    if (response.status === 204) {
      return {} as T
    }

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.error || data.detail || 'Request failed')
    }

    return data
  }
}

export const api = new ApiClient()
