"""User Model - User database schema"""

from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from datetime import datetime
from .base import BaseModel


class User(BaseModel):
    """
    User Model
    
    Stores user information:
    - Authentication (email, password hash)
    - Profile info
    - Preferences
    - Activity tracking
    """
    
    __tablename__ = 'users'
    
    # User Identity
    username = Column(String(100), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    
    # Profile Info
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    display_name = Column(String(255), nullable=True)
    
    # User Preferences
    favorite_team = Column(String(255), nullable=True)
    favorite_player = Column(String(255), nullable=True)
    preferred_league = Column(String(100), nullable=True)
    preferred_language = Column(String(10), default='en')
    
    # Theme & Display
    theme = Column(String(50), default='light')  # light or dark
    notifications_enabled = Column(Boolean, default=True)
    
    # Account Status
    is_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    
    # Activity Tracking
    last_login = Column(DateTime, nullable=True)
    last_activity = Column(DateTime, nullable=True)
    login_count = Column(Integer, default=0)
    
    # Additional Info
    bio = Column(Text, nullable=True)
    avatar_url = Column(String(500), nullable=True)
    
    def __repr__(self):
        return f"<User {self.username}>"
    
    def to_dict(self, include_sensitive=False):
        """Convert to dictionary"""
        data = {
            'id': self.id,
            'username': self.username,
            'display_name': self.display_name,
            'email': self.email if include_sensitive else '***',
            'first_name': self.first_name,
            'last_name': self.last_name,
            'favorite_team': self.favorite_team,
            'favorite_player': self.favorite_player,
            'preferred_league': self.preferred_league,
            'theme': self.theme,
            'avatar_url': self.avatar_url,
            'is_verified': self.is_verified,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'last_login': self.last_login.isoformat() if self.last_login else None
        }
        
        return data
    
    @property
    def full_name(self):
        """Get full name"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        else:
            return self.username
    
    def update_last_activity(self):
        """Update last activity timestamp"""
        self.last_activity = datetime.utcnow()
    
    def update_last_login(self):
        """Update last login timestamp"""
        self.last_login = datetime.utcnow()
        self.login_count += 1
    
    def set_preferences(self, **kwargs):
        """Update user preferences"""
        allowed_keys = [
            'favorite_team',
            'favorite_player',
            'preferred_league',
            'preferred_language',
            'theme'
        ]
        
        for key, value in kwargs.items():
            if key in allowed_keys:
                setattr(self, key, value)
    
    def is_preferences_complete(self):
        """Check if user has set preferences"""
        return all([
            self.favorite_team,
            self.preferred_league
        ])
