import os
import json
from langchain_community.document_loaders import CSVLoader
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI


api_key = "sk-proj-2sHF2xEZiznorUs4TMd3T3BlbkFJl9c9z1PspIx0udBsDHHI"


def openAi():
    embedding_function = OpenAIEmbeddings(api_key=api_key, model="gpt-3.5-turbo")

    loader = CSVLoader("./apartment_data.csv", encoding="utf-8")
    documents = loader.load()

    db = Chroma.from_documents(documents, embedding_function)
    retriever = db.as_retriever()

    template = """Answer the question based only on the following context:
    {context}

    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    model = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo",
                       max_tokens=100, temperature=0.5)

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

    print(chain.invoke("What bank failed in North Carolina?"))


openAi()

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

        return "response"

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


openAi()
