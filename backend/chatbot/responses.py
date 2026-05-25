"""Response Generation Module - Generates natural language responses"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class ResponseGenerator:
    """
    Generates natural language responses for chatbot
    
    Converts data into readable, conversational text
    """
    
    def __init__(self):
        """Initialize response generator"""
        logger.info("✅ Initializing Response Generator...")
        
        # Response templates
        self.templates = {
            'player_stats': [
                "{player_name} has scored {goals} goals and {assists} assists this season.",
                "{player_name}'s performance: {goals} goals, {assists} assists. Rating: {rating}/10",
                "Stats for {player_name}: {goals}G, {assists}A in {matches} matches. Avg rating: {rating}"
            ],
            'top_scorers': [
                "Top scorers this season: {players}",
                "Leading goal scorers: {list_players}",
                "Here are the top {count} scorers: {list_players}"
            ],
            'team_stats': [
                "{team_name} has {wins} wins, {draws} draws, and {losses} losses.",
                "{team_name}'s record: W-D-L {wins}-{draws}-{losses}, Points: {points}",
                "{team_name} is currently ranked #{position} with {points} points"
            ],
            'comparison': [
                "Comparing {player1} and {player2}: {comparison_text}",
                "{player1} has {p1_goals} goals vs {player2}'s {p2_goals} goals",
                "Difference: {player1} leads by {difference} goals"
            ],
            'prediction': [
                "My prediction: {home_team} will win with {confidence}% confidence",
                "{home_team} vs {away_team}: I predict {predicted_winner} will win ({confidence}% confidence)",
                "Predicted score: {predicted_score}. Confidence: {confidence}%"
            ],
            'help': [
                "I can help you with:\n- Player statistics\n- Team performance\n- Match predictions\n- Top scorers\n- Comparisons",
                "You can ask me about:\n📊 Player stats\n🏆 Team rankings\n🎯 Match predictions\n📈 Trending players\n🔄 Comparisons"
            ]
        }
        
        logger.info("✅ Response Generator initialized")
    
    def generate_response(self, intent: str, data: Dict[str, Any]) -> str:
        """
        Generate response based on intent and data
        
        Args:
            intent: User's classified intent
            data: Data from database/services
            
        Returns:
            Natural language response
        """
        
        logger.info(f"Generating response for intent: {intent}")
        
        # Generate based on intent
        if intent == 'player_stats':
            return self.generate_player_stats_response(data)
        
        elif intent == 'top_performers':
            return self.generate_top_performers_response(data)
        
        elif intent == 'team_stats':
            return self.generate_team_stats_response(data)
        
        elif intent == 'player_comparison':
            return self.generate_comparison_response(data)
        
        elif intent == 'match_prediction':
            return self.generate_prediction_response(data)
        
        elif intent == 'team_performance':
            return self.generate_team_performance_response(data)
        
        elif intent == 'trending':
            return self.generate_trending_response(data)
        
        elif intent == 'report':
            return self.generate_report_response(data)
        
        elif intent == 'help':
            return self.generate_help_response()
        
        else:
            return self.generate_general_response(data)
    
    def generate_player_stats_response(self, data: Dict) -> str:
        """Generate response for player statistics"""
        
        if not data or 'player' not in data:
            return "I couldn't find player information. Could you provide more details?"
        
        player = data['player']
        stats = data.get('stats', {})
        
        response = f"📊 **{player.get('name', 'Unknown')}**\n\n"
        response += f"Position: {player.get('position', 'N/A')}\n"
        response += f"Team: {player.get('team', 'N/A')}\n\n"
        response += f"⚽ Goals: {stats.get('goals', 0)}\n"
        response += f"🎯 Assists: {stats.get('assists', 0)}\n"
        response += f"📈 Matches Played: {stats.get('appearances', 0)}\n"
        response += f"⭐ Average Rating: {stats.get('rating', 0)}/10\n"
        response += f"🤝 Pass Success: {stats.get('pass_success_rate', 0)}%"
        
        return response
    
    def generate_top_performers_response(self, data: Dict) -> str:
        """Generate response for top performers"""
        
        if not data or 'players' not in data:
            return "I couldn't retrieve the top performers. Please try again."
        
        players = data.get('players', [])[:10]
        
        response = "🏆 **Top Performers**\n\n"
        
        for idx, player in enumerate(players, 1):
            name = player.get('name', 'Unknown')
            goals = player.get('goals', 0)
            response += f"{idx}. {name} - {goals} goals\n"
        
        return response
    
    def generate_team_stats_response(self, data: Dict) -> str:
        """Generate response for team statistics"""
        
        if not data or 'team' not in data:
            return "I couldn't find team information. Could you specify which team?"
        
        team = data['team']
        stats = data.get('stats', {})
        
        response = f"🏆 **{team.get('name', 'Unknown')}**\n\n"
        response += f"League: {team.get('league', 'N/A')}\n"
        response += f"Rank: #{stats.get('position', 'N/A')}\n\n"
        response += f"📊 Record:\n"
        response += f"  Wins: {stats.get('wins', 0)}\n"
        response += f"  Draws: {stats.get('draws', 0)}\n"
        response += f"  Losses: {stats.get('losses', 0)}\n\n"
        response += f"⚽ Goals For: {stats.get('goals_for', 0)}\n"
        response += f"🛡️ Goals Against: {stats.get('goals_against', 0)}\n"
        response += f"📈 Points: {stats.get('points', 0)}"
        
        return response
    
    def generate_comparison_response(self, data: Dict) -> str:
        """Generate response for player comparison"""
        
        if not data or 'players' not in data or len(data['players']) < 2:
            return "I need at least two players to compare. Please specify."
        
        players = data['players'][:2]
        p1, p2 = players[0], players[1]
        
        response = f"🔄 **Comparison: {p1.get('name')} vs {p2.get('name')}**\n\n"
        response += f"{'Stat':<20} | {p1.get('name'):<15} | {p2.get('name'):<15}\n"
        response += "-" * 55 + "\n"
        response += f"{'Goals':<20} | {p1.get('goals', 0):<15} | {p2.get('goals', 0):<15}\n"
        response += f"{'Assists':<20} | {p1.get('assists', 0):<15} | {p2.get('assists', 0):<15}\n"
        response += f"{'Rating':<20} | {p1.get('rating', 0):<15} | {p2.get('rating', 0):<15}\n"
        response += f"{'Matches':<20} | {p1.get('appearances', 0):<15} | {p2.get('appearances', 0):<15}"
        
        return response
    
    def generate_prediction_response(self, data: Dict) -> str:
        """Generate response for match predictions"""
        
        if not data or 'prediction' not in data:
            return "I couldn't generate a prediction. Please try again."
        
        pred = data['prediction']
        
        response = f"🎯 **Match Prediction**\n\n"
        response += f"Match: {pred.get('home_team', 'N/A')} vs {pred.get('away_team', 'N/A')}\n\n"
        response += f"🔮 Prediction: {pred.get('predicted_winner', 'N/A')} will win\n"
        response += f"📊 Confidence: {pred.get('confidence', 0)}%\n\n"
        
        prob = pred.get('probability', {})
        response += f"📈 Probabilities:\n"
        response += f"  Home Win: {prob.get('home_win', 0)*100:.1f}%\n"
        response += f"  Draw: {prob.get('draw', 0)*100:.1f}%\n"
        response += f"  Away Win: {prob.get('away_win', 0)*100:.1f}%"
        
        return response
    
    def generate_team_performance_response(self, data: Dict) -> str:
        """Generate response for team performance"""
        
        if not data:
            return "I couldn't retrieve team performance data."
        
        team = data.get('team', {})
        performance = data.get('performance', {})
        
        response = f"📈 **{team.get('name', 'Unknown')} Performance**\n\n"
        response += f"Recent Form: {performance.get('trend', 'Stable')}\n"
        response += f"Recent Results:\n"
        
        recent = performance.get('recent_matches', [])[:5]
        for match in recent:
            response += f"  {match.get('opponent', 'N/A')}: {match.get('result', 'N/A')}\n"
        
        return response
    
    def generate_trending_response(self, data: Dict) -> str:
        """Generate response for trending players"""
        
        if not data or 'players' not in data:
            return "I couldn't find trending players."
        
        players = data['players'][:5]
        
        response = "🔥 **Trending Players (In Form)**\n\n"
        
        for idx, player in enumerate(players, 1):
            name = player.get('name', 'Unknown')
            trend = player.get('trend', 'Improving')
            response += f"{idx}. {name} - {trend} ⬆️\n"
        
        return response
    
    def generate_report_response(self, data: Dict) -> str:
        """Generate response for analytics report"""
        
        if not data:
            return "I couldn't generate a report."
        
        report = data.get('report', {})
        
        response = "📋 **Analytics Report**\n\n"
        response += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        response += f"Report Type: {report.get('type', 'General')}\n"
        response += f"Period: {report.get('period', 'Unknown')}\n\n"
        response += f"Key Metrics:\n"
        
        metrics = report.get('metrics', {})
        for key, value in metrics.items():
            response += f"  {key}: {value}\n"
        
        return response
    
    def generate_help_response(self) -> str:
        """Generate help response"""
        
        response = "🤖 **Sports Analytics Chatbot - Help**\n\n"
        response += "I can help you with:\n\n"
        response += "📊 **Player Statistics**\n"
        response += "  'Show Messi's stats' or 'Goals scored by Ronaldo'\n\n"
        response += "🏆 **Team Rankings**\n"
        response += "  'League standings' or 'How is Manchester City performing?'\n\n"
        response += "🎯 **Match Predictions**\n"
        response += "  'Predict the next match' or 'Will Arsenal win?'\n\n"
        response += "🔄 **Comparisons**\n"
        response += "  'Compare Messi vs Ronaldo' or 'Manchester United vs Liverpool'\n\n"
        response += "🔥 **Trending**\n"
        response += "  'Who's in good form?' or 'Top scorers this season'\n\n"
        response += "📋 **Reports**\n"
        response += "  'Generate a performance report' or 'Analytics for 2024'\n\n"
        response += "Just ask me anything about sports! ⚽"
        
        return response
    
    def generate_general_response(self, data: Dict) -> str:
        """Generate general response for unclassified queries"""
        
        return "I understand you're asking about sports analytics. Could you be more specific? For example:\n\n" \
               "- 'Show me player stats for [player name]'\n" \
               "- 'What's the current league standing?'\n" \
               "- 'Predict the outcome of [match]'\n" \
               "- 'Compare [player 1] and [player 2]'\n\n" \
               "Type 'help' to see all available commands."
    
    def format_list(self, items: List[str], max_items: int = 5) -> str:
        """Format list of items nicely"""
        
        items = items[:max_items]
        
        if len(items) == 0:
            return "No items"
        elif len(items) == 1:
            return items[0]
        elif len(items) == 2:
            return f"{items[0]} and {items[1]}"
        else:
            return ", ".join(items[:-1]) + f", and {items[-1]}"
    
    def add_emoji_to_response(self, response: str, intent: str) -> str:
        """Add relevant emojis to response based on intent"""
        
        emoji_map = {
            'player_stats': '⚽',
            'team_stats': '🏆',
            'match_prediction': '🎯',
            'top_performers': '🔥',
            'help': '❓'
        }
        
        emoji = emoji_map.get(intent, '💬')
        
        if not response.startswith(emoji):
            response = f"{emoji} {response}"
        
        return response
    
    def add_confidence_indicator(self, response: str, confidence: float) -> str:
        """Add confidence indicator to response"""
        
        if confidence >= 0.9:
            indicator = "✅ (Very confident)"
        elif confidence >= 0.7:
            indicator = "👍 (Confident)"
        elif confidence >= 0.5:
            indicator = "🤔 (Moderate confidence)"
        else:
            indicator = "❓ (Low confidence)"
        
        return f"{response}\n\n{indicator}"
    
    def generate_error_response(self, error_type: str, details: Optional[str] = None) -> str:
        """Generate error response"""
        
        error_responses = {
            'no_data': "I couldn't find data for your query. Could you provide more details?",
            'invalid_player': "I couldn't find this player. Did you spell it correctly?",
            'invalid_team': "I couldn't find this team. Please check the name.",
            'invalid_date': "I couldn't understand the date format. Try YYYY-MM-DD.",
            'timeout': "The request took too long. Please try again.",
            'server_error': "Something went wrong. Please try again later.",
            'invalid_query': "I didn't understand your question. Please rephrase it."
        }
        
        base_response = error_responses.get(error_type, "An error occurred. Please try again.")
        
        if details:
            return f"{base_response}\n\nDetails: {details}"
        
        return base_response
