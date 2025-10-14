import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
// import './index.css'
import App from './App.jsx'
import Appx from './components/hooks/hooks.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
    <Appx />
  </StrictMode>,
)
