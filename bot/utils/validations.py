import os
import telebot
from dotenv import load_dotenv

load_dotenv()
VALID_USER = os.environ.get('VALID_USER')

def isValidUser(message: telebot.types.Message) -> bool:
  """
  Check if the user is a valid user.

  Args:
    message (telebot.types.Message): The message object.

  Returns:
    bool: True if the user is valid, False otherwise.
  """
  return message.from_user.username == VALID_USER