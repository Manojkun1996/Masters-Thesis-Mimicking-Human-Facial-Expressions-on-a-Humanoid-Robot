from hr_little_api.functional import say, motor, close_mouth, command_list, wait_for_motors_and_speaking, \
    head_turn_middle, neutral_eyebrows, frown_eyebrows, head_turn_right, head_turn_left, poke_tounge, wait, \
    raise_eyebrows, wait_for_motors
from hr_little_api.robot import Robot, MotorId, logbook
from hr_little_api.robot import Robot, Animation


robot=Robot()
robot.connect()


#Expressions

# All the EyeBrows Movements

cheeky_eyebrow_raise_cmd = command_list(
    motor(MotorId.eyebrows, 0.0, 0.5),  # move the eyebrow motor to position 0.0 in 0.5 seconds
    
    motor(MotorId.eyebrows, 1.0, 0.5),  # move the eyebrow motor to position 1.0 in 0.5 seconds
    
    motor(MotorId.eyebrows, 0.0, 0.5),  # move the eyebrow motor to position 0.0 in 0.5 seconds
     

    motor(MotorId.eyebrows, 1.0, 0.5),  # move the eyebrow motor to position 1.0 in 0.5 seconds
    
    motor(MotorId.eyebrows, 0.0, 0.5),  # move the eyebrow motor to position 0.0 in 0.5 seconds
    
    motor(MotorId.eyebrows, 1.0, 0.5),  # move the eyebrow motor to position 1.0 in 0.5 seconds
    
)

robot.do(

    cheeky_eyebrow_raise_cmd,
    cheeky_eyebrow_raise_cmd,
    
)


frown_eyebrow_raise_cmd = command_list(
    motor(MotorId.eyebrows, 0.5, 0.5),  # move the eyebrow motor to position 0.0 in 0.5 seconds
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),  # wait for a time
)
robot.do(
    say("frown Eyebrows"),
    wait(1.0),
    frown_eyebrow_raise_cmd,

    )
neutral_eyebrow_raise_cmd = command_list(
    motor(MotorId.eyebrows, 0.0, 0.5),  # move the eyebrow motor to position 0.0 in 0.5 seconds
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),  # wait for a time
)
robot.do(
    say("neutral Eyebrows"),
    wait(1.0),
    neutral_eyebrow_raise_cmd,

    )

