import os
import telebot
from dotenv import load_dotenv
from flask import Flask, request, jsonify
load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

app = Flask(__name__)

# Load .env file and get the bot token


bot = telebot.TeleBot(BOT_TOKEN)

def send_message(message: str) -> None:
  bot.send_message(1765717834, message)


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

if __name__ == '__main__':
  app.run(debug=True)

