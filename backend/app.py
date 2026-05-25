#!/usr/bin/env python
"""
Sports Analytics Dashboard & Chatbot - Main Flask Application
Author: College Project
Date: 2025
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
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config.from_mapping(
    DEBUG=os.getenv('FLASK_DEBUG', False),
    JSON_SORT_KEYS=False,
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY', 'your-secret-key-change-in-production'),
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=24),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    CACHE_TYPE='simple',
    CACHE_DEFAULT_TIMEOUT=300,
)

# Initialize extensions
CORS(app, resources={
    r"/api/*": {
        "origins": os.getenv('CORS_ORIGINS', 'http://localhost:5173,http://localhost:3000').split(','),
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

jwt = JWTManager(app)
cache = Cache(app)

logger.info("✅ Flask app initialized with extensions")

# ============================================
# IMPORT AND REGISTER BLUEPRINTS (ROUTES)
# ============================================

# Import all route blueprints
try:
    from routes.health import health_bp
    from routes.players import players_bp
    from routes.teams import teams_bp
    from routes.matches import matches_bp
    from routes.stats import stats_bp
    from routes.predictions import predictions_bp
    from routes.chatbot_routes import chatbot_bp
    
    logger.info("✅ All route modules imported successfully")
except ImportError as e:
    logger.error(f"❌ Error importing routes: {e}")
    raise

# Register blueprints with URL prefixes
app.register_blueprint(health_bp, url_prefix='/api/v1/health')
app.register_blueprint(players_bp, url_prefix='/api/v1/players')
app.register_blueprint(teams_bp, url_prefix='/api/v1/teams')
app.register_blueprint(matches_bp, url_prefix='/api/v1/matches')
app.register_blueprint(stats_bp, url_prefix='/api/v1/stats')
app.register_blueprint(predictions_bp, url_prefix='/api/v1/predictions')
app.register_blueprint(chatbot_bp, url_prefix='/api/v1/chatbot')

logger.info("✅ All blueprints registered successfully")

# ============================================
# ERROR HANDLERS
# ============================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 Not Found errors"""
    return jsonify({
        'status': 'error',
        'code': 404,
        'message': 'Resource not found',
        'error': str(error)
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 Internal Server errors"""
    logger.error(f"Internal error: {str(error)}")
    return jsonify({
        'status': 'error',
        'code': 500,
        'message': 'Internal server error',
        'error': str(error)
    }), 500

@app.errorhandler(400)
def bad_request(error):
    """Handle 400 Bad Request errors"""
    return jsonify({
        'status': 'error',
        'code': 400,
        'message': 'Bad request',
        'error': str(error)
    }), 400

@app.errorhandler(403)
def forbidden(error):
    """Handle 403 Forbidden errors"""
    return jsonify({
        'status': 'error',
        'code': 403,
        'message': 'Forbidden',
        'error': str(error)
    }), 403

# ============================================
# ROOT ENDPOINTS
# ============================================

@app.route('/')
def index():
    """Root endpoint - API information"""
    return jsonify({
        'status': 'success',
        'message': '🏆 Sports Analytics Dashboard API v1.0',
        'description': 'Professional sports analytics platform with AI chatbot',
        'version': '1.0.0',
        'endpoints': {
            'health': '/api/v1/health',
            'players': '/api/v1/players',
            'teams': '/api/v1/teams',
            'matches': '/api/v1/matches',
            'stats': '/api/v1/stats',
            'predictions': '/api/v1/predictions',
            'chatbot': '/api/v1/chatbot',
            'docs': '/api/docs'
        }
    })

@app.route('/api')
def api_root():
    """API root endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'Sports Analytics API v1',
        'base_url': '/api/v1',
        'endpoints': [
            '/api/v1/health',
            '/api/v1/players',
            '/api/v1/teams',
            '/api/v1/matches',
            '/api/v1/stats',
            '/api/v1/predictions',
            '/api/v1/chatbot'
        ]
    })

