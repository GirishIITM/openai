import React, { useEffect } from 'react'
import toast from 'react-hot-toast'
import { FaTelegramPlane } from 'react-icons/fa'
import subMitAndfetchResponse from '../services/subMitAndfetchResponse'
import '../styles/chat.css'

export default function Chat() {

    const [messages, setMessages] = React.useState<string[]>([])
    const [input, setInput] = React.useState('')
    const inputRef = React.useRef<HTMLInputElement>(null)


    const handleSubmit = async () => {
        if (!input) return toast.error('Please enter a message')
        setMessages(messages => [...messages, input])
        setInput('')

        subMitAndfetchResponse({ userId: inputRef.current?.value || "girish", prompt: input })
            .then(response => {
                setMessages(messages => [...messages, response])
            })
            .catch(error => {
                setMessages(messages => [...messages, 'Error: ' + error])
            })
    }

    return (
        <div className='chat'>
            <div>
                <input ref={inputRef} type="text" placeholder='your name' />
            </div>
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
