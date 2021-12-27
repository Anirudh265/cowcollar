# Stationary data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
time = []
x = []
y = []
z = []
f = open('stationary data.txt', 'r')
for row in f:
    row = row.split(',')
    time.append(row[0])
    x.append(float(row[1]))
    y.append(float(row[2]))
    z.append(float(row[3]))
xarr = np.array(x)
yarr = np.array(y)
zarr = np.array(z)
plt.title("acceleration")
plt.plot(time, xarr, label="x",color="red")
plt.plot(time, yarr, label="y",color="blue")
plt.plot(time, zarr, label="z",color="green")
plt.legend()
plt.show()

rmsx = np.sqrt(np.mean(xarr**2))
rmsy = np.sqrt(np.mean(yarr**2))
rmsz = np.sqrt(np.mean(zarr**2))

xarr = xarr+rmsx
yarr = yarr+rmsy
zarr = zarr+rmsz
plt.title("actual acceleration")
plt.plot(time, xarr, label="x",color="red")
plt.plot(time, yarr, label="y",color="blue")
plt.plot(time, zarr, label="z",color="green")
plt.legend()
plt.show()
