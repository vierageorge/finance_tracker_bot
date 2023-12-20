import os
import telebot
from dotenv import load_dotenv
from utils.validations import is_valid_user, is_valid_expense_message
from utils.message_processing import get_expense_components
from utils.messages import GREETING_MESSAGE, NOT_VALID_USER_MESSAGE, HELP_MESSAGE
import logging

# Load .env file and get the bot token
load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message: telebot.types.Message) -> None:
  if not is_valid_user(message):
    logging.warning(f"Unauthorized user: {message.from_user} | {message.text}")
    bot.send_message(message.chat.id, NOT_VALID_USER_MESSAGE)
    return
  bot.send_message(message.chat.id, GREETING_MESSAGE)

@bot.message_handler(commands=['help'], func=is_valid_user)
def sned_help_message(message: telebot.types.Message) -> None:
  bot.send_message(message.chat.id, HELP_MESSAGE)

@bot.message_handler(func=is_valid_user)
def handle_message(message: telebot.types.Message) -> None:
  if not is_valid_expense_message(message.text):
    bot.reply_to(message, "Sorry, I don't understand.")
    return
  value, media, description = get_expense_components(message.text)
  bot.reply_to(message, f"Value: {value}\nMedia: {media}\nDescription: {description}")

bot.infinity_polling()