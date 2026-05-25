"""Chatbot Service - Main chatbot orchestration"""

import logging
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import uuid

from .nlu import NLUEngine
from .responses import ResponseGenerator
from .knowledge_base import KnowledgeBase

logger = logging.getLogger(__name__)


class ChatbotService:
    """
    Main Chatbot Service
    Orchestrates NLU, Response Generation, and Knowledge Base
    """
    
    def __init__(self):
        """Initialize Chatbot Service"""
        logger.info("🚀 Initializing Chatbot Service...")
        
        # Initialize components
        self.nlu_engine = NLUEngine()
        self.response_generator = ResponseGenerator()
        self.knowledge_base = KnowledgeBase()
        
        # Conversation history
        self.conversation_history = {}
        
        logger.info("✅ Chatbot Service ready!")
    
    def process_message(
        self,
        user_message: str,
        user_id: Optional[str] = None,
        context: Optional[Dict] = None
    ) -> Dict:
        """
        Process user message and generate response
        
        Args:
            user_message: User's question/statement
            user_id: ID of the user (for history)
            context: Previous conversation context
            
        Returns:
            Dict with response and metadata
        """
        
        try:
            # Validate input
            is_valid, error = self.nlu_engine.validate_query(user_message)
            if not is_valid:
                return self._create_error_response(error or "Invalid query", user_id)
            
            # Generate session ID if needed
            if user_id is None:
                user_id = str(uuid.uuid4())
            
            logger.info(f"Processing message from user {user_id}: {user_message}")
            
            # Step 1: NLU Processing
            nlu_result = self.nlu_engine.process_query(user_message)
            logger.debug(f"NLU Result: {nlu_result}")
            
            # Step 2: Query Context
            intent = nlu_result['intent']
            confidence = nlu_result['confidence']
            entities = nlu_result['entities']
            
            # Check if we can answer
            if confidence < 0.3:
                return self._create_clarification_response(user_message, user_id)
            
            # Step 3: Fetch Data (from database/services)
            data = self._fetch_data_for_intent(intent, nlu_result)
            
            # Step 4: Generate Response
            response_text = self.response_generator.generate_response(intent, data)
            
            # Add confidence indicator
            if confidence < 0.7:
                response_text = self.response_generator.add_confidence_indicator(
                    response_text, confidence
                )
            
            # Step 5: Store in history
            self._store_message(user_id, user_message, response_text, intent, confidence)
            
            # Step 6: Create response object
            response = {
                'status': 'success',
                'message': response_text,
                'user_id': user_id,
                'intent': intent,
                'confidence': confidence,
                'entities': entities,
                'timestamp': datetime.now().isoformat(),
                'follow_up_question': self.knowledge_base.get_context_questions(intent)[0] 
                    if self.knowledge_base.get_context_questions(intent) else None,
                'suggestions': [] if confidence > 0.7 else self.nlu_engine.get_suggestions()[:3]
            }
            
            logger.info(f"Response generated successfully for user {user_id}")
            
            return response
            
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}", exc_info=True)
            return self._create_error_response(f"Error: {str(e)}", user_id)
    
    def _fetch_data_for_intent(self, intent: str, nlu_result: Dict) -> Dict:
        """Fetch data from database based on intent"""
        
        logger.info(f"Fetching data for intent: {intent}")
        
        data = {}
        parameters = nlu_result['instruction']['parameters']
        
        try:
            if intent == 'player_stats' and 'player_names' in parameters:
                # TODO: Fetch from player service
                data['player'] = {'name': parameters['player_names'][0]}
                data['stats'] = {}
            
            elif intent == 'top_performers':
                # TODO: Fetch from stats service
                limit = parameters.get('limit', 10)
                data['players'] = []
            
            elif intent == 'team_stats' and 'teams' in parameters:
                # TODO: Fetch from team service
                data['team'] = {'name': parameters['teams'][0]}
                data['stats'] = {}
            
            elif intent == 'match_prediction':
                # TODO: Fetch from prediction service
                data['prediction'] = {}
            
            elif intent == 'player_comparison' and 'player_names' in parameters:
                # TODO: Fetch comparison data
                data['players'] = []
            
        except Exception as e:
            logger.error(f"Error fetching data: {str(e)}")
            data['error'] = str(e)
        
        return data
    
    def _store_message(
        self,
        user_id: str,
        user_message: str,
        response_text: str,
        intent: str,
        confidence: float
    ):
        """Store message in conversation history"""
        
        if user_id not in self.conversation_history:
            self.conversation_history[user_id] = []
        
        message_record = {
            'timestamp': datetime.now().isoformat(),
            'user_message': user_message,
            'bot_response': response_text,
            'intent': intent,
            'confidence': confidence
        }
        
        self.conversation_history[user_id].append(message_record)
        
        # Keep only last 50 messages per user
        if len(self.conversation_history[user_id]) > 50:
            self.conversation_history[user_id] = self.conversation_history[user_id][-50:]
    
    def get_conversation_history(self, user_id: str, limit: int = 20) -> List[Dict]:
        """Get conversation history for user"""
        
        logger.info(f"Retrieving history for user {user_id}")
        
        if user_id not in self.conversation_history:
            return []
        
        return self.conversation_history[user_id][-limit:]
    
    def clear_conversation_history(self, user_id: str) -> bool:
        """Clear conversation history for user"""
        
        logger.info(f"Clearing history for user {user_id}")
        
        if user_id in self.conversation_history:
            del self.conversation_history[user_id]
            return True
        
        return False
    
    def get_suggestions(self) -> List[str]:
        """Get example questions"""
        return self.nlu_engine.get_suggestions()
    
    def _create_error_response(self, error_message: str, user_id: Optional[str] = None) -> Dict:
        """Create error response"""
        
        return {
            'status': 'error',
            'message': self.response_generator.generate_error_response('server_error', error_message),
            'user_id': user_id,
            'timestamp': datetime.now().isoformat(),
            'suggestions': self.get_suggestions()[:3]
        }
    
    def _create_clarification_response(self, user_message: str, user_id: str) -> Dict:
        """Create clarification request response"""
        
        return {
            'status': 'clarification_needed',
            'message': "I'm not sure I understood correctly. Could you rephrase your question?",
            'user_id': user_id,
            'timestamp': datetime.now().isoformat(),
            'suggestions': self.get_suggestions()[:3]
        }
    
    def get_chatbot_stats(self) -> Dict:
        """Get chatbot usage statistics"""
        
        stats = {
            'total_conversations': len(self.conversation_history),
            'total_messages': sum(
                len(messages) for messages in self.conversation_history.values()
            ),
            'unique_users': len(self.conversation_history),
            'average_messages_per_user': 0,
            'timestamp': datetime.now().isoformat()
        }
        
        if stats['unique_users'] > 0:
            stats['average_messages_per_user'] = stats['total_messages'] / stats['unique_users']
        
        return stats
    
    def health_check(self) -> Dict:
        """Check chatbot health"""
        
        return {
            'status': 'healthy',
            'components': {
                'nlu_engine': 'operational',
                'response_generator': 'operational',
                'knowledge_base': 'operational',
                'conversation_history': f"{len(self.conversation_history)} users"
            },
            'timestamp': datetime.now().isoformat()
        }
    
    def generate_report(self, user_id: str) -> Dict:
        """Generate analytics report from conversation"""
        
        logger.info(f"Generating report for user {user_id}")
        
        history = self.get_conversation_history(user_id, limit=100)
        
        if not history:
            return {'error': 'No conversation history found'}
        
        # Analyze conversation
        intents_count = {}
        for msg in history:
            intent = msg.get('intent', 'unknown')
            intents_count[intent] = intents_count.get(intent, 0) + 1
        
        report = {
            'user_id': user_id,
            'generated_at': datetime.now().isoformat(),
            'total_messages': len(history),
            'intents_used': intents_count,
            'most_common_intent': max(intents_count, key=intents_count.get) if intents_count else None,
            'conversation_summary': f"User asked {len(history)} questions with focus on {list(intents_count.keys())}"
        }
        
        return report
    
    def batch_process_messages(
        self,
        messages: List[str],
        user_id: str
    ) -> List[Dict]:
        """Process multiple messages (useful for batch testing)"""
        
        logger.info(f"Processing batch of {len(messages)} messages")
        
        responses = []
        for message in messages:
            response = self.process_message(message, user_id)
            responses.append(response)
        
        return responses
