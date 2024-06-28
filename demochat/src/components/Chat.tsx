import React, { useEffect } from 'react'
import toast from 'react-hot-toast'
import { FaTelegramPlane } from 'react-icons/fa'

export default function Chat() {

    const [messages, setMessages] = React.useState<string[]>([])
    const [input, setInput] = React.useState('')

    useEffect(() => {
    }, [])

    const handleSubmit = () => {
        if (!input) return toast.error('Please enter a message')
        setMessages([...messages, input])
        setInput('')
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
                <textarea name="" id="" placeholder='Enter the prompt'
                    onKeyDown={e => (e.key === 'Enter' && e.ctrlKey) && handleSubmit()}
                    value={input} onChange={(e) => setInput(e.target.value)} />
                <button onClick={handleSubmit}><FaTelegramPlane /></button>
            </div>
        </div>
    )
}
