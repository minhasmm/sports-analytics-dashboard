"""Match endpoints"""
from flask import Blueprint, jsonify, request

matches_bp = Blueprint('matches', __name__)

@matches_bp.route('', methods=['GET'])
def get_matches():
    """Get matches"""
    team = request.args.get('team')
    status = request.args.get('status', 'all')
    
    return jsonify({
        'status': 'success',
        'filters': {'team': team, 'status': status},
        'data': []
    }), 200

@matches_bp.route('/<int:match_id>', methods=['GET'])
def get_match(match_id):
    """Get specific match"""
    return jsonify({
        'status': 'success',
        'data': {}
    }), 200