eye_lid_open= command_list(
    

    motor(MotorId.eyelids, 0.2, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),

    motor(MotorId.eyelids, 0.5, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
    
    motor(MotorId.eyelids, 0.7, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),

    motor(MotorId.eyelids, 1, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
)

eye_lid_close= command_list(    

    motor(MotorId.eyelids,1 , 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),

    motor(MotorId.eyelids, 0.8, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),

    motor(MotorId.eyelids, 0.6, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),

    motor(MotorId.eyelids, 0.4, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),

    motor(MotorId.eyelids, 0, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
    

)

#Eyelid Movements    
robot.do(
    say("close Eyelid"),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
    
    eye_lid_open,
    eye_lid_open,

    
    say("open Eyelids"),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
    
    eye_lid_close,
    eye_lid_close,
    
    
    )

#mouth Movements
open_mouth= command_list(    

    motor(MotorId.mouth,0.3, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),

    motor(MotorId.mouth,0.8 , 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),

    motor(MotorId.mouth,1 , 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
)
robot.do(

    say("open Mouth"),
    wait_for_motors(),
    wait(0.2),

    open_mouth,

    )
close_mouth= command_list(    

    motor(MotorId.mouth,1, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),

    motor(MotorId.mouth,0.7 , 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),

    motor(MotorId.mouth,0.5 , 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),

    motor(MotorId.mouth,0 , 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
)
robot.do(
    say("close Mouth"),
    wait_for_motors(),
    wait(0.2),

    close_mouth,
    
    )
mouth_neutral= command_list(    

    motor(MotorId.lip_corners,0.5, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
)

robot.do(
    say("Mouth Neutral"),
    wait_for_motors(),
    wait(0.2),

    mouth_neutral,
    
    )
mouth_frown= command_list(    

    motor(MotorId.lip_corners,1, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
)    
robot.do(
    say("Mouth Frown"),
    wait_for_motors(),
    wait(0.2),

    mouth_frown,
    
    )
#Poke Tounge


poke_tounge= command_list(
    motor(MotorId.mouth,1 , 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
)    
robot.do(
    say("Poke Toungue"),
    wait_for_motors(),
    wait(0.2),

    poke_tounge,
    poke_tounge,
    
    )

#Head Movements

head_down= command_list(    

    motor(MotorId.head_pitch, 0, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
)    
robot.do(
    say("head_down"),
    wait_for_motors(),
    wait(0.2),

    head_down,
    
    )

head_middle= command_list(    

    motor(MotorId.head_pitch, 0.5, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
)    
robot.do(
    say("head_middle"),
    wait_for_motors(),
    wait(0.2),

    head_middle,
    
    )

head_up= command_list(    

    motor(MotorId.head_pitch, 1, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
)    
robot.do(
    say("head_up"),
    wait_for_motors(),
    wait(0.2),

    head_up,
    
    )

head_turn_left= command_list(    

    motor(MotorId.head_turn, 1, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
)    
robot.do(
    say("head_turn_left"),
    wait_for_motors(),
    wait(0.2),

    head_turn_left,
    
    )
head_turn_middle= command_list(    

    motor(MotorId.head_turn, 0.5, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
)    
robot.do(
    say("head_turn_middle"),
    wait_for_motors(),
    wait(0.2),

    head_turn_middle,
    
    )

head_turn_right= command_list(    

    motor(MotorId.head_turn, 0, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
)    
robot.do(
    say("head_turn_right"),
    wait_for_motors(),
    wait(0.2),

    head_turn_right,
    
    )

awkward=command_list(
    

        motor(MotorId.lip_corners, 0.7, 1.0),
        motor(MotorId.eyebrows, 0.3, 1.0),
        motor(MotorId.head_pitch, 1.0, 1.0),
        wait(0.6),

        motor(MotorId.eyelids, 1.0, 0.3),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.0, 0.3),
        wait(0.3),

        motor(MotorId.lip_corners, 0.6, 0.2),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.2, 0.5),
        motor(MotorId.eyebrows, 0.38, 0.5),
        motor(MotorId.eyelids, 0.43, 0.5),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.4, 0.1),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.26, 0.2),
        motor(MotorId.eyebrows, 0.43, 0.2),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.7, 0.7),
        motor(MotorId.eyebrows, 0.5, 0.7),
        motor(MotorId.eyelids, 0.0, 0.7),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.5, 1.0),
        motor(MotorId.head_pitch, 0.5, 1.0),
        wait_for_motors()
    )

robot.do(
    say("Im feeling very awkward"),
    wait_for_motors(),
    wait(0.2),

    awkward,
    
    )

smile= command_list(    

    motor(MotorId.head_pitch, 0, 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
)    
robot.do(
    say("smile"),
    wait_for_motors(),
    wait(0.2),

    smile,
    
    )

cute1=command_list(
        

        motor(MotorId.lip_corners, 0.37, 0.2),
        motor(MotorId.eyebrows, 1.0, 0.2),
        motor(MotorId.eyelids, 1.0, 0.2),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.14, 0.2),
        motor(MotorId.eyelids, 0.0, 0.2),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.0, 0.2),
        wait(0.4),

        motor(MotorId.eyelids, 1.0, 0.2),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.0, 0.2),
        wait_for_motors(),

        motor(MotorId.eyelids, 1.0, 0.2),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.0, 0.2),
        wait_for_motors(),
    )
robot.do(
    say("Im cute, AM I??"),
    wait_for_motors(),
    wait(0.2),

    cute1,
    
    )

Worry=command_list(
       

        motor(MotorId.eyebrows, 0.05, 0.2),
        motor(MotorId.eyelids, 0.74, 0.2),
        motor(MotorId.head_pitch, 0.28, 0.2),
        motor(MotorId.head_turn, 0.68, 0.2),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.3, 0.1),
        motor(MotorId.eyelids, 1.0, 0.1),
        motor(MotorId.head_pitch, 0.2, 0.1),
        motor(MotorId.head_turn, 0.58, 0.1),
        motor(MotorId.mouth, 0.26, 0.1),
        wait_for_motors(),

        motor(MotorId.eyebrows, 1.0, 0.2),
        motor(MotorId.eyelids, 0.0, 0.2),
        motor(MotorId.head_pitch, 1.0, 0.2),
        motor(MotorId.head_turn, 0.29, 0.2),
        motor(MotorId.mouth, 1.0, 0.2),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.86, 0.2),
        motor(MotorId.eyebrows, 0.0, 0.2),
        motor(MotorId.eyelids, 0.5, 0.2),
        motor(MotorId.head_pitch, 0.98, 0.2),
        motor(MotorId.head_turn, 0.0, 0.2),
        motor(MotorId.mouth, 0.0, 0.2),
        wait_for_motors(),

        motor(MotorId.head_pitch, 0.94, 0.1),
        motor(MotorId.head_turn, 0.5, 0.1),
        wait_for_motors(),

        motor(MotorId.head_pitch, 0.9, 0.1),
        motor(MotorId.head_turn, 1.0, 0.1),
        wait_for_motors(),

        motor(MotorId.head_pitch, 0.86, 0.1),
        motor(MotorId.head_turn, 0.5, 0.1),
        wait_for_motors(),

        motor(MotorId.head_pitch, 0.82, 0.1),
        motor(MotorId.head_turn, 0.0, 0.1),
        wait_for_motors(),

        motor(MotorId.head_pitch, 0.78, 0.1),
        motor(MotorId.head_turn, 0.43, 0.1),
        wait_for_motors(),

        motor(MotorId.head_pitch, 0.74, 0.1),
        motor(MotorId.head_turn, 0.87, 0.1),
        wait_for_motors(),

        motor(MotorId.head_pitch, 0.66, 0.2),
        motor(MotorId.head_turn, 0.29, 0.2),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.73, 0.1),
        motor(MotorId.head_pitch, 0.62, 0.1),
        motor(MotorId.head_turn, 0.31, 0.1),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.6, 0.1),
        motor(MotorId.eyebrows, 0.08, 0.1),
        motor(MotorId.eyelids, 0.75, 0.1),
        motor(MotorId.head_pitch, 0.58, 0.1),
        motor(MotorId.head_turn, 0.36, 0.1),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.24, 0.1),
        motor(MotorId.eyelids, 1.0, 0.1),
        motor(MotorId.head_pitch, 0.55, 0.1),
        motor(MotorId.head_turn, 0.42, 0.1),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.5, 0.2),
        motor(MotorId.eyelids, 0.2, 0.2),
        motor(MotorId.head_pitch, 0.5, 0.2),
        motor(MotorId.head_turn, 0.5, 0.2),
        wait_for_motors(),

        motor(MotorId.eyelids, 1.0, 0.2),
        motor(MotorId.eyelids, 0.0, 0.2),
        motor(MotorId.eyelids, 0.2, 0.2),
        wait_for_motors()
    )
