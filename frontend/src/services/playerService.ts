import { apiClient } from './api'

/**
 * Player Service
 * Handles all player-related API calls
 */

export interface Player {
  id: number
  name: string
  age: number
  nationality: string
  position: string
  team_id: number
  team_name?: string
  jersey_number: number
  height: string
  weight: string
  foot: string
  goals: number
  assists: number
  appearances: number
  rating: number
  pass_accuracy: number
  tackles: number
  yellow_cards: number
  red_cards: number
  fouls_committed: number
  created_at: string
  updated_at: string
}

export interface PlayerStats {
  player_id: number
  goals: number
  assists: number
  appearances: number
  rating: number
  pass_accuracy: number
  tackles: number
  interceptions: number
  yellow_cards: number
  red_cards: number
}

export interface PlayerResponse {
  status: string
  data: Player | Player[]
  message: string
}

class PlayerService {
  /**
   * Get all players
   */
  static async getPlayers(page = 1, perPage = 20, filters?: any) {
    try {
      const response = await apiClient.get<PlayerResponse>('/players', {
        params: {
          page,
          per_page: perPage,
          ...filters,
        },
      })
      return response.data
    } catch (error) {
      console.error('Error fetching players:', error)
      throw error
    }
  }

  /**
   * Get player by ID
   */
  static async getPlayerById(playerId: number) {
    try {
      const response = await apiClient.get<PlayerResponse>(`/players/${playerId}`)
      return response.data
    } catch (error) {
      console.error(`Error fetching player ${playerId}:`, error)
      throw error
    }
  }

  /**
   * Search players
   */
  static async searchPlayers(query: string, limit = 20) {
    try {
      const response = await apiClient.get<PlayerResponse>('/players/search', {
        params: { q: query, limit },
      })
      return response.data
    } catch (error) {
      console.error('Error searching players:', error)
      throw error
    }
  }

  /**
   * Get player statistics
   */
  static async getPlayerStats(playerId: number) {
    try {
      const response = await apiClient.get<PlayerResponse>(`/players/${playerId}/stats`)
      return response.data
    } catch (error) {
      console.error(`Error fetching player stats for ${playerId}:`, error)
      throw error
    }
  }

  /**
   * Get top scorers
   */
  static async getTopScorers(limit = 10) {
    try {
      const response = await apiClient.get<PlayerResponse>('/players/top-scorers', {
        params: { limit },
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
  static async getTopAssists(limit = 10) {
    try {
      const response = await apiClient.get<PlayerResponse>('/stats/top-assists', {
        params: { limit },
      })
      return response.data
    } catch (error) {
      console.error('Error fetching top assists:', error)
      throw error
    }
  }

  /**
   * Get players by team
   */
  static async getPlayersByTeam(teamId: number) {
    try {
      const response = await apiClient.get<PlayerResponse>(`/teams/${teamId}/players`)
      return response.data
    } catch (error) {
      console.error(`Error fetching players for team ${teamId}:`, error)
      throw error
    }
  }

  /**
   * Compare players
   */
  static async comparePlayers(playerIds: number[]) {
    try {
      const response = await apiClient.post<PlayerResponse>('/players/compare', {
        player_ids: playerIds,
      })
      return response.data
    } catch (error) {
      console.error('Error comparing players:', error)
      throw error
    }
  }

  /**
   * Get player form
   */
  static async getPlayerForm(playerId: number, lastMatches = 5) {
    try {
      const response = await apiClient.get<PlayerResponse>(`/players/${playerId}/form`, {
        params: { last_matches: lastMatches },
      })
      return response.data
    } catch (error) {
      console.error(`Error fetching player form for ${playerId}:`, error)
      throw error
    }
  }

  /**
   * Get player efficiency rating
   */
  static async getPlayerEfficiency(playerId: number) {
    try {
      const response = await apiClient.get<PlayerResponse>(`/players/${playerId}/efficiency`)
      return response.data
    } catch (error) {
      console.error(`Error fetching player efficiency for ${playerId}:`, error)
      throw error
    }
  }

  /**
   * Get trending players
   */
  static async getTrendingPlayers(limit = 10) {
    try {
      const response = await apiClient.get<PlayerResponse>('/stats/trending', {
        params: { limit },
      })
      return response.data
    } catch (error) {
      console.error('Error fetching trending players:', error)
      throw error
    }
  }
}

export default PlayerService
