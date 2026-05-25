import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { ThemeProvider, createTheme } from '@mui/material/styles'
import CssBaseline from '@mui/material/CssBaseline'

const theme = createTheme({
  palette: {
    primary: { main: '#1976d2' },
    secondary: { main: '#dc004e' },
  },
})

export default function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <div className="app">
          <h1>🏆 Sports Analytics Dashboard</h1>
          <p>Welcome! This is your main dashboard.</p>
          <Routes>
            <Route path="/" element={<div>Home Page</div>} />
          </Routes>
        </div>
      </Router>
    </ThemeProvider>
  )
}
