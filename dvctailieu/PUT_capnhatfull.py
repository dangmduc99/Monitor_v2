import requests
import random
import string
import json
from datetime import datetime

ROOT_URL = "http://159.89.211.103/apps/api/dvctailieuquandinh/"
AUTHORIZATION = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwNDUwMTQyOSwiZXhwIjoxNjA0NTA1MDI5fQ.eyJ1c2VybmFtZSI6InN0cmluZyJ9.whFf_YVVekjbmNiGu1251oIcs9ZMbuCPXe5M-_r87bzdO8hNxAk3r2gt5tQ2oRRfGLo947ciSe0VESE7q3L4oQ"

UPDATE_DATA = []

with open('POST_themmoi.json') as f:
    createData = json.load(f)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def put_tailieu(Id):
    url = ROOT_URL + "CapNhatFull"

    data = {
        'ID': Id,
        'MaHoSo': get_random_string(10),
        'LoaiTaiLieu': get_random_string(10),
        'TenTaiLieu': get_random_string(10),
        'CreatedDate': get_random_string(10),
        'ModifiedDate': get_random_string(10),
        'CreatedBy': get_random_string(10),
        'ModifiedBy': get_random_string(10)
    }
    

    files=[
        ('TaiLieu', open('/home/ducdm/Pictures/122953568_652145808817518_4137528532679010030_n.png','rb'))
    ]


    headers = {
        'Authorization': AUTHORIZATION
    }

    response = requests.request("PUT", url, headers=headers, data=data, files=files)


    if response.status_code == 200:
        data['statusCode'] = 200
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(data)
        UPDATE_DATA.append(data)

    else:
        data['statusCode'] = response.status_code
        data['error'] = json.loads(response.text)["error"]
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(data)
        UPDATE_DATA.append(data)


for ob in createData:
    if ("ID" in ob):
        put_tailieu(ob['ID'])

with open('PUT_capnhatfull.json', 'w') as f:
    json.dump(UPDATE_DATA, f)