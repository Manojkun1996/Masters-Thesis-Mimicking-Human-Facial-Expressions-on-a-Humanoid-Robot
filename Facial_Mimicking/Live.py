import pandas as pd
import os
import time
from hr_little_api.functional import say, motor, close_mouth, command_list, wait_for_motors_and_speaking, \
    head_turn_middle, neutral_eyebrows, frown_eyebrows, head_turn_right, head_turn_left, poke_tounge, wait, \
    raise_eyebrows, wait_for_motors, move_robot, eye_lid_close, eye_lid_open, reset_motors
from hr_little_api.robot import Robot, MotorId, Animation
from hr_little_api.builders import MotorId, MotorCommandBuilder, SayCommandBuilder, \
    WalkCommandBuilder, MotorId, WalkDirection, WaitCommandBuilder, WaitType, CallbackCommandBuilder, CallbackType, \
    CommandListBuilder
from threading import Thread
import _thread
import numpy as np
import matplotlib.pyplot as plt
robot = Robot()
robot.connect()
path ='./Read/'
#'./read/'
headers = ['frame',' confidence',' AU01_r',' AU02_r',' AU04_r',' AU05_r',' AU07_r',' AU10_r',' AU12_r',' AU15_r',' AU25_r',' AU26_r',' AU20_r',' AU23_r',' AU01_c',' AU02_c',' AU04_c',' AU05_c',' AU07_c',' AU10_c',' AU12_c',' AU15_c',' AU25_c',' AU26_c',' AU20_c',' AU23_c',' AU45_c']

def avg(new_data,X,Nmin,Nmax,window_size = 30):    
    #new_data[X] = np.clip((new_data[X] - -1) / (3 - -1),Nmin,Nmax)
    b = moving_average(new_data[X],20)
    norm = [(float(i)-min(b))/(max(b)-min(b)) for i in b]
    df = pd.DataFrame({'X':norm})
    #new_data[X] = np.clip((new_data[X] - Nmin) / (Nmax - Nmin),0,1)
    #new_data = new_data[new_data[" confidence"] >=0.75]
    grouper = np.arange(df['X'].shape[0]) // window_size
    x=df['X'].groupby(grouper).mean()
    x=list(x)
    return x

def moving_average(values, window):
    weights = np.repeat(1.0, window) / window
    #z=np.convolve(values, weights, 'valid')
    #values.astype(float)
    return np.convolve(values, weights, 'valid')

#def new(df,z,Zmin,Zmax,window_size=30):
def new(df,z,window_size=25):
    #df[z] = Normalization(df,z,Zmin,Zmax)
    df[z] = Normalization(df,z)
    b = moving_average(df[z],2)
    b = np.array(b)
    dd = pd.DataFrame({'norm':b})
    grouper = np.arange(dd['norm'].shape[0]) // window_size
    x=dd['norm'].groupby(grouper).mean()
    x=list(x)
    
    return x

def yes(df,X,Nmin,Nmax):
    grouper = np.arange(df[X].shape[0]) // 100
    k=df[X].groupby(grouper).mean()
    k=list(k)
    ma= moving_average(k,1)
    norm1 = [np.clip((float(i)-Nmin)/(Nmax-Nmin),0,1) for i in ma]
    return norm1




'''def Normalization(df,z,Zmin,Zmax):
    return np.clip((df[z] - Zmin) / (Zmax - Zmin),0,1)'''      


def Normalization(df,z):
    return (df[z] - df[z].min()) / (df[z].max() - df[z].min())

def avg(new_data,X,window_size = 35):    
    grouper = np.arange(new_data[X].shape[0]) // window_size
    x=new_data[X].groupby(grouper).mean()
    x=list(x)
    return x

'''def Norm_rob(df,z):
    b = moving_average(df[z],30)
    norm = [(float(i)-1)/(3-1) for i in b]
    return norm



def norm_avg(df,m):
    norm= Norm_rob(df,m)
    df = pd.DataFrame({'norm':norm})
    av = avg(df,'norm',window_size = 10)
    #av = [i for i in av if i == i]
    return av'''

