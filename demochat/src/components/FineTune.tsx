import { useEffect, useState } from "react"
import "../styles/fineTune.css"
import { fineTuneType, getfineTune, setfineTune } from "../services/fineTune"

const initState: fineTuneType = {
  prompt: "",
  maxToken: 0,
  temperature: 0,
  maxCharacters: 0,
  eroor: ""
}

export default function FineTune() {
  const [fineTune, setFineTune] = useState<fineTuneType>(initState)

  useEffect(() => {
    getfineTune().then(response => {
      setFineTune(response)
    }).catch(error => {
      console.log(error)
    })
  }, [])

  const handleChange = (e: React.ChangeEvent<HTMLTextAreaElement> | React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.name === "rate")
      setFineTune({
        ...fineTune,
        rate: {
          ...fineTune.rate,
          [e.target.name as string]: +(e.target.value || 0)
        }
      })
    else
      setFineTune({
        ...fineTune,
        [e.target.name]: e.target.value
      })
  }

  const handleSubmit = async () => {
    setfineTune(fineTune).then(response => {
      console.log(response)
    }).catch(error => {
      console.log(error)
    })
  }

  return (
    <div className="fine_tune">
      <form action="" onSubmit={handleSubmit}>
        <textarea onChange={handleChange} name="prompt" cols={30} rows={10} placeholder="enter fine tune prompt" value={fineTune?.prompt} />
        <div>
          <label htmlFor="maxToken">Max Token</label>
          <input onChange={handleChange} type="range" name="maxToken" value={fineTune.maxToken} max={10000} min={100} />
          <p>Defines the maximum number of tokens (words or characters) in the response. : {fineTune.maxToken}</p>
        </div>
        <div>
          <label htmlFor="temperature">Temperature</label>
          <input onChange={handleChange} type="range" name="temperature" value={fineTune.temperature} max={100} min={0} />
          <p>Controls the randomness of the response. Lower values make the model more deterministic. : {fineTune.temperature}</p>
        </div>
        <div>
          <label htmlFor="maxCharacters">Max Characters</label>
          <input onChange={handleChange} type="range" name="maxCharacters" value={fineTune.maxCharacters} max={1000} min={100} />
          <p>Defines the maximum number of characters allowed in the response. : {fineTune.maxCharacters}</p>
        </div>
        <div>
          <h3>
            This is the rate at which the model will charge for the number of bedrooms in the house. The model will charge the rate for the number of bedrooms in the appartment.
          </h3>
          <div>
            <input onChange={handleChange} type="range" name="1BD" value={fineTune.rate?.["1BD"]} max={10000} min={10} />
            <label>1BD : $ {fineTune.rate?.["1BD"]}</label>
          </div>

          <div>
            <input onChange={handleChange} type="range" name="2BD" value={fineTune.rate?.["2BD"]} max={10000} min={10} />
            <label>2BD : $ {fineTune.rate?.["2BD"]}</label>
          </div>

          <div>
            <input onChange={handleChange} type="range" name="3BD" value={fineTune.rate?.["3BD"]} max={10000} min={10} />
            <label>3BD : $ {fineTune.rate?.["3BD"]}</label>
          </div>
        </div>

        <button onClick={handleSubmit} type="button">Update</button>
      </form>
    </div>
  )
}
