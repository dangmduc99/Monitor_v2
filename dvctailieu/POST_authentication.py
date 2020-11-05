import requests
import random
import string
import json
from datetime import datetime

ROOT_URL = "http://159.89.211.103/apps/api/dvctailieuquandinh/"
AUTHORIZATION = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwNDUwMTQyOSwiZXhwIjoxNjA0NTA1MDI5fQ.eyJ1c2VybmFtZSI6InN0cmluZyJ9.whFf_YVVekjbmNiGu1251oIcs9ZMbuCPXe5M-_r87bzdO8hNxAk3r2gt5tQ2oRRfGLo947ciSe0VESE7q3L4oQ"

AUTHEN_DATA = []

with open('POST_user.json') as f:
  userData = json.load(f)

def post_user(user):
    url = ROOT_URL + "authentication"

    headers = {
        'Authorization': AUTHORIZATION
    }

    data = {
        "username": user['username'],
        "password": user['password'],
    }

    response = requests.request("POST", url, headers=headers, data = json.dumps(data))


    if response.status_code == 200:
        data['key'] = json.loads(response.text)["authorization"]
        data['statusCode'] = 200
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(data)
        AUTHEN_DATA.append(data)
    else:
        data['statusCode'] = response.status_code
        data['error'] = json.loads(response.text)["error"]
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(response)
        AUTHEN_DATA.append(data)


for i in userData:
    post_user(i)

with open('POST_authentication.json', 'w') as f:
    json.dump(AUTHEN_DATA, f)
