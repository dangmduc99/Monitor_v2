import requests
import random
import string
import json
from datetime import datetime

ROOT_URL = "http://159.89.211.103/apps/api/dvctailieuquandinh/"
AUTHORIZATION = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwNDUwMTQyOSwiZXhwIjoxNjA0NTA1MDI5fQ.eyJ1c2VybmFtZSI6InN0cmluZyJ9.whFf_YVVekjbmNiGu1251oIcs9ZMbuCPXe5M-_r87bzdO8hNxAk3r2gt5tQ2oRRfGLo947ciSe0VESE7q3L4oQ"
ROLE = ['CHUYENVIEN', 'LANHDAO']
USER_DATA = []

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def post_user():
    url = ROOT_URL + "user"

    headers = {
        'Authorization': AUTHORIZATION
    }

    data = {
        "username": get_random_string(10),
        "password": get_random_string(10),
        "role": random.choice(ROLE)
    }

    response = requests.request("POST", url, headers=headers, data = json.dumps(data))


    if response.status_code == 200:
        data['statusCode'] = 200
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(data)
        USER_DATA.append(data)
    else:
        data['statusCode'] = response.status_code
        data['error'] = json.loads(response.text)["error"]
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(response)
        USER_DATA.append(data)


for i in range(100):
    post_user()

with open('POST_user.json', 'w') as f:
    json.dump(USER_DATA, f)
