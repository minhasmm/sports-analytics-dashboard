"""Database Configuration - SQLAlchemy setup and session management"""

import os
import logging
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool, QueuePool

logger = logging.getLogger(__name__)


# Get database URL from environment
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///sports_analytics.db')

logger.info(f"Using database: {DATABASE_URL}")

# Create engine based on database type
if DATABASE_URL.startswith('sqlite'):
    # SQLite configuration
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        echo=False
    )
else:
    # PostgreSQL or other database configuration
    engine = create_engine(
        DATABASE_URL,
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True,
        echo=False
    )

# Create SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    """
    Dependency for getting database session
    Used in route handlers
    
    Usage:
        @app.route('/example')
        def my_route(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Initialize database - create all tables"""
    from models.base import Base
    
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("✅ Database tables created successfully")


def drop_db():
    """Drop all tables - USE WITH CAUTION!"""
    from models.base import Base
    
    logger.warning("⚠️ DROPPING ALL DATABASE TABLES!")
    Base.metadata.drop_all(bind=engine)
    logger.warning("✅ All tables dropped")


def check_db_connection():
    """Check database connection"""
    try:
        with engine.connect() as connection:
            logger.info("✅ Database connection successful")
            return True
    except Exception as e:
        logger.error(f"❌ Database connection failed: {e}")
        return False


# Event listeners for logging
@event.listens_for(engine, "connect")
def receive_connect(dbapi_conn, connection_record):
    """Log database connection"""
    logger.debug("Database connection established")


@event.listens_for(engine, "close")
def receive_close(dbapi_conn, connection_record):
    """Log database disconnection"""
    logger.debug("Database connection closed")


# Optional: Event listener for query logging
@event.listens_for(engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    """Log SQL queries in development"""
    if os.getenv('FLASK_DEBUG') == 'True':
        logger.debug(f"SQL: {statement}")
