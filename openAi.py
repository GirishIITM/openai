from openai import OpenAI

client = OpenAI(
    api_key="sk-proj-O9lg3fmlnmx2WPP9VOWqT3BlbkFJSczlQbEjPwbEEsMgR9Te",
)

messages = {}


def openAiChat(data):
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
        print(response)[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ]
        return response

    except Exception as e:
        print(e)


openAiChat({
    "userId": "girish",
    "prompt": "say hello"
})
