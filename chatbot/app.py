# chatbot/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import asyncio

from chat_engine import generate_response

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '')
        if not message:
            return jsonify({'error': 'No message provided'}), 400

        # Run async response generation
        response = asyncio.run(generate_response(message))

        return jsonify({'response': response})
    except Exception as e:
        print("API Error:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
