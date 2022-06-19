from hr_little_api.functional import say, motor, close_mouth, command_list, wait_for_motors_and_speaking, \
    head_turn_middle, neutral_eyebrows, frown_eyebrows, head_turn_right, head_turn_left, poke_tounge, wait, \
    raise_eyebrows, wait_for_motors, move_robot, eye_lid_close, eye_lid_open, reset_motors
from hr_little_api.robot import Robot, MotorId, Animation
from hr_little_api.builders import MotorId, MotorCommandBuilder, SayCommandBuilder, \
    WalkCommandBuilder, MotorId, WalkDirection, WaitCommandBuilder, WaitType, CallbackCommandBuilder, CallbackType, \
    CommandListBuilder
from threading import Thread
import time
import os

import _thread
import time
robot = Robot()
robot.connect()

# Define a function for the thread


def print_time(threadname, delay):

    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("{}: {} : {}".format(threadname, time.ctime(time.time()), "This is from name function\n"))
      
def constant_thread(x,y):
    count = 0
    while True:
        count += 1
        time.sleep(0.01)
        robot.do(
           #set_motors(x,y),
            arousal(x),
            valence(y),

        )
'''def thread_function(X,x,y):
   
    count = 0
    while count < X:
       try:
          #X = int(input("how many times you want to give command "))
           time.sleep(1)
           robot.do(
                        
               set_motors(x,y),
                        
                            )
          
       except Exception as ex:
         print(type(ex).__name__, ex.args)'''
       
'''DUMMY FUNCTION - USE ORIGINAL 1'''
'''def set_motors(x,y): #working function
    """ Reset motors animation.

    :return: the animation command.
    """

    return command_list(
        motor(MotorId.lip_corners, y*0.05, 1.0),
        motor(MotorId.eyebrows,y*0.1, 1.0),
        motor(MotorId.eyelids, 1-(x*0.1), 1.0),
        #motor(MotorId.head_pitch, y, 1.0),
        motor(MotorId.head_turn, 0.5, 1.0),
        motor(MotorId.mouth, x*0.05, 1.0),
        wait_for_motors()
    )'''
def arousal(x):
    EL = (1-(0.55+(x-1)*0.05))
    M = (x+10)*(0.025)
    HP = (x+10)*0.05

    if x == -10:
        HP = 0.05
    
    return command_list(
        motor(MotorId.head_pitch, HP, 1.0),
        motor(MotorId.eyelids, EL, 1.0),
        motor(MotorId.mouth, M, 1.0),
        wait(0.1),
        wait_for_motors(),
    )



def valence(y):

    EB = (y+10)*0.05
    LC = 1-(0.55+(y-1)*0.05)
    #HT = (y+10)*0.05
    
    
    return command_list(
        motor(MotorId.head_turn, 0.5, 1.0),
        motor(MotorId.eyebrows, EB, 1.0),
        motor(MotorId.lip_corners, LC, 1.0),
        wait(0.1),
        wait_for_motors(),
        )

def print_aroual(x):
    EL = (1-(0.55+(x-1)*0.05))
    M = (x+10)*(0.025)
    HP = (x+10)*0.05
    return print("(-10(1.0)  0(0.5)  +10(0.0)Eyelids=", (EL)),print("(-10(0.0)  0(0.25)  +10(0.5)Mouth=", (M)),  print("(-10(0.0)  0(0.5)  +10(1.0)HeadPitch=", (HP))  

def print_valence(y):
    EB = (y+10)*0.05
    LC = 1-(0.55+(y-1)*0.05)
 
    return print("(-10(0.0)  0(0.5)  +10(1.0)Eyebrows=", (EB)),print("-10(1.0)  0(0.5)  +10(0.0)Lipcorners=", (LC))

# Create two threads as follows
X = int(input("how many times you want to give command "))

for i in range(X):
#print("lip_corners, eyebrows, eyelids ,head_pitch ,head_turn ,mouth")
    x=float(input("Enter the Arousal(Eyelids, Mouth )"        ))
    y=float(input("Enter the Valence(Eyebrows, Lipcorners) " ))

    print_aroual(x)
    print_valence(y)

    print('-------------------------NEXT Command---------------------------------')
    


    _thread.start_new_thread( constant_thread, (x,y))
        

robot.disconnect()

   
    



