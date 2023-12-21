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

def save_expense(media, description, value):
  worksheet.append_row(['Gasto','2023/12/20','REGALOS|Cumpleaños', media, description, value, None], value_input_option='USER_ENTERED')