import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

time = []
x = []
y = []
z = []
f = open('INST4.txt', 'r')
for row in f:
    row = row.split(',')
    time.append(row[0])
    x.append(float(row[1]))
    y.append(float(row[2]))
    z.append(float(row[3]))
xarr = np.array(x)
yarr = np.array(y)
zarr = np.array(z)

'''****************************'''

# plt.title("acceleration")
# plt.plot(time, xarr, label="x",color="red")
# plt.plot(time, yarr, label="y",color="blue")
# plt.plot(time, zarr, label="z",color="green")
# plt.legend()
# plt.show()
rmsx=np.average(x)
rmsy=np.average(y)
rmsz=np.average(z)
# rmsx = np.sqrt(np.mean(xarr**2))
# rmsy = np.sqrt(np.mean(yarr**2))
# rmsz = np.sqrt(np.mean(zarr**2))

xarr = xarr-rmsx
yarr = yarr-rmsy
zarr = zarr-rmsz

plt.title("actual acceleration")
plt.plot(time, xarr, label="x",color="red")
plt.plot(time, yarr, label="y",color="blue")
plt.plot(time, zarr, label="z",color="green")
plt.legend()
plt.show()
'''****************************'''
velocityx=[0]
velocityy=[0]
velocityz=[0]

for i in range(1,len(xarr)):
    time_in_sec=float(time[i][-12:-10])*60+float(time[i][-9:])-float(time[i-1][-12:-10])*60-float(time[i-1][-9:])
    velocityx.append(velocityx[-1]+xarr[i]*time_in_sec)

vxarr= np.array(velocityx)
plt.plot(time,vxarr,label='vx')

for i in range(1,len(yarr)):
    time_in_sec=float(time[i][-12:-10])*60+float(time[i][-9:])-float(time[i-1][-12:-10])*60-float(time[i-1][-9:])
    velocityy.append(velocityy[-1]+yarr[i]*time_in_sec)

vyarr= np.array(velocityy)
plt.plot(time,vyarr,label='vy')


for i in range(1,len(zarr)):
    time_in_sec=float(time[i][-12:-10])*60+float(time[i][-9:])-float(time[i-1][-12:-10])*60-float(time[i-1][-9:])
    velocityz.append(velocityz[-1]+zarr[i]*time_in_sec)

vzarr= np.array(velocityz)
plt.plot(time,vzarr,label='vz')
plt.legend()
plt.show()
# '''****************************'''
distancex=[0]
distancey=[0]
distancez=[0]

for i in range(1,len(vxarr)):
    time_in_sec=float(time[i][-12:-10])*60+float(time[i][-9:])-float(time[i-1][-12:-10])*60-float(time[i-1][-9:])
    distancex.append(distancex[-1]+abs(vxarr[i]*time_in_sec))

dxarr= np.array(distancex)
plt.plot(time,dxarr,label='x')

for i in range(1,len(vyarr)):
    time_in_sec=float(time[i][-12:-10])*60+float(time[i][-9:])-float(time[i-1][-12:-10])*60-float(time[i-1][-9:])
    distancey.append(distancey[-1]+abs(vyarr[i]*time_in_sec))

dyarr= np.array(distancey)
plt.plot(time,dyarr,label='y')

for i in range(1,len(vzarr)):
    time_in_sec=float(time[i][-12:-10])*60+float(time[i][-9:])-float(time[i-1][-12:-10])*60-float(time[i-1][-9:])
    distancez.append(distancez[-1]+abs(vzarr[i]*time_in_sec))

dzarr= np.array(distancez)
plt.plot(time,dzarr,label='z')

plt.legend()
plt.show()
'''*********************'''