import numpy as np
import json
import matplotlib.pyplot as plt


with open('PUT_capnhatfull.json') as f:
  createData = json.load(f)

time = []

for data in createData:
       time.append(data['time'])

mean = [np.mean(time)]*len(time)

fig, ax = plt.subplots()

time_line = ax.plot(time, label='Thời gian xử lý')
mean_line = ax.plot(mean, label='Trung bình', linestyle='--')

plt.xlabel('Lần')
plt.ylabel('Thời gian xử lý')

plt.axis([0,100,0,5])

# plt.title(label='Visualize time response of 100 request')
plt.text(25, -0.65, 'Biểu đồ thời gian xử lý khi thực hiện tác vụ Cập nhật tất cả', fontdict={'fontsize': 14})

legend = ax.legend(loc='upper right')

plt.show()
