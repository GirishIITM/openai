import { Toaster } from 'react-hot-toast'
import './App.css'
import Chat from './components/Chat'
import FineTune from './components/FineTune'
import { Route, Routes } from 'react-router-dom'
import axios from 'axios'
import { useEffect } from 'react'

function App() {

  useEffect(() => {
    axios.defaults.baseURL = "http://127.0.0.1:5000";
  }, [])

  return (
    <>
      <Routes>
        <Route path="/" element={<Chat />} />
        <Route path="/chat" element={<Chat />} />
        <Route path='/fineTune' element={<FineTune />} />
      </Routes>
      <Toaster />
    </>
  )
}

export default App
