from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/v1/chat/completions', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])
    last_message = messages[-1]['content'] if messages else ""
    
    response = {
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": f"Lab 8: Software Engineering Toolkit Lab 8"
            },
            "finish_reason": "stop"
        }]
    }
    return jsonify(response)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/v1/models', methods=['GET'])
def models():
    return jsonify({"data": [{"id": "coder-model"}]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
