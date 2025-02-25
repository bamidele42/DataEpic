import gspread
from google.oauth2.service_account import Credentials
from scraper import generate_content

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(
    "credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1x-ZvUs-NaadiQ3DZVJGDzzEISTEEYXd_Bl5tiEHFX_0"
workbook = client.open_by_key(sheet_id)


result = generate_content(["Ibadan", "Lagos", "Jos"])
workbook.sheet1.update(f"A1:D{len(result)}", result)
