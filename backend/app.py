#!/usr/bin/env python
"""
Sports Analytics Dashboard & Chatbot - Main Flask Application
"""

import os
import logging
from datetime import timedelta
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_caching import Cache
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config.from_mapping(
    DEBUG=os.getenv('FLASK_DEBUG', False),
    JSON_SORT_KEYS=False,
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY', 'your-secret-key'),
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=24),
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL', 'sqlite:///sports.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# Initialize extensions
CORS(app)
jwt = JWTManager(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

logger.info("✅ Flask app initialized")

# Root endpoint
@app.route('/')
def index():
    return jsonify({
        'status': 'success',
        'message': '🏆 Sports Analytics Dashboard API v1.0',
        'endpoints': {
            'health': '/api/v1/health',
            'players': '/api/v1/players',
            'teams': '/api/v1/teams',
            'matches': '/api/v1/matches',
            'stats': '/api/v1/stats',
            'chatbot': '/api/v1/chatbot'
        }
    })

# Health check
@app.route('/api/v1/health')
def health():
    return jsonify({
        'status': 'healthy',
        'message': '✅ API is running'
    }), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'status': 'error', 'code': 404, 'message': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'status': 'error', 'code': 500, 'message': 'Server error'}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    logger.info(f"🚀 Starting API on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)
