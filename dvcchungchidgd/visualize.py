import numpy as np
import json
import matplotlib.pyplot as plt


with open('POST_themmoi.json') as f:
  createData = json.load(f)

time = []

for data in createData:
       time.append(data['time'])

mean = [np.mean(time)]*len(time)

fig, ax = plt.subplots()

time_line = ax.plot(time, label='Thời gian phản hồi')
mean_line = ax.plot(mean, label='Trung bình', linestyle='--')

plt.xlabel('Lần')
plt.ylabel('Thời gian phản hồi')

plt.axis([0,100,0,5])

# plt.title(label='Visualize time response of 100 request')
plt.text(25, -0.65, 'Biểu đồ biểu diễn thời gian phản hồi của 100 request', fontdict={'fontsize': 14})

legend = ax.legend(loc='upper right')

plt.show()
