import pandas as pd
import os
import time
import numpy as np
from hr_little_api.functional import say, motor, close_mouth, command_list, wait_for_motors_and_speaking, \
    head_turn_middle, neutral_eyebrows, frown_eyebrows, head_turn_right, head_turn_left, poke_tounge, wait, \
    raise_eyebrows, wait_for_motors, move_robot, eye_lid_close, eye_lid_open, reset_motors
from hr_little_api.robot import Robot, MotorId, Animation
from hr_little_api.builders import MotorId, MotorCommandBuilder, SayCommandBuilder, \
    WalkCommandBuilder, MotorId, WalkDirection, WaitCommandBuilder, WaitType, CallbackCommandBuilder, CallbackType, \
    CommandListBuilder
from threading import Thread
import _thread
robot = Robot()
robot.connect()



'''
k=10
while True:
    txt_files = [f for f in os.listdir(path) if f.endswith('.csv')]
    df = pd.read_csv(txt_files)
    last_row = df[-1]
    for f in os.listdir(path):
        os.remove(os.path.join(path, f))
    time.sleep(10)
'''
path = './read/'
headers = [' AU01_r',' AU02_r',' AU04_r',' AU05_r',' AU07_r',' AU10_r',' AU12_r',' AU15_r',' AU25_r',' AU26_r',' AU20_r',' AU23_r',' AU01_c',' AU02_c',' AU04_c',' AU05_c',' AU07_c',' AU10_c',' AU12_c',' AU15_c',' AU25_c',' AU26_c',' AU20_c',' AU23_c']

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
            #Normalize column values
            #Eyebrows
            #new_data[' AU02_r']=new_data([' AU02_r'])#eyebrows
            '''new_data[' AU05_r']=(new_data[' AU05_r'])#eyebrows
            new_data[' AU26_r']=(new_data[' AU26_r'])#lipcorners
            new_data[' AU15_r']=(new_data[' AU15_r'])'''
            #new_data[' AU01_r'] = np.clip((new_data[' AU01_r'] - 0) / (0.61 - 0),0,1)
    
            df = pd.read_csv(file_name)
            print(new_data[' AU01_r'])
            
            if len(new_data>0):
                for index, row in new_data.iterrows():

                    print(row[' AU02_r'])
                    '''if (row[' AU02_r'] > row[' AU01_r']) and (row[' AU02_r'] >row[' AU04_r']):
                        eb = 0.5
                    elif (row[' AU01_r'] > row[' AU02_r']) and (row[' AU01_r'] > row[' AU04_r']):
                        eb = 1.0
                    else:
                        eb = 0.0'''
                #print(row[' AU01_r'])

                #print('EB',row[' AU02_r'])

                    
                '''if (row[' AU05_c'] >= row[' AU07_c']):
                        el = 0.0
                    else:
                        el = 1.0

                    print('EL',el)

                    if (row[' AU10_c'] >= row[' AU12_c']) and (row[' AU10_c'] >= row[' AU15_c']):
                        lc = 0.0
                    elif (row[' AU12_c'] >= row[' AU10_c']) and (row[' AU12_c'] >= row[' AU15_c']):
                        lc = 1.0
                    else:
                        lc = 0.5

                    print('LC',lc)


                    if (row[' AU02_c'] > row[' AU01_c']):
                        m=1.0
                    else:
                        m=0.5

                    print('M',m)'''
                
                #print('eb', row[' AU02_r'])
                    #print('el', row[' AU05_r'])
                    #print('m',row[' AU25_r'])
                    #print('lp',row[' AU12_r'])
                robot.do(
                        motor(MotorId.head_turn,0.5, 0.0),
                        motor(MotorId.head_pitch,1.0, 0.0),
                        motor(MotorId.eyebrows,row[' AU02_r'],1.0),
                        #motor(MotorId.eyelids,el, 0.0),
                        #motor(MotorId.lip_corners,lc, 0.0),
                        motor(MotorId.mouth,0,0),
                        
                        
                            )
                    
                
        
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


        
    
