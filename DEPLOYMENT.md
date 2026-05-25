# 🚀 Sports Analytics Dashboard - Deployment Guide

Complete guide to deploy the Sports Analytics Dashboard to production.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Local Development](#local-development)
- [Docker Setup](#docker-setup)
- [Production Deployment](#production-deployment)
- [Environment Variables](#environment-variables)
- [Database Setup](#database-setup)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required Software

- Docker & Docker Compose (v20.10+)
- Python 3.11+ (for local development)
- Node.js 18+ (for local development)
- Git

### System Requirements

- **CPU:** Minimum 2 cores
- **RAM:** Minimum 4GB
- **Storage:** 10GB free space
- **OS:** Linux, macOS, or Windows with WSL2

---

## Local Development

# Copy example environment files
cp .env.example .env.development

# Edit environment variables
nano .env.development

# Using Docker Compose (recommended)
docker-compose -f docker-compose.dev.yml up

# Access applications
# Frontend: http://localhost:5173
# Backend: http://localhost:5000/api/v1

# Inside backend container
docker-compose exec backend python scripts/init_db.py
docker-compose exec backend python scripts/seed_data.py

# Build and start containers
docker-compose -f docker-compose.dev.yml up --build

# View logs
docker-compose -f docker-compose.dev.yml logs -f

# Stop containers
docker-compose -f docker-compose.dev.yml down

# Build production images
docker-compose -f docker-compose.yml build

# Start services
docker-compose -f docker-compose.yml up -d

# Check status
docker-compose -f docker-compose.yml ps

# View logs
docker-compose -f docker-compose.yml logs -f

# 1. Launch EC2 Instance
# - AMI: Ubuntu 22.04 LTS
# - Type: t3.medium or larger
# - Storage: 20GB gp3

# 2. Connect to instance
ssh -i your-key.pem ubuntu@your-instance-ip

# 3. Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# 4. Clone repository
git clone your-repo
cd sports-analytics-dashboard

# 5. Configure environment
cp .env.production .env
nano .env  # Edit with your settings

# 6. Start services
docker-compose -f docker-compose.yml up -d

# 7. Set up SSL/HTTPS (recommended)
# Use AWS Certificate Manager or Let's Encrypt



# 1. Connect GitHub repository
# 2. Select Branch: main
# 3. Configure services:
#    - Backend (Flask)
#    - Frontend (React)
#    - Database (PostgreSQL)
# 4. Deploy

# 1. Install Heroku CLI
curl https://cli.heroku.com/install.sh | sh

# 2. Login
heroku login

# 3. Create app
heroku create your-app-name

# 4. Add buildpacks
heroku buildpacks:add heroku/python
heroku buildpacks:add heroku/nodejs

# 5. Set environment variables
heroku config:set FLASK_ENV=production
heroku config:set JWT_SECRET_KEY=your-secret

# 6. Deploy
git push heroku mai

# Flask
FLASK_ENV=production
FLASK_DEBUG=False

# Database
DATABASE_URL=postgresql://user:password@host:5432/dbname
REDIS_URL=redis://host:6379/0

# Security
JWT_SECRET_KEY=your-32-char-min-secret
SECRET_KEY=your-32-char-min-secret

# CORS
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# Email
MAIL_SERVER=smtp.gmail.com
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

VITE_API_URL=https://api.yourdomain.com/api/v1
VITE_ENVIRONMENT=productioVITE_API_URL=https://api.yourdomain.com/api/v1
VITE_ENVIRONMENT=production



# 1. Install PostgreSQL
sudo apt-get install postgresql postgresql-contrib

# 2. Create database
sudo -u postgres createdb sports_analytics
sudo -u postgres createuser sports_admin

# 3. Set password
sudo -u postgres psql
ALTER USER sports_admin WITH PASSWORD 'your-secure-password';
GRANT ALL PRIVILEGES ON DATABASE sports_analytics TO sports_admin;

# 4. Update DATABASE_URL
DATABASE_URL=postgresql://sports_admin:password@localhost:5432/sports_analytics

# Backup
pg_dump sports_analytics > backup.sql

# Restore
psql sports_analytics < backup.sql

# Check backend health
curl http://your-domain/api/v1/health

# Check frontend
curl http://your-domain/

# Check database
docker-compose exec postgres pg_isready

# Check Redis
docker-compose exec redis redis-cli ping

# Find process using port
sudo lsof -i :5000

# Kill process
kill -9 <PID>

# Verify DATABASE_URL
echo $DATABASE_URL

# Test connection
psql "$DATABASE_URL"

# Clear node_modules and reinstall
rm -rf frontend/node_modules
npm install --prefix frontend

# Rebuild
docker-compose build --no-cache frontend


# View all logs
docker-compose logs

# Follow logs
docker-compose logs -f

# Specific service
docker-compose logs -f backend



# Verify Redis is running
docker-compose ps redis

# Monitor Redis
docker-compose exec redis redis-cli monitor

-- Add indexes for frequently queried columns
CREATE INDEX idx_player_name ON players(name);
CREATE INDEX idx_team_league ON teams(league);
CREATE INDEX idx_match_date ON matches(match_date);


CDN Setup
Use CloudFlare for global distribution
Configure for static assets caching
Enable gzip compression


Security Checklist
✅ Change default passwords
✅ Set JWT_SECRET_KEY to secure value
✅ Enable HTTPS/SSL
✅ Configure firewall rules
✅ Set CORS properly
✅ Use environment variables
✅ Enable database backups
✅ Monitor logs regularly
✅ Update dependencies
✅ Use non-root user in containers

# Install Prometheus
docker run -d -p 9090:9090 prom/prometheus

# Install Grafana
docker run -d -p 3000:3000 grafana/grafana

Support
For issues or questions:

Check logs: docker-compose logs
Review error messages
Check GitHub Issues
Contact support: support@yourdomain.com


### **STEP 77.2: Commit**
**Click "Commit changes"**

✅ **DEPLOYMENT.md is created!**

---

## ✅ **STEP 78: Create DOCKER_README.md (Docker Guide)**

### **How to Create It:**

1. **Click "Add file"**
2. **Click "Create new file"**
3. **Type filename:**

4. 
### **STEP 78.1: Add Content**

**Copy and paste this:**

```markdown
# 🐳 Docker Setup - Sports Analytics Dashboard

Quick start guide for Docker deployment.

## Prerequisites

```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Clone repository
git clone your-repo && cd sports-analytics-dashboard

# Start development services
docker-compose -f docker-compose.dev.yml up

# Initialize database (in new terminal)
docker-compose exec backend python scripts/init_db.py
docker-compose exec backend python scripts/seed_data.py

# Access applications
# Frontend: http://localhost:5173
# Backend: http://localhost:5000/api/v1

# Set environment variables
cp .env.production .env

# Edit configuration
nano .env

# Build and start
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f

# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f backend

# Execute command in container
docker-compose exec backend python scripts/init_db.py

# Rebuild images
docker-compose build --no-cache

# Remove all
docker-compose down -v

# Check container status
docker ps -a

# View service logs
docker-compose logs service-name

# Restart service
docker-compose restart service-name

# Clean up
docker system prune -a 

# Run main function
main "$@"
