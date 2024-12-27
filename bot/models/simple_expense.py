
from utils.api import save_cash_expense

class SimpleExpense:
  def __init__(self, description: str, value: int):
    self.description = description
    self.value = value

    self.category = None

  def save(self):
    save_cash_expense(self.description, self.value)

  def __str__(self):
    return f"Value: {self.value}\nDescription: {self.description}"
