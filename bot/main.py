import os
import telebot
from dotenv import load_dotenv
from utils.validations import isValidUser
from utils.messages import GREETING_MESSAGE, NOT_VALID_USER_MESSAGE

# Load .env file and get the bot token
load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
  if not isValidUser(message):
    bot.reply_to(message, NOT_VALID_USER_MESSAGE)
    return
  bot.reply_to(message, GREETING_MESSAGE)

@bot.message_handler(func=isValidUser)
def handle_message(message: telebot.types.Message) -> None:
  bot.reply_to(message, message.text)

bot.infinity_polling()