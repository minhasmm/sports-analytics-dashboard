import { apiClient } from './api'

/**
 * Stats Service
 * Handles all statistics-related API calls
 */

export interface Stat {
  id: number
  player_id?: number
  team_id?: number
  goals: number
  assists: number
  rating: number
  [key: string]: any
}

export interface StatsResponse {
  status: string
  data: Stat | Stat[]
  message: string
}

class StatsService {
  /**
   * Get top scorers
   */
  static async getTopScorers(limit = 10, league?: string) {
    try {
      const response = await apiClient.get<StatsResponse>('/stats/top-scorers', {
        params: { limit, league },
      })
      return response.data
    } catch (error) {
      console.error('Error fetching top scorers:', error)
      throw error
    }
  }

  /**
   * Get top assists
   */
  static async getTopAssists(limit = 10, league?: string) {
    try {
      const response = await apiClient.get<StatsResponse>('/stats/top-assists', {
        params: { limit, league },
      })
      return response.data
    } catch (error) {
      console.error('Error fetching top assists:', error)
      throw error
    }
  }

  /**
   * Get league standings
   */
  static async getLeagueStandings(league: string) {
    try {
      const response = await apiClient.get<StatsResponse>('/stats/league-standings', {
        params: { league },
      })
      return response.data
    } catch (error) {
      console.error(`Error fetching standings for ${league}:`, error)
      throw error
    }
  }

  /**
   * Get best defense teams
   */
  static async getBestDefense(limit = 10) {
    try {
      const response = await apiClient.get<StatsResponse>('/stats/best-defense', {
        params: { limit },
      })
      return response.data
    } catch (error) {
      console.error('Error fetching best defense stats:', error)
      throw error
    }
  }

  /**
   * Get efficiency ratings
   */
  static async getEfficiencyRatings(limit = 20) {
    try {
      const response = await apiClient.get<StatsResponse>('/stats/efficiency', {
        params: { limit },
      })
      return response.data
    } catch (error) {
      console.error('Error fetching efficiency ratings:', error)
      throw error
    }
  }

  /**
   * Get statistical trends
   */
  static async getTrends(period = 'season') {
    try {
      const response = await apiClient.get<StatsResponse>('/stats/trends', {
        params: { period },
      })
      return response.data
    } catch (error) {
      console.error(`Error fetching trends for period ${period}:`, error)
      throw error
    }
  }

  /**
   * Get weekly stats
   */
  static async getWeeklyStats() {
    try {
      const response = await apiClient.get<StatsResponse>('/stats/weekly')
      return response.data
    } catch (error) {
      console.error('Error fetching weekly stats:', error)
      throw error
    }
  }

  /**
   * Get monthly stats
   */
  static async getMonthlyStats(year: number, month: number) {
    try {
      const response = await apiClient.get<StatsResponse>('/stats/monthly', {
        params: { year, month },
      })
      return response.data
    } catch (error) {
      console.error(`Error fetching monthly stats for ${month}/${year}:`, error)
      throw error
    }
  }

  /**
   * Get seasonal stats
   */
  static async getSeasonalStats(season: string) {
    try {
      const response = await apiClient.get<StatsResponse>('/stats/seasonal', {
        params: { season },
      })
      return response.data
    } catch (error) {
      console.error(`Error fetching seasonal stats for ${season}:`, error)
      throw error
    }
  }

  /**
   * Get trending players
   */
  static async getTrendingPlayers(limit = 10) {
    try {
      const response = await apiClient.get<StatsResponse>('/stats/trending-players', {
        params: { limit },
      })
      return response.data
    } catch (error) {
      console.error('Error fetching trending players:', error)
      throw error
    }
  }

  /**
   * Get consistency ratings
   */
  static async getConsistencyRatings(limit = 20) {
    try {
      const response = await apiClient.get<StatsResponse>('/stats/consistency', {
        params: { limit },
      })
      return response.data
    } catch (error) {
      console.error('Error fetching consistency ratings:', error)
      throw error
    }
  }
}

export default StatsService
