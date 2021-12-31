import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


time = []
x = []
y = []
z = []
f = open('stat_data.txt', 'r')
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

for i in range(len(xarr)-1,9,-1):
    xarr[i]=xarr[i]-((xarr[i]+xarr[i-1]+xarr[i-2]+xarr[i-3]+xarr[i-4]+xarr[i-5]+xarr[i-6]+xarr[i-7]+xarr[i-8]+xarr[i-9])/10.0)  
for i in range(len(yarr)-1,9,-1):
    yarr[i]=yarr[i]-((yarr[i]+yarr[i-1]+yarr[i-2]+yarr[i-3]+yarr[i-4]+yarr[i-5]+yarr[i-6]+yarr[i-7]+yarr[i-8]+yarr[i-9])/10.0)  
for i in range(len(zarr)-1,9,-1):
    zarr[i]=zarr[i]-((zarr[i]+zarr[i-1]+zarr[i-2]+zarr[i-3]+zarr[i-4]+zarr[i-5]+zarr[i-6]+zarr[i-7]+zarr[i-8]+zarr[i-9])/10.0)  

xarr[0]=xarr[1]=xarr[2]=xarr[3]=xarr[4]=xarr[5]=xarr[6]=xarr[7]=xarr[8]=xarr[9]=xarr[10]
yarr[0]=yarr[1]=yarr[2]=yarr[3]=yarr[4]=yarr[5]=yarr[6]=yarr[7]=yarr[8]=yarr[9]=yarr[10]
zarr[0]=zarr[1]=zarr[2]=zarr[3]=zarr[4]=zarr[5]=zarr[6]=zarr[7]=zarr[8]=zarr[9]=zarr[10]
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
distancex1=[0]
distancey1=[0]
distancez1=[0]


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

for i in range(1,len(vxarr)):
    distancex1.append(distancex1[i-1]+abs((vxarr[i-1]*timediffarr[i-1])+0.5*xarr[i-1]*timediffarr[i-1]*timediffarr[i-1]))

for i in range(1,len(vzarr)):
    distancez1.append(distancez1[i-1]+abs((vzarr[i-1]*timediffarr[i-1])+0.5*zarr[i-1]*timediffarr[i-1]*timediffarr[i-1]))

for i in range(1,len(vyarr)):
    distancey1.append(distancey1[i-1]+abs((vyarr[i-1]*timediffarr[i-1])+0.5*yarr[i-1]*timediffarr[i-1]*timediffarr[i-1]))
print(distancex1[-1],distancey1[-1],distancez1[-1])
# print(timediffarr[0],timediffarr[1],timediffarr[2])
# print(yarr[0],yarr[1],yarr[2])
# print(vyarr[0],vyarr[1],vyarr[2])
# print(dyarr[0],dyarr[1],dyarr[2])

'''*********************'''