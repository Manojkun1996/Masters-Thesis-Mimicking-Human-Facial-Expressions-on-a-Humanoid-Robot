import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
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
filename='./FianlTeset/webcam_2022-06-07-18-05.csv' #'./Read - Copy/Mano/eb.csv' #'./unRead/webcam_2022-04-19-15-27.csv' #



#print(df.head())
headers = [' timestamp',' confidence',' AU01_r',' AU02_r',' AU04_r',' AU05_r',' AU07_r',' AU10_r',' AU12_r',' AU15_r',' AU25_r',' AU26_r',' AU20_r',' AU23_r']

csv_name =['eb','el','lc','M']

def moving_average(values, window):
    weights = np.repeat(1.0, window) / window
    #z=np.convolve(values, weights, 'valid')
    #values.astype(float)
    return np.convolve(values, weights, 'valid')


def Normalization(df,z):
    return (df[z] - df[z].min()) / (df[z].max() - df[z].min())

def Norm_rob(df,z):
    b = moving_average(df[z],5)
    norm = [(float(i)-min(b))/(max(b)-min(b)) for i in b]
    return norm

def avg(new_data,X,window_size = 15):    
    grouper = np.arange(new_data[X].shape[0]) // window_size
    x=new_data[X].groupby(grouper).mean()
    x=list(x)
    return x

def norm_avg(df,m):
    norm= Norm_rob(df,m)
    df = pd.DataFrame({'norm':norm})
    av = avg(df,'norm',window_size = 15)
    #av = [i for i in av if i == i]
    '''if av:
        av=eb[0]
    else:
        av'''
    return av



df= pd.read_csv(filename)

#To find min and max values of a particular row
print(df[' AU15_r'].min())
print(df[' AU15_r'].max())

eb= norm_avg(df,' AU02_r')
el= norm_avg(df,' AU05_r')
m= norm_avg(df,' AU25_r')
lc= norm_avg(df,' AU15_r')




#Final output of average of normalization of moving average of data(convert 30FPS to 1FPS)
for i in range(len(eb)):
    print('eb',lc[i])
    #print('el',el[i])
    #print('lc',lc[i])
    #print('m',m[i])
    robot.do(
        motor(MotorId.head_turn,0.5, 0.0),
        motor(MotorId.head_pitch,1.0, 0.0),
        #motor(MotorId.eyelids,0.0,0.0),
        motor(MotorId.eyelids,el[i],0.0),
        motor(MotorId.eyebrows,eb[i],0.0),
        motor(MotorId.mouth,m[i],0.1),
        motor(MotorId.lip_corners,lc[i], 0.0),
        
        )
    '''robot.do(
        motor(MotorId.head_turn,0.5, 0.0),
        motor(MotorId.head_pitch,1.0, 0.0),
        motor(MotorId.eyelids,0.0,0.0),
        motor(MotorId.eyelids,el[i],0.0),
        motor(MotorId.eyebrows,eb[i],0.0),
        motor(MotorId.mouth,0.9,0.1),
        motor(MotorId.lip_corners,0.25, 0.0),
        
        )'''
'''for i in range(len(el)):
    print('el',el[i])
    robot.do(
        motor(MotorId.head_turn,0.5, 0.0),
        motor(MotorId.head_pitch,1.0, 0.0),
        motor(MotorId.eyelids,el[i],0.0),
        )'''
'''for i in range(len(m)):
    print('m',m[i])
    robot.do(
        motor(MotorId.head_turn,0.5, 0.0),
        motor(MotorId.head_pitch,1.0, 0.0),
        motor(MotorId.mouth,m[i],0.1),
        )'''
'''for i in range(len(lc)):
    print('lc',lc[i])
    robot.do(
        motor(MotorId.head_turn,0.5, 0.0),
        motor(MotorId.head_pitch,1.0, 0.0),
        motor(MotorId.lip_corners,lc[i], 0.0)
        )'''

#Normalization of moving average
'''norm = norm_rob(df,' AU01_r')
b = norm_rob(df,' AU02_r')
c = norm_rob(df,' AU04_r')
d = norm_rob(df,' AU012_r')
for i in range(len(norm)):
    print(norm[i])'''
