from flask import Flask, request, jsonify
from openAi import openAiChat, getfineTune, setfineTune
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from db import client

uri = "mongodb+srv://gir:1@cluster0.ajxxi2q.mongodb.net/?appName=Cluster0"

app = Flask(__name__)
CORS(app)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    response = openAiChat(data)
    return jsonify({"message": response})


@app.route("/setFineTune", methods=["POST"])
def sfineTune():
    data = request.get_json()
    response = setfineTune(data)
    return jsonify({"message": response})


@app.route("/getFineTune", methods=["GET"])
def gfineTune():
    response = getfineTune()
    return jsonify(response)


if __name__ == '__main__':
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        app.run(port=5000, debug=True)
    except Exception as e:
        print(e)
