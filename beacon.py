import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np
import math
import os

files=os.listdir('beacon data')

for fil in files:
    f = open('data2/'+fil, 'r')
    time = []
    x = []
    y = []
    z = []
    for row in f:
        row = re.split(r' |,|\n',row)
        time.append(row[1])
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
    parent_dir="beacon output/";
    dir=fil
    path=os.path.join(parent_dir,dir)
    mode=0o666
    os.mkdir(path,mode)

    offx=0
    offy=0
    offz=0
    for i in range(15):
        offx=xarr[i]+offx
    offx=offx/15.0
    for i in range(15):
        offz=zarr[i]+offz
    offz=offz/15.0
    for i in range(15):
        offy=yarr[i]+offy
    offy=offy/15.0
    '''******************'''
    time_in_sec=[]
    for i in range(1,len(xarr)):
        time_in_sec.append(float(time[i][0:2])*60*60+float(time[i][3:5])*60+float(time[i][-9:])-float(time[i-1][0:2])*60*60-float(time[i-1][3:5])*60-float(time[i-1][-9:]))

    timediffarr= np.array(time_in_sec) 
    timeconstant=np.average(timediffarr)
    timearr=[0]
    for i in range(1,len(time)):
        timearr.append(timearr[-1]+timeconstant)
    timearr1=np.array(timearr)

    plt.title("raw acceleration")
    plt.plot(timearr1, xarr, label="ax",linewidth=0.5)
    plt.plot(timearr1, yarr, label="ay",linewidth=0.5)
    plt.plot(timearr1, zarr, label="az",linewidth=0.5)
    plt.legend()
    # plt.savefig('output new/'+fil+"/"+'raw acceleration'+fil+'.png',dpi=1600)
    plt.clf()

    for i in range(0,len(xarr)):
        xarr[i]=xarr[i]-offx
    for i in range(0,len(yarr)):
        yarr[i]=yarr[i]-offy 
    for i in range(0,len(zarr)):
        zarr[i]=zarr[i]-offz


    plt.title("after offset acceleration")
    plt.plot(timearr1, xarr, label="ax",linewidth=0.5)
    plt.plot(timearr1, yarr, label="ay",linewidth=0.5)
    plt.plot(timearr1, zarr, label="az",linewidth=0.5)
    plt.legend()
    plt.savefig('beacon output/'+fil+"/"+'after offset acceleration '+fil+'.png',dpi=1600)
    plt.clf()

    
    velocity1x=[0]
    velocity1y=[0]
    velocity1z=[0]
    for i in range(1,len(yarr)):
        velocity1y.append(velocity1y[-1]+np.trapz([yarr[i-1],yarr[i]],[timearr1[i-1],timearr1[i]]))
    velocity1yy=np.array(velocity1y)
    plt.plot(timearr1,velocity1yy,label='vx',linewidth=0.5)

    for i in range(1,len(xarr)):
        velocity1x.append(velocity1x[-1]+np.trapz([xarr[i-1],xarr[i]],[timearr1[i-1],timearr1[i]]))
    velocity1xx=np.array(velocity1x)
    plt.plot(timearr1,velocity1xx,label='vy',linewidth=0.5)

    for i in range(1,len(zarr)):
        velocity1z.append(velocity1z[-1]+np.trapz([zarr[i-1],zarr[i]],[timearr1[i-1],timearr1[i]]))
    velocity1zz=np.array(velocity1z)
    plt.plot(timearr1,velocity1zz,label='vz',linewidth=0.5)
    plt.title("after offset velocity by integration")
    plt.legend()
    plt.clf()
    plt.plot(timearr1, xarr, label="ax1",linewidth=0.5)
    plt.plot(timearr1, yarr, label="ay1",linewidth=0.5)
    for i in range(len(xarr)-1,4,-1):
        k=0
        for j in range(1,6):

            k=k+xarr[i-j]
        xarr[i]=k/5.0
    for i in range(len(yarr)-1,4,-1):
        k=0
        for j in range(1,6):
            k=k+yarr[i-j]
        yarr[i]=k/5.0
        
    for i in range(len(zarr)-1,4,-1):
        k=0
        for j in range(1,6):
            k=k+zarr[i-j]
        zarr[i]=k/5.0
        
    zarr[0]=zarr[1]=zarr[2]=zarr[3]=zarr[4]=zarr[5]
    yarr[0]=yarr[1]=yarr[2]=yarr[3]=yarr[4]=yarr[5]
    xarr[0]=xarr[1]=xarr[2]=xarr[3]=xarr[4]=xarr[5]

    # for i in range(len(xarr)-1,19,-1):
    #     k=0
    #     for j in range(1,21):--- 
    #         k=k+xarr[i-j]
    #     xarr[i]=k/20.0
    # for i in range(len(yarr)-1,19,-1):
    #     k=0
    #     for j in range(1,21):
    #         k=k+yarr[i-j]
    #     yarr[i]=k/20.0
        
    # for i in range(len(zarr)-1,19,-1):
    #     k=0
    #     for j in range(1,21):
    #         k=k+zarr[i-j]
    #     zarr[i]=k/20.0
        



    # xarr[0]=xarr[1]=xarr[2]=xarr[3]=xarr[4]=xarr[5]=xarr[6]=xarr[7]=xarr[8]=xarr[9]=xarr[10]=xarr[11]=xarr[12]=xarr[13]=xarr[14]=xarr[15]=xarr[16]=xarr[17]=xarr[18]=xarr[19]=xarr[20]
    # yarr[0]=yarr[1]=yarr[2]=yarr[3]=yarr[4]=yarr[5]=yarr[6]=yarr[7]=yarr[8]=yarr[9]=yarr[10]=yarr[11]=yarr[12]=yarr[13]=yarr[14]=yarr[15]=yarr[16]=yarr[17]=yarr[18]=yarr[19]=yarr[20]
    # zarr[0]=zarr[1]=zarr[2]=zarr[3]=zarr[4]=zarr[5]=zarr[6]=zarr[7]=zarr[8]=zarr[9]=zarr[10]=zarr[11]=zarr[12]=zarr[13]=zarr[14]=zarr[15]=zarr[16]=zarr[17]=zarr[18]=zarr[19]=zarr[20]
    plt.title('comparison of acceleration')
    plt.plot(timearr1, xarr, label="ax2",linewidth=0.5)
    plt.plot(timearr1, yarr, label="ay2",linewidth=0.5)
    plt.legend()
    plt.clf()

    '''**********************'''
    plt.title("after average acceleration")
    plt.plot(timearr1, xarr, label="ax",linewidth=0.5)
    plt.plot(timearr1, yarr, label="ay",linewidth=0.5)
    plt.plot(timearr1, zarr, label="az",linewidth=0.5)
    plt.legend()
    plt.savefig('beacon output/'+fil+"/"+'after average acceleration '+fil+'.png',dpi=1600)
    plt.clf()
    '''*******************'''

    velocityx=[0]
    velocityy=[0]
    velocityz=[0]


    for i in range(1,len(xarr)):
        velocityx.append(velocityx[-1]+np.trapz([xarr[i-1],xarr[i]],[timearr[i-1],timearr[i]]))

    vxarr= np.array(velocityx)
    plt.plot(timearr1,vxarr,label='vx',linewidth=0.5)

    for i in range(1,len(yarr)):
        
        velocityy.append(velocityy[-1]+np.trapz([yarr[i-1],yarr[i]],[timearr[i-1],timearr[i]]))

    vyarr= np.array(velocityy)
    plt.plot(timearr1,vyarr,label='vy',linewidth=0.5)
    for i in range(1,len(zarr)):
    
        velocityz.append(velocityz[-1]+np.trapz([zarr[i-1],zarr[i]],[timearr[i-1],timearr[i]]))

    vzarr= np.array(velocityz)
    plt.plot(timearr1,vzarr,label='vz',linewidth=0.5)
    plt.title("velocity after average by integration")
    plt.legend()
    plt.savefig('beacon output/'+fil+"/"+'velocity after integration '+fil+'.png',dpi=1600)
    plt.clf()
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
        distancex.append(distancex[i-1]+(np.trapz([vxarr[i-1],vxarr[i]],[timearr1[i-1],timearr1[i]])))

    dxarr= np.array(distancex)
    plt.plot(timearr1,dxarr,label='x',linewidth=0.5)

    for i in range(1,len(vyarr)):
        distancey.append(distancey[i-1]+(np.trapz([vyarr[i-1],vyarr[i]],[timearr1[i-1],timearr1[i]])))
    dyarr= np.array(distancey)
    plt.plot(timearr1,dyarr,label='y',linewidth=0.5)
    for i in range(1,len(vzarr)):
        distancez.append(distancez[i-1]+(np.trapz([vzarr[i-1],vzarr[i]],[timearr1[i-1],timearr1[i]])))

    dzarr= np.array(distancez)
    plt.plot(timearr1,dzarr,label='z',linewidth=0.5)
    plt.title("displacement")
    plt.legend()
    plt.savefig('beacon output/'+fil+"/"+'displacement '+fil+'.png',dpi=1600)
    plt.clf()

    # for i in range(1,len(vxarr)):
    #     distancex1.append(distancex1[i-1]+abs((np.trapz([vxarr[i-1],vxarr[i]],[timearr1[i-1],timearr1[i]]))))


    # for i in range(1,len(vyarr)):
    #     distancey1.append(distancey1[i-1]+abs((np.trapz([vyarr[i-1],vyarr[i]],[timearr1[i-1],timearr1[i]]))))


    # for i in range(1,len(vzarr)):
    #     distancez1.append(distancez1[i-1]+abs((np.trapz([vzarr[i-1],vzarr[i]],[timearr1[i-1],timearr1[i]]))))
    # print(math.sqrt(distancex1[-1]**2+distancey1[-1]**2+distancez1[-1]**2))
'''*********************'''