robot.do(
    say("IM Worried. Please dont ask me why??"),
    wait_for_motors(),
    wait(0.2),

    Worry,
    
    )

wake_up=command_list(
    
        wait(seconds=0.9),

        motor(MotorId.eyebrows, 1.0, 0.5),
        motor(MotorId.eyelids, 1.0, 0.5),
        motor(MotorId.head_pitch, 0.2415, 0.5),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.5, 0.3),
        wait_for_motors(),

        motor(MotorId.eyelids, 1.0, 0.1),
        motor(MotorId.eyelids, 1.0, 0.04),
        wait_for_motors(),

        motor(MotorId.eyebrows, 1.0, 0.2),
        motor(MotorId.eyelids, 0.734, 0.16),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.465, 0.2),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.555, 0.4),
        wait_for_motors(),

        motor(MotorId.eyelids, 1.0, 0.2),
        motor(MotorId.eyelids, 0.921, 0.1),
        motor(MotorId.head_pitch, 0.2415, 0.1),
        motor(MotorId.head_pitch, 0.508, 0.2),
        motor(MotorId.mouth, 0.0, 0.1),
        motor(MotorId.mouth, 0.51, 0.2),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.748, 0.1),
        motor(MotorId.head_pitch, 0.5465, 0.1),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.332, 0.2),
        motor(MotorId.head_pitch, 0.516, 0.2),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.411, 0.2),
        motor(MotorId.head_pitch, 0.525, 0.2),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.431, 0.1),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.437, 0.3),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.446, 0.3),
        motor(MotorId.head_pitch, 0.4465, 0.3),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.583, 0.1),
        motor(MotorId.head_pitch, 0.439, 0.1),
        motor(MotorId.head_turn, 0.4775, 0.1),
        motor(MotorId.mouth, 0.446, 0.1),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.988, 0.1),
        motor(MotorId.head_pitch, 0.499, 0.1),
        motor(MotorId.head_turn, 0.3735, 0.1),
        motor(MotorId.mouth, 0.215, 0.1),
        wait_for_motors(),

        motor(MotorId.eyelids, 1.0, 0.1),
        motor(MotorId.eyelids, 0.635, 0.1),
        motor(MotorId.head_pitch, 0.629, 0.2),
        motor(MotorId.head_turn, 0.196, 0.2),
        motor(MotorId.mouth, 0.0, 0.2),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.135, 0.2),
        motor(MotorId.head_turn, 0.145, 0.2),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.4675, 0.2),
        motor(MotorId.eyebrows, 0.82, 0.2),
        motor(MotorId.eyelids, 0.65, 0.2),
        motor(MotorId.head_pitch, 0.546, 0.2),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.4035, 0.2),
        motor(MotorId.eyebrows, 0.63, 0.2),
        motor(MotorId.eyelids, 0.792, 0.16),
        motor(MotorId.eyelids, 0.724, 0.08),
        motor(MotorId.head_pitch, 0.496, 0.2),
        motor(MotorId.head_turn, 0.3395, 0.2),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.334, 0.2),
        motor(MotorId.eyebrows, 0.512, 0.2),
        motor(MotorId.eyelids, 0.275, 0.16),
        motor(MotorId.head_pitch, 0.527, 0.2),
        motor(MotorId.head_turn, 0.642, 0.2),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.294, 0.2),
        motor(MotorId.eyebrows, 0.56, 0.2),
        motor(MotorId.eyelids, 0.135, 0.2),
        motor(MotorId.head_pitch, 0.5585, 0.2),
        motor(MotorId.head_turn, 0.735, 0.2),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.2255, 0.2),
        motor(MotorId.eyebrows, 0.774, 0.2),
        motor(MotorId.eyelids, 1.0, 0.2),
        motor(MotorId.head_pitch, 0.613, 0.2),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.172, 0.1),
        motor(MotorId.eyebrows, 0.935, 0.1),
        motor(MotorId.eyelids, 0.245, 0.1),
        motor(MotorId.head_pitch, 0.629, 0.1),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.0, 0.7),
        motor(MotorId.eyebrows, 1.0, 0.2),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.0, 0.2),
        motor(MotorId.eyelids, 0.707, 0.2),
        motor(MotorId.head_pitch, 0.652, 0.2),
        motor(MotorId.head_pitch, 0.652, 0.00333333333333),
        motor(MotorId.head_turn, 0.627, 0.2),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.0, 0.3),
        motor(MotorId.eyelids, 1.0, 0.3),
        motor(MotorId.head_pitch, 0.5975, 0.296666666667),
        motor(MotorId.head_turn, 0.447, 0.3),
        wait_for_motors(),

        motor(MotorId.head_pitch, 0.57, 0.2),
        motor(MotorId.head_turn, 0.4385, 0.2),
        wait_for_motors(),

        motor(MotorId.head_pitch, 0.5385, 0.3),
        motor(MotorId.head_turn, 0.409, 0.3),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.971, 0.3),
        motor(MotorId.head_pitch, 0.507, 0.3),
        motor(MotorId.head_turn, 0.3815, 0.3),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.821, 0.3),
        motor(MotorId.head_pitch, 0.5485, 0.3),
        motor(MotorId.head_turn, 0.372, 0.3),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.512, 0.7),
        motor(MotorId.eyelids, 0.135, 0.7),
        motor(MotorId.head_pitch, 0.5225, 0.7),
        motor(MotorId.head_turn, 0.449, 0.7),
        wait_for_motors(),

        motor(MotorId.head_pitch, 0.5015, 0.6),
        motor(MotorId.head_turn, 0.543, 0.6),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0., 0.3),
        motor(MotorId.head_pitch, 0.492, 0.3),
        motor(MotorId.head_turn, 0.563, 0.3),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.05, 0.8),
        motor(MotorId.head_pitch, 0.4455, 0.8),
        motor(MotorId.head_turn, 0.457, 0.8),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.115, 0.2),
        motor(MotorId.eyelids, 1.0, 0.2),
        motor(MotorId.head_pitch, 0.454, 0.2),
        motor(MotorId.head_turn, 0.419, 0.2),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.166, 0.3),
        motor(MotorId.eyelids, 0.327, 0.3),
        motor(MotorId.head_pitch, 0.471, 0.3),
        motor(MotorId.head_turn, 0.402, 0.3),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.1805, 0.1),
        motor(MotorId.eyelids, 0.114, 0.1),
        motor(MotorId.head_pitch, 0.4765, 0.1),
        motor(MotorId.head_turn, 0.4025, 0.1),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.2875, 0.7),
        motor(MotorId.eyelids, 0.121, 0.7),
        motor(MotorId.head_pitch, 0.52, 0.7),
        motor(MotorId.head_turn, 0.4655, 0.7),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.135, 1.0),
        motor(MotorId.head_pitch, 0.4905, 1.0),
        motor(MotorId.head_turn, 0.548, 1.0),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.135, 0.1),
        motor(MotorId.head_pitch, 0.4855, 0.1),
        motor(MotorId.head_turn, 0.547, 0.1),
        wait_for_motors(),

        motor(MotorId.eyelids, 1.0, 0.3),
        motor(MotorId.head_pitch, 0.4735, 0.3),
        motor(MotorId.head_turn, 0.5375, 0.3),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.114, 0.3),
        motor(MotorId.head_pitch, 0.459, 0.3),
        motor(MotorId.head_turn, 0.524, 0.3),
        wait_for_motors(),

        motor(MotorId.head_pitch, 0.4345, 0.6),
        motor(MotorId.head_turn, 0.506, 0.6),
        wait_for_motors(),

        motor(MotorId.head_pitch, 0.4295, 0.3),
        motor(MotorId.head_turn, 0.504, 0.3),
        wait_for_motors(),

        motor(MotorId.head_pitch, 0.568, 1.1),
        motor(MotorId.head_turn, 0.469, 1.1),
        wait_for_motors(),

        motor(MotorId.head_turn, 0.4435, 1.3),
        wait_for_motors()
    )
