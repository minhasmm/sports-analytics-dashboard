"""Chatbot API endpoints"""
from flask import Blueprint, jsonify, request

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/query', methods=['POST'])
def chat_query():
    """Process chatbot query"""
    data = request.get_json()
    query = data.get('message', '')
    
    if not query:
        return jsonify({'status': 'error', 'message': 'No message'}), 400
    
    return jsonify({
        'status': 'success',
        'query': query,
        'response': 'Chatbot response',
        'data': []
    }), 200

@chatbot_bp.route('/history', methods=['GET'])
def chat_history():
    """Get chat history"""
    return jsonify({
        'status': 'success',
        'data': []
    }), 200
