import { apiClient } from './api'

/**
 * Team Service
 * Handles all team-related API calls
 */

export interface Team {
  id: number
  name: string
  short_name: string
  league: string
  country: string
  city: string
  stadium: string
  founded_year: number
  capacity: number
  coach: string
  website: string
  matches_played: number
  wins: number
  draws: number
  losses: number
  goals_for: number
  goals_against: number
  points: number
  position: number
  created_at: string
  updated_at: string
}

export interface TeamStats {
  team_id: number
  wins: number
  draws: number
  losses: number
  goals_for: number
  goals_against: number
  points: number
  position: number
  win_percentage: number
}

export interface TeamResponse {
  status: string
  data: Team | Team[]
  message: string
}

class TeamService {
  /**
   * Get all teams
   */
  static async getTeams(league?: string) {
    try {
      const response = await apiClient.get<TeamResponse>('/teams', {
        params: { league },
      })
      return response.data
    } catch (error) {
      console.error('Error fetching teams:', error)
      throw error
    }
  }

  /**
   * Get team by ID
   */
  static async getTeamById(teamId: number) {
    try {
      const response = await apiClient.get<TeamResponse>(`/teams/${teamId}`)
      return response.data
    } catch (error) {
      console.error(`Error fetching team ${teamId}:`, error)
      throw error
    }
  }

  /**
   * Get team statistics
   */
  static async getTeamStats(teamId: number) {
    try {
      const response = await apiClient.get<TeamResponse>(`/teams/${teamId}/stats`)
      return response.data
    } catch (error) {
      console.error(`Error fetching team stats for ${teamId}:`, error)
      throw error
    }
  }

  /**
   * Get league standings
   */
  static async getLeagueStandings(league: string) {
    try {
      const response = await apiClient.get<TeamResponse>('/stats/league-standings', {
        params: { league },
      })
      return response.data
    } catch (error) {
      console.error(`Error fetching standings for ${league}:`, error)
      throw error
    }
  }

  /**
   * Get team players
   */
  static async getTeamPlayers(teamId: number) {
    try {
      const response = await apiClient.get<TeamResponse>(`/teams/${teamId}/players`)
      return response.data
    } catch (error) {
      console.error(`Error fetching players for team ${teamId}:`, error)
      throw error
    }
  }

  /**
   * Get team recent matches
   */
  static async getTeamRecentMatches(teamId: number, limit = 10) {
    try {
      const response = await apiClient.get<TeamResponse>(`/teams/${teamId}/recent-matches`, {
        params: { limit },
      })
      return response.data
    } catch (error) {
      console.error(`Error fetching recent matches for team ${teamId}:`, error)
      throw error
    }
  }

  /**
   * Get team upcoming matches
   */
  static async getTeamUpcomingMatches(teamId: number, limit = 10) {
    try {
      const response = await apiClient.get<TeamResponse>(`/teams/${teamId}/upcoming-matches`, {
        params: { limit },
      })
      return response.data
    } catch (error) {
      console.error(`Error fetching upcoming matches for team ${teamId}:`, error)
      throw error
    }
  }

  /**
   * Get head-to-head statistics
   */
  static async getHeadToHead(teamId1: number, teamId2: number) {
    try {
      const response = await apiClient.get<TeamResponse>(`/teams/${teamId1}/head-to-head`, {
        params: { opponent_id: teamId2 },
      })
      return response.data
    } catch (error) {
      console.error(`Error fetching h2h for teams ${teamId1} vs ${teamId2}:`, error)
      throw error
    }
  }

  /**
   * Get team form
   */
  static async getTeamForm(teamId: number, lastMatches = 5) {
    try {
      const response = await apiClient.get<TeamResponse>(`/teams/${teamId}/form`, {
        params: { last_matches: lastMatches },
      })
      return response.data
    } catch (error) {
      console.error(`Error fetching team form for ${teamId}:`, error)
      throw error
    }
  }

  /**
   * Get home/away statistics
   */
  static async getHomeAwayStats(teamId: number) {
    try {
      const response = await apiClient.get<TeamResponse>(`/teams/${teamId}/home-away-stats`)
      return response.data
    } catch (error) {
      console.error(`Error fetching home/away stats for team ${teamId}:`, error)
      throw error
    }
  }
}

export default TeamService
