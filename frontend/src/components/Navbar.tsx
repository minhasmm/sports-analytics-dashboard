import React from 'react'
import {
  AppBar,
  Toolbar,
  Typography,
  IconButton,
  InputBase,
  Box,
  Menu,
  MenuItem,
  Avatar,
} from '@mui/material'
import {
  Menu as MenuIcon,
  Search as SearchIcon,
  Brightness4 as DarkModeIcon,
  Brightness7 as LightModeIcon,
  Notifications as NotificationsIcon,
  AccountCircle as ProfileIcon,
} from '@mui/icons-material'
import { styled } from '@mui/material/styles'

interface NavbarProps {
  isDarkMode: boolean
  onThemeToggle: () => void
  onMenuClick: () => void
}

const SearchContainer = styled('div')(({ theme }) => ({
  position: 'relative',
  borderRadius: theme.shape.borderRadius,
  backgroundColor: theme.palette.mode === 'dark' ? '#333' : '#f5f5f5',
  marginLeft: theme.spacing(2),
  width: '100%',
  maxWidth: '400px',
  [theme.breakpoints.down('md')]: {
    maxWidth: '200px',
  },
}))

const SearchIconWrapper = styled('div')(({ theme }) => ({
  padding: theme.spacing(0, 2),
  height: '100%',
  position: 'absolute',
  pointerEvents: 'none',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
}))

const StyledInputBase = styled(InputBase)(({ theme }) => ({
  color: 'inherit',
  '& .MuiInputBase-input': {
    padding: theme.spacing(1, 1, 1, 0),
    paddingLeft: `calc(1em + ${theme.spacing(4)})`,
    transition: theme.transitions.create('width'),
    width: '100%',
  },
}))

const Navbar: React.FC<NavbarProps> = ({ isDarkMode, onThemeToggle, onMenuClick }) => {
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null)

  const handleProfileMenuOpen = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget)
  }

  const handleMenuClose = () => {
    setAnchorEl(null)
  }

  return (
    <>
      <AppBar position="static" elevation={1}>
        <Toolbar>
          <IconButton
            color="inherit"
            edge="start"
            onClick={onMenuClick}
            sx={{ mr: 2 }}
          >
            <MenuIcon />
          </IconButton>

          {/* Logo */}
          <Typography
            variant="h6"
            sx={{
              fontWeight: 700,
              mr: 3,
              background: 'linear-gradient(45deg, #1976d2 30%, #dc004e 90%)',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent',
              cursor: 'pointer',
            }}
          >
            🏆 Sports Analytics
          </Typography>

          {/* Search Bar */}
          <SearchContainer>
            <SearchIconWrapper>
              <SearchIcon />
            </SearchIconWrapper>
            <StyledInputBase
              placeholder="Search players, teams..."
              inputProps={{ 'aria-label': 'search' }}
            />
          </SearchContainer>

          {/* Right side icons */}
          <Box sx={{ flexGrow: 1 }} />
          
          <IconButton color="inherit" onClick={onThemeToggle}>
            {isDarkMode ? <LightModeIcon /> : <DarkModeIcon />}
          </IconButton>

          <IconButton color="inherit">
            <NotificationsIcon />
          </IconButton>

          <IconButton color="inherit" onClick={handleProfileMenuOpen}>
            <ProfileIcon />
          </IconButton>
        </Toolbar>
      </AppBar>

      {/* Profile Menu */}
      <Menu
        anchorEl={anchorEl}
        open={Boolean(anchorEl)}
        onClose={handleMenuClose}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
        transformOrigin={{ vertical: 'top', horizontal: 'right' }}
      >
        <MenuItem onClick={handleMenuClose}>👤 Profile</MenuItem>
        <MenuItem onClick={handleMenuClose}>⚙️ Settings</MenuItem>
        <MenuItem onClick={handleMenuClose}>📊 Preferences</MenuItem>
        <MenuItem onClick={handleMenuClose}>📞 Help</MenuItem>
        <MenuItem onClick={handleMenuClose}>🚪 Logout</MenuItem>
      </Menu>
    </>
  )
}

export default Navbar
