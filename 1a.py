import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np


time = []
x = []
y = []
z = []
f = open('step_mov.txt', 'r')
for row in f:
    row = re.split(r' |,|\n',row)
    time.append(row[0])
    x.append(float(row[2]))
    y.append(float(row[3]))
    z.append(float(row[4]))

xarr = np.array(x)
yarr = np.array(y)
zarr = np.array(z)
'''****************************'''
# rmsx=round(np.average(x),2)
# rmsy=round(np.average(y),2)
# rmsz=round(np.average(z),2)
# rmsx = np.sqrt(np.mean(xarr**2))
# rmsy = np.sqrt(np.mean(yarr**2))
# rmsz = np.sqrt(np.mean(zarr**2))

# xarr = xarr-rmsx
# yarr = yarr-rmsy 
# zarr = zarr-rmsz  

offx=0
offy=0
offz=0
for i in range(30):
    offx=xarr[i]+offx
offx=offx/30.0
for i in range(30):
    offz=zarr[i]+offz
offz=offz/30.0
for i in range(30):
    offy=yarr[i]+offy
offy=offy/30.0
'''******************'''
time_in_sec=[]
for i in range(1,len(xarr)):
    time_in_sec.append(float(time[i][-9:-7])*60+float(time[i][-6:])-float(time[i-1][-9:-7])*60-float(time[i-1][-6:]))

timediffarr= np.array(time_in_sec) 
timeconstant=np.average(timediffarr)
timearr=[0]
for i in range(1,len(time)):
    timearr.append(timearr[-1]+timeconstant)
timearr1=np.array(timearr)

plt.title("raw acceleration")
plt.plot(timearr1, xarr, label="ax")
plt.plot(timearr1, yarr, label="ay")
plt.plot(timearr1, zarr, label="az")
plt.legend()
plt.show()

for i in range(0,len(xarr)):
    xarr[i]=xarr[i]-offx
for i in range(0,len(yarr)):
    yarr[i]=yarr[i]-offy 
for i in range(0,len(zarr)):
    zarr[i]=zarr[i]-offz


plt.title("after offset acceleration")
plt.plot(timearr1, xarr, label="ax")
plt.plot(timearr1, yarr, label="ay")
plt.plot(timearr1, zarr, label="az")
plt.legend()
plt.show()

velocity1x=[0]
velocity1y=[0]
velocity1z=[0]
for i in range(1,len(xarr)):
    velocity1x.append(velocity1x[i-1]+xarr[i-1]*timediffarr[i-1])

vx1arr= np.array(velocity1x)
plt.plot(timearr1,vx1arr,label='vx')

for i in range(1,len(yarr)):
    
    velocity1y.append(velocity1y[i-1]+yarr[i-1]*timediffarr[i-1])

vy1arr= np.array(velocity1y)
plt.plot(timearr1,vy1arr,label='vy')
for i in range(1,len(zarr)):
 
    velocity1z.append(velocity1z[i-1]+zarr[i-1]*timediffarr[i-1])

vz1arr= np.array(velocity1z)
plt.plot(timearr1,vz1arr,label='vz')
plt.title("velocity after offset")
plt.legend()
plt.show()
# for i in range(len(xarr)-1,4,-1):
#     xarr[i]=((xarr[i-5]+xarr[i-1]+xarr[i-2]+xarr[i-3]+xarr[i-4])/5.0)  
# for i in range(len(yarr)-1,4,-1):
#     yarr[i]=((yarr[i-5]+yarr[i-1]+yarr[i-2]+yarr[i-3]+yarr[i-4])/5.0)  
# for i in range(len(zarr)-1,4,-1):
#     zarr[i]=((zarr[i-5]+zarr[i-1]+zarr[i-2]+zarr[i-3]+zarr[i-4])/5.0)  

# xarr[0]=xarr[1]=xarr[2]=xarr[3]=xarr[4]=xarr[5]
# yarr[0]=yarr[1]=yarr[2]=yarr[3]=yarr[4]=yarr[5]
# zarr[0]=zarr[1]=zarr[2]=zarr[3]=zarr[4]=zarr[5]
plt.title("comparison acceleration")
plt.plot(timearr1, xarr, label="ax1")
plt.plot(timearr1, yarr, label="ay1")

for i in range(len(xarr)-1,19,-1):
    k=0
    for j in range(1,21):
        k=k+xarr[i-j]
    xarr[i]=k/20.0
for i in range(len(yarr)-1,19,-1):
    k=0
    for j in range(1,21):
        k=k+yarr[i-j]
    yarr[i]=k/20.0
      
for i in range(len(zarr)-1,19,-1):
    k=0
    for j in range(1,21):
        k=k+zarr[i-j]
    zarr[i]=k/20.0
    



xarr[0]=xarr[1]=xarr[2]=xarr[3]=xarr[4]=xarr[5]=xarr[6]=xarr[7]=xarr[8]=xarr[9]=xarr[10]=xarr[11]=xarr[12]=xarr[13]=xarr[14]=xarr[15]=xarr[16]=xarr[17]=xarr[18]=xarr[19]=xarr[20]
yarr[0]=yarr[1]=yarr[2]=yarr[3]=yarr[4]=yarr[5]=yarr[6]=yarr[7]=yarr[8]=yarr[9]=yarr[10]=yarr[11]=yarr[12]=yarr[13]=yarr[14]=yarr[15]=yarr[16]=yarr[17]=yarr[18]=yarr[19]=yarr[20]
zarr[0]=zarr[1]=zarr[2]=zarr[3]=zarr[4]=zarr[5]=zarr[6]=zarr[7]=zarr[8]=zarr[9]=zarr[10]=zarr[11]=zarr[12]=zarr[13]=zarr[14]=zarr[15]=zarr[16]=zarr[17]=zarr[18]=zarr[19]=zarr[20]
plt.plot(timearr1, xarr, label="ax2")
plt.plot(timearr1, yarr, label="ay2")
plt.legend()
plt.show()

'''**********************'''
plt.title("after average acceleration")
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
plt.title("velocity after average")
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

# print(timediffarr[0],timediffarr[1],timediffarr[2])
# print(yarr[0],yarr[1],yarr[2])
# print(vyarr[0],vyarr[1],vyarr[2])
# print(dyarr[0],dyarr[1],dyarr[2])

'''*********************'''