import axios, { AxiosInstance, AxiosError, AxiosResponse } from 'axios'

/**
 * API Service Configuration
 * Handles all HTTP requests to backend
 */

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api/v1'

class APIClient {
  private client: AxiosInstance

  constructor(baseURL: string = API_BASE_URL) {
    this.client = axios.create({
      baseURL,
      timeout: 10000,
      headers: {
        'Content-Type': 'application/json',
      },
    })

    // Add request interceptor
    this.client.interceptors.request.use(
      (config) => {
        // Add auth token if available
        const token = localStorage.getItem('auth_token')
        if (token) {
          config.headers.Authorization = `Bearer ${token}`
        }
        return config
      },
      (error) => {
        return Promise.reject(error)
      }
    )

    // Add response interceptor
    this.client.interceptors.response.use(
      (response) => response,
      (error: AxiosError) => {
        // Handle errors
        if (error.response?.status === 401) {
          // Unauthorized - redirect to login
          localStorage.removeItem('auth_token')
          window.location.href = '/login'
        }
        return Promise.reject(error)
      }
    )
  }

  /**
   * GET request
   */
  public get<T>(url: string, config?: any): Promise<AxiosResponse<T>> {
    return this.client.get<T>(url, config)
  }

  /**
   * POST request
   */
  public post<T>(url: string, data?: any, config?: any): Promise<AxiosResponse<T>> {
    return this.client.post<T>(url, data, config)
  }

  /**
   * PUT request
   */
  public put<T>(url: string, data?: any, config?: any): Promise<AxiosResponse<T>> {
    return this.client.put<T>(url, data, config)
  }

  /**
   * DELETE request
   */
  public delete<T>(url: string, config?: any): Promise<AxiosResponse<T>> {
    return this.client.delete<T>(url, config)
  }

  /**
   * PATCH request
   */
  public patch<T>(url: string, data?: any, config?: any): Promise<AxiosResponse<T>> {
    return this.client.patch<T>(url, data, config)
  }
}

export const apiClient = new APIClient()
