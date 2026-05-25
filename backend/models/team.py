"""Team Model - Team database schema"""

from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from .base import BaseModel


class Team(BaseModel):
    """
    Team Model
    
    Stores information about all teams:
    - Team identity (name, league, country)
    - Facility info (stadium, founded year)
    - Contact info (website, email)
    - Performance statistics
    """
    
    __tablename__ = 'teams'
    
    # Team Identity
    name = Column(String(255), nullable=False, unique=True, index=True)
    short_name = Column(String(50), nullable=True)
    league = Column(String(100), nullable=False, index=True)
    country = Column(String(100), nullable=False, index=True)
    
    # Facility Information
    city = Column(String(100), nullable=True)
    stadium = Column(String(255), nullable=True)
    founded_year = Column(Integer, nullable=True)
    capacity = Column(Integer, nullable=True)
    
    # Contact Information
    website = Column(String(500), nullable=True)
    email = Column(String(255), nullable=True)
    
    # Team Management
    coach = Column(String(255), nullable=True)
    manager = Column(String(255), nullable=True)
    
    # Performance Stats
    matches_played = Column(Integer, default=0)
    wins = Column(Integer, default=0)
    draws = Column(Integer, default=0)
    losses = Column(Integer, default=0)
    
    goals_for = Column(Integer, default=0)
    goals_against = Column(Integer, default=0)
    
    points = Column(Integer, default=0)
    position = Column(Integer, nullable=True)
    
    # Additional Info
    description = Column(Text, nullable=True)
    logo_url = Column(String(500), nullable=True)
    
    # Relationships
    players = relationship('Player', back_populates='team')
    home_matches = relationship(
        'Match',
        foreign_keys='Match.home_team_id',
        back_populates='home_team'
    )
    away_matches = relationship(
        'Match',
        foreign_keys='Match.away_team_id',
        back_populates='away_team'
    )
    statistics = relationship('TeamStat', back_populates='team', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<Team {self.name} - {self.league}>"
    
    def to_dict(self):
        """Convert to dictionary"""
        data = super().to_dict()
        
        # Add calculated fields
        data['goal_difference'] = self.goals_for - self.goals_against
        data['win_percentage'] = round((self.wins / self.matches_played * 100), 2) if self.matches_played > 0 else 0
        
        return data
    
    @property
    def goal_difference(self):
        """Calculate goal difference"""
        return self.goals_for - self.goals_against
    
    @property
    def win_percentage(self):
        """Calculate win percentage"""
        if self.matches_played == 0:
            return 0.0
        return round((self.wins / self.matches_played) * 100, 2)
    
    @property
    def average_goals_per_game(self):
        """Calculate average goals per game"""
        if self.matches_played == 0:
            return 0.0
        return round(self.goals_for / self.matches_played, 2)
    
    @property
    def average_goals_against(self):
        """Calculate average goals against per game"""
        if self.matches_played == 0:
            return 0.0
        return round(self.goals_against / self.matches_played, 2)
    
    @property
    def form_status(self):
        """Determine team's current form"""
        if self.win_percentage >= 60:
            return 'Excellent'
        elif self.win_percentage >= 50:
            return 'Good'
        elif self.win_percentage >= 40:
            return 'Average'
        else:
            return 'Poor'
    
    def get_all_players(self):
        """Get all players in team"""
        return self.players
    
    def get_squad_size(self):
        """Get number of players"""
        return len(self.players)
    
    def get_player_by_position(self, position):
        """Get players by position"""
        return [p for p in self.players if p.position == position]
    
    @classmethod
    def get_league_standings(cls, league):
        """Get standings for league (placeholder)"""
        # TODO: Implement with database query
        return []
    
    @classmethod
    def get_best_attack(cls, limit=5):
        """Get teams with best attack (placeholder)"""
        # TODO: Query by goals_for
        return []
    
    @classmethod
    def get_best_defense(cls, limit=5):
        """Get teams with best defense (placeholder)"""
        # TODO: Query by goals_against
        return []