#a = input('Enter the user: Aerial, Marco, Manoj :', )
while True:
    print('------------------------------------------------------------------')
    txt_files = [f for f in os.listdir(path) if f.endswith('.csv')]
    first_idx = 0
    if len(txt_files)>0:
        file_name = os.path.join(path,txt_files[0])
        df = pd.read_csv(file_name) 
        
        print('----------------------------------------------------------------')
        
        while True:
            last_row = df.iloc[[-1]]
            last_idx = last_row.index[0]
            new_data = df[first_idx:]
            new_data = new_data[headers]
            
            df = pd.read_csv(file_name)
            t=df[' timestamp']
            
            x=yes(df,X=' AU02_r',Nmin=-1,Nmax=3)
            if x:
                eb=x[-1]
            else:
                eb
            #print(eb)

            
            
            x=yes(df,X=' AU05_r',Nmin=2,Nmax=-1)
            if x:
                el=x[-1]
            else:
                el
            #print(el)

            #print(df[' AU07_r'].min())
            #print(df[' AU07_r'].max())
            
            x=yes(df,X=' AU12_r',Nmin=3.5,Nmax=-1.71)
            if x:
                lc=x[-1]
            else:
                lc
            #print(lc)
            
            x=yes(df,X=' AU25_r',Nmin=0,Nmax=3.5)#Nmin=-0.5,Nmax=3.5
            if x:
                m=x[-1]
            else:
                m
            #print(m)

            print('eb=',eb, 'el=',el, 'lc=',lc, 'm=',m)

            '''xb=t[len(t)-len(x):]
            plt.plot(xb,x)
            plt.show()'''
            

            #print(df[' AU02_r'].min())
            #print(df[' AU02_r'].max())
            robot.do(
                #motor(MotorId.head_turn,0.5, 0.0),
                #motor(MotorId.head_pitch,1.0, 0.0),
                motor(MotorId.eyebrows,eb,0.0),
                motor(MotorId.eyelids,el,0.0),
                motor(MotorId.mouth,m,0.0),
                motor(MotorId.lip_corners,lc, 0.0),
                            )
          
            
            
            
            '''b = moving_average(df[' AU02_r'],5)
            xb=t[len(t)-len(b):]
            plt.plot(xb,b)
            plt.show()
            
            norm = [(float(i)-min(b))/(max(b)-min(b)) for i in b]
            xb=t[len(t)-len(norm):]
            plt.plot(xb,norm)
            plt.show()
            
            b = np.array(norm)
            dd = pd.DataFrame({'norm':b})
            grouper = np.arange(dd['norm'].shape[0]) // 30
            x=dd['norm'].groupby(grouper).mean()
            x=list(x)
            
            if x:
                m=x[-1]
            else:
                m
            xb=t[len(t)-len(x):]
            plt.plot(xb,x)
            plt.show()'''

            

            #for i in range(len(x)):
               
                
            

            #n = new(df,' AU12_r',Zmin=0,Zmax=-3)
            '''n = new(df,' AU02_r')
            if n:
                m=n[-1]
            else:
                m
            print(m)'''
            #print(df[' AU12_r'].min())
            #print(df[' AU12_r'].max())
            #print(len(n))
            
            

            #Eyebrows
            #x=norm_avg(df,' AU01_r')

            '''eb= norm_avg(df,' AU04_r')
            el= norm_avg(df,' AU07_r')
            m= norm_avg(df,' AU25_r')
            lc= norm_avg(df,' AU12_r')'''
            #print(len(eb),len(el),len(m),len(lc))
            #Final output of average of normalization of moving average of data(convert 30FPS to 1FPS)
            #for i in range(len(eb)):
                #print('eb',eb[i])
                #print('el',el[i])
                #print('lc',lc[i])
                #print('m',m[i])
            #x=avg(new_data,X=' AU01_r',Nmin=-1,Nmax=3,window_size = 30)#Nmin=-1,Nmax=3
            #x=avg(new_data,X=' AU04_r',Nmin=new_data[' AU04_r'].min(),Nmax=new_data[' AU04_r'].max(),window_size = 30)
            '''if x:
                eb=x[0]
            else:
                eb
            print(eb)''' 
            '''robot.do(
                motor(MotorId.head_turn,0.5, 0.0),
                motor(MotorId.head_pitch,1.0, 0.0),
                #motor(MotorId.eyebrows,eb,0.0),
                #motor(MotorId.eyelids,el,0.0),
                #motor(MotorId.mouth,m,0.1),
                motor(MotorId.lip_corners,m, 0.0),
                            )'''
             
            if first_idx == last_idx+1:
                for f in os.listdir(path):
                    try:
                        os.remove(os.path.join(path, f))
                    except:
                        q=1
            txt_files = [f for f in os.listdir(path) if f.endswith('.csv')]
            if len(txt_files)<1:
                break
            first_idx = last_idx+1
