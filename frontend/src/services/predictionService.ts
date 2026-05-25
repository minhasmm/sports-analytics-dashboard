import { apiClient } from './api'

/**
 * Prediction Service
 * Handles all prediction-related API calls
 */

export interface Prediction {
  id: number
  match_id: number
  home_team: string
  away_team: string
  predicted_winner: string
  confidence: number
  probability: {
    home_win: number
    draw: number
    away_win: number
  }
  predicted_score: string
  created_at: string
}

export interface PlayerPerformancePrediction {
  player_id: number
  match_id: number
  expected_goals: number
  expected_assists: number
  expected_rating: number
  performance_category: 'high' | 'medium' | 'low'
}

export interface PredictionResponse {
  status: string
  data: Prediction | Prediction[] | any
  message: string
}

class PredictionService {
  /**
   * Get match predictions
   */
  static async getPredictions(limit = 10, league?: string) {
    try {
      const response = await apiClient.get<PredictionResponse>('/predictions', {
        params: { limit, league },
      })
      return response.data
    } catch (error) {
      console.error('Error fetching predictions:', error)
      throw error
    }
  }

  /**
   * Predict specific match
   */
  static async predictMatch(matchId: number) {
    try {
      const response = await apiClient.get<PredictionResponse>(`/predictions/${matchId}`)
      return response.data
    } catch (error) {
      console.error(`Error predicting match ${matchId}:`, error)
      throw error
    }
  }

  /**
   * Predict league winner
   */
  static async predictLeagueWinner(league: string) {
    try {
      const response = await apiClient.get<PredictionResponse>('/predictions/league-winner', {
        params: { league },
      })
      return response.data
    } catch (error) {
      console.error(`Error predicting league winner for ${league}:`, error)
      throw error
    }
  }

  /**
   * Get prediction accuracy
   */
  static async getPredictionAccuracy() {
    try {
      const response = await apiClient.get<PredictionResponse>('/predictions/accuracy')
      return response.data
    } catch (error) {
      console.error('Error fetching prediction accuracy:', error)
      throw error
    }
  }

  /**
   * Predict player performance
   */
  static async predictPlayerPerformance(playerId: number, matchId: number) {
    try {
      const response = await apiClient.get<PredictionResponse>(
        `/predictions/player-performance`,
        {
          params: { player_id: playerId, match_id: matchId },
        }
      )
      return response.data
    } catch (error) {
      console.error(
        `Error predicting player ${playerId} performance in match ${matchId}:`,
        error
      )
      throw error
    }
  }

  /**
   * Predict player injury risk
   */
  static async predictInjuryRisk(playerId: number) {
    try {
      const response = await apiClient.get<PredictionResponse>(
        `/predictions/injury-risk`,
        {
          params: { player_id: playerId },
        }
      )
      return response.data
    } catch (error) {
      console.error(`Error predicting injury risk for player ${playerId}:`, error)
      throw error
    }
  }

  /**
   * Predict top scorers end of season
   */
  static async predictTopScorersEndOfSeason(limit = 5) {
    try {
      const response = await apiClient.get<PredictionResponse>(
        '/predictions/top-scorers-end-of-season',
        {
          params: { limit },
        }
      )
      return response.data
    } catch (error) {
      console.error('Error predicting top scorers:', error)
      throw error
    }
  }

  /**
   * Predict team final position
   */
  static async predictTeamFinalPosition(teamId: number) {
    try {
      const response = await apiClient.get<PredictionResponse>(
        `/predictions/team-finish-position`,
        {
          params: { team_id: teamId },
        }
      )
      return response.data
    } catch (error) {
      console.error(`Error predicting final position for team ${teamId}:`, error)
      throw error
    }
  }

  /**
   * Get upset probability
   */
  static async getUpsetProbability(matchId: number) {
    try {
      const response = await apiClient.get<PredictionResponse>(
        `/predictions/${matchId}/upset-probability`
      )
      return response.data
    } catch (error) {
      console.error(`Error calculating upset probability for match ${matchId}:`, error)
      throw error
    }
  }

  /**
   * Predict total goals
   */
  static async predictTotalGoals(matchId: number) {
    try {
      const response = await apiClient.get<PredictionResponse>(
        `/predictions/${matchId}/total-goals`
      )
      return response.data
    } catch (error) {
      console.error(`Error predicting total goals for match ${matchId}:`, error)
      throw error
    }
  }
}

export default PredictionService
