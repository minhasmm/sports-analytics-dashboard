"""Database initialization script"""

import os
import sys
import logging

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import init_db, check_db_connection, engine
from models.base import Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Initialize database"""
    
    logger.info("=" * 50)
    logger.info("🏆 Sports Analytics Database Initialization")
    logger.info("=" * 50)
    
    # Check connection
    logger.info("\n1️⃣ Checking database connection...")
    if not check_db_connection():
        logger.error("Failed to connect to database")
        sys.exit(1)
    
    # Create tables
    logger.info("\n2️⃣ Creating database tables...")
    try:
        init_db()
        logger.info("✅ Tables created successfully")
    except Exception as e:
        logger.error(f"❌ Error creating tables: {e}")
        sys.exit(1)
    
    # Verify tables
    logger.info("\n3️⃣ Verifying tables...")
    try:
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        
        expected_tables = ['players', 'teams', 'matches', 'player_stats', 'team_stats', 'users']
        
        logger.info(f"Found {len(tables)} tables:")
        for table in tables:
            logger.info(f"  ✓ {table}")
        
        missing_tables = set(expected_tables) - set(tables)
        if missing_tables:
            logger.warning(f"⚠️ Missing tables: {missing_tables}")
        else:
            logger.info("✅ All expected tables present")
    
    except Exception as e:
        logger.error(f"Error verifying tables: {e}")
        sys.exit(1)
    
    logger.info("\n" + "=" * 50)
    logger.info("✅ Database initialization complete!")
    logger.info("=" * 50)


if __name__ == '__main__':
    main()
