from utils.api import save_money_transfer

class MoneyTransfer:
  def __init__(self, description: str, value: int, category: str = None):
    self.description = description
    self.value = value
    self.category = category

  def save(self):
    save_money_transfer(self.description, self.value, self.category)

  def __str__(self):
    return f"Value: {self.value}\nDescription: {self.description}\nCategory: {self.category}"
