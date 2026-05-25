import React, { useState } from 'react'
import { Box, Typography, Paper, TextField, Button, Card, CardContent, LinearProgress } from '@mui/material'
import { Send as SendIcon } from '@mui/icons-material'

interface Message {
  id: number
  text: string
  sender: 'user' | 'bot'
  timestamp: Date
}

const ChatbotPage: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 1,
      text: 'Hello! I\'m your Sports Analytics Chatbot. Ask me anything about players, teams, or predictions!',
      sender: 'bot',
      timestamp: new Date(),
    },
  ])
  const [inputValue, setInputValue] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSendMessage = () => {
    if (!inputValue.trim()) return

    // Add user message
    const newMessage: Message = {
      id: messages.length + 1,
      text: inputValue,
      sender: 'user',
      timestamp: new Date(),
    }
    setMessages([...messages, newMessage])
    setInputValue('')

    // Simulate bot response
    setLoading(true)
    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        {
          id: prev.length + 1,
          text: 'This is a sample response. Connect to the backend API for real answers!',
          sender: 'bot',
          timestamp: new Date(),
        },
      ])
      setLoading(false)
    }, 1000)
  }

  return (
    <Box>
      <Typography variant="h3" sx={{ mb: 3 }}>
        💬 Sports Chatbot
      </Typography>

      <Paper sx={{ height: '600px', display: 'flex', flexDirection: 'column', p: 2 }}>
        {/* Chat Messages */}
        <Box sx={{ flex: 1, overflow: 'auto', mb: 2 }}>
          {messages.map((msg) => (
            <Box
              key={msg.id}
              sx={{
                mb: 2,
                display: 'flex',
                justifyContent: msg.sender === 'user' ? 'flex-end' : 'flex-start',
              }}
            >
              <Card
                sx={{
                  maxWidth: '70%',
                  backgroundColor: msg.sender === 'user' ? '#1976d2' : '#f5f5f5',
                  color: msg.sender === 'user' ? 'white' : 'black',
                }}
              >
                <CardContent sx={{ py: 1, px: 2 }}>
                  <Typography variant="body2">{msg.text}</Typography>
                </CardContent>
              </Card>
            </Box>
          ))}
          {loading && <LinearProgress sx={{ mt: 2 }} />}
        </Box>

        {/* Input Area */}
        <Box sx={{ display: 'flex', gap: 1 }}>
          <TextField
            fullWidth
            placeholder="Ask me something..."
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
            disabled={loading}
          />
          <Button onClick={handleSendMessage} disabled={loading} variant="contained" sx={{ px: 3 }}>
            <SendIcon />
          </Button>
        </Box>
      </Paper>
    </Box>
  )
}

export default ChatbotPage
