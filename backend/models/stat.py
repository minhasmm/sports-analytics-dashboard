"""Stat Models - Statistics tracking for players and teams"""

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import BaseModel


class PlayerStat(BaseModel):
    """
    Player Statistics
    
    Tracks player performance statistics over time
    Can be used to:
    - Track performance trends
    - Calculate averages
    - Analyze seasonal progress
    """
    
    __tablename__ = 'player_stats'
    
    # Foreign Key
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False, index=True)
    
    # Time Period
    season = Column(String(50), nullable=False, index=True)
    match_day = Column(Integer, nullable=True)
    
    # Performance Stats
    goals = Column(Integer, default=0)
    assists = Column(Integer, default=0)
    appearances = Column(Integer, default=0)
    minutes_played = Column(Integer, default=0)
    
    # Offensive Stats
    shots = Column(Integer, default=0)
    shots_on_target = Column(Integer, default=0)
    pass_accuracy = Column(Float, default=0.0)
    key_passes = Column(Integer, default=0)
    
    # Defensive Stats
    tackles = Column(Integer, default=0)
    interceptions = Column(Integer, default=0)
    blocks = Column(Integer, default=0)
    clearances = Column(Integer, default=0)
    
    # Discipline
    yellow_cards = Column(Integer, default=0)
    red_cards = Column(Integer, default=0)
    fouls_committed = Column(Integer, default=0)
    fouls_drawn = Column(Integer, default=0)
    
    # Rating
    average_rating = Column(Float, default=0.0)
    
    # Relationship
    player = relationship('Player', back_populates='statistics')
    
    def __repr__(self):
        return f"<PlayerStat Player:{self.player_id} Season:{self.season}>"
    
    @property
    def efficiency_rating(self):
        """Calculate efficiency"""
        if self.appearances == 0:
            return 0.0
        return round(((self.goals + self.assists) / self.appearances), 2)
    
    @property
    def goals_per_game(self):
        """Calculate goals per game"""
        if self.appearances == 0:
            return 0.0
        return round(self.goals / self.appearances, 2)
    
    @classmethod
    def get_player_season_stats(cls, player_id, season):
        """Get player's stats for specific season (placeholder)"""
        # TODO: Query where player_id = ? and season = ?
        return None


class TeamStat(BaseModel):
    """
    Team Statistics
    
    Tracks team performance statistics
    Can be used to:
    - Track team progress
    - Compare performance across seasons
    - Analyze strength/weakness areas
    """
    
    __tablename__ = 'team_stats'
    
    # Foreign Key
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False, index=True)
    
    # Time Period
    season = Column(String(50), nullable=False, index=True)
    match_day = Column(Integer, nullable=True)
    
    # Match Results
    matches_played = Column(Integer, default=0)
    wins = Column(Integer, default=0)
    draws = Column(Integer, default=0)
    losses = Column(Integer, default=0)
    
    # Goals
    goals_for = Column(Integer, default=0)
    goals_against = Column(Integer, default=0)
    
    # League Points
    points = Column(Integer, default=0)
    position = Column(Integer, nullable=True)
    
    # Performance Metrics
    possession_percentage = Column(Float, default=0.0)
    pass_accuracy = Column(Float, default=0.0)
    
    # Offensive
    shots_per_match = Column(Float, default=0.0)
    shots_on_target_per_match = Column(Float, default=0.0)
    
    # Defensive
    tackles_per_match = Column(Float, default=0.0)
    clean_sheets = Column(Integer, default=0)
    
    # Discipline
    yellow_cards = Column(Integer, default=0)
    red_cards = Column(Integer, default=0)
    
    # Relationship
    team = relationship('Team', back_populates='statistics')
    
    def __repr__(self):
        return f"<TeamStat Team:{self.team_id} Season:{self.season}>"
    
    @property
    def win_percentage(self):
        """Calculate win percentage"""
        if self.matches_played == 0:
            return 0.0
        return round((self.wins / self.matches_played) * 100, 2)
    
    @property
    def goal_difference(self):
        """Calculate goal difference"""
        return self.goals_for - self.goals_against
    
    @property
    def average_goals_per_game(self):
        """Calculate average goals per game"""
        if self.matches_played == 0:
            return 0.0
        return round(self.goals_for / self.matches_played, 2)
    
    @classmethod
    def get_team_season_stats(cls, team_id, season):
        """Get team's stats for specific season (placeholder)"""
        # TODO: Query where team_id = ? and season = ?
        return None
    
    @classmethod
    def get_league_season_stats(cls, league, season):
        """Get all teams' stats for specific league/season (placeholder)"""
        # TODO: Query all teams for league and season
        return []