robot.do(
    say(" I woke up just now. I badly need a coffee"),
    wait_for_motors(),
    wait(0.2),

     wake_up,
    
    )  

Sleepy=command_list(
        

        motor(MotorId.eyebrows, 1.0, 0.6),
        motor(MotorId.eyelids, 0.5, 0.6),
        motor(MotorId.head_pitch, 0.7, 0.6),
        motor(MotorId.mouth, 0.5, 0.6),
        wait_for_motors(),

        motor(MotorId.head_pitch, 0.57, 0.4),
        wait_for_motors(),

        motor(MotorId.head_pitch, 0.49, 0.2),
        motor(MotorId.mouth, 0.4, 0.2),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.81, 0.3),
        motor(MotorId.eyelids, 0.64, 0.3),
        motor(MotorId.head_pitch, 0.4, 0.3),
        motor(MotorId.mouth, 0.11, 0.3),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.74, 0.1),
        motor(MotorId.eyelids, 0.67, 0.1),
        motor(MotorId.head_pitch, 0.41, 0.1),
        motor(MotorId.mouth, 0.03, 0.1),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.7, 0.1),
        motor(MotorId.head_pitch, 0.43, 0.1),
        motor(MotorId.mouth, 0.0, 0.1),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.78, 0.2),
        motor(MotorId.head_pitch, 0.49, 0.2),
        motor(MotorId.mouth, 0.06, 0.2),
        wait_for_motors(),

        motor(MotorId.eyebrows, 1.0, 0.4),
        motor(MotorId.eyelids, 0.43, 0.4),
        motor(MotorId.head_pitch, 0.6, 0.4),
        motor(MotorId.mouth, 0.37, 0.4),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.4, 0.1),
        motor(MotorId.head_pitch, 0.62, 0.1),
        motor(MotorId.mouth, 0.43, 0.1),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.4, 0.2),
        motor(MotorId.head_pitch, 0.65, 0.2),
        motor(MotorId.mouth, 0.5, 0.2),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.41, 0.4),
        motor(MotorId.head_pitch, 0.72, 0.4),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.92, 0.1),
        motor(MotorId.eyelids, 0.42, 0.1),
        motor(MotorId.head_pitch, 0.72, 0.1),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.76, 0.1),
        motor(MotorId.eyelids, 0.43, 0.1),
        motor(MotorId.head_pitch, 0.71, 0.1),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.5, 0.2),
        motor(MotorId.eyelids, 0.5, 0.2),
        motor(MotorId.head_pitch, 0.65, 0.2),
        motor(MotorId.mouth, 0.25, 0.2),
        wait_for_motors(),

        motor(MotorId.eyelids, 1.0, 0.2),
        motor(MotorId.head_pitch, 0.0, 0.2),
        motor(MotorId.mouth, 0.0, 0.2),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.58, 0.1),
        motor(MotorId.eyelids, 0.5, 0.1),
        motor(MotorId.head_pitch, 0.35, 0.1),
        motor(MotorId.mouth, 0.13, 0.1),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.71, 0.1),
        motor(MotorId.eyebrows, 0.75, 0.1),
        motor(MotorId.eyelids, 0.0, 0.1),
        motor(MotorId.head_pitch, 0.7, 0.1),
        motor(MotorId.mouth, 0.36, 0.1),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.8, 0.1),
        motor(MotorId.eyebrows, 1.0, 0.1),
        motor(MotorId.head_pitch, 0.62, 0.1),
        motor(MotorId.mouth, 0.5, 0.1),
        wait_for_motors(),

        motor(MotorId.head_pitch, 0.55, 0.1),
        motor(MotorId.head_pitch, 0.65, 0.2),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.99, 0.3),
        motor(MotorId.head_pitch, 0.64, 0.3),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.98, 0.1),
        motor(MotorId.eyelids, 0.5, 0.1),
        motor(MotorId.head_pitch, 0.63, 0.1),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.97, 0.1),
        motor(MotorId.eyelids, 1.0, 0.1),
        motor(MotorId.head_pitch, 0.62, 0.1),
        motor(MotorId.head_turn, 0.54, 0.1),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.94, 0.2),
        motor(MotorId.eyelids, 0.0, 0.2),
        motor(MotorId.head_pitch, 0.61, 0.2),
        motor(MotorId.head_turn, 0.65, 0.2),
        motor(MotorId.mouth, 0.13, 0.2),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.93, 0.1),
        motor(MotorId.head_pitch, 0.6, 0.1),
        motor(MotorId.mouth, 0.0, 0.1),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.92, 0.1),
        motor(MotorId.head_pitch, 0.59, 0.1),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.91, 0.1),
        motor(MotorId.head_pitch, 0.58, 0.1),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.87, 0.3),
        motor(MotorId.head_pitch, 0.55, 0.3),
        motor(MotorId.head_turn, 0.4, 0.3),
        wait_for_motors(),

        motor(MotorId.eyebrows, 0.81, 0.5),
        motor(MotorId.head_pitch, 0.51, 0.5),
        wait_for_motors(),

        motor(MotorId.lip_corners, 0.5, 0.2),
        motor(MotorId.eyebrows, 0.8, 0.2),
        motor(MotorId.head_pitch, 0.5, 0.2),
        motor(MotorId.head_turn, 0.5, 0.2),
        wait_for_motors(),
    )    
