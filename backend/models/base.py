"""Base Model - Parent class for all database models"""

from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

# Create base class for all models
Base = declarative_base()


class BaseModel(Base):
    """
    Base model with common fields for all models
    
    Provides:
    - Automatic ID generation
    - Timestamps (created_at, updated_at)
    - Serialization methods
    """
    
    __abstract__ = True
    
    # Common fields
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    
    def to_dict(self):
        """Convert model to dictionary"""
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }
    
    def to_json(self):
        """Convert model to JSON-serializable dict"""
        data = self.to_dict()
        
        # Handle datetime objects
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()
        
        return data
    
    def __repr__(self):
        """String representation"""
        return f"<{self.__class__.__name__} id={self.id}>"
