import json
import numpy as np

with open('GET_gcnbysovaoso.json') as f:
  data = json.load(f)

time = []

for d in data:
    time.append(d['time'])

mean = [np.mean(time)]*len(time)

print(mean[0])