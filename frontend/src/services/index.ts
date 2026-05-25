/**
 * Services Index
 * Central export point for all API services
 */

export { default as PlayerService } from './playerService'
export { default as TeamService } from './teamService'
export { default as MatchService } from './matchService'
export { default as PredictionService } from './predictionService'
export { default as ChatbotService } from './chatbotService'
export { default as StatsService } from './statsService'
export { apiClient } from './api'

// Export types
export type { Player } from './playerService'
export type { Team } from './teamService'
export type { Match } from './matchService'
export type { Prediction } from './predictionService'
export type { ChatMessage } from './chatbotService'
export type { Stat } from './statsService'
