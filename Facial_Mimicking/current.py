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
path = './read/'
headers = ['frame',' confidence',' AU01_r',' AU02_r',' AU04_r',' AU05_r',' AU07_r',' AU10_r',' AU12_r',' AU15_r',' AU25_r',' AU26_r',' AU20_r',' AU23_r',' AU01_c',' AU02_c',' AU04_c',' AU05_c',' AU07_c',' AU10_c',' AU12_c',' AU15_c',' AU25_c',' AU26_c',' AU20_c',' AU23_c',' AU45_c']

def avg(new_data,X,Nmin,Nmax,window_size = 30):    
    #new_data[X] = np.clip((new_data[X] - -1) / (3 - -1),Nmin,Nmax)
    new_data[X] = np.clip((new_data[X] - Nmin) / (Nmax - Nmin),0,1)
    #new_data[X] = (new_data[X] - Nmin) / (Nmax - Nmin)
    new_data = new_data[new_data[" confidence"] >=0.0]
    grouper = np.arange(new_data[X].shape[0]) // window_size
    #print(len(grouper))
    x=new_data[X].groupby(grouper).mean()
    x=list(x)
    return x
'''robot.do(
    motor(MotorId.head_turn,0.5, 0.0),
    motor(MotorId.head_pitch,1.0, 0.0),
    )'''
while True:
    print('------------------------------------------------------------------')
    txt_files = [f for f in os.listdir(path) if f.endswith('.csv')]
    first_idx = 0
    if len(txt_files)>0:
        file_name = os.path.join(path,txt_files[0])
        df = pd.read_csv(file_name) 
        
        print('----------------------------------------------------------------')
        #a= input('Enter the user', )
        while True:
            last_row = df.iloc[[-1]]
            last_idx = last_row.index[0]
            new_data = df[first_idx:]
            new_data = new_data[headers]
            #Normalize column values
            #Eyebrows
            #new_data[' AU12_r']=(new_data[' AU12_r'])
            #new_data[' AU02_r']=(new_data[' AU02_r']*2.25+10)*0.04#eyebrows
            #new_data[' AU26_r']=(new_data[' AU26_r'])
            #new_data[' AU25_r']=(new_data[' AU25_r']) #*0.2
            #new_data[' AU01_r'] = np.clip((new_data[' AU01_r'] - 0) / (5 - 0),0.5,1)

            
            #a=new_data[' AU02_r'] = np.clip(((new_data[' AU02_r']*2+10)*0.05),0,1)
            
            #b=new_data[' AU02_r'] = np.clip(((new_data[' AU02_r']*3.33+10)*0.050),0,0.49)
            
            
            df = pd.read_csv(file_name)
            #t=df[' timestamp']

            #Eyebrows
            x=avg(new_data,X=' AU02_r',Nmin=-1,Nmax=3,window_size = 30)#Nmin=-1,Nmax=3
            #x=avg(new_data,X=' AU04_r',Nmin=new_data[' AU04_r'].min(),Nmax=new_data[' AU04_r'].max(),window_size = 30)
            if x:
                eb=x[0]
            else:
                eb
            #print(eb)
            
                      
            #Eyelids
            x=avg(new_data,X=' AU05_r',Nmin=2.0,Nmax=-1.0,window_size = 30)#Nmin=2.80,Nmax=-1.08
            if x:
                el=x[0]
            else:
                el
            

            
            #print(el)
            #print(df[' AU05_r'].min())
            #print(df[' AU05_r'].max())
                
            #Lip_corners
            x=avg(new_data,X=' AU12_r',Nmin=3.5,Nmax=-1.75,window_size = 30)#Nmin=3.5,Nmax=-1.71
            #x=avg(new_data,X=' AU12_r',Nmin=new_data[' AU12_r'].min(),Nmax=new_data[' AU12_r'].max(),window_size = 30)
            if x:
                lc=x[0]
            else:
                lc
            #print(lc)

            
            
            
            #Mouth
            x=avg(new_data,X=' AU25_r',Nmin=1.15,Nmax=3.85,window_size = 30)#Nmin=1,Nmax=4
            if x:
                m=x[0]
            else:
                m
            #print(m)
            '''xb=t[len(t)-len(x):]
            plt.plot(xb,x)
            plt.show()'''

            
            

            print('eb=',eb, 'el=',el, 'lc=',lc, 'm=',m)

            robot.do(
                motor(MotorId.head_turn,0.5, 0.0),
                motor(MotorId.head_pitch,1.0, 0.0),
                motor(MotorId.eyebrows,eb,0.0),
                motor(MotorId.eyelids,el,0.0),
                motor(MotorId.mouth,m,0.0),
                motor(MotorId.lip_corners,lc, 0.0),
                            )

            
        
            
            
            #print(avg(new_data,X=' AU02_r',window_size = 30))

            
            '''new_data[' AU02_r'] = np.clip((new_data[' AU02_r'] - 0) / (5 - 0),0,1)
            df = pd.read_csv(file_name)
            new_data = new_data[new_data[" confidence"] >=0.7]
            window_size = 30
            grouper = np.arange(new_data[' AU02_r'].shape[0]) // window_size
            x=new_data[' AU02_r'].groupby(grouper).mean()
            #x=x.to_frame()
            #x=x.values.to_list()
            #print('Eyebrows = ',x[0:100])
            x=list(x)
            #x= list(filter(None, x))
            if x:
                eb=x[0]
                print(eb)
            else:
                eb
            print(eb)'''
            '''robot.do(
                motor(MotorId.head_turn,0.5, 0.0),
                motor(MotorId.head_pitch,1.0, 0.0),
                motor(MotorId.eyebrows,eb,0.0)
                )'''
           
            if len(new_data>0):
                for index, row in new_data.iterrows():
                   '''robot.do(
                        motor(MotorId.head_turn,0.5, 0.0),
                        motor(MotorId.head_pitch,1.0, 0.0),
                        motor(MotorId.eyebrows,eb1,0.0),
                        #motor(MotorId.eyelids,el,0.0),
                        #motor(MotorId.mouth,m,0.1),
                        #motor(MotorId.lip_corners,lc, 0.0),
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
