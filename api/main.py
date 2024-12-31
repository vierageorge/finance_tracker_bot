import os
import telebot
from dotenv import load_dotenv
from flask import Flask, request, jsonify
load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
VALID_API_KEY = os.environ.get('VALID_API_KEY')

app = Flask(__name__)

# Load .env file and get the bot token


bot = telebot.TeleBot(BOT_TOKEN)

def send_message(message: str) -> None:
  bot.send_message(CHAT_ID, message)



def is_valid_api_key(key):
  return key == VALID_API_KEY

@app.before_request
def check_api_key():
  api_key = request.headers.get("x-api-key")
  if not api_key or not is_valid_api_key(api_key):
    return jsonify({"error": "Unauthorized"}), 401


@app.route('/send', methods=['POST'])
def send():
  try:
    # Parse the JSON body
    data = request.get_json()

    if not data or 'message' not in data:
      return jsonify({"error": "Invalid request"}), 400

    message = data['message']

    # Call the send_message method
    send_message(message)
    return jsonify({"status": "Message sent successfully"}), 200

  except Exception as e:
    return jsonify({"error": str(e)}), 500
  
@app.route('/health', methods=['GET'])
def health():
  return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
  app.run(debug=True)

