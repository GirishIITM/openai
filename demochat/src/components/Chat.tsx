import React, { useEffect } from 'react'
import toast from 'react-hot-toast'
import { FaTelegramPlane } from 'react-icons/fa'
import subMitAndfetchResponse from '../services/subMitAndfetchResponse'
import '../styles/chat.css'

export default function Chat() {

    const [messages, setMessages] = React.useState<string[]>([])
    const [input, setInput] = React.useState('')

    useEffect(() => {
    }, [])

    const handleSubmit = async () => {
        if (!input) return toast.error('Please enter a message')
        setMessages([...messages, input])
        setInput('')

        subMitAndfetchResponse({ userId: 'gir123', prompt: input })
            .then(response => {
                setMessages([...messages, response])
            })
            .catch(error => {
                setMessages([...messages, 'Error: ' + error])
            })
    }

    return (
        <div className='chat'>
            <div className="chats">
                {messages.map((message, index) => (
                    <div key={index} className="message">
                        <p>{message}</p>
                    </div>
                ))}
            </div>
            <div className="input_box">
                <textarea name="" id="" placeholder='Enter the prompt, CTRL + Enter to send'
                    onKeyDown={e => (e.key === 'Enter' && e.ctrlKey) && handleSubmit()}
                    value={input} onChange={(e) => setInput(e.target.value)} />
                <button onClick={handleSubmit}><FaTelegramPlane /></button>
            </div>
        </div>
    )
}
