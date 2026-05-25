import React from 'react'
import { Box, Typography, Paper, Grid, Card, CardContent, LinearProgress } from '@mui/material'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

const TeamPerformance: React.FC = () => {
  const standingsData = [
    { name: 'Man City', wins: 30, draws: 5, losses: 3, points: 95 },
    { name: 'Arsenal', wins: 28, draws: 6, losses: 4, points: 90 },
    { name: 'Man United', wins: 25, draws: 7, losses: 6, points: 82 },
    { name: 'Liverpool', wins: 24, draws: 8, losses: 6, points: 80 },
    { name: 'Chelsea', wins: 20, draws: 5, losses: 13, points: 65 },
  ]

  return (
    <Box>
      <Typography variant="h3" sx={{ mb: 3 }}>
        🏆 Team Performance
      </Typography>

      <Grid container spacing={2}>
        <Grid item xs={12} md={8}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" sx={{ mb: 2 }}>
              📊 League Standings
            </Typography>
            <ResponsiveContainer width="100%" height={400}>
              <BarChart data={standingsData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="wins" fill="#4caf50" />
                <Bar dataKey="draws" fill="#ff9800" />
                <Bar dataKey="losses" fill="#f44336" />
              </BarChart>
            </ResponsiveContainer>
          </Paper>
        </Grid>

        <Grid item xs={12} md={4}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" sx={{ mb: 2 }}>
              🥇 Top Teams
            </Typography>
            {standingsData.map((team, idx) => (
              <Box key={idx} sx={{ mb: 2 }}>
                <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 1 }}>
                  <Typography variant="body2">{idx + 1}. {team.name}</Typography>
                  <Typography variant="body2" sx={{ fontWeight: 700 }}>{team.points}pts</Typography>
                </Box>
                <LinearProgress variant="determinate" value={(team.points / 95) * 100} />
              </Box>
            ))}
          </Paper>
        </Grid>
      </Grid>
    </Box>
  )
}

export default TeamPerformance
