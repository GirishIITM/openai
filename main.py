from flask import Flask, request, jsonify
from openAi import openAiChat
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    response = openAiChat(data)
    return jsonify({"message": response})


app.run(port=5000, debug=True)
