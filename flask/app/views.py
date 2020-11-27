from app import app, request
from datetime import datetime
import csv
import os

fieldsname = ['date', 'time', 'ip']
with open('../logs/ip.csv', 'w+') as f:
    writer = csv.DictWriter(f, fieldnames=fieldsname)
    writer.writeheader()

@app.route('/', methods=['GET'])
def index():

    assert request.method == 'GET'
    app_name = os.getenv('APP_NAME')
    ip = request.remote_addr  # str
    moment = datetime.today()  # datetime object
    day = datetime.strftime(moment, '%d/%m/%y')
    instant = datetime.strftime(moment, '%H:%M:%S:%f')
    payload = {'date': day, 'time': instant, 'ip': ip}
    with open('../logs/ip.csv', 'a+', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldsname)
        writer.writerow(payload)
    return f'Welcome to {app_name}!'

