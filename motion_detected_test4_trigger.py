from gpiozero import MotionSensor import OutputDevice
from time import sleep
import os, random

def rndmp3 ():
    randomfile = random.choice(os.listdir("/home/pi/Desktop/Audio/"))
    file = ' \'/home/pi/Desktop/Audio/'+ randomfile + '\''
    os.system ('omxplayer -o local' + file)
    print(file)

pir = MotionSensor(4)
el_arduino = OutputDevice(17)
while True:
    time.sleep(5) # delays for 5 seconds
    if pir.motion_detected:   
        print("Motion detected!")
        rndmp3 ()
	print("In Delay")
	    el_arduino.on()  //turn on pin 17 send signal to arduino
        time.sleep(30) # delays for 30 seconds
	    el_arduino.off()  //turn off pin 17 stops arduino
    else:
        print("NO Motion!")

print("DONE")
    


