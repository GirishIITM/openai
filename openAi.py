from openai import OpenAI
import json

client = OpenAI(
    api_key="sk-proj-O9lg3fmlnmx2WPP9VOWqT3BlbkFJSczlQbEjPwbEEsMgR9Te",
)

messages = {}


def openAiChat(data):
    return "Hello"
    try:
        userId = data["userId"]
        prompt = data["prompt"]
        content = {
            "role": "user",
            "content": prompt
        }

        if (messages[userId]):
            messages[userId].append(content)
        else:
            messages[userId] = [content]

        chat_completion = client.chat.completions.create(
            messages=messages[userId],
            model="gpt-3.5-turbo",
        )

        response = chat_completion.choices[0].message.content
        print(response)
        return response

    except Exception as e:
        print(e)


openAiChat({
    "userId": "girish",
    "prompt": "say hello"
})


def setfineTune(details):
    try:
        f = open("fineTune.json", "w")
        f.write(json.dumps(details))
        f.close()
    except Exception as e:
        print(e)
        return "internal server error"


def getfineTune():
    try:
        f = open("fineTune.json", "r")
        data = f.read()
        f.close()
        return json.loads(data)
    except Exception as e:
        print(e)
        return "internal server error"
