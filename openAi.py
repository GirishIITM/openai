import os
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


def openAi(query):
    embedding_function = OpenAIEmbeddings(api_key=api_key)

    loader = CSVLoader("./apartment_data.csv", encoding="utf-8")
    documents = loader.load()

    db = Chroma.from_documents(
        documents, embedding_function, persist_directory="./chroma")
    retriever = db.as_retriever()

    template = """
    here is the rate for the apartments as per number of beds in dollars:
    {data.rate}
    {data.promt}

    """
    prompt = ChatPromptTemplate.from_template(template)

    model = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo",
                       max_tokens=1000, temperature=0.5)

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

    response = chain.invoke(query)
    return response


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
        historyPrompts = chatHistory["messages"].join("\n")
        completePrompt = (historyPrompts + prompt).slice(0, data.maxChars)
        return "response"

    except Exception as e:
        print(e)
        return "internal server error"


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
