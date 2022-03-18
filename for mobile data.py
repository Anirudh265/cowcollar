import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np
import math
import os
from scipy.signal import butter, lfilter, filtfilt

files=os.listdir('dataa') 

for fil in files:
    f = open('dataa/'+fil, 'r')
    time = [0]
    x = []
    y = []
    z = []
    for row in f:
        row = re.split(r' |,|\n', row)
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))

    xarr = np.array(x)
    yarr = np.array(y)
    zarr = np.array(z)
    '''**********'''
    # rmsx=round(np.average(x),2)
    # rmsy=round(np.average(y),2)
    # rmsz=round(np.average(z),2)
    # rmsx = np.sqrt(np.mean(xarr**2))
    # rmsy = np.sqrt(np.mean(yarr**2))
    # rmsz = np.sqrt(np.mean(zarr**2))

    # xarr = xarr-rmsx
    # yarr = yarr-rmsy 
    # zarr = zarr-rmsz  

    parent_dir="output mobile/";
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
    '''******'''
    # time_in_sec=[]
    # for i in range(1,len(xarr)):
    #     time_in_sec.append(float(time[i][0:2])*60*60+float(time[i][3:5])*60+float(time[i][-6:])-float(time[i-1][0:2])*60*60-float(time[i-1][3:5])*60-float(time[i-1][-6:]))

    # timediffarr= np.array(time_in_sec) 
    # timeconstant=np.average(timediffarr)
    # tim for i in range (1,len(xarr)):
    for i in range (1,len(xarr)):
        time.append(time[i-1]+0.02)
    timearr1 = np.array(time)
    plt.title("raw acceleration")
    plt.plot(timearr1, xarr, label="ax",linewidth=0.5)
    plt.plot(timearr1, yarr, label="ay",linewidth=0.5)
    plt.plot(timearr1, zarr, label="az",linewidth=0.5)
    plt.legend()
    plt.savefig('output mobile/'+fil+"/"+'raw acceleration'+'.png',dpi=1600)
    plt.clf()

    # for i in range(0,len(xarr)):
    #     xarr[i]=xarr[i]-offx
    # for i in range(0,len(yarr)):
    #     yarr[i]=yarr[i]-offy 
    # for i in range(0,len(zarr)):
    #     zarr[i]=zarr[i]-offz


    # plt.title("after offset acceleration")
    # plt.plot(timearr1, xarr, label="ax",linewidth=0.5)
    # plt.plot(timearr1, yarr, label="ay",linewidth=0.5)
    # plt.plot(timearr1, zarr, label="az",linewidth=0.5)
    # plt.legend()
    # plt.savefig('output mobile/'+fil+"/"+'after offset acceleration '+'.png',dpi=1600)
    # plt.clf()

    
    # velocity1x=[0]
    # velocity1y=[0]
    # velocity1z=[0]
    # for i in range(1,len(yarr)):
    #     velocity1y.append(velocity1y[-1]+np.trapz([yarr[i-1],yarr[i]],[timearr1[i-1],timearr1[i]]))
    # velocity1yy=np.array(velocity1y)
    # plt.plot(timearr1,velocity1yy,label='vx',linewidth=0.5)

    # for i in range(1,len(xarr)):
    #     velocity1x.append(velocity1x[-1]+np.trapz([xarr[i-1],xarr[i]],[timearr1[i-1],timearr1[i]]))
    # velocity1xx=np.array(velocity1x)
    # plt.plot(timearr1,velocity1xx,label='vy',linewidth=0.5)

    # for i in range(1,len(zarr)):
    #     velocity1z.append(velocity1z[-1]+np.trapz([zarr[i-1],zarr[i]],[timearr1[i-1],timearr1[i]]))
    # velocity1zz=np.array(velocity1z)
    # plt.plot(timearr1,velocity1zz,label='vz',linewidth=0.5)
    # plt.title("after offset velocity by integration")
    # plt.legend()
    # plt.clf()
    # plt.plot(timearr1, xarr, label="ax1",linewidth=0.5)
    # plt.plot(timearr1, yarr, label="ay1",linewidth=0.5)
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

    '''********'''
    def butter_lowpass(cutoff, fs, order=5):
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        return b, a
    
    def butter_highpass(cutoff, fs, order=5):
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype='high', analog=False)
        return b, a

    def butter_lowpass_filter(data, cutoff, fs, order=5):
        b, a = butter_lowpass(cutoff, fs, order=order)
        y = lfilter(b, a, data)
        return y

    def butter_highpass_filter(data, cutoff, fs, order=5):
        b, a = butter_highpass(cutoff, fs, order=order)
        y = filtfilt(b, a, data)
        return y

    xarr= butter_lowpass_filter(xarr,6, 50,3)
    yarr= butter_lowpass_filter(yarr,6, 50,3)
    zarr= butter_lowpass_filter(zarr,6, 50,3)


    # xarr= butter_lowpass_filter(xarr,6, 25,3)
    # yarr= butter_lowpass_filter(yarr,6, 25,3)
    # zarr= butter_lowpass_filter(zarr,6, 25,3)


  

  

    

    plt.title("after high and lpf acceleration")
    plt.plot(timearr1, xarr, label="ax",linewidth=0.5)
    plt.plot(timearr1, yarr, label="ay",linewidth=0.5)
    plt.plot(timearr1, zarr, label="az",linewidth=0.5)
    plt.legend()
    plt.savefig('output mobile/'+fil+"/"+'after high and lpf acceleration '+'.png',dpi=1600)
    plt.clf()



    # for i in range(len(xarr)-1,4,-1):
    #     k=0
    #     for j in range(1,6):

    #         k=k+xarr[i-j]
    #     xarr[i]=xarr[i]-k/5.0
    # for i in range(len(yarr)-1,4,-1):
    #     k=0
    #     for j in range(1,6):
    #         k=k+yarr[i-j]
    #     yarr[i]=yarr[i]-k/5.0
        
    # for i in range(len(zarr)-1,4,-1):
    #     k=0
    #     for j in range(1,6):
    #         k=k+zarr[i-j]
    #     zarr[i]=zarr[i]-k/5.0
        
    # zarr[0]=zarr[1]=zarr[2]=zarr[3]=zarr[4]=zarr[5]
    # yarr[0]=yarr[1]=yarr[2]=yarr[3]=yarr[4]=yarr[5]
    # xarr[0]=xarr[1]=xarr[2]=xarr[3]=xarr[4]=xarr[5]

    # plt.title("after average acceleration")
    # plt.plot(timearr1, xarr, label="ax",linewidth=0.5)
    # plt.plot(timearr1, yarr, label="ay",linewidth=0.5)
    # plt.plot(timearr1, zarr, label="az",linewidth=0.5)
    # plt.legend()
    # plt.savefig('output mobile/'+fil+"/"+'after average acceleration '+'.png',dpi=1600)
    # plt.clf()
    '''*******'''
    velocityx=[0]
    velocityy=[0]
    velocityz=[0]
    for i in range(1,len(xarr)):
        velocityx.append(velocityx[i-1]+xarr[i]*(timearr1[i]-timearr1[i-1]))

    vxarr= np.array(velocityx)
    plt.plot(timearr1,vxarr,label='vx',linewidth=0.5)

    for i in range(1,len(yarr)):
        
        velocityy.append(velocityy[i-1]+yarr[i]*(timearr1[i]-timearr1[i-1]))

    vyarr= np.array(velocityy)
    plt.plot(timearr1,vyarr,label='vy',linewidth=0.5)
    for i in range(1,len(zarr)):
    
        velocityz.append(velocityz[i-1]+zarr[i]*(timearr1[i]-timearr1[i-1]))

    vzarr= np.array(velocityz)
    plt.plot(timearr1,vzarr,label='vz',linewidth=0.5)
    plt.title("velocity after average by integration")
    plt.legend()
    plt.savefig('output mobile/'+fil+"/"+'velocity after integration '+'.png',dpi=1600)
    plt.clf()
   


    # for i in range(1,len(xarr)):
    #     velocityx.append(velocityx[-1]+np.trapz([xarr[i-1],xarr[i]],[timearr1[i-1],timearr1[i]]))

    # vxarr= np.array(velocityx)
    # plt.plot(timearr1,vxarr,label='vx',linewidth=0.5)

    # for i in range(1,len(yarr)):
        
    #     velocityy.append(velocityy[-1]+np.trapz([yarr[i-1],yarr[i]],[timearr1[i-1],timearr1[i]]))

    # vyarr= np.array(velocityy)
    # plt.plot(timearr1,vyarr,label='vy',linewidth=0.5)
    # for i in range(1,len(zarr)):
    
    #     velocityz.append(velocityz[-1]+np.trapz([zarr[i-1],zarr[i]],[timearr1[i-1],timearr1[i]]))

    # vzarr= np.array(velocityz)
    # plt.plot(timearr1,vzarr,label='vz',linewidth=0.5)
    # plt.title("velocity after average by integration")
    # plt.legend()
    # plt.savefig('output mobile/'+fil+"/"+'velocity after integration '+'.png',dpi=1600)
    # plt.clf()
    # for j in yarr:
    #     print(j,end=' ')
    '''**********'''
    distancex=[0]
    distancey=[0]
    distancez=[0]
    distancex1=[0]
    distancey1=[0]
    distancez1=[0]


    for i in range(1,len(vxarr)):
        distancex.append(distancex[i-1]+vxarr[i-1]*(timearr1[i]-timearr1[i-1])+0.5*xarr[i-1]*(timearr1[i]-timearr1[i-1])*(timearr1[i]-timearr1[i-1]))

    dxarr= np.array(distancex)
    plt.plot(timearr1,dxarr,label='x',linewidth=0.5)

    for i in range(1,len(vyarr)):
        distancey.append(distancey[i-1]+vyarr[i-1]*(timearr1[i]-timearr1[i-1])+0.5*yarr[i-1]*(timearr1[i]-timearr1[i-1])*(timearr1[i]-timearr1[i-1]))
    dyarr= np.array(distancey)
    plt.plot(timearr1,dyarr,label='y',linewidth=0.5)
    for i in range(1,len(vzarr)):
        distancez.append(distancez[i-1]+vzarr[i-1]*(timearr1[i]-timearr1[i-1])+0.5*zarr[i-1]*(timearr1[i]-timearr1[i-1])*(timearr1[i]-timearr1[i-1]))

    dzarr= np.array(distancez)
    plt.plot(timearr1,dzarr,label='z',linewidth=0.5)
    plt.title("displacement")
    plt.legend()
    plt.savefig('output mobile/'+fil+"/"+'displacement '+'.png',dpi=1600)
    plt.clf()

    # for i in range(1,len(vxarr)):
    #     distancex1.append(distancex1[i-1]+abs((np.trapz([vxarr[i-1],vxarr[i]],[timearr1[i-1],timearr1[i]]))))


    # for i in range(1,len(vyarr)):
    #     distancey1.append(distancey1[i-1]+abs((np.trapz([vyarr[i-1],vyarr[i]],[timearr1[i-1],timearr1[i]]))))


    # for i in range(1,len(vzarr)):
    #     distancez1.append(distancez1[i-1]+abs((np.trapz([vzarr[i-1],vzarr[i]],[timearr1[i-1],timearr1[i]]))))
    # print(math.sqrt(distancex1[-1]*2+distancey1[-1]2+distancez1[-1]*2))
'''*******'''