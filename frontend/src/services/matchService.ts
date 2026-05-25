import { apiClient } from './api'

/**
 * Match Service
 * Handles all match-related API calls
 */

export interface Match {
  id: number
  home_team_id: number
  away_team_id: number
  home_team_name?: string
  away_team_name?: string
  league: string
  season: string
  match_date: string
  venue: string
  home_score: number | null
  away_score: number | null
  status: 'scheduled' | 'ongoing' | 'completed' | 'postponed'
  possession_home: number | null
  possession_away: number | null
  shots_home: number | null
  shots_away: number | null
  created_at: string
  updated_at: string
}

export interface MatchStats {
  match_id: number
  possession_home: number
  possession_away: number
  shots: number
  shots_on_target: number
  passes: number
  tackles: number
  fouls: number
}

export interface MatchResponse {
  status: string
  data: Match | Match[]
  message: string
}

class MatchService {
  /**
   * Get all matches
   */
  static async getMatches(league?: string, status = 'all', limit = 20) {
    try {
      const response = await apiClient.get<MatchResponse>('/matches', {
        params: { league, status, limit },
      })
      return response.data
    } catch (error) {
      console.error('Error fetching matches:', error)
      throw error
    }
  }

  /**
   * Get match by ID
   */
  static async getMatchById(matchId: number) {
    try {
      const response = await apiClient.get<MatchResponse>(`/matches/${matchId}`)
      return response.data
    } catch (error) {
      console.error(`Error fetching match ${matchId}:`, error)
      throw error
    }
  }

  /**
   * Get upcoming matches
   */
  static async getUpcomingMatches(limit = 10, league?: string) {
    try {
      const response = await apiClient.get<MatchResponse>('/matches/upcoming', {
        params: { limit, league },
      })
      return response.data
    } catch (error) {
      console.error('Error fetching upcoming matches:', error)
      throw error
    }
  }

  /**
   * Get recent matches
   */
  static async getRecentMatches(limit = 10) {
    try {
      const response = await apiClient.get<MatchResponse>('/matches/recent', {
        params: { limit },
      })
      return response.data
    } catch (error) {
      console.error('Error fetching recent matches:', error)
      throw error
    }
  }

  /**
   * Get team matches
   */
  static async getTeamMatches(teamId: number, limit = 20) {
    try {
      const response = await apiClient.get<MatchResponse>(`/teams/${teamId}/matches`, {
        params: { limit },
      })
      return response.data
    } catch (error) {
      console.error(`Error fetching matches for team ${teamId}:`, error)
      throw error
    }
  }

  /**
   * Get head-to-head matches
   */
  static async getHeadToHeadMatches(teamId1: number, teamId2: number) {
    try {
      const response = await apiClient.get<MatchResponse>(`/matches/${teamId1}/head-to-head`, {
        params: { opponent_id: teamId2 },
      })
      return response.data
    } catch (error) {
      console.error(`Error fetching h2h matches:`, error)
      throw error
    }
  }

  /**
   * Get match statistics
   */
  static async getMatchStats(matchId: number) {
    try {
      const response = await apiClient.get<MatchResponse>(`/matches/${matchId}/stats`)
      return response.data
    } catch (error) {
      console.error(`Error fetching stats for match ${matchId}:`, error)
      throw error
    }
  }

  /**
   * Get match events
   */
  static async getMatchEvents(matchId: number) {
    try {
      const response = await apiClient.get<MatchResponse>(`/matches/${matchId}/events`)
      return response.data
    } catch (error) {
      console.error(`Error fetching events for match ${matchId}:`, error)
      throw error
    }
  }

  /**
   * Get player match performance
   */
  static async getPlayerMatchPerformance(matchId: number, playerId: number) {
    try {
      const response = await apiClient.get<MatchResponse>(
        `/matches/${matchId}/players/${playerId}`
      )
      return response.data
    } catch (error) {
      console.error(
        `Error fetching player ${playerId} performance in match ${matchId}:`,
        error
      )
      throw error
    }
  }
}

export default MatchService
