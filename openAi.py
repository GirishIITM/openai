import traceback
import json
from langchain_community.document_loaders import CSVLoader
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from db import client

api_key = "sk-proj-2sHF2xEZiznorUs4TMd3T3BlbkFJl9c9z1PspIx0udBsDHHI"

messages = {}
data = {}

try:
    f = open("fineTune.json", "r")
    data = json.loads(f.read())
    f.close()
except Exception as e:
    print(e)
    traceback.print_exc()


def openAi(query):
    try:
        embedding_function = OpenAIEmbeddings(api_key=api_key)

        loader = CSVLoader("./apartment_data.csv", encoding="utf-8")
        documents = loader.load()

        db = Chroma.from_documents(
            documents, embedding_function, persist_directory="./chroma")
        retriever = db.as_retriever()
        rate = data.get("rate", {
            "1BD": 2200,
            "2BD": 2650,
            "3BD": 2850
        })
        rate_string = ', '.join(f'{key}: {value}' for key, value in rate.items())
        prompt = data.get("prompt", "Hi! Thanks for reaching out to XYZ Realty about our apartments for rent. I'm on the other line and will call you back soon.\nWhich property are you reaching out about?\n[User provides the property name]\nGot it. We'll call you back soon. What's your name?\n[If user already provided name earlier] Got it. We'll call you back soon.\nThanks. Do you mind sharing if there are any special amenities you are looking for or any other requirements?\n[If user asks about amenities, price, availability, minimum credit, or income]\n[Look up the information on the Google Sheet]\nGot it. Our team will be with you shortly.\nPlease can you also share your income and credit so we can verify that your application would be accepted? We have many options for apartments in this area, and if this building doesn't work for you we can perhaps help you with an apartment somewhere else.\n[If the user shares their income and credit, look up the sheet to see if they are eligible]\nGreat! Your income and credit meet the requirements of the application process for this building. I'll give you a call shortly.",)
        template = "here is the rate for the apartments as per number of beds in dollars: \n" + rate_string +"\n" 
        + "and this is some of example responses and guidence how should be your response if user asks any query just directly answer other wise follow below instrouctions" 
        + prompt

        model = ChatOpenAI(
            api_key=api_key, model="gpt-3.5-turbo",
            max_tokens=data.get("maxTokens", 1000),
            temperature=data.get("temperature", 1000))

        chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | template
            | model
            | StrOutputParser()
        )

        response = chain.invoke(query)
        return response
    except Exception as e:
        print(e)
        traceback.print_exc()
        return "internal server error"


def openAiChat(req):
    try:
        userId = req["userId"]
        prompt = req["prompt"]
        db = client['user_db']
        collection = db['chat_history']

        chatHistory = collection.find_one({"userId": userId})
        if chatHistory == None:
            chat = {
                'userId': userId,
                'messages': [prompt]
            }
            collection.insert_one(chat)
            chatHistory = chat
            chatHistory["messages"] = []
        else:
            collection.update_one({"userId": userId}, {
                                  "$push": {"messages": prompt}})
        historyPrompts = "\n".join(chatHistory["messages"])
        completePrompt = (
            historyPrompts + prompt)[0: int(data["maxCharacters"]) or 1000]
        response = openAi(completePrompt)
        return response

    except Exception as e:
        print(e)
        traceback.print_exc()
        return "internal server error"


def setfineTune(details):
    try:
        f = open("fineTune.json", "w")
        f.write(json.dumps(details))
        f.close()
        return "fine tune set"
    except Exception as e:
        print(e)
        traceback.print_exc()
        return "internal server error"


def getfineTune():
    try:
        return data
    except Exception as e:
        print(e)
        traceback.print_exc()
        return "internal server error"
