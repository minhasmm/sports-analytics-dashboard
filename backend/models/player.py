"""Player Model - Player database schema"""

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import BaseModel


class Player(BaseModel):
    """
    Player Model
    
    Stores information about all players:
    - Personal info (name, age, position)
    - Physical attributes (height, weight)
    - Career info (team, jersey number)
    - Statistics (goals, assists, rating)
    """
    
    __tablename__ = 'players'
    
    # Personal Information
    name = Column(String(255), nullable=False, index=True)
    age = Column(Integer, nullable=True)
    nationality = Column(String(100), nullable=True)
    date_of_birth = Column(DateTime, nullable=True)
    
    # Position & Team Info
    position = Column(String(50), nullable=False, index=True)  # GK, DEF, MID, FWD
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=True, index=True)
    jersey_number = Column(Integer, nullable=True)
    
    # Physical Attributes
    height = Column(String(50), nullable=True)  # e.g., "180 cm"
    weight = Column(String(50), nullable=True)  # e.g., "75 kg"
    foot = Column(String(50), nullable=True)    # Left or Right
    
    # Career Information
    contract_until = Column(String(50), nullable=True)
    market_value = Column(String(100), nullable=True)  # e.g., "€50M"
    
    # Performance Metrics
    goals = Column(Integer, default=0)
    assists = Column(Integer, default=0)
    appearances = Column(Integer, default=0)
    minutes_played = Column(Integer, default=0)
    rating = Column(Float, default=0.0)
    
    # Additional Stats
    pass_accuracy = Column(Float, default=0.0)
    tackles = Column(Integer, default=0)
    interceptions = Column(Integer, default=0)
    yellow_cards = Column(Integer, default=0)
    red_cards = Column(Integer, default=0)
    fouls_committed = Column(Integer, default=0)
    fouls_drawn = Column(Integer, default=0)
    
    # Additional Info
    bio = Column(Text, nullable=True)
    image_url = Column(String(500), nullable=True)
    
    # Relationships
    team = relationship('Team', back_populates='players')
    statistics = relationship('PlayerStat', back_populates='player', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<Player {self.name} - {self.position}>"
    
    def to_dict(self):
        """Convert to dictionary with related data"""
        data = super().to_dict()
        
        # Add team info
        if self.team:
            data['team_name'] = self.team.name
        
        # Add statistics summary
        data['stats_summary'] = {
            'goals': self.goals,
            'assists': self.assists,
            'appearances': self.appearances,
            'rating': self.rating
        }
        
        return data
    
    @property
    def goals_per_game(self):
        """Calculate goals per game"""
        if self.appearances == 0:
            return 0.0
        return round(self.goals / self.appearances, 2)
    
    @property
    def assists_per_game(self):
        """Calculate assists per game"""
        if self.appearances == 0:
            return 0.0
        return round(self.assists / self.appearances, 2)
    
    @property
    def efficiency_rating(self):
        """Calculate player efficiency"""
        total_contributions = self.goals + self.assists
        if self.appearances == 0:
            return 0.0
        return round((total_contributions / self.appearances) * 10, 2)
    
    @property
    def form_status(self):
        """Determine player's current form"""
        if self.rating >= 7.5:
            return 'Excellent'
        elif self.rating >= 7.0:
            return 'Very Good'
        elif self.rating >= 6.5:
            return 'Good'
        elif self.rating >= 6.0:
            return 'Average'
        else:
            return 'Poor'
    
    @classmethod
    def get_top_scorers(cls, limit=10):
        """Get top scorers (placeholder)"""
        # TODO: Implement with database query
        return []
    
    @classmethod
    def get_top_assists(cls, limit=10):
        """Get top assist providers (placeholder)"""
        # TODO: Implement with database query
        return []
    
    @classmethod
    def search_by_name(cls, name):
        """Search player by name (placeholder)"""
        # TODO: Implement with database query
        return []
