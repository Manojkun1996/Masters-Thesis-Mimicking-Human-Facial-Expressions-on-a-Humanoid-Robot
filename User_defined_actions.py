from hr_little_api.functional import say, motor, close_mouth, command_list, wait_for_motors_and_speaking, \
    head_turn_middle, neutral_eyebrows, frown_eyebrows, head_turn_right, head_turn_left, poke_tounge, wait, \
    raise_eyebrows, wait_for_motors, move_robot, eye_lid_close,go_crazy3
from hr_little_api.robot import Robot, MotorId
from hr_little_api.robot import Robot, Animation
from hr_little_api.builders import MotorId
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List
from hr_little_api.builders import MotorCommandBuilder, SayCommandBuilder, \
    WalkCommandBuilder, MotorId, WalkDirection, WaitCommandBuilder, WaitType, CallbackCommandBuilder, CallbackType, \
    CommandListBuilder

robot=Robot()
robot.connect()

X = int(input("how many times you want to give command "))

for i in range(X):
    print("lip_corners, eyebrows, eyelids ,head_pitch ,head_turn ,mouth")

    
    x=input("motorid ")
    y=float(input("Enter the Motor position(0.0 -1.0) " ))
    z=float(input("Enter the time delay(0.0 -1.0))" ))
     
    robot.do(
            
        move_robot(x,y,z),
            
                )

# To repeat the movement for n Times



'''X = int(input("how many times you want to give command "))
print("lip_corners, eyebrows, eyelids ,head_pitch ,head_turn ,mouth")
x=input("motorid ")

    
for i in range(X):
    
    #y=float(input("Enter the Motor position(0.0 -1.0) " ))
    #y1=float(input("Enter the Motor position 2(0.0 -1.0) " ))
    
    
    

    robot.do(
                
        move_robot(x,1.0,1.0),
        
          
        )
    robot.do(
                
        move_robot(x,0.0,0.0),
          
                )'''
    


    

