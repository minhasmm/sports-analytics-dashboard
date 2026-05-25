import React from 'react'
import { Box, Typography, Paper, Grid, Card, CardContent, Chip, LinearProgress } from '@mui/material'

const MatchPredictions: React.FC = () => {
  const predictions = [
    {
      id: 1,
      home: 'Manchester City',
      away: 'Liverpool',
      prediction: 'Man City',
      confidence: 0.78,
      probHome: 0.55,
      probDraw: 0.25,
      probAway: 0.20,
    },
    {
      id: 2,
      home: 'Arsenal',
      away: 'Chelsea',
      prediction: 'Arsenal',
      confidence: 0.72,
      probHome: 0.60,
      probDraw: 0.20,
      probAway: 0.20,
    },
  ]

  return (
    <Box>
      <Typography variant="h3" sx={{ mb: 3 }}>
        🎯 Match Predictions
      </Typography>

      <Grid container spacing={2}>
        {predictions.map((pred) => (
          <Grid item xs={12} md={6} key={pred.id}>
            <Card>
              <CardContent>
                <Typography variant="h6" sx={{ mb: 2 }}>
                  {pred.home} vs {pred.away}
                </Typography>
                <Box sx={{ mb: 2 }}>
                  <Chip label={`🏆 Winner: ${pred.prediction}`} color="primary" />
                  <Chip label={`${(pred.confidence * 100).toFixed(0)}% Confidence`} sx={{ ml: 1 }} />
                </Box>
                <Typography variant="body2" color="textSecondary" sx={{ mb: 1 }}>
                  Win Probabilities:
                </Typography>
                <Box sx={{ mb: 1 }}>
                  <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.5 }}>
                    <Typography variant="body2">{pred.home}</Typography>
                    <Typography variant="body2">{(pred.probHome * 100).toFixed(0)}%</Typography>
                  </Box>
                  <LinearProgress variant="determinate" value={pred.probHome * 100} />
                </Box>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Box>
  )
}

export default MatchPredictions
