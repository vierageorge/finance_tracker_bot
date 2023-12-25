
from utils.persist import save_expense
from utils.ai_classifier import get_category
from datetime import datetime, timezone, timedelta

timezone_offset = -5.0
tzinfo = timezone(timedelta(hours=timezone_offset))
default_media = 'RappiCard'

media_mapping = {
  'e': 'Efectivo',
  'd': 'Débito',
  'r': default_media
}

class Expense:
  def __init__(self, media: str, description: str, value: int, date: str = None):
    self.description = description
    self.value = value

    self.media = media_mapping.get(media, default_media)
    self.paid = 'FALSE' if self.media == default_media else None
    
    self.date = date if date else datetime.now(tzinfo).strftime("%Y/%m/%d")
    self.category = None
    self.set_category()

  def set_category(self):
    self.category = get_category(self.description)

  def save(self):
    save_expense(self.media, self.description, self.value, self.date, self.paid, self.category)

  def __str__(self):
    return f"Value: {self.value}\nMedia: {self.media}\nDescription: {self.description}\nDate: {self.date}\nCategory: {self.category}"
