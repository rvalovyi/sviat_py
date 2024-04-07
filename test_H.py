#!/usr/bin/env/python
#import ultra
import RPi.GPIO as GPIO
import time

def checkdist_():
    GPIO.output(Tr, GPIO.HIGH) # Set the input end of the module to high level and emit an initial sound wave
    time.sleep(0.000015)
    GPIO.output(Tr, GPIO.LOW)
    while not GPIO.input(Ec): # When the module no longer receives the initial sound wave
        pass
    t1 = time.time() # Note the time when the initial sound wave is emitted
    while GPIO.input(Ec): # When the module receives the return sound wave
        pass
    t2 = time.time() # Note the time when the return sound wave is captured
    return round((t2-t1)*340/2,2) # Calculate distance
    
if __name__ == '__main__':
    Tr = 11 # Pin number of input terminal of ultrasonic module
    Ec = 8 # Pin number of output terminal of ultrasonic module
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Tr, GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(Ec, GPIO.IN)    

    time.sleep(5)

    GPIO.output(Tr, GPIO.HIGH)
    print("High")
    time.sleep(5)
    GPIO.output(Tr, GPIO.LOW)
    print("Low")

#    for i in range(10):
#        print(checkdist_())
#        time.sleep(1)

#    while  1:
#        try:                  #Start server,waiting for client
#            dist = ultra.checkdist()
#            print("dist = ", str(dist))
#            time.sleep(0.5)
#        except Exception as e:
#            print("Error: ", str(e))
#            RL.setColor(0,0,0)
#            break
        