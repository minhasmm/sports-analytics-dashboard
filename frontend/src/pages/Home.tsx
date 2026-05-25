import React, { useEffect, useState } from 'react'
import {
  Grid,
  Paper,
  Box,
  Typography,
  Card,
  CardContent,
  LinearProgress,
  Chip,
} from '@mui/material'
import {
  TrendingUp as TrendingUpIcon,
  Sports as SportsIcon,
  People as PeopleIcon,
  EmojiEvents as TrophyIcon,
} from '@mui/icons-material'
import {
  LineChart,
  Line,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
} from 'recharts'

const Home: React.FC = () => {
  const [loading, setLoading] = useState(true)
  const [stats, setStats] = useState({
    totalPlayers: 18000,
    totalTeams: 500,
    totalMatches: 5000,
    accuracyRate: 78,
  })

  // Sample data for charts
  const trendData = [
    { name: 'Jan', goals: 340, assists: 120 },
    { name: 'Feb', goals: 380, assists: 130 },
    { name: 'Mar', goals: 420, assists: 145 },
    { name: 'Apr', goals: 390, assists: 150 },
    { name: 'May', goals: 450, assists: 160 },
    { name: 'Jun', goals: 480, assists: 175 },
  ]

  const topScorersData = [
    { name: 'Messi', value: 800, fill: '#1976d2' },
    { name: 'Ronaldo', value: 850, fill: '#dc004e' },
    { name: 'Haaland', value: 100, fill: '#4caf50' },
    { name: 'Salah', value: 200, fill: '#ff9800' },
  ]

  useEffect(() => {
    // Simulate data loading
    setTimeout(() => setLoading(false), 1000)
  }, [])

  const StatCard: React.FC<{
    title: string
    value: number | string
    icon: React.ReactNode
    trend?: string
  }> = ({ title, value, icon, trend }) => (
    <Card>
      <CardContent>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 2 }}>
          <Typography color="textSecondary" gutterBottom>
            {title}
          </Typography>
          <Box sx={{ color: 'primary.main', fontSize: 24 }}>{icon}</Box>
        </Box>
        <Typography variant="h4" sx={{ mb: 1 }}>
          {value}
        </Typography>
        {trend && (
          <Chip
            icon={<TrendingUpIcon />}
            label={trend}
            size="small"
            color="success"
            variant="outlined"
          />
        )}
      </CardContent>
    </Card>
  )

  return (
    <Box>
      <Typography variant="h3" sx={{ mb: 3 }}>
        🏆 Sports Analytics Dashboard
      </Typography>

      {/* Stats Cards */}
      <Grid container spacing={2} sx={{ mb: 3 }}>
        <Grid item xs={12} sm={6} md={3}>
          <StatCard
            title="Total Players"
            value={stats.totalPlayers.toLocaleString()}
            icon={<PeopleIcon />}
            trend="+5%"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <StatCard
            title="Total Teams"
            value={stats.totalTeams}
            icon={<SportsIcon />}
            trend="+2%"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <StatCard
            title="Matches Analyzed"
            value={stats.totalMatches.toLocaleString()}
            icon={<TrophyIcon />}
            trend="+12%"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <StatCard
            title="Prediction Accuracy"
            value={`${stats.accuracyRate}%`}
            icon={<TrendingUpIcon />}
            trend="+3%"
          />
        </Grid>
      </Grid>

      {/* Charts */}
      <Grid container spacing={2}>
        {/* Trend Chart */}
        <Grid item xs={12} md={8}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" sx={{ mb: 2 }}>
              📈 Goals & Assists Trend
            </Typography>
            {loading ? (
              <LinearProgress />
            ) : (
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={trendData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Line
                    type="monotone"
                    dataKey="goals"
                    stroke="#1976d2"
                    dot={{ fill: '#1976d2' }}
                  />
                  <Line
                    type="monotone"
                    dataKey="assists"
                    stroke="#dc004e"
                    dot={{ fill: '#dc004e' }}
                  />
                </LineChart>
              </ResponsiveContainer>
            )}
          </Paper>
        </Grid>

        {/* Top Scorers Pie Chart */}
        <Grid item xs={12} md={4}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" sx={{ mb: 2 }}>
              ⚽ Top Scorers
            </Typography>
            {loading ? (
              <LinearProgress />
            ) : (
              <ResponsiveContainer width="100%" height={300}>
                <PieChart>
                  <Pie
                    data={topScorersData}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    label={({ name, value }) => `${name}: ${value}`}
                    outerRadius={80}
                    fill="#8884d8"
                    dataKey="value"
                  >
                    {topScorersData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.fill} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
            )}
          </Paper>
        </Grid>

        {/* Recent Activities */}
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" sx={{ mb: 2 }}>
              📋 Recent Matches
            </Typography>
            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
              {[1, 2, 3, 4].map((i) => (
                <Box
                  key={i}
                  sx={{
                    p: 1.5,
                    bgcolor: 'action.hover',
                    borderRadius: 1,
                    display: 'flex',
                    justifyContent: 'space-between',
                  }}
                >
                  <Typography variant="body2">
                    Manchester United vs Liverpool
                  </Typography>
                  <Chip label="2-1" size="small" color="primary" />
                </Box>
              ))}
            </Box>
          </Paper>
        </Grid>

        {/* Quick Stats */}
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" sx={{ mb: 2 }}>
              🎯 Quick Stats
            </Typography>
            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
              <Box>
                <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 1 }}>
                  <Typography variant="body2">Goals Accuracy</Typography>
                  <Typography variant="body2" sx={{ fontWeight: 700 }}>
                    85%
                  </Typography>
                </Box>
                <LinearProgress variant="determinate" value={85} />
              </Box>
              <Box>
                <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 1 }}>
                  <Typography variant="body2">Assists Accuracy</Typography>
                  <Typography variant="body2" sx={{ fontWeight: 700 }}>
                    78%
                  </Typography>
                </Box>
                <LinearProgress variant="determinate" value={78} />
              </Box>
              <Box>
                <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 1 }}>
                  <Typography variant="body2">Match Prediction</Typography>
                  <Typography variant="body2" sx={{ fontWeight: 700 }}>
                    72%
                  </Typography>
                </Box>
                <LinearProgress variant="determinate" value={72} />
              </Box>
            </Box>
          </Paper>
        </Grid>
      </Grid>
    </Box>
  )
}

export default Home
