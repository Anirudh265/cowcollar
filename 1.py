import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as it

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

'''****************************'''
velocityx=[0]
velocityy=[0]
velocityz=[0]
time_in_sec=[]
for i in range(1,len(xarr)):
    time_in_sec.append(float(time[i][-12:-10])*60+float(time[i][-9:])-float(time[i-1][-12:-10])*60-float(time[i-1][-9:]))
    velocityx.append(velocityx[-1]+yarr[i]*time_in_sec[-1])
timediffarr= np.array(time_in_sec) 
timeconstant=np.average(timediffarr)
timearr=[0]
for i in range(1,len(time)):
    timearr.append(timearr[-1]+timeconstant)
timearr1=np.array(timearr)

plt.title("actual acceleration")
plt.plot(timearr1, xarr, label="x",color="red")
plt.plot(timearr1, yarr, label="y",color="blue")
plt.plot(timearr1, zarr, label="z",color="green")
plt.legend()
plt.show()
'''*******************'''
xarr1=xarr[(timearr1/timeconstant)]


y_int = it.cumtrapz(  xarr1  ,  timearr1, initial=0.0)
plt.plot(timearr1, y_int)
plt.show()
# vxarr= np.array(velocityx)
# plt.plot(timearr1,vxarr,label='vx')

# for i in range(1,len(yarr)):
#     time_in_sec=float(time[i][-12:-10])*60+float(time[i][-9:])-float(time[i-1][-12:-10])*60-float(time[i-1][-9:])
#     velocityy.append(velocityy[-1]+yarr[i]*time_in_sec)

# vyarr= np.array(velocityy)
# plt.plot(timearr1,vyarr,label='vy')


# for i in range(1,len(zarr)):
#     time_in_sec=float(time[i][-12:-10])*60+float(time[i][-9:])-float(time[i-1][-12:-10])*60-float(time[i-1][-9:])
    
#     velocityz.append(velocityz[-1]+zarr[i]*time_in_sec)

# vzarr= np.array(velocityz)
# plt.plot(timearr1,vzarr,label='vz')
# plt.legend()
# plt.show()
# # '''****************************'''
# distancex=[0]
# distancey=[0]
# distancez=[0]

# for i in range(1,len(vxarr)):
#     time_in_sec=float(time[i][-12:-10])*60+float(time[i][-9:])-float(time[i-1][-12:-10])*60-float(time[i-1][-9:])
#     distancex.append(distancex[-1]+(vxarr[i]*time_in_sec))

# dxarr= np.array(distancex)
# plt.plot(timearr1,dxarr,label='x')

# for i in range(1,len(vyarr)):
#     time_in_sec=float(time[i][-12:-10])*60+float(time[i][-9:])-float(time[i-1][-12:-10])*60-float(time[i-1][-9:])
#     distancey.append(distancey[-1]+(vyarr[i]*time_in_sec))

# dyarr= np.array(distancey)
# plt.plot(timearr1,dyarr,label='y')

# for i in range(1,len(vzarr)):
#     time_in_sec=float(time[i][-12:-10])*60+float(time[i][-9:])-float(time[i-1][-12:-10])*60-float(time[i-1][-9:])
#     distancez.append(distancez[-1]+(vzarr[i]*time_in_sec))

# dzarr= np.array(distancez)
# plt.plot(timearr1,dzarr,label='z')

# plt.legend()
# plt.show()
'''*********************'''
