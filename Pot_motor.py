import RoboPiLib_pwm as RPL #to pull all the files needed to run the motors
from time import sleep
RPL.RoboPiInit("/dev/ttyAMA0", 115200) #connect to RoboPi

a_shoulder = 200

RPL.pinMode(0, RPL.PWM) #set shoulder_pul pin as a pulse-width modulation output
RPL.pinMode(1, RPL.OUTPUT) #set shoulder_dir pin to an output and write 1 to it

ppin = 7
while True:
    p1 = RPL.analogRead(ppin) * 145 / 512 - 55
    print("p = ", int(p1))
    shoulder()
    sleep(0.1)

def stop(): #stop the motors
    RPL.pwmWrite(0, 0, 1)

def shoulder(): #to run the motors
    motor_speed = 500
    if abs(round(pot_1, 0) - round(a_shoulder, 0)) < 5: #so there is a margin of error of max 3 degrees
        if pot_1 > a_shoulder:
            RPL.digitalWrite(1, 1) #turn clockwise
        else:
            RPL.digitalWrite(1, 0) #turn counterclockwise
        RPL.pwmWrite(0, motor_speed, motor_speed * 2) #RPL.pwmWrite(pin value, number of on pulses, total pulses duration)
    else:
        stop()
