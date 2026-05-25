import React from 'react'
import { Link as RouterLink, useLocation } from 'react-router-dom'
import {
  Drawer,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Divider,
  Box,
  useTheme,
  useMediaQuery,
} from '@mui/material'
import {
  Dashboard as DashboardIcon,
  Person as PlayerIcon,
  Groups as TeamIcon,
  SportsFootball as MatchIcon,
  BarChart as StatsIcon,
  Psychology as PredictionIcon,
  Chat as ChatIcon,
  Settings as SettingsIcon,
  Help as HelpIcon,
} from '@mui/icons-material'

interface SidebarProps {
  open: boolean
  onClose: () => void
}

const menuItems = [
  { label: 'Dashboard', path: '/', icon: DashboardIcon },
  { label: 'Players', path: '/players', icon: PlayerIcon },
  { label: 'Teams', path: '/teams', icon: TeamIcon },
  { label: 'Matches', path: '/predictions', icon: MatchIcon },
  { label: 'Statistics', path: '/stats', icon: StatsIcon },
  { label: 'Predictions', path: '/predictions', icon: PredictionIcon },
  { label: 'Chatbot', path: '/chatbot', icon: ChatIcon },
]

const bottomMenuItems = [
  { label: 'Settings', path: '/settings', icon: SettingsIcon },
  { label: 'Help', path: '/help', icon: HelpIcon },
]

const Sidebar: React.FC<SidebarProps> = ({ open, onClose }) => {
  const location = useLocation()
  const theme = useTheme()
  const isMobile = useMediaQuery(theme.breakpoints.down('md'))

  const drawer = (
    <Box sx={{ width: 250, display: 'flex', flexDirection: 'column', height: '100%' }}>
      {/* Logo Area */}
      <Box sx={{ p: 2 }}>
        <Typography variant="h6" sx={{ fontWeight: 700, color: 'primary.main' }}>
          🏆 Sports
        </Typography>
      </Box>

      <Divider />

      {/* Main Menu */}
      <List sx={{ flex: 1 }}>
        {menuItems.map((item) => {
          const Icon = item.icon
          const isActive = location.pathname === item.path

          return (
            <ListItem key={item.path} disablePadding>
              <ListItemButton
                component={RouterLink}
                to={item.path}
                selected={isActive}
                sx={{
                  backgroundColor: isActive ? 'primary.light' : 'transparent',
                  color: isActive ? 'primary.main' : 'inherit',
                  '&:hover': {
                    backgroundColor: 'action.hover',
                  },
                }}
              >
                <ListItemIcon
                  sx={{
                    color: isActive ? 'primary.main' : 'inherit',
                    minWidth: 40,
                  }}
                >
                  <Icon />
                </ListItemIcon>
                <ListItemText primary={item.label} />
              </ListItemButton>
            </ListItem>
          )
        })}
      </List>

      <Divider />

      {/* Bottom Menu */}
      <List>
        {bottomMenuItems.map((item) => {
          const Icon = item.icon

          return (
            <ListItem key={item.path} disablePadding>
              <ListItemButton component={RouterLink} to={item.path}>
                <ListItemIcon sx={{ minWidth: 40 }}>
                  <Icon />
                </ListItemIcon>
                <ListItemText primary={item.label} />
              </ListItemButton>
            </ListItem>
          )
        })}
      </List>
    </Box>
  )

  return (
    <Drawer
      variant={isMobile ? 'temporary' : 'permanent'}
      open={open}
      onClose={onClose}
      sx={{
        width: 250,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: 250,
          boxSizing: 'border-box',
          mt: '64px',
          height: 'calc(100vh - 64px)',
        },
      }}
    >
      {drawer}
    </Drawer>
  )
}

import { Typography } from '@mui/material'

export default Sidebar
