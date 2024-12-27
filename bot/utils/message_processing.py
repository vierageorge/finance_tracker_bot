import re
import logging

def get_expense_components(text: str) -> tuple:
  """
  Extracts the value, media, and description components from the given text.

  Args:
    text (str): The input text containing the expense components.

  Returns:
    tuple: A tuple containing the extracted value, media, and description components.
  """
  pattern = r'^([+-]?)(\d{1,6})\s(.+)'
  match = re.match(pattern, text)
  sign = 1 if match.group(1) == '+' else -1
  value = sign * int(match.group(2)) * 1000
  description = match.group(3)
  return (description, value)