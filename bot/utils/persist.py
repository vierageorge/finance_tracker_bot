import gspread
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

CRED_FILE = os.path.join(os.getcwd(), 'credentials.json')
EXPENSE_SHEET_ID = "18k3LTJhscnO3WVIY-P39WlFr8wR6TtsHV_V3h9-NaKY"
SHEET_NAME = "movement_fact"

sheet_service = gspread.service_account(CRED_FILE)
sheet_file = sheet_service.open_by_key(EXPENSE_SHEET_ID)
worksheet = sheet_file.worksheet(SHEET_NAME)
worksheet.append_row(['Gasto','2023/12/20','REGALOS|Cumpleaños','RappiCard','La descripcion', 39900, 'TRUE'], value_input_option='USER_ENTERED')