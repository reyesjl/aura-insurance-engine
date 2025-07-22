import axios, {
    AxiosError,
    type AxiosInstance,
    type AxiosRequestConfig,
    type AxiosResponse
} from 'axios'

const API_BASE =
  import.meta.env.VITE_API_BASE || (import.meta.env.PROD ? '' : 'http://localhost:8000')
const API_VERSION = import.meta.env.VITE_API_VERSION || '/api'
const BASE_URL = `${API_BASE}${API_VERSION}`

class OrbitClient {
  private axiosInstance: AxiosInstance

  constructor() {
    this.axiosInstance = axios.create({
      baseURL: BASE_URL,
      headers: {
        'Content-Type': 'application/json',
      },
    })

    // Attach auth token if present
    this.axiosInstance.interceptors.request.use((config) => {
      const token = localStorage.getItem('access_token')
      if (token) {
        config.headers = config.headers || {}
        config.headers['Authorization'] = `Bearer ${token}`
      }
      return config
    })

    // Add response interceptor for 401 handling
    this.axiosInstance.interceptors.response.use(
      response => response,
      async error => {
        if (
          error.response &&
          error.response.status === 401 &&
          localStorage.getItem('refresh_token')
        ) {
          // Try to refresh token
          try {
            const refreshToken = localStorage.getItem('refresh_token')
            // Import your authAPI and call refreshToken
            const { access } = await import('./auth').then(m => m.authAPI.refreshToken(refreshToken!))
            localStorage.setItem('access_token', access)
            // Update Authorization header and retry original request
            error.config.headers['Authorization'] = `Bearer ${access}`
            return this.axiosInstance.request(error.config)
          } catch (refreshError) {
            // If refresh fails, clear tokens and optionally redirect to login
            localStorage.removeItem('access_token')
            localStorage.removeItem('refresh_token')
          }
        }
        return Promise.reject(error)
      }
    )
  }

  async get<T>(endpoint: string, config?: AxiosRequestConfig): Promise<T> {
    try {
      const response = await this.axiosInstance.get<T>(endpoint, config)
      return response.data
    } catch (error) {
      this.handleError(error)
    }
  }

  async post<T>(endpoint: string, body: any, config?: AxiosRequestConfig): Promise<T> {
    try {
      const response = await this.axiosInstance.post<T>(endpoint, body, config)
      return response.data
    } catch (error) {
      this.handleError(error)
    }
  }

  async put<T>(endpoint: string, body: any, config?: AxiosRequestConfig): Promise<T> {
    try {
      const response = await this.axiosInstance.put<T>(endpoint, body, config)
      return response.data
    } catch (error) {
      this.handleError(error)
    }
  }

  async delete<T>(endpoint: string, config?: AxiosRequestConfig): Promise<T> {
    try {
      const response = await this.axiosInstance.delete<T>(endpoint, config)
      return response.data ?? ({} as T)
    } catch (error) {
      this.handleError(error)
    }
  }

  private handleError(error: unknown): never {
    if (axios.isAxiosError(error)) {
      const data = error.response?.data
      throw new AxiosError(data?.error || data?.detail || error.message || 'Request failed')
    }
    throw error
  }
}

export const Orbit = new OrbitClient()