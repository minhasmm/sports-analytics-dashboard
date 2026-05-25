"""Seed database with sample data"""

import os
import sys
import logging

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SessionLocal
from models.team import Team
from models.player import Player
from models.user import User
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def seed_teams(db):
    """Seed sample teams"""
    logger.info("Seeding teams...")
    
    teams_data = [
        {
            'name': 'Manchester United',
            'short_name': 'MAN',
            'league': 'Premier League',
            'country': 'England',
            'city': 'Manchester',
            'stadium': 'Old Trafford',
            'founded_year': 1878,
            'capacity': 74310
        },
        {
            'name': 'Liverpool FC',
            'short_name': 'LIV',
            'league': 'Premier League',
            'country': 'England',
            'city': 'Liverpool',
            'stadium': 'Anfield',
            'founded_year': 1892,
            'capacity': 61394
        },
        {
            'name': 'Manchester City',
            'short_name': 'MCY',
            'league': 'Premier League',
            'country': 'England',
            'city': 'Manchester',
            'stadium': 'Etihad Stadium',
            'founded_year': 1880,
            'capacity': 55097
        },
        {
            'name': 'Chelsea FC',
            'short_name': 'CHE',
            'league': 'Premier League',
            'country': 'England',
            'city': 'London',
            'stadium': 'Stamford Bridge',
            'founded_year': 1905,
            'capacity': 40341
        },
        {
            'name': 'Arsenal FC',
            'short_name': 'ARS',
            'league': 'Premier League',
            'country': 'England',
            'city': 'London',
            'stadium': 'Emirates Stadium',
            'founded_year': 1886,
            'capacity': 60704
        }
    ]
    
    for team_data in teams_data:
        team = Team(**team_data)
        db.add(team)
    
    db.commit()
    logger.info(f"✅ Added {len(teams_data)} teams")


def seed_players(db):
    """Seed sample players"""
    logger.info("Seeding players...")
    
    # Get teams
    teams = db.query(Team).all()
    
    players_data = [
        {
            'name': 'Lionel Messi',
            'age': 36,
            'nationality': 'Argentina',
            'position': 'FWD',
            'team_id': teams[0].id if teams else None,
            'jersey_number': 7,
            'height': '170 cm',
            'weight': '72 kg',
            'foot': 'Left',
            'goals': 800,
            'assists': 300,
            'appearances': 900,
            'rating': 9.2
        },
        {
            'name': 'Cristiano Ronaldo',
            'age': 38,
            'nationality': 'Portugal',
            'position': 'FWD',
            'team_id': teams[0].id if teams else None,
            'jersey_number': 7,
            'height': '187 cm',
            'weight': '84 kg',
            'foot': 'Right',
            'goals': 850,
            'assists': 250,
            'appearances': 1000,
            'rating': 8.9
        },
        {
            'name': 'Mohamed Salah',
            'age': 31,
            'nationality': 'Egypt',
            'position': 'FWD',
            'team_id': teams[1].id if len(teams) > 1 else None,
            'jersey_number': 11,
            'height': '175 cm',
            'weight': '71 kg',
            'foot': 'Left',
            'goals': 200,
            'assists': 80,
            'appearances': 350,
            'rating': 8.5
        },
        {
            'name': 'Erling Haaland',
            'age': 23,
            'nationality': 'Norway',
            'position': 'FWD',
            'team_id': teams[2].id if len(teams) > 2 else None,
            'jersey_number': 9,
            'height': '194 cm',
            'weight': '88 kg',
            'foot': 'Left',
            'goals': 100,
            'assists': 20,
            'appearances': 150,
            'rating': 8.7
        }
    ]
    
    for player_data in players_data:
        player = Player(**player_data)
        db.add(player)
    
    db.commit()
    logger.info(f"✅ Added {len(players_data)} players")


def seed_users(db):
    """Seed sample users"""
    logger.info("Seeding users...")
    
    users_data = [
        {
            'username': 'admin',
            'email': 'admin@sportsanalytics.com',
            'password_hash': 'hashed_password_123',  # TODO: Properly hash
            'display_name': 'Admin User',
            'is_admin': True,
            'is_verified': True
        },
        {
            'username': 'user1',
            'email': 'user1@example.com',
            'password_hash': 'hashed_password_456',
            'display_name': 'Sports Fan',
            'favorite_team': 'Manchester United',
            'is_verified': True
        }
    ]
    
    for user_data in users_data:
        user = User(**user_data)
        db.add(user)
    
    db.commit()
    logger.info(f"✅ Added {len(users_data)} users")


def main():
    """Seed database with sample data"""
    
    logger.info("=" * 50)
    logger.info("🌱 Seeding Database with Sample Data")
    logger.info("=" * 50)
    
    db = SessionLocal()
    
    try:
        seed_teams(db)
        seed_players(db)
        seed_users(db)
        
        logger.info("\n" + "=" * 50)
        logger.info("✅ Database seeding complete!")
        logger.info("=" * 50)
    
    except Exception as e:
        logger.error(f"Error seeding data: {e}")
        db.rollback()
    
    finally:
        db.close()


if __name__ == '__main__':
    main()
