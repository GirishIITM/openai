from openai import OpenAI
import os
import json
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI, OpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent

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
        print(data)
        userId = data["userId"]
        prompt = data["prompt"]
        prompt = prompt + data["prompt"]
        content = {
            "role": "user",
            "content": prompt
        }

        agent = create_csv_agent(
            ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613",api_key="sk-proj-2sHF2xEZiznorUs4TMd3T3BlbkFJl9c9z1PspIx0udBsDHHI"),
            "apartment_data.csv",
            verbose=True,
            agent_type=AgentType.OPENAI_FUNCTIONS,
        )

        response = agent.run("how many rows are there?")
        print(response)
        return response

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
