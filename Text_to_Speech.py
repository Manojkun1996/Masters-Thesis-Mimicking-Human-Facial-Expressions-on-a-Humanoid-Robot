from hr_little_api.robot import Robot
from hr_little_api.functional import say, go_crazy, poke_tounge, right_arm_point, walk_forward
from hr_little_api.robot import Animation
from hr_little_api.functional import say, go_crazy, poke_tounge, right_arm_point, walk_forward





robot = Robot()
robot.connect()

import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text1 = r.recognize_google(audio)
        print("You said : {}".format(text1))
        
        robot.say ("{}".format(text1))



    except:
        x = print("Sorry could not recognize what you said")

        

    
   




    