@app.route('/api/v1')
def api_v1():
    """API v1 root endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'Sports Analytics API v1.0',
        'available_endpoints': {
            'health_check': 'GET /api/v1/health',
            'players': {
                'list': 'GET /api/v1/players',
                'search': 'GET /api/v1/players/search?q=query',
                'by_id': 'GET /api/v1/players/<id>',
                'stats': 'GET /api/v1/players/<id>/stats',
                'top_scorers': 'GET /api/v1/players/top-scorers'
            },
            'teams': {
                'list': 'GET /api/v1/teams',
                'by_id': 'GET /api/v1/teams/<id>',
                'stats': 'GET /api/v1/teams/<id>/stats',
                'players': 'GET /api/v1/teams/<id>/players',
                'rankings': 'GET /api/v1/teams/rankings'
            },
            'matches': {
                'list': 'GET /api/v1/matches',
                'by_id': 'GET /api/v1/matches/<id>',
                'upcoming': 'GET /api/v1/matches/upcoming',
                'recent': 'GET /api/v1/matches/recent',
                'head_to_head': 'GET /api/v1/matches/<id>/head-to-head'
            },
            'stats': {
                'top_scorers': 'GET /api/v1/stats/top-scorers',
                'top_assists': 'GET /api/v1/stats/top-assists',
                'standings': 'GET /api/v1/stats/league-standings',
                'efficiency': 'GET /api/v1/stats/efficiency',
                'trends': 'GET /api/v1/stats/trends'
            },
            'predictions': {
                'list': 'GET /api/v1/predictions',
                'by_match': 'GET /api/v1/predictions/<match_id>',
                'league_winner': 'GET /api/v1/predictions/league-winner',
                'accuracy': 'GET /api/v1/predictions/accuracy'
            },
            'chatbot': {
                'query': 'POST /api/v1/chatbot/query',
                'history': 'GET /api/v1/chatbot/history',
                'suggestions': 'GET /api/v1/chatbot/suggestions',
                'clear_history': 'POST /api/v1/chatbot/clear-history',
                'generate_report': 'POST /api/v1/chatbot/report'
            }
        }
    })

@app.route('/api/docs')
def api_docs():
    """API Documentation endpoint"""
    return jsonify({
        'title': 'Sports Analytics Dashboard API',
        'version': '1.0.0',
        'description': 'Complete sports analytics platform with AI chatbot',
        'base_url': 'http://localhost:5000/api/v1',
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'documentation_url': 'https://docs.sportsanalytics.dev',
        'github_repo': 'https://github.com/minhasmm/sports-analytics-dashboard'
    })

# ============================================
# CONTEXT PROCESSORS
# ============================================

@app.context_processor
def inject_config():
    """Inject configuration into context"""
    return {
        'app_name': 'Sports Analytics Dashboard',
        'app_version': '1.0.0'
    }

# ============================================
# BEFORE/AFTER REQUEST HOOKS
# ============================================

@app.before_request
def before_request():
    """Execute before each request"""
    logger.debug(f"Request: {request.method} {request.path}")

@app.after_request
def after_request(response):
    """Execute after each request"""
    response.headers['X-API-Version'] = '1.0.0'
    response.headers['X-App-Name'] = 'Sports Analytics Dashboard'
    return response

# ============================================
# HEALTH CHECK FUNCTION
# ============================================

def check_system_health():
    """Check overall system health"""
    health_status = {
        'app': True,
        'database': False,
        'cache': False,
        'timestamp': None
    }
    
    # TODO: Add database health check
    # TODO: Add cache health check
    
    return health_status

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == '__main__':
    import sys
    
    logger.info("=" * 50)
    logger.info("🏆 SPORTS ANALYTICS DASHBOARD")
    logger.info("=" * 50)
    logger.info(f"Python Version: {sys.version}")
    logger.info(f"Flask Version: {Flask.__version__}")
    logger.info(f"Environment: {os.getenv('ENVIRONMENT', 'development')}")
    logger.info("=" * 50)
    
    # Configuration
    port = int(os.getenv('PORT', 5000))
    host = os.getenv('HOST', '0.0.0.0')
    debug_mode = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    logger.info(f"🚀 Starting Sports Analytics Dashboard")
    logger.info(f"📍 Server: {host}:{port}")
    logger.info(f"🔧 Debug Mode: {debug_mode}")
    logger.info(f"📊 API Base URL: http://{host}:{port}/api/v1")
    logger.info(f"📖 Documentation: http://{host}:{port}/api/docs")
    logger.info("=" * 50)
    
    try:
        app.run(
            host=host,
            port=port,
            debug=debug_mode,
            use_reloader=debug_mode
        )
    except Exception as e:
        logger.error(f"❌ Failed to start application: {e}")
        sys.exit(1)
