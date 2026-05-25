"""Statistics endpoints"""
from flask import Blueprint, jsonify, request

stats_bp = Blueprint('stats', __name__)

@stats_bp.route('/top-scorers', methods=['GET'])
def top_scorers():
    """Get top scorers"""
    limit = request.args.get('limit', 10, type=int)
    return jsonify({
        'status': 'success',
        'message': 'Top scorers',
        'data': []
    }), 200

@stats_bp.route('/league-standings', methods=['GET'])
def league_standings():
    """Get league standings"""
    league = request.args.get('league')
    return jsonify({
        'status': 'success',
        'data': []
    }), 200
