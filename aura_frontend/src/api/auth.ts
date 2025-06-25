import type { User } from '@/types'

// In production, API_BASE should be empty (same origin)
// In development, it should be http://localhost:8000
const API_BASE =
  import.meta.env.VITE_API_BASE || (import.meta.env.PROD ? '' : 'http://localhost:8000')
const API_VERSION = import.meta.env.VITE_API_VERSION || '/api'
const BASE_URL = `${API_BASE}${API_VERSION}`

export interface LoginRequest {
  // email: string
  // username: string
  loginField: string // using this one!
  password: string
}

export interface RegisterRequest {
  email: string
  username: string
  password: string
  confirmPassword: string
}

export interface AuthResponse {
  access: string
  refresh: string
  user: User
}

export interface ApiError {
  error: string
}

class AuthAPI {
  private getAuthHeaders(): HeadersInit {
    const token = localStorage.getItem('access_token')
    return {
      'Content-Type': 'application/json',
      ...(token && { Authorization: `Bearer ${token}` }),
    }
  }

  async login(credentials: LoginRequest): Promise<AuthResponse> {
    // Transform loginField to the backend expected format
    const payload = {
      email: credentials.loginField, // Backend expects 'email' field for login
      password: credentials.password,
    }

    const response = await fetch(`${BASE_URL}/auth/login/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    })

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.error || 'Login failed')
    }

    return data
  }

  async register(userData: RegisterRequest): Promise<AuthResponse> {
    const response = await fetch(`${BASE_URL}/auth/register/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    })

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.error || 'Registration failed')
    }

    return data
  }

  async logout(refreshToken: string): Promise<void> {
    try {
      await fetch(`${BASE_URL}/auth/logout/`, {
        method: 'POST',
        headers: this.getAuthHeaders(),
        body: JSON.stringify({ refresh: refreshToken }),
      })
    } catch (error) {
      // Continue with logout even if API call fails
      console.warn('Logout API call failed:', error)
    }
  }

  async refreshToken(refreshToken: string): Promise<{ access: string }> {
    const response = await fetch(`${BASE_URL}/auth/refresh/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ refresh: refreshToken }),
    })

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.error || 'Token refresh failed')
    }

    return data
  }

  async getUserProfile(): Promise<User> {
    const response = await fetch(`${BASE_URL}/auth/profile/`, {
      headers: this.getAuthHeaders(),
    })

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.error || 'Failed to fetch user profile')
    }

    return data
  }
}

export const authAPI = new AuthAPI()
