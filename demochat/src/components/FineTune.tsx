
import { useEffect, useState } from "react"
import "../styles/fineTune.css"
import { fineTuneType, getfineTune } from "../services/fineTune"

export default function FineTune() {

  const [fineTune, setFineTune] = useState<fineTuneType>({
    prompt: "",
    maxToken: 0,
    temperature: 0,
    topP: 0,
    maxCharacters: 0,
    eroor: ""
  })

  useEffect(() => {
    getfineTune().then(response => {
      console.log(response)
      setFineTune(response)
    }).catch(error => {
      console.log(error)
    })
  }, [])

  return (
    <div className="fine_tune">
      <textarea name="" id="">{fineTune?.prompt}</textarea>
      <button>submit</button>
    </div>
  )
}
