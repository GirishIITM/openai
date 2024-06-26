import openai


def openAiChat(data):
    response = openai.Completion.create(
        engine="davinci",
        prompt=data["message"],
        max_tokens=100
    )
    openai.api_key
