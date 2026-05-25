"""Team endpoints"""
from flask import Blueprint, jsonify, request

teams_bp = Blueprint('teams', __name__)

@teams_bp.route('', methods=['GET'])
def get_teams():
    """Get all teams"""
    league = request.args.get('league')
    return jsonify({
        'status': 'success',
        'league': league,
        'data': []
    }), 200

@teams_bp.route('/<int:team_id>', methods=['GET'])
def get_team(team_id):
    """Get specific team"""
    return jsonify({
        'status': 'success',
        'data': {}
    }), 200

@teams_bp.route('/<int:team_id>/stats', methods=['GET'])
def get_team_stats(team_id):
    """Get team statistics"""
    return jsonify({
        'status': 'success',
        'data': {}
    }), 200
