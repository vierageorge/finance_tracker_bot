import os
import telebot
from dotenv import load_dotenv
from utils.validations import is_valid_user, is_valid_expense_message
from utils.message_processing import get_expense_components
from utils.messages import GREETING_MESSAGE, NOT_VALID_USER_MESSAGE, HELP_MESSAGE
from utils.ai_data_extractor import analyze_image
from models.simple_expense import SimpleExpense
from models.money_transfer import MoneyTransfer
import logging
import json

# Load .env file and get the bot token
load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=is_valid_user, content_types=['photo'])
def handle_photo(message: telebot.types.Message) -> None:
  file_url = bot.get_file_url(message.photo[-1].file_id)
  image_details = analyze_image(file_url, message.caption)
  print(image_details)
  amount = image_details.get('amount')
  category = image_details.get('category')
  if amount is None or category is None:
    bot.reply_to(message, "Sorry, I couldn't extract the amount or category from the image.")
    return
  money_transfer = MoneyTransfer(message.caption, amount, category)
  money_transfer.save()
  bot.reply_to(message, f"Got a transfer!\n{money_transfer}")

@bot.message_handler(func=is_valid_user)
def handle_message(message: telebot.types.Message) -> None:
  if not is_valid_expense_message(message.text):
    # bot.reply_to(message, "Sorry, I don't understand. /help for more info.")
    bot.reply_to(message, "Invalid message format.")
    return
  description, value = get_expense_components(message.text)
  
  expense = SimpleExpense(description, value)  # Instantiate a new Expense object
  expense.save()
  bot.reply_to(message, f"Expense saved!\n{expense}")

bot.infinity_polling()