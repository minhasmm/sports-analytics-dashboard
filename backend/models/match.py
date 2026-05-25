"""Match Model - Match database schema"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import BaseModel


class Match(BaseModel):
    """
    Match Model
    
    Stores information about all matches:
    - Teams (home and away)
    - Date and venue
    - Score and result
    - Statistics
    - Status
    """
    
    __tablename__ = 'matches'
    
    # Teams
    home_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False, index=True)
    away_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False, index=True)
    
    # Match Details
    league = Column(String(100), nullable=False, index=True)
    season = Column(String(50), nullable=False)
    match_day = Column(Integer, nullable=True)
    
    # Date & Venue
    match_date = Column(DateTime, nullable=False, index=True)
    venue = Column(String(255), nullable=True)
    attendance = Column(Integer, nullable=True)
    referee = Column(String(255), nullable=True)
    
    # Score & Result
    home_score = Column(Integer, nullable=True)
    away_score = Column(Integer, nullable=True)
    status = Column(
        String(50),
        default='scheduled',
        nullable=False,
        index=True
    )  # scheduled, ongoing, completed, postponed, cancelled
    
    # Match Statistics
    possession_home = Column(Float, nullable=True)
    possession_away = Column(Float, nullable=True)
    
    shots_home = Column(Integer, nullable=True)
    shots_away = Column(Integer, nullable=True)
    
    shots_on_target_home = Column(Integer, nullable=True)
    shots_on_target_away = Column(Integer, nullable=True)
    
    passes_home = Column(Integer, nullable=True)
    passes_away = Column(Integer, nullable=True)
    
    tackles_home = Column(Integer, nullable=True)
    tackles_away = Column(Integer, nullable=True)
    
    fouls_home = Column(Integer, nullable=True)
    fouls_away = Column(Integer, nullable=True)
    
    yellow_cards_home = Column(Integer, default=0)
    yellow_cards_away = Column(Integer, default=0)
    red_cards_home = Column(Integer, default=0)
    red_cards_away = Column(Integer, default=0)
    
    # Additional Info
    notes = Column(Text, nullable=True)
    
    # Relationships
    home_team = relationship('Team', foreign_keys=[home_team_id], back_populates='home_matches')
    away_team = relationship('Team', foreign_keys=[away_team_id], back_populates='away_matches')
    
    def __repr__(self):
        return f"<Match {self.home_team} vs {self.away_team} - {self.match_date}>"
    
    def to_dict(self):
        """Convert to dictionary"""
        data = super().to_dict()
        
        # Add team names
        if self.home_team:
            data['home_team_name'] = self.home_team.name
        if self.away_team:
            data['away_team_name'] = self.away_team.name
        
        # Add result
        data['result'] = self.get_result()
        
        # Add match format
        data['match_format'] = {
            'home_team': self.home_team.name if self.home_team else 'Unknown',
            'away_team': self.away_team.name if self.away_team else 'Unknown',
            'score': f"{self.home_score or '?'} - {self.away_score or '?'}"
        }
        
        return data
    
    def get_result(self):
        """Get match result (home_win, away_win, draw, ongoing, scheduled)"""
        if self.status != 'completed':
            return self.status
        
        if self.home_score is None or self.away_score is None:
            return 'unknown'
        
        if self.home_score > self.away_score:
            return 'home_win'
        elif self.away_score > self.home_score:
            return 'away_win'
        else:
            return 'draw'
    
    def is_finished(self):
        """Check if match is finished"""
        return self.status == 'completed'
    
    def is_scheduled(self):
        """Check if match is scheduled"""
        return self.status == 'scheduled'
    
    def is_ongoing(self):
        """Check if match is ongoing"""
        return self.status == 'ongoing'
    
    @property
    def total_goals(self):
        """Get total goals in match"""
        if self.home_score is None or self.away_score is None:
            return None
        return self.home_score + self.away_score
    
    @property
    def total_shots(self):
        """Get total shots"""
        if self.shots_home is None or self.shots_away is None:
            return None
        return self.shots_home + self.shots_away
    
    @property
    def total_fouls(self):
        """Get total fouls"""
        if self.fouls_home is None or self.fouls_away is None:
            return None
        return self.fouls_home + self.fouls_away
    
    @classmethod
    def get_upcoming_matches(cls, limit=10):
        """Get upcoming matches (placeholder)"""
        # TODO: Query with match_date > now() and status = 'scheduled'
        return []
    
    @classmethod
    def get_recent_matches(cls, limit=10):
        """Get recent matches (placeholder)"""
        # TODO: Query with status = 'completed' order by date desc
        return []
    
    @classmethod
    def get_team_matches(cls, team_id, limit=20):
        """Get matches for specific team (placeholder)"""
        # TODO: Query where home_team_id = team_id OR away_team_id = team_id
        return []
