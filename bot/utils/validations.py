import os
import telebot
from dotenv import load_dotenv
import re

load_dotenv()
VALID_USER = os.environ.get('VALID_USER')

def is_valid_user(message: telebot.types.Message) -> bool:
  """
  Check if the user is a valid user.

  Args:
    message (telebot.types.Message): The message object.

  Returns:
    bool: True if the user is valid, False otherwise.
  """
  return message.from_user.username == VALID_USER

def is_valid_expense_message(message: str) -> bool:
  """
  Check if the given message is a valid expense message.

  Args:
    message (str): The message to be validated.

  Returns:
    bool: True if the message is valid, False otherwise.
  """

  pattern = r'^([+-]?)(\d{1,6})\s(.+)'
  return re.match(pattern, message) is not None