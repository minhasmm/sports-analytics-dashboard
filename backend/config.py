"""Configuration module for Sports Analytics Dashboard"""

import os
from datetime import timedelta

class Config:
    """Base configuration - common settings for all environments"""
    
    # Flask
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
    JSON_SORT_KEYS = False
    
    # JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-change-in-production')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
    
    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    
    # Cache
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300
    CACHE_KEY_PREFIX = 'sports_analytics_'
    
    # API
    API_TITLE = 'Sports Analytics Dashboard API'
    API_VERSION = 'v1.0'
    OPENAPI_VERSION = '3.0.2'
    
    # CORS
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:5173,http://localhost:3000').split(',')
    CORS_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
    CORS_ALLOW_HEADERS = ['Content-Type', 'Authorization']
    
    # Logging
    LOG_LEVEL = 'INFO'
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # Pagination
    ITEMS_PER_PAGE = 20
    MAX_ITEMS_PER_PAGE = 100
    
    # Limits
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file upload
    JSON_MAX_SIZE = 1024 * 1024  # 1MB max JSON payload


class DevelopmentConfig(Config):
    """Development environment configuration"""
    
    DEBUG = True
    TESTING = False
    SQLALCHEMY_ECHO = True
    
    # Database - SQLite for development
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'sqlite:///sports_analytics.db'
    )
    
    # Cache - Simple in-memory cache
    CACHE_TYPE = 'simple'
    
    # Redis (optional for development)
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    
    # Features
    ENABLE_PROFILER = True
    PRESERVE_CONTEXT_ON_EXCEPTION = True


class ProductionConfig(Config):
    """Production environment configuration"""
    
    DEBUG = False
    TESTING = False
    
    # Database - PostgreSQL for production
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("DATABASE_URL environment variable is not set")
    
    # Cache - Redis for production
    CACHE_TYPE = 'redis'
    CACHE_REDIS_URL = os.getenv('REDIS_URL')
    if not CACHE_REDIS_URL:
        raise ValueError("REDIS_URL environment variable is not set")
    
    # Security
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # JWT
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    
    # Features
    ENABLE_PROFILER = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class TestingConfig(Config):
    """Testing environment configuration"""
    
    DEBUG = True
    TESTING = True
    
    # Database - In-memory SQLite for testing
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    
    # Cache - Simple in-memory cache
    CACHE_TYPE = 'simple'
    
    # JWT - Shorter expiration for testing
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=5)
    
    # Features
    ENABLE_PROFILER = False
    PRESERVE_CONTEXT_ON_EXCEPTION = True


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config():
    """Get configuration based on environment"""
    env = os.getenv('FLASK_ENV', 'development').lower()
    return config.get(env, config['default'])
