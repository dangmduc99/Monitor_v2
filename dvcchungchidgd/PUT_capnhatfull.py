import requests
import random
import string
import json
from datetime import datetime

ROOT_URL = "http://159.89.211.103/apps/api/dvctailieuquandinh/"
AUTHORIZATION = ""

UPDATE_DATA = []

with open('POST_themmoi.json') as f:
    createData = json.load(f)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def put_chungchi(id):
    url = ROOT_URL + "CapNhatFull"

    data = {
        'MaHoSo': get_random_string(10),
        'SoChungChi': get_random_string(10),
        'NgayCoHieuLuc': get_random_string(10),
        'NgayHetHieuLuc': get_random_string(10),
        'CoQuanCap': get_random_string(10),
        'ChuSoHuu': get_random_string(10),
        'QuocTich': get_random_string(10),
        'SoCMND': get_random_string(10),
        'NgayCapCMND': get_random_string(10),
        'NguoiKy': get_random_string(10),
        'NgaySinh': get_random_string(10),
        'ChungChi': get_random_string(10),
        'CreatedDate': get_random_string(10),
        'ModifiedDate': get_random_string(10),
        'CreatedBy': get_random_string(10),
        'ModifiedBy': get_random_string(10),
        'SoChungChiCu': get_random_string(10)
    }
    

    data['ID'] = id

    headers = {
        'Authorization': AUTHORIZATION,
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data = json.dumps(data))


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
        put_chungchi(ob['ID'])

with open('PUT_capnhatfull.json', 'w') as f:
    json.dump(UPDATE_DATA, f)