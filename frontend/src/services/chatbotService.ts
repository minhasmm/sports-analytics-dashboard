import { apiClient } from './api'

/**
 * Chatbot Service
 * Handles all chatbot-related API calls
 */

export interface ChatMessage {
  id: string
  message: string
  response: string
  intent: string
  confidence: number
  timestamp: string
}

export interface ChatbotResponse {
  status: string
  message: string
  user_id: string
  intent: string
  confidence: number
  entities: any
  timestamp: string
  follow_up_question?: string
  suggestions?: string[]
}

export interface ChatbotSuggestion {
  id: number
  text: string
}

class ChatbotService {
  /**
   * Send message to chatbot
   */
  static async sendMessage(message: string, userId?: string) {
    try {
      const response = await apiClient.post<ChatbotResponse>('/chatbot/query', {
        message,
        user_id: userId,
      })
      return response.data
    } catch (error) {
      console.error('Error sending message to chatbot:', error)
      throw error
    }
  }

  /**
   * Get chat history
   */
  static async getChatHistory(userId: string, limit = 50) {
    try {
      const response = await apiClient.get<ChatbotResponse>('/chatbot/history', {
        params: { user_id: userId, limit },
      })
      return response.data
    } catch (error) {
      console.error(`Error fetching chat history for user ${userId}:`, error)
      throw error
    }
  }

  /**
   * Get chatbot suggestions
   */
  static async getSuggestions() {
    try {
      const response = await apiClient.get<{ data: string[] }>('/chatbot/suggestions')
      return response.data
    } catch (error) {
      console.error('Error fetching chatbot suggestions:', error)
      throw error
    }
  }

  /**
   * Clear chat history
   */
  static async clearChatHistory(userId: string) {
    try {
      const response = await apiClient.post<ChatbotResponse>('/chatbot/clear-history', {
        user_id: userId,
      })
      return response.data
    } catch (error) {
      console.error(`Error clearing chat history for user ${userId}:`, error)
      throw error
    }
  }

  /**
   * Generate report from chat
   */
  static async generateReport(userId: string, reportType = 'general') {
    try {
      const response = await apiClient.post<ChatbotResponse>('/chatbot/report', {
        user_id: userId,
        report_type: reportType,
      })
      return response.data
    } catch (error) {
      console.error(`Error generating report for user ${userId}:`, error)
      throw error
    }
  }

  /**
   * Get chatbot health status
   */
  static async getHealthStatus() {
    try {
      const response = await apiClient.get('/chatbot/health')
      return response.data
    } catch (error) {
      console.error('Error fetching chatbot health status:', error)
      throw error
    }
  }
}

export default ChatbotService
