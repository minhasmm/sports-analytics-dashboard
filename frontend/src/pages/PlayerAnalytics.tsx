import React, { useState } from 'react'
import {
  Grid,
  Paper,
  Box,
  Typography,
  TextField,
  Button,
  Card,
  CardContent,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Chip,
  Dialog,
  DialogTitle,
  DialogContent,
} from '@mui/material'
import {
  Search as SearchIcon,
  BarChart as ChartIcon,
} from '@mui/icons-material'
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Radar,
} from 'recharts'

interface Player {
  id: number
  name: string
  team: string
  position: string
  goals: number
  assists: number
  rating: number
  appearances: number
}

const PlayerAnalytics: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedPlayer, setSelectedPlayer] = useState<Player | null>(null)
  const [openDialog, setOpenDialog] = useState(false)

  // Sample players data
  const players: Player[] = [
    {
      id: 1,
      name: 'Lionel Messi',
      team: 'Barcelona',
      position: 'FWD',
      goals: 800,
      assists: 300,
      rating: 9.2,
      appearances: 900,
    },
    {
      id: 2,
      name: 'Cristiano Ronaldo',
      team: 'Manchester United',
      position: 'FWD',
      goals: 850,
      assists: 250,
      rating: 8.9,
      appearances: 1000,
    },
    {
      id: 3,
      name: 'Mohamed Salah',
      team: 'Liverpool',
      position: 'FWD',
      goals: 200,
      assists: 80,
      rating: 8.5,
      appearances: 350,
    },
    {
      id: 4,
      name: 'Erling Haaland',
      team: 'Manchester City',
      position: 'FWD',
      goals: 100,
      assists: 20,
      rating: 8.7,
      appearances: 150,
    },
  ]

  // Player stats for radar chart
  const playerStatsData = [
    { stat: 'Goals', value: 80 },
    { stat: 'Assists', value: 75 },
    { stat: 'Dribling', value: 88 },
    { stat: 'Defense', value: 35 },
    { stat: 'Passing', value: 82 },
    { stat: 'Pace', value: 85 },
  ]

  const filteredPlayers = players.filter((player) =>
    player.name.toLowerCase().includes(searchTerm.toLowerCase())
  )

  const handlePlayerClick = (player: Player) => {
    setSelectedPlayer(player)
    setOpenDialog(true)
  }

  return (
    <Box>
      <Typography variant="h3" sx={{ mb: 3 }}>
        👥 Player Analytics
      </Typography>

      {/* Search Bar */}
      <Paper sx={{ p: 2, mb: 3 }}>
        <TextField
          fullWidth
          placeholder="Search players..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          InputProps={{
            startAdornment: <SearchIcon sx={{ mr: 1 }} />,
          }}
        />
      </Paper>

      <Grid container spacing={2}>
        {/* Players Table */}
        <Grid item xs={12} md={8}>
          <TableContainer component={Paper}>
            <Table>
              <TableHead>
                <TableRow sx={{ backgroundColor: '#f5f5f5' }}>
                  <TableCell sx={{ fontWeight: 700 }}>Name</TableCell>
                  <TableCell sx={{ fontWeight: 700 }}>Team</TableCell>
                  <TableCell align="right" sx={{ fontWeight: 700 }}>
                    Goals
                  </TableCell>
                  <TableCell align="right" sx={{ fontWeight: 700 }}>
                    Assists
                  </TableCell>
                  <TableCell align="right" sx={{ fontWeight: 700 }}>
                    Rating
                  </TableCell>
                  <TableCell align="center" sx={{ fontWeight: 700 }}>
                    Action
                  </TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {filteredPlayers.map((player) => (
                  <TableRow key={player.id} hover>
                    <TableCell sx={{ fontWeight: 500 }}>{player.name}</TableCell>
                    <TableCell>{player.team}</TableCell>
                    <TableCell align="right">
                      <Chip label={player.goals} size="small" color="primary" />
                    </TableCell>
                    <TableCell align="right">
                      <Chip label={player.assists} size="small" color="secondary" />
                    </TableCell>
                    <TableCell align="right">
                      <Chip
                        label={player.rating.toFixed(1)}
                        size="small"
                        color={player.rating >= 8.5 ? 'success' : 'default'}
                      />
                    </TableCell>
                    <TableCell align="center">
                      <Button
                        size="small"
                        onClick={() => handlePlayerClick(player)}
                      >
                        View
                      </Button>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        </Grid>

        {/* Player Stats Summary */}
        <Grid item xs={12} md={4}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" sx={{ mb: 2 }}>
              📊 Player Radar Stats
            </Typography>
            <ResponsiveContainer width="100%" height={300}>
              <RadarChart data={playerStatsData}>
                <PolarGrid />
                <PolarAngleAxis dataKey="stat" />
                <PolarRadiusAxis />
                <Radar
                  name="Stats"
                  dataKey="value"
                  stroke="#1976d2"
                  fill="#1976d2"
                  fillOpacity={0.6}
                />
                <Tooltip />
              </RadarChart>
            </ResponsiveContainer>
          </Paper>
        </Grid>

        {/* Top Performers */}
        <Grid item xs={12}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" sx={{ mb: 2 }}>
              🔥 Top Performers This Season
            </Typography>
            <Grid container spacing={2}>
              {players.slice(0, 4).map((player) => (
                <Grid item xs={12} sm={6} md={3} key={player.id}>
                  <Card>
                    <CardContent>
                      <Typography color="textSecondary" gutterBottom>
                        {player.team}
                      </Typography>
                      <Typography variant="h6" sx={{ mb: 1 }}>
                        {player.name}
                      </Typography>
                      <Box sx={{ display: 'flex', gap: 1 }}>
                        <Chip
                          label={`⚽ ${player.goals}G`}
                          size="small"
                          color="primary"
                          variant="outlined"
                        />
                        <Chip
                          label={`🎯 ${player.assists}A`}
                          size="small"
                          color="secondary"
                          variant="outlined"
                        />
                      </Box>
                    </CardContent>
                  </Card>
                </Grid>
              ))}
            </Grid>
          </Paper>
        </Grid>
      </Grid>

      {/* Player Detail Dialog */}
      <Dialog open={openDialog} onClose={() => setOpenDialog(false)} maxWidth="sm" fullWidth>
        <DialogTitle>{selectedPlayer?.name}</DialogTitle>
        <DialogContent>
          {selectedPlayer && (
            <Box sx={{ pt: 2 }}>
              <Grid container spacing={2}>
                <Grid item xs={6}>
                  <Typography variant="body2" color="textSecondary">
                    Team
                  </Typography>
                  <Typography variant="h6">{selectedPlayer.team}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="textSecondary">
                    Position
                  </Typography>
                  <Typography variant="h6">{selectedPlayer.position}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="textSecondary">
                    Goals
                  </Typography>
                  <Typography variant="h6">{selectedPlayer.goals}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="textSecondary">
                    Assists
                  </Typography>
                  <Typography variant="h6">{selectedPlayer.assists}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="textSecondary">
                    Rating
                  </Typography>
                  <Typography variant="h6">{selectedPlayer.rating}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="textSecondary">
                    Appearances
                  </Typography>
                  <Typography variant="h6">{selectedPlayer.appearances}</Typography>
                </Grid>
              </Grid>
            </Box>
          )}
        </DialogContent>
      </Dialog>
    </Box>
  )
}

export default PlayerAnalytics
