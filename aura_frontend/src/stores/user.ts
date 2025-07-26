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

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import type { User } from '@/types'
import { authAPI, type LoginRequest, type RegisterRequest } from '@/api/auth'

export const useUserStore = defineStore('user', () => {
  // State
  const user = ref<User | null>(null)
  const accessToken = ref<string | null>(null)
  const refreshToken = ref<string | null>(null)
  const isLoading = ref(false)

  // Computed
  const isLoggedIn = computed(() => !!user.value && !!accessToken.value)
  const isAgent = computed(() => user.value?.is_agent || false)

  // Initialize from localStorage
  function initializeFromStorage() {
    const savedUser = localStorage.getItem('user')
    const savedAccessToken = localStorage.getItem('access_token')
    const savedRefreshToken = localStorage.getItem('refresh_token')

    if (savedUser && savedAccessToken) {
      user.value = JSON.parse(savedUser)
      accessToken.value = savedAccessToken
      refreshToken.value = savedRefreshToken
    }
  }

  // Save to localStorage
  function saveToStorage() {
    if (user.value && accessToken.value) {
      localStorage.setItem('user', JSON.stringify(user.value))
      localStorage.setItem('access_token', accessToken.value)
      if (refreshToken.value) {
        localStorage.setItem('refresh_token', refreshToken.value)
      }
    }
  }

  // Clear storage
  function clearStorage() {
    localStorage.removeItem('user')
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
  }

  // Login
  async function login(loginField: string, password: string) {
    isLoading.value = true
    try {
      const response = await authAPI.login({ loginField, password })

      user.value = response.user
      accessToken.value = response.access
      refreshToken.value = response.refresh

      saveToStorage()

      console.log('User logged in:', user.value)
    } catch (error) {
      console.error('Login failed:', error)
      throw error
    } finally {
      isLoading.value = false
    }
  }

  // Register
  async function register(
    email: string,
    username: string,
    password: string,
    confirmPassword: string,
  ) {
    isLoading.value = true
    try {
      const response = await authAPI.register({ email, username, password, confirmPassword })

      user.value = response.user
      accessToken.value = response.access
      refreshToken.value = response.refresh

      saveToStorage()

      console.log('User registered:', user.value)
    } catch (error) {
      console.error('Registration failed:', error)
      throw error
    } finally {
      isLoading.value = false
    }
  }

  // Logout
  async function logout() {
    isLoading.value = true
    try {
      if (refreshToken.value) {
        await authAPI.logout(refreshToken.value)
      }
    } catch (error) {
      console.warn('Logout API call failed:', error)
    } finally {
      user.value = null
      accessToken.value = null
      refreshToken.value = null
      clearStorage()
      isLoading.value = false
      console.log('User logged out')
    }
  }

  // Refresh token
  async function refreshAccessToken() {
    if (!refreshToken.value) {
      throw new Error('No refresh token available')
    }

    try {
      const response = await authAPI.refreshToken(refreshToken.value)
      accessToken.value = response.access
      saveToStorage()
      return response.access
    } catch (error) {
      // If refresh fails, logout user
      await logout()
      throw error
    }
  }

  // TODO: Implement the actual API call for password reset
  async function resetPassword(email: string) {
    // Implement this API endpoint later
    console.log(`Password reset email sent to ${email}`)
    return { success: true, message: 'Password reset email sent successfully!' }
  }

  // Initialize on store creation
  initializeFromStorage()

  return {
    // State
    user,
    accessToken,
    refreshToken,
    isLoading,

    // Computed
    isLoggedIn,
    isAgent,

    // Actions
    login,
    logout,
    register,
    resetPassword,
    refreshAccessToken,
  }
})
