import gspread
import os
from dotenv import load_dotenv

load_dotenv()

CRED_FILE = os.path.join(os.getcwd(), 'credentials.json')
EXPENSE_SHEET_ID = os.environ.get('SHEET_ID')
EXPENSES_SHEET_NAME = os.environ.get('SHEET_NAME')
CONFIG_SHEET_NAME = os.environ.get('CONFIG_SHEET_NAME')

sheet_service = gspread.service_account(CRED_FILE)
sheet_file = sheet_service.open_by_key(EXPENSE_SHEET_ID)
factsheet = sheet_file.worksheet(EXPENSES_SHEET_NAME)
configsheet = sheet_file.worksheet(CONFIG_SHEET_NAME)

def save_expense(media: str, description: str, value: int, date: str, paid: str, category: str):
  factsheet.append_row(['Gasto',date, category, media, description, value, paid], value_input_option='USER_ENTERED')

def get_categories():
  configs = configsheet.get("CATEGORIA_MES")
  return [config[0] for config in configs[1:] if config[1] == 'TRUE']

def get_total_debt() -> int:
  expenses = factsheet.get_all_records(value_render_option='UNFORMATTED_VALUE')
  return sum([expense['Valor'] for expense in expenses if expense['TC_Pago'] == False and expense['Medio'] == 'RappiCard'])