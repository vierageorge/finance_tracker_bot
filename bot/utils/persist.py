import gspread
import os
from dotenv import load_dotenv

load_dotenv()

CRED_FILE = os.path.join(os.getcwd(), 'credentials.json')
EXPENSE_SHEET_ID = os.environ.get('SHEET_ID')
SHEET_NAME = os.environ.get('SHEET_NAME')

sheet_service = gspread.service_account(CRED_FILE)
sheet_file = sheet_service.open_by_key(EXPENSE_SHEET_ID)
worksheet = sheet_file.worksheet(SHEET_NAME)

def save_expense(media: str, description: str, value: int, date: str, paid: str):
  worksheet.append_row(['Gasto',date, None, media, description, value, paid], value_input_option='USER_ENTERED')