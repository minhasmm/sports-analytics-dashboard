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


main "$@"
