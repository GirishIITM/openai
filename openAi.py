from openai import OpenAI
import json

client = OpenAI(
    api_key="sk-proj-O9lg3fmlnmx2WPP9VOWqT3BlbkFJSczlQbEjPwbEEsMgR9Te",
)

messages = {}
data = {}

try:
    f = open("fineTune.json", "r")
    data = f.read()
    f.close()
except Exception as e:
    print(e)


def openAiChat(data):
    try:
        userId = data["userId"]
        prompt = data["prompt"]
        prompt = prompt + data["prompt"]
        content = {
            "role": "user",
            "content": prompt
        }

        agent = create_csv_agent(
            OpenAI(temperature=0),
            "titanic.csv",
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        )

    except Exception as e:
        print(e)
        return "internal server error"


openAiChat({
    "userId": "girish",
    "prompt": "say hello"
})


def setfineTune(details):
    try:
        f = open("fineTune.json", "w")
        f.write(json.dumps(details))
        f.close()
        return "fine tune set"
    except Exception as e:
        print(e)
        return "internal server error"


def getfineTune():
    try:
        return json.loads(data)
    except Exception as e:
        print(e)
        return "internal server error"
