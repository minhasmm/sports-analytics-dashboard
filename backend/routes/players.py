"""Player endpoints"""
from flask import Blueprint, jsonify, request

players_bp = Blueprint('players', __name__)

@players_bp.route('', methods=['GET'])
def get_players():
    """Get all players"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    
    return jsonify({
        'status': 'success',
        'message': 'Players endpoint',
        'page': page,
        'data': []
    }), 200

@players_bp.route('/<int:player_id>', methods=['GET'])
def get_player(player_id):
    """Get specific player"""
    return jsonify({
        'status': 'success',
        'message': f'Player {player_id}',
        'data': {}
    }), 200

@players_bp.route('/search', methods=['GET'])
def search_players():
    """Search players"""
    query = request.args.get('q', '')
    return jsonify({
        'status': 'success',
        'query': query,
        'data': []
    }), 200
