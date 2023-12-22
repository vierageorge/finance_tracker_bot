import re

def get_expense_components(text: str) -> tuple:
  """
  Extracts the value, media, and description components from the given text.

  Args:
    text (str): The input text containing the expense components.

  Returns:
    tuple: A tuple containing the extracted value, media, and description components.
  """
  pattern = r'^(\d{3,8})([re]?)(.*)'
  match = re.match(pattern, text)
  value = int(match.group(1))
  media = match.group(2)
  description = match.group(3)
  return (media, description, value)