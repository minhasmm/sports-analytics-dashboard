import React from 'react'
import { Box, Typography, Paper, Grid, Card, CardContent, Chip, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from '@mui/material'

const LeagueStats: React.FC = () => {
  const topScorers = [
    { rank: 1, name: 'Messi', team: 'Barcelona', goals: 800 },
    { rank: 2, name: 'Ronaldo', team: 'Man United', goals: 850 },
    { rank: 3, name: 'Salah', team: 'Liverpool', goals: 200 },
    { rank: 4, name: 'Haaland', team: 'Man City', goals: 100 },
    { rank: 5, name: 'Kane', team: 'Bayern', goals: 215 },
  ]

  return (
    <Box>
      <Typography variant="h3" sx={{ mb: 3 }}>
        📊 League Statistics
      </Typography>

      <Grid container spacing={2}>
        <Grid item xs={12}>
          <TableContainer component={Paper}>
            <Table>
              <TableHead>
                <TableRow sx={{ backgroundColor: '#f5f5f5' }}>
                  <TableCell sx={{ fontWeight: 700 }}>Rank</TableCell>
                  <TableCell sx={{ fontWeight: 700 }}>Player</TableCell>
                  <TableCell sx={{ fontWeight: 700 }}>Team</TableCell>
                  <TableCell align="right" sx={{ fontWeight: 700 }}>Goals</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {topScorers.map((scorer) => (
                  <TableRow key={scorer.rank} hover>
                    <TableCell><Chip label={scorer.rank} color="primary" /></TableCell>
                    <TableCell sx={{ fontWeight: 500 }}>{scorer.name}</TableCell>
                    <TableCell>{scorer.team}</TableCell>
                    <TableCell align="right"><Chip label={scorer.goals} color="success" /></TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        </Grid>
      </Grid>
    </Box>
  )
}

export default LeagueStats
