"""Natural Language Understanding Engine - NLU Module"""

import logging
from typing import Dict, List, Tuple, Optional
import re
from datetime import datetime

logger = logging.getLogger(__name__)


class NLUEngine:
    """
    Natural Language Understanding Engine for Sports Chatbot
    
    Capabilities:
    - Intent classification (what the user wants)
    - Entity extraction (player names, teams, stats)
    - Question analysis
    - Query preprocessing
    """
    
    def __init__(self):
        """Initialize NLU Engine"""
        logger.info("✅ Initializing NLU Engine...")
        
        # Define intents
        self.intents = {
            'player_stats': ['goals', 'assists', 'performance', 'rating', 'stats'],
            'player_search': ['who', 'find', 'search', 'show me'],
            'player_comparison': ['compare', 'vs', 'versus', 'better', 'difference'],
            'team_stats': ['team', 'league', 'standings', 'ranking'],
            'team_performance': ['performance', 'form', 'recent', 'trend'],
            'match_prediction': ['predict', 'will win', 'outcome', 'forecast'],
            'top_performers': ['top', 'best', 'leading', 'highest', 'golden boot'],
            'trending': ['trending', 'in form', 'hot', 'cold', 'improvement'],
            'historical': ['last', 'previous', 'history', 'record', 'ever'],
            'report': ['report', 'analysis', 'summary', 'export'],
            'general_info': ['how', 'what', 'when', 'where', 'why'],
            'help': ['help', 'support', 'guide', 'tutorial']
        }
        
        # Define entity types
        self.entity_types = {
            'PLAYER': r'\b[A-Z][a-z]+ [A-Z][a-z]+\b',
            'TEAM': r'\b(?:Manchester|Liverpool|Chelsea|Arsenal|PSG|Barcelona|Real Madrid)\b',
            'NUMBER': r'\b\d+\b',
            'STAT': r'\b(?:goals|assists|matches|rating|saves|tackles)\b'
        }
        
        # Common aliases
        self.aliases = {
            'messi': 'Lionel Messi',
            'ronaldo': 'Cristiano Ronaldo',
            'neymar': 'Neymar Jr',
            'man utd': 'Manchester United',
            'man city': 'Manchester City',
            'liverpool': 'Liverpool FC'
        }
        
        logger.info("✅ NLU Engine initialized successfully")
    
    def process_query(self, query: str) -> Dict:
        """
        Main processing function - analyze user query
        
        Args:
            query: User's natural language query
            
        Returns:
            Dict with processed query information
        """
        logger.info(f"Processing query: {query}")
        
        # Preprocess query
        cleaned_query = self.preprocess_text(query)
        
        # Classify intent
        intent, confidence = self.classify_intent(cleaned_query)
        
        # Extract entities
        entities = self.extract_entities(cleaned_query)
        
        # Extract keywords
        keywords = self.extract_keywords(cleaned_query)
        
        # Generate response instruction
        response_instruction = self.generate_instruction(intent, entities, keywords)
        
        result = {
            'original_query': query,
            'cleaned_query': cleaned_query,
            'intent': intent,
            'confidence': confidence,
            'entities': entities,
            'keywords': keywords,
            'instruction': response_instruction
        }
        
        logger.debug(f"Processing result: {result}")
        
        return result
    
    def preprocess_text(self, text: str) -> str:
        """Preprocess text - clean and normalize"""
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove extra spaces
        text = ' '.join(text.split())
        
        # Remove punctuation
        text = re.sub(r'[!?.,;:]', '', text)
        
        # Expand common contractions
        text = text.replace("don't", "do not")
        text = text.replace("won't", "will not")
        text = text.replace("can't", "can not")
        
        # Replace aliases
        for alias, full_name in self.aliases.items():
            pattern = r'\b' + alias + r'\b'
            text = re.sub(pattern, full_name.lower(), text)
        
        return text
    
    def classify_intent(self, query: str) -> Tuple[str, float]:
        """
        Classify user intent
        
        Returns:
            Tuple of (intent_name, confidence_score)
        """
        
        intent_scores = {}
        
        # Score each intent
        for intent_name, keywords in self.intents.items():
            score = sum(1 for keyword in keywords if keyword in query)
            intent_scores[intent_name] = score
        
        # Find best intent
        if not intent_scores or max(intent_scores.values()) == 0:
            return 'general_info', 0.5
        
        best_intent = max(intent_scores, key=intent_scores.get)
        confidence = min(1.0, intent_scores[best_intent] / len(self.intents[best_intent]))
        
        logger.debug(f"Classified intent: {best_intent} (confidence: {confidence})")
        
        return best_intent, confidence
    
    def extract_entities(self, query: str) -> Dict[str, List[str]]:
        """
        Extract named entities from query
        
        Returns:
            Dict of entity types and their occurrences
        """
        
        entities = {}
        
        for entity_type, pattern in self.entity_types.items():
            matches = re.findall(pattern, query, re.IGNORECASE)
            if matches:
                entities[entity_type] = list(set(matches))
        
        logger.debug(f"Extracted entities: {entities}")
        
        return entities
    
    def extract_keywords(self, query: str) -> List[str]:
        """Extract important keywords from query"""
        
        # Remove stop words
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'is', 'are', 'was', 'were',
            'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did',
            'will', 'would', 'should', 'could', 'may', 'might', 'can', 'must',
            'in', 'on', 'at', 'to', 'for', 'of', 'by', 'with', 'from'
        }
        
        words = query.split()
        keywords = [word for word in words if word not in stop_words and len(word) > 2]
        
        logger.debug(f"Extracted keywords: {keywords}")
        
        return keywords
    
    def generate_instruction(self, intent: str, entities: Dict, keywords: List[str]) -> Dict:
        """Generate instruction for response generation"""
        
        instruction = {
            'intent': intent,
            'action': self.map_intent_to_action(intent),
            'parameters': self.extract_parameters(intent, entities, keywords),
            'filters': self.extract_filters(intent, entities, keywords)
        }
        
        return instruction
    
    def map_intent_to_action(self, intent: str) -> str:
        """Map intent to database/service action"""
        
        intent_action_map = {
            'player_stats': 'get_player_stats',
            'player_search': 'search_players',
            'player_comparison': 'compare_players',
            'team_stats': 'get_team_stats',
            'team_performance': 'get_team_performance',
            'match_prediction': 'predict_match',
            'top_performers': 'get_top_performers',
            'trending': 'get_trending_players',
            'historical': 'get_historical_data',
            'report': 'generate_report',
            'general_info': 'provide_info',
            'help': 'show_help'
        }
        
        return intent_action_map.get(intent, 'general_query')
    
    def extract_parameters(self, intent: str, entities: Dict, keywords: List[str]) -> Dict:
        """Extract action parameters"""
        
        parameters = {}
        
        # Extract player names
        if 'PLAYER' in entities:
            parameters['player_names'] = entities['PLAYER']
        
        # Extract team names
        if 'TEAM' in entities:
            parameters['teams'] = entities['TEAM']
        
        # Extract numbers (for limit, rank, etc.)
        if 'NUMBER' in entities:
            parameters['numbers'] = [int(n) for n in entities['NUMBER']]
        
        # Extract statistics
        if 'STAT' in entities:
            parameters['statistics'] = entities['STAT']
        
        # Limit
        if 'top' in keywords or 'best' in keywords:
            numbers = parameters.get('numbers', [5])
            parameters['limit'] = numbers[0] if numbers else 5
        
        return parameters
    
    def extract_filters(self, intent: str, entities: Dict, keywords: List[str]) -> Dict:
        """Extract filtering options"""
        
        filters = {}
        
        # Time filters
        if 'recent' in keywords or 'last' in keywords:
            filters['time_period'] = 'recent'
        elif 'historical' in keywords or 'all time' in keywords:
            filters['time_period'] = 'all_time'
        elif 'season' in keywords:
            filters['time_period'] = 'season'
        
        # League filters
        if 'premier league' in ' '.join(keywords):
            filters['league'] = 'Premier League'
        elif 'la liga' in ' '.join(keywords):
            filters['league'] = 'La Liga'
        elif 'serie a' in ' '.join(keywords):
            filters['league'] = 'Serie A'
        
        return filters
    
    def validate_query(self, query: str) -> Tuple[bool, Optional[str]]:
        """Validate if query is valid and answerable"""
        
        # Check if query is empty
        if not query or len(query.strip()) == 0:
            return False, "Please provide a question"
        
        # Check if query is too short
        if len(query.split()) < 2:
            return False, "Question too short. Please provide more details"
        
        # Check if query is too long
        if len(query) > 500:
            return False, "Question too long. Please keep it under 500 characters"
        
        return True, None
    
    def get_suggestions(self) -> List[str]:
        """Get example questions users can ask"""
        
        suggestions = [
            "Who is the top scorer in the Premier League?",
            "Compare Messi and Ronaldo's performance",
            "Show me Manchester City's recent form",
            "Predict the outcome of the next match",
            "Which players are in good form this week?",
            "What's the league standing?",
            "Generate a performance report for 2024",
            "Show me the best defenders",
            "How many goals did Messi score this season?",
            "Which teams have improved the most?"
        ]
        
        return suggestions
    
    def parse_time_reference(self, query: str) -> Optional[str]:
        """Extract time reference from query"""
        
        time_patterns = {
            'this week': 'week',
            'this month': 'month',
            'this season': 'season',
            'this year': 'year',
            'last week': 'last_week',
            'last month': 'last_month',
            'last season': 'last_season',
            'all time': 'all_time'
        }
        
        for pattern, time_ref in time_patterns.items():
            if pattern in query:
                return time_ref
        
        return None
    
    def parse_comparison_query(self, query: str) -> Optional[Tuple[str, str]]:
        """Parse comparison queries like 'A vs B'"""
        
        if ' vs ' in query or ' versus ' in query:
            separator = ' vs ' if ' vs ' in query else ' versus '
            parts = query.split(separator)
            if len(parts) == 2:
                return (parts[0].strip(), parts[1].strip())
        
        return None
    
    def extract_quantity(self, query: str) -> int:
        """Extract quantity request (top 5, top 10, etc.)"""
        
        # Look for patterns like "top 5", "top five", etc.
        patterns = [
            r'top\s+(\d+)',
            r'best\s+(\d+)',
            r'show\s+(\d+)',
            r'give\s+me\s+(\d+)',
            r'(\d+)\s+(?:top|best|leading)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, query, re.IGNORECASE)
            if match:
                return int(match.group(1))
        
        return 10  # Default
    
    def score_query_relevance(self, query: str, context: Optional[Dict] = None) -> float:
        """Score how relevant a query is to sports analytics"""
        
        score = 0.0
        
        # Check for sports keywords
        sports_keywords = ['player', 'team', 'match', 'goal', 'score', 'league', 'season', 'game']
        sports_count = sum(1 for keyword in sports_keywords if keyword in query)
        score += (sports_count / len(sports_keywords)) * 0.7
        
        # Check for action words
        action_keywords = ['show', 'tell', 'predict', 'compare', 'analyze', 'report']
        action_count = sum(1 for keyword in action_keywords if keyword in query)
        score += (action_count / len(action_keywords)) * 0.3
        
        return min(1.0, score)
    
    def get_followup_question(self, last_intent: str) -> str:
        """Generate followup question based on last intent"""
        
        followup_map = {
            'player_stats': 'Would you like to compare this player with someone else?',
            'team_stats': 'Would you like to see upcoming matches for this team?',
            'match_prediction': 'Would you like to see player predictions for this match?',
            'top_performers': 'Would you like detailed stats for any of these players?',
            'general_info': 'What specific information would you like?'
        }
        
        return followup_map.get(last_intent, 'Is there anything else you would like to know?')
