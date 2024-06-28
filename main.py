from flask import Flask, request, jsonify
from openAi import openAiChat

app = Flask(__name__)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    response = openAiChat(data)
    return jsonify({"message": response})


app.run(port=5000, debug=True)