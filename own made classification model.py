import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np
import math
import os
from scipy.signal import butter, lfilter, filtfilt
fil="body_acc_x_test.txt"
fil1="body_acc_y_test.txt"
fil2="body_acc_z_test.txt"
f = open('iden/'+fil, 'r')
f1 = open('iden/'+fil1, 'r')
f2= open('iden/'+fil2, 'r')
c1=f.readlines()
c2=f1.readlines()
c3=f2.readlines()
result=[]
for z in range(0,150):
    time = [0]
    x = []
    y=[]
    z1=[]

    row=c1[z]
    row = re.split(r' |,|\n', row)
    for k in row:
        if(k!='' and k!=' '):

            x.append(float(k))
    
    j=c2[z]
    j= re.split(r' |,|\n', j)
    for m in j:
        if(m!='' and m!=' '):

            y.append(float(m))
            
    
    ll=c3[z]
    ll= re.split(r' |,|\n', ll)
    for bb in ll:
        if(bb!='' and bb!=' '):
            z1.append(float(bb))
    


    

    xarr = np.array(x)
    yarr = np.array(y)
    zarr = np.array(z1)
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
    offx=0
    offy=0
    offz=0
    # for i in range(15):
    #     offx=xarr[i]+offx
    # offx=offx/15.0

    '''******'''
    # time_in_sec=[]
    # for i in range(1,len(xarr)):
    #     time_in_sec.append(float(time[i][0:2])*60*60+float(time[i][3:5])*60+float(time[i][-6:])-float(time[i-1][0:2])*60*60-float(time[i-1][3:5])*60-float(time[i-1][-6:]))

    # timediffarr= np.array(time_in_sec) 
    # timeconstant=np.average(timediffarr)
    # timearr=[0]
    # for i in range(1,len(time)):
    #     timearr.append(timearr[-1]+timeconstant)
    # timearr1=np.array(timearr)

    for i in range (1,len(xarr)):
        time.append(time[i-1]+0.02)
    timearr1 = np.array(time)
    # plt.title("raw acceleration")
    # plt.plot(timearr1, xarr, label="ax",linewidth=0.5)
    # plt.plot(timearr1, yarr, label="ay",linewidth=0.5)
    # plt.plot(timearr1, zarr, label="az",linewidth=0.5)
    # plt.legend()
    # plt.savefig('output mobile/'+fil+"/"+str(z)+'raw acceleration'+'.png',dpi=1600)
    # plt.clf()

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
    # plt.title('comparison of acceleration')
    # plt.plot(timearr1, xarr, label="ax2",linewidth=0.5)

    # plt.legend()
    # plt.clf()

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

    # xarr= butter_lowpass_filter(xarr,17, 50,2)
    # yarr= butter_lowpass_filter(yarr,17, 50,2)
    # zarr= butter_lowpass_filter(zarr,17, 50,2)


    # xarr= butter_lowpass_filter(xarr,6, 25,3)
    # yarr= butter_lowpass_filter(yarr,6, 25,3)
    # zarr= butter_lowpass_filter(zarr,6, 25,3)






    

    # plt.title("after high and lpf acceleration")
    # plt.plot(timearr1, xarr, label="ax",linewidth=0.5)
    # plt.plot(timearr1, yarr, label="ay",linewidth=0.5)
    # plt.plot(timearr1, zarr, label="az",linewidth=0.5)
    # plt.legend()
    # plt.savefig('output mobile/'+fil+"/"+str(z)+'after high and lpf acceleration '+'.png',dpi=1600)
    # plt.clf()



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
    # plt.plot(timearr1,vzarr,label='vz',linewidth=0.5)
    # plt.title("velocity after average by integration")
    # plt.legend()
    # plt.savefig('output mobile/'+fil+"/"+str(z)+'velocity after integration '+'.png',dpi=1600)
    # plt.clf()



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
    # plt.savefig('output mobile/'+fil+"/"+str(z)+'velocity after integration '+'.png',dpi=1600)
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
    # plt.plot(timearr1,dzarr,label='z',linewidth=0.5)
    # plt.title("displacement")
    # plt.legend()
    # plt.savefig('output mobile/'+fil+"/"+str(z)+'displacement '+'.png',dpi=1600)
    # plt.clf()

    # for i in range(1,len(vxarr)):
    #     distancex1.append(distancex1[i-1]+abs((np.trapz([vxarr[i-1],vxarr[i]],[timearr1[i-1],timearr1[i]]))))


    # for i in range(1,len(vyarr)):
    #     distancey1.append(distancey1[i-1]+abs((np.trapz([vyarr[i-1],vyarr[i]],[timearr1[i-1],timearr1[i]]))))


    # for i in range(1,len(vzarr)):
    #     distancez1.append(distancez1[i-1]+abs((np.trapz([vzarr[i-1],vzarr[i]],[timearr1[i-1],timearr1[i]]))))
    # print(math.sqrt(distancex1[-1]*2+distancey1[-1]2+distancez1[-1]*2))
    x.sort()
    y.sort()
    z2=z1
    z1.sort()
    x2=np.average(xarr[-20:-1])*1000
    x3=np.average(xarr)*100
    yz2=np.average(zarr[-20:-1])*1000+np.average(yarr[-20:-1])*1000
    
    if((x[-10])<0.1 and (y[-10])< 0.1 and (z1[-10])<0.2):
        
        if((yz2<-4.81 or yz2>3.97) and (x2<0.29 or x2 >0.93)):
            result.append(str(z+1)+" is standing ")
        else:
            if((x3>0.056 or x3<-1.48) or ((x2>1.92 or x2<-1.56) and (yz2>-4.8 and yz2<3.97))):
                result.append(str(z+1)+" is laying")
            
            else:
                result.append(str(z+1)+" is sitting")




    elif(max(abs(x[5]) , abs(x[-5]))>0.2 and max(abs(y[5]), abs(y[-5]))>0.2 and max(abs(z1[5]) ,abs(z1[-5]))>0.1):
        if((x[-1])>0.8):
            result.append(str(z+1)+" is walking downstairs")

        elif(x[-1]<0.527):
            result.append(str(z+1)+" is walking" )

        elif(x[-1]<0.8 and x[-1]>0.535):
            result.append(str(z+1)+" is walking upstairs")
        else:
            if(y[-1]>0.3):
                result.append(str(z+1)+" is walking upstairs")
            else:
                result.append(str(z+1)+" is walking")

    


    else:
        result.append(str(z)+" is unidentified")



f=open("result.txt",'w')
for i in result:
    f.write(i)
    f.write('\n')