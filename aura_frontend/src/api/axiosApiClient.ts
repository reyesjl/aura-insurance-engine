import axios, { 
    AxiosError,
    type AxiosInstance, 
    type AxiosRequestConfig } 
    from 'axios'

// In production, API_BASE should be empty (same origin)
// In development, it should be http://localhost:8000
const API_BASE =
  import.meta.env.VITE_API_BASE || (import.meta.env.PROD ? '' : 'http://localhost:8000')
const API_VERSION = import.meta.env.VITE_API_VERSION || '/api'
const BASE_URL = `${API_BASE}${API_VERSION}`

class ApiClient {
  private axiosInstance: AxiosInstance

  constructor() {
    this.axiosInstance = axios.create({
      baseURL: BASE_URL,
      headers: {
        'Content-Type': 'application/json',
      },
    })

    // Add a request interceptor to set auth headers
    this.axiosInstance.interceptors.request.use((config) => {
      const token = localStorage.getItem('access_token')
      if (token) {
        config.headers = config.headers || {}
        config.headers['Authorization'] = `Bearer ${token}`
      }
      return config
    })
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
      // Axios returns data as undefined for 204, so return empty object
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

export const api = new ApiClient()