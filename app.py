import analyzer
from flask import Flask, request, jsonify

app = Flask(__name__)


INITIAL_MESSAGE = "Hello, I am iChatBot."
DEFAULT_RESPONSE = "We are friends forever!"
CHAT_MESSAGE = "chat_message"
CHAT_RESPONSE = "chat_response"


@app.route('/')
def hello_world():
    return 'Hello this is IChatBot!'


@app.route('/chat', methods=["GET", "POST"])
def chat_service():
    response = {}
    if request.method == "GET":
        response['default'] = INITIAL_MESSAGE
    else:
        req_data = request.get_json()
        message = req_data[CHAT_MESSAGE]
        res_msg = analyzer.generate_response(message)
        if len(res_msg) == 0:
            res_msg = DEFAULT_RESPONSE
        response[CHAT_RESPONSE] = res_msg
    return jsonify(response)


@app.route('/train/chat')
def train_chat_service():
    return ""


@app.route('/train/class')
def train_class_service():
    return ""


if __name__ == '__main__':
    app.run()
