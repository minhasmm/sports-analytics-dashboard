import React, { useState, useEffect } from 'react'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import { ThemeProvider, createTheme, CssBaseline } from '@mui/material'
import Navbar from './components/Navbar'
import Sidebar from './components/Sidebar'
import Home from './pages/Home'
import PlayerAnalytics from './pages/PlayerAnalytics'
import TeamPerformance from './pages/TeamPerformance'
import MatchPredictions from './pages/MatchPredictions'
import LeagueStats from './pages/LeagueStats'
import ChatbotPage from './pages/ChatbotPage'
import './App.css'

const App: React.FC = () => {
  const [isDarkMode, setIsDarkMode] = useState(false)
  const [sidebarOpen, setSidebarOpen] = useState(true)

  // Theme configuration
  const theme = createTheme({
    palette: {
      mode: isDarkMode ? 'dark' : 'light',
      primary: {
        main: '#1976d2',
        light: '#42a5f5',
        dark: '#1565c0',
      },
      secondary: {
        main: '#dc004e',
        light: '#ff5983',
        dark: '#9a0036',
      },
      success: {
        main: '#4caf50',
      },
      error: {
        main: '#f44336',
      },
      warning: {
        main: '#ff9800',
      },
      info: {
        main: '#2196f3',
      },
      background: {
        default: isDarkMode ? '#121212' : '#f5f5f5',
        paper: isDarkMode ? '#1e1e1e' : '#ffffff',
      },
    },
    typography: {
      fontFamily: [
        '-apple-system',
        'BlinkMacSystemFont',
        '"Segoe UI"',
        'Roboto',
        '"Helvetica Neue"',
        'Arial',
        'sans-serif',
      ].join(','),
      h1: {
        fontSize: '2.5rem',
        fontWeight: 700,
        marginBottom: '1rem',
      },
      h2: {
        fontSize: '2rem',
        fontWeight: 600,
        marginBottom: '0.8rem',
      },
      h3: {
        fontSize: '1.5rem',
        fontWeight: 600,
      },
    },
    shape: {
      borderRadius: 8,
    },
  })

  // Load theme preference
  useEffect(() => {
    const savedTheme = localStorage.getItem('theme')
    if (savedTheme) {
      setIsDarkMode(savedTheme === 'dark')
    }
  }, [])

  // Save theme preference
  const toggleTheme = () => {
    const newMode = !isDarkMode
    setIsDarkMode(newMode)
    localStorage.setItem('theme', newMode ? 'dark' : 'light')
  }

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen)
  }

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <div className="app-container">
          <Navbar 
            isDarkMode={isDarkMode}
            onThemeToggle={toggleTheme}
            onMenuClick={toggleSidebar}
          />
          <div className="app-body">
            <Sidebar open={sidebarOpen} onClose={() => setSidebarOpen(false)} />
            <main className="app-main">
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/players" element={<PlayerAnalytics />} />
                <Route path="/teams" element={<TeamPerformance />} />
                <Route path="/predictions" element={<MatchPredictions />} />
                <Route path="/stats" element={<LeagueStats />} />
                <Route path="/chatbot" element={<ChatbotPage />} />
                <Route path="*" element={<Navigate to="/" replace />} />
              </Routes>
            </main>
          </div>
        </div>
      </Router>
    </ThemeProvider>
  )
}

export default App