robot.do(
    say("IM tired and Sleepy"),
    wait_for_motors(),
    wait(0.2),

    Sleepy,
    
    )

#sleep with open mouth
yes_cmd=command_list(
        motor(MotorId.mouth, 1, 0.0),
        wait(0.5),
        motor(MotorId.head_pitch, 1, 0.0),
        wait(0.5),
        motor(MotorId.eyebrows, 1, 0.0),
        wait(0.5),
        motor(MotorId.eyelids, 1, 0.0),
        wait(0.5),
        
        motor(MotorId.head_turn, 1, 0.0),
        wait(0.5),
        
        motor(MotorId.lip_corners, 1, 0.0),
        wait(seconds=0.7)
    )

robot.do(

    say('I sleep with my mouth open'),
    
    yes_cmd,
    yes_cmd,
    yes_cmd,

    )
#go crazy 2
go_crazy2=command_list(
        motor(MotorId.eyelids, 1, 0.5),
        wait(1.5),

        motor(MotorId.head_turn, 0, 0.1),
        wait(0.8),

        motor(MotorId.head_turn, 1, 0.2),
        wait(0.5),

        motor(MotorId.head_turn, 0.5, 0.2),
        wait_for_motors(),

        motor(MotorId.mouth, 0, 0.1),
        motor(MotorId.eyebrows, 1, 0.1),
        wait_for_motors(),

        motor(MotorId.mouth, 1, 0.1),
        wait_for_motors(),

        motor(MotorId.eyelids, 0.0, 0.5),
        wait_for_motors()
    )
robot.do(

    say('IM going crazy again'),
    go_crazy2,
    go_crazy2,
    go_crazy2,

    )


robot.disconnect()
