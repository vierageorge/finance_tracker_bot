
from utils.persist import save_expense
from datetime import datetime

default_media = 'RappiCard'

media_mapping = {
  'e': 'Efectivo',
  'r': default_media
}

class Expense:
  def __init__(self, description: str, value: int, media: str = None, date: str = None, category: str = None):
    self.description = description
    self.value = value

    self.media = media_mapping.get(media, default_media)
    self.paid = 'FALSE' if self.media == default_media else None
    
    self.date = date if date else datetime.now().strftime("%Y/%m/%d")
    self.category = category

  def save(self):
    save_expense(self.media, self.description, self.value, self.date, self.paid)
