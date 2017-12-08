from flask import Flask
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

@app.route("/")
def hello():
    sheet = client.open('phi').sheet1
    legislators = sheet.get_all_records()
    return str(legislators)

if __name__ == '__main__':
    app.run(host='localhost')
