"""Prediction endpoints"""
from flask import Blueprint, jsonify, request

predictions_bp = Blueprint('predictions', __name__)

@predictions_bp.route('', methods=['GET'])
def get_predictions():
    """Get match predictions"""
    limit = request.args.get('limit', 10, type=int)
    return jsonify({
        'status': 'success',
        'data': []
    }), 200

@predictions_bp.route('/<int:match_id>', methods=['GET'])
def predict_match(match_id):
    """Predict specific match"""
    return jsonify({
        'status': 'success',
        'data': {}
    }), 200
