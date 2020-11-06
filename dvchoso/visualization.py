import numpy as np
import json
import matplotlib.pyplot as plt

with open('GET_laytheoid.json') as f:
    laytheoid = json.load(f)

with open('GET_laytheoma.json') as f:
    laytheoma = json.load(f)

with open('POST_authentication.json') as f:
    authentication = json.load(f)

with open('POST_themmoi.json') as f:
    themmoi = json.load(f)

with open('POST_user.json') as f:
    user = json.load(f)

with open('PUT_capnhat.json') as f:
    capnhat = json.load(f)

with open('PUT_capnhatfull.json') as f:
    capnhatfull = json.load(f)

time = []

for i in range(len(themmoi)):
    time.append(laytheoid[i]['time'] + laytheoma[i]['time'] +
                authentication[i]['time'] + themmoi[i]['time'] +
                user[i]['time'] + capnhat[i]['time'] + capnhatfull[i]['time'])

mean = [np.mean(time)]*len(time)

fig, ax = plt.subplots()
time_line = ax.plot(time, label='Thời gian xử lý')
mean_line = ax.plot(mean, label='Trung bình', linestyle='--')

plt.xlabel('Lần')
plt.ylabel('Thời gian xử lý')

plt.axis([0,100,0,15])

plt.text(25, -1.5, 'Biểu đồ thời gian xử lý khi thực hiện Luồng các tác vụ', fontdict={'fontsize': 14})

legend = ax.legend(loc='upper right')

plt.show()