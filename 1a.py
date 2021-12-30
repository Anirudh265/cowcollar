import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


time = []
x = []
y = []
z = []
f = open('stat_jump_stat.txt', 'r')
for row in f:
    row = row.split(',')
    time.append(row[0][0:12])
    x.append(float(row[0][-5:]))
    y.append(float(row[1]))
    z.append(float(row[2]))
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
rmsx=round(np.average(x),2)
rmsy=round(np.average(y),2)
rmsz=round(np.average(z),2)
# rmsx = np.sqrt(np.mean(xarr**2))
# rmsy = np.sqrt(np.mean(yarr**2))
# rmsz = np.sqrt(np.mean(zarr**2))

# xarr = xarr-rmsx
# yarr = yarr-rmsy 
# zarr = zarr-rmsz  

for i in range(len(xarr)-1,0,-1):
    xarr[i]=xarr[i]-((xarr[i]+xarr[i-1])/2.0)  
for i in range(len(yarr)-1,0,-1):
    yarr[i]=yarr[i]-((yarr[i]+yarr[i-1])/2.0)  
for i in range(len(zarr)-1,0,-1):
    zarr[i]=zarr[i]-((zarr[i]+zarr[i-1])/2.0)  

xarr[0]=0
yarr[0]=0
zarr[0]=0
'''****************************'''
time_in_sec=[]
for i in range(1,len(xarr)):
    time_in_sec.append(float(time[i][-9:-7])*60+float(time[i][-6:])-float(time[i-1][-9:-7])*60-float(time[i-1][-6:]))

timediffarr= np.array(time_in_sec) 
timeconstant=np.average(timediffarr)
timearr=[0]
for i in range(1,len(time)):
    timearr.append(timearr[-1]+timeconstant)
timearr1=np.array(timearr)
'''********************'''
plt.title("actual acceleration")
plt.plot(timearr1, xarr, label="ax")
plt.plot(timearr1, yarr, label="ay")
plt.plot(timearr1, zarr, label="az")
plt.legend()
plt.show()
'''*******************'''

velocityx=[0]
velocityy=[0]
velocityz=[0]
for i in range(1,len(xarr)):
    velocityx.append(velocityx[i-1]+xarr[i-1]*timediffarr[i-1])

vxarr= np.array(velocityx)
plt.plot(timearr1,vxarr,label='vx')

for i in range(1,len(yarr)):
    
    velocityy.append(velocityy[i-1]+yarr[i-1]*timediffarr[i-1])

vyarr= np.array(velocityy)
plt.plot(timearr1,vyarr,label='vy')
for i in range(1,len(zarr)):
 
    velocityz.append(velocityz[i-1]+zarr[i-1]*timediffarr[i-1])

vzarr= np.array(velocityz)
plt.plot(timearr1,vzarr,label='vz')
plt.title("velocity")
plt.legend()
plt.show()
# for j in yarr:
#     print(j,end=' ')
'''****************************'''
distancex=[0]
distancey=[0]
distancez=[0]

for i in range(1,len(vxarr)):
    distancex.append(distancex[i-1]+(vxarr[i-1]*timediffarr[i-1])+0.5*xarr[i-1]*timediffarr[i-1]*timediffarr[i-1])

dxarr= np.array(distancex)
plt.plot(timearr1,dxarr,label='x')

for i in range(1,len(vyarr)):
    distancey.append(distancey[i-1]+(vyarr[i-1]*timediffarr[i-1])+0.5*yarr[i-1]*timediffarr[i-1]*timediffarr[i-1])

dyarr= np.array(distancey)
plt.plot(timearr1,dyarr,label='y')
for i in range(1,len(vzarr)):
    distancez.append(distancez[i-1]+(vzarr[i-1]*timediffarr[i-1])+0.5*zarr[i-1]*timediffarr[i-1]*timediffarr[i-1])

dzarr= np.array(distancez)
plt.plot(timearr1,dzarr,label='z')
plt.title("displacement")
plt.legend()
plt.show()
# print(timediffarr[0],timediffarr[1],timediffarr[2])
# print(yarr[0],yarr[1],yarr[2])
# print(vyarr[0],vyarr[1],vyarr[2])
# print(dyarr[0],dyarr[1],dyarr[2])

'''*********************'''