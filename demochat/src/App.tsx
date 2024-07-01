import { Toaster } from 'react-hot-toast'
import './App.css'
import Chat from './components/Chat'
import FineTune from './components/FineTune'
import { Route, Routes } from 'react-router-dom'

function App() {

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
