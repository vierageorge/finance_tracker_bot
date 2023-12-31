import os
import telebot
from dotenv import load_dotenv
from utils.validations import is_valid_user, is_valid_expense_message
from utils.persist import get_total_debt, get_monthly_expenses
from utils.message_processing import get_expense_components
from utils.messages import GREETING_MESSAGE, NOT_VALID_USER_MESSAGE, HELP_MESSAGE
from models.expense import Expense
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

@bot.message_handler(commands=['debt'], func=is_valid_user)
def send_total(message: telebot.types.Message) -> None:
  total_debt = get_total_debt()
  bot.send_message(message.chat.id, f"Total debt: {total_debt}")

@bot.message_handler(commands=['monthly'], func=is_valid_user)
def send_monthly_expenses(message: telebot.types.Message) -> None:
  monthly_expenses_status = f"<b>Monthly expenses</b>\n\n{get_monthly_expenses()}"
  bot.send_message(message.chat.id, monthly_expenses_status, parse_mode='HTML')

@bot.message_handler(commands=['help'], func=is_valid_user)
def send_help_message(message: telebot.types.Message) -> None:
  bot.send_message(message.chat.id, HELP_MESSAGE)

@bot.message_handler(func=is_valid_user)
def handle_message(message: telebot.types.Message) -> None:
  if not is_valid_expense_message(message.text):
    bot.reply_to(message, "Sorry, I don't understand. /help for more info.")
    return
  media, description, value = get_expense_components(message.text)
  
  expense = Expense(media, description, value)  # Instantiate a new Expense object
  expense.save()
  bot.reply_to(message, f"Expense saved!\n{expense}")

bot.infinity_polling()