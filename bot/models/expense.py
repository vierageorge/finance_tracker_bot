
from utils.persist import save_expense

default_media = 'RappiCard'

media_mapping = {
  'e': 'Efectivo',
  'r': default_media
}

class Expense:
  def __init__(self, description: str, value: int, media: str = None, date: str = None, category: str = None, paid: bool = None):
    self.description = description
    self.value = value

    self.media = media_mapping.get(media, default_media)
    self.paid = paid

    self.date = date
    self.category = category

  def save(self):
    save_expense(self.value, self.media, self.description)
