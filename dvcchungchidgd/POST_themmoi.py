import requests
import random
import string
import json
from datetime import datetime

ROOT_URL = "http://159.89.211.103/apps/api/dvcchungchidgdquandinh/"
AUTHORIZATION = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwNDU1NTE1NiwiZXhwIjoxNjA0NTU4NzU2fQ.eyJ1c2VybmFtZSI6InN0cmluZyJ9.MIiRFHwJsz-yFv8wqOD-dRceM2lj4WCpnSSXFr0whvxkYSiBOcrPwa9kNwwUhaOr5s2tiH22ZTxA2IQNZI4-PA"

CREATE_DATA = []

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def post_chungchi():
    url = ROOT_URL + "ThemMoi"

    headers = {
        'Authorization': AUTHORIZATION
    }
    
    data = {
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
        'CreatedDate': get_random_string(10),
        'ModifiedDate': get_random_string(10),
        'CreatedBy': get_random_string(10),
        'ModifiedBy': get_random_string(10),
        'MaHoSo': get_random_string(10),
        'SoChungChiCu': get_random_string(10)
    }

    files=[
        ('ChungChi', open('/home/ducdm/Pictures/122953568_652145808817518_4137528532679010030_n.png','rb'))
    ]

    response = requests.request("POST", url, headers=headers, data = data, files=files)


    if response.status_code == 200:
        data['statusCode'] = 200
        data['profileId'] = json.loads(response.text)["ID"]
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(data)
        CREATE_DATA.append(data)
    else:
        data['statusCode'] = response.status_code
        data['error'] = json.loads(response.text)["error"]
        data['time'] = response.elapsed.total_seconds()
        data['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(data)
        CREATE_DATA.append(data)


for i in range(100):
    post_chungchi()

with open('POST_themmoi.json', 'w') as f:
    json.dump(CREATE_DATA, f)

