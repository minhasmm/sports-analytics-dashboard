"""Knowledge Base - Sports Facts and Rules"""

import logging

logger = logging.getLogger(__name__)


class KnowledgeBase:
    """
    Sports domain knowledge base
    Contains facts, rules, and relationships about sports
    """
    
    def __init__(self):
        """Initialize knowledge base"""
        logger.info("✅ Initializing Knowledge Base...")
        
        # Sports facts
        self.facts = {
            'teams': {
                'manchester_united': {
                    'name': 'Manchester United',
                    'league': 'Premier League',
                    'country': 'England',
                    'founded': 1878,
                    'stadium': 'Old Trafford'
                },
                'liverpool': {
                    'name': 'Liverpool FC',
                    'league': 'Premier League',
                    'country': 'England',
                    'founded': 1892,
                    'stadium': 'Anfield'
                },
                'barcelona': {
                    'name': 'FC Barcelona',
                    'league': 'La Liga',
                    'country': 'Spain',
                    'founded': 1899,
                    'stadium': 'Camp Nou'
                }
            },
            'players': {
                'messi': {
                    'name': 'Lionel Messi',
                    'position': 'Forward',
                    'nationality': 'Argentina',
                    'height': '170 cm',
                    'foot': 'Left'
                },
                'ronaldo': {
                    'name': 'Cristiano Ronaldo',
                    'position': 'Forward',
                    'nationality': 'Portugal',
                    'height': '187 cm',
                    'foot': 'Right'
                }
            }
        }
        
        # Statistics rules
        self.rules = {
            'top_scorer': 'Player with most goals scored',
            'assists_leader': 'Player with most assists provided',
            'clean_sheet': 'Match where goalkeeper didn\'t concede',
            'hat_trick': 'Player scoring 3 goals in one match',
            'double_digit': 'Player with 10 or more goals/assists'
        }
        
        # Position info
        self.positions = {
            'GK': 'Goalkeeper',
            'DEF': 'Defender',
            'MID': 'Midfielder',
            'FWD': 'Forward',
            'CB': 'Center Back',
            'LB': 'Left Back',
            'RB': 'Right Back',
            'CM': 'Central Midfielder',
            'LM': 'Left Midfielder',
            'RM': 'Right Midfielder',
            'CAM': 'Central Attacking Midfielder',
            'ST': 'Striker'
        }
        
        # Statistics explanations
        self.stat_explanations = {
            'goals': 'Number of times player scored',
            'assists': 'Number of goals player set up',
            'rating': 'Overall performance rating (0-10)',
            'passes': 'Number of successful passes',
            'tackles': 'Number of defensive challenges won',
            'interceptions': 'Number of passes intercepted',
            'shots': 'Number of shots taken',
            'key_passes': 'Number of passes leading to shot',
            'fouls': 'Number of fouls committed',
            'yellow_cards': 'Number of yellow cards received',
            'red_cards': 'Number of red cards received',
            'clean_sheets': 'Number of matches without conceding'
        }
        
        # Leagues
        self.leagues = {
            'premier_league': {
                'name': 'English Premier League',
                'country': 'England',
                'teams': 20,
                'season_start': 'August',
                'season_end': 'May'
            },
            'la_liga': {
                'name': 'Spanish La Liga',
                'country': 'Spain',
                'teams': 20,
                'season_start': 'August',
                'season_end': 'May'
            },
            'serie_a': {
                'name': 'Italian Serie A',
                'country': 'Italy',
                'teams': 20,
                'season_start': 'August',
                'season_end': 'May'
            },
            'bundesliga': {
                'name': 'German Bundesliga',
                'country': 'Germany',
                'teams': 18,
                'season_start': 'August',
                'season_end': 'May'
            },
            'ligue_1': {
                'name': 'French Ligue 1',
                'country': 'France',
                'teams': 20,
                'season_start': 'August',
                'season_end': 'May'
            }
        }
        
        logger.info("✅ Knowledge Base initialized")
    
    def get_team_info(self, team_name: str) -> dict:
        """Get team information"""
        team_key = team_name.lower().replace(' ', '_')
        return self.facts['teams'].get(team_key, {})
    
    def get_player_info(self, player_name: str) -> dict:
        """Get player information"""
        player_key = player_name.lower().replace(' ', '_')
        return self.facts['players'].get(player_key, {})
    
    def get_position_info(self, position_code: str) -> str:
        """Get position information"""
        return self.positions.get(position_code, 'Unknown Position')
    
    def get_stat_explanation(self, stat_name: str) -> str:
        """Get explanation of a statistic"""
        return self.stat_explanations.get(stat_name, 'Unknown statistic')
    
    def get_league_info(self, league_name: str) -> dict:
        """Get league information"""
        league_key = league_name.lower().replace(' ', '_')
        return self.leagues.get(league_key, {})
    
    def is_valid_position(self, position: str) -> bool:
        """Check if position is valid"""
        return position.upper() in self.positions
    
    def is_valid_league(self, league: str) -> bool:
        """Check if league is valid"""
        return league.lower().replace(' ', '_') in self.leagues
    
    def get_all_positions(self) -> list:
        """Get all valid positions"""
        return list(self.positions.keys())
    
    def get_all_leagues(self) -> list:
        """Get all available leagues"""
        return list(self.leagues.keys())
    
    def get_team_players(self, team_name: str) -> list:
        """Get players in a team (placeholder)"""
        # TODO: Return actual players from database
        return []
    
    def get_league_teams(self, league_name: str) -> list:
        """Get teams in a league (placeholder)"""
        # TODO: Return actual teams from database
        return []
    
    def add_fact(self, category: str, key: str, fact: dict):
        """Add new fact to knowledge base"""
        if category not in self.facts:
            self.facts[category] = {}
        self.facts[category][key] = fact
        logger.info(f"Added fact: {category}/{key}")
    
    def get_context_questions(self, last_intent: str) -> list:
        """Get contextual follow-up questions"""
        
        context_map = {
            'player_stats': [
                'Would you like to compare this player with another?',
                'Do you want to see their career history?',
                'Would you like predictions for their next match?'
            ],
            'team_stats': [
                'Would you like to see upcoming matches?',
                'Do you want head-to-head stats with another team?',
                'Would you like to see individual player stats?'
            ],
            'match_prediction': [
                'Would you like predictions for player performances?',
                'Do you want to see historical head-to-head?',
                'Would you like stat comparisons?'
            ]
        }
        
        return context_map.get(last_intent, [])
