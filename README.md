# 🏆 Sports Analytics Dashboard & AI Chatbot

A **professional-grade** sports analytics platform with interactive dashboards and an AI-powered chatbot for intelligent data analysis.

## 🌟 Features Overview

### 📊 Dashboard Features
- ✅ Real-time Analytics: Live player stats, team performance, match predictions
- ✅ Interactive Visualizations: Line charts, bar charts, heat maps, scatter plots
- ✅ Advanced Filtering: Search by team, player, season, league
- ✅ Performance Metrics: Win rates, scoring trends, player rankings
- ✅ Comparative Analysis: Team vs Team, Player vs Player
- ✅ Statistical Reports: Detailed performance analysis with export
- ✅ Responsive Design: Mobile, tablet, desktop optimized
- ✅ Dark/Light Theme: User preference persistence

### 🤖 Chatbot Features
- 💬 Natural Language Processing: Understands conversational queries
- 📊 Data Insights: Answers questions about player stats and teams
- 🎯 Context Awareness: Maintains conversation history
- 🔍 Advanced Search: Semantic search across datasets
- 📈 Predictive Analysis: ML-powered trend forecasting
- 📋 Report Generation: Creates custom analytics reports

## 📊 Dataset Information

**Primary Dataset**: FIFA 21+ Player Statistics
- 18,000+ player records
- 500+ teams across multiple leagues
- 5+ years of historical data
- 50+ performance metrics per player

## 🛠️ Technology Stack

### Frontend
- React 18 + TypeScript
- Material-UI v5 + Tailwind CSS
- Recharts for visualizations
- Redux Toolkit for state management
- Vite build tool

### Backend
- Python 3.11+ with Flask
- PostgreSQL database
- Redis caching
- Pandas/NumPy for data processing

### Chatbot
- Hugging Face Transformers
- spaCy for NLP
- PyTorch for ML models

### DevOps
- Docker & Docker Compose
- GitHub Actions CI/CD

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker (optional)

### Installation

```bash
# Clone the repository
git clone https://github.com/minhasmm/sports-analytics-dashboard.git
cd sports-analytics-dashboard

# Install backend dependencies
pip install -r requirements.txt

# Install frontend dependencies
cd frontend
npm install

# Terminal 1: Start Backend
python backend/app.py

# Terminal 2: Start Frontend
npm run dev

# Or use Docker
docker-compose up -d

Access the Application
Dashboard: http://localhost:5173
API: http://localhost:5000
API Docs: http://localhost:5000/api/docs
📁 Project Structuresports-analytics-dashboard/
├── README.md
├── LICENSE
├── .gitignore
├── docker-compose.yml
├── requirements.txt
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── health.py
│   │   ├── players.py
│   │   ├── teams.py
│   │   ├── matches.py
│   │   ├── stats.py
│   │   ├── predictions.py
│   │   └── chatbot_routes.py
│   ├── services/
│   ├── models/
│   └── chatbot/
└── frontend/
    ├── package.json
    ├── tsconfig.json
    ├── vite.config.ts
    └── src/
        └── App.tsx

## 💬 Chatbot Capabilities

The chatbot can answer questions like:
- "Who is the top scorer this season?"
- "Compare Messi and Ronaldo's performance"
- "What's Liverpool's win percentage?"
- "Predict the next match outcome"
- "Show me Manchester City's performance trends"

## 📈 Analytics Features

1. **Descriptive Analytics**: What happened?
2. **Diagnostic Analytics**: Why did it happen?
3. **Predictive Analytics**: What will happen?
4. **Prescriptive Analytics**: What should we do?

## 🔒 Security Features

- ✅ JWT Authentication
- ✅ Rate Limiting
- ✅ CORS Enabled
- ✅ Input Validation
- ✅ Error Handling

## 📝 License

MIT License - See LICENSE file for details

## 🎓 Perfect for College Project

✨ Demonstrates:
- Full-stack development
- Machine Learning integration
- Data visualization expertise
- API design & REST principles
- Database optimization
- Real-time data handling
- NLP & Chatbot development
- Docker containerization

## 👨‍💻 Author

Developed for college project | Sports Analytics & AI

---

**Ready to impress your mentors?** 🚀
