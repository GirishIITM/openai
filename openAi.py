import openai

openai.api_key = 'your-api-key'

prompt = "Once upon a time,"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci", 
        prompt=prompt,
        max_tokens=150  
    )
    return response['choices'][0]['text'].strip()

prompt += " there was a wizard who..."
response1 = generate_response(prompt)
print("Response 1:", response1)

prompt += f" {response1} He used his powers to..."
response2 = generate_response(prompt)
print("Response 2:", response2)
