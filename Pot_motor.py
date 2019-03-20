import RoboPiLib_pwm as MOTOR #to pull all the files needed to run the motors
import RoboPiLib as POT #to pull all files needed to read the potentiometers
from time import sleep
MOTOR.RoboPiInit("/dev/ttyAMA0", 115200) #connect to RoboPi

a_shoulder = 200

MOTOR.pinMode(0, RPL.PWM) #set shoulder_pul pin as a pulse-width modulation output
MOTOR.pinMode(1, RPL.OUTPUT) #set shoulder_dir pin to an output and write 1 to it

ppin = 7
pot_1 = POT.analogRead(ppin) * 145 / 512 - 55

print(pot_1)
sleep(0.1)

def stop(): #stop the motors
    MOTOR.pwmWrite(0, 0, 1)

def shoulder(): #to run the motors
    motor_speed = 500
    if abs(round(pot_1, 0) - round(a_shoulder, 0)) > 3: #so there is a margin of error of max 3 degrees
        if pot_1 > a_shoulder:
            MOTOR.digitalWrite(1, 1) #turn clockwise
        else:
            MOTOR.digitalWrite(1, 0) #turn counterclockwise
        MOTOR.pwmWrite(0, motor_speed, motor_speed * 2) #RPL.pwmWrite(pin value, number of on pulses, total pulses duration)
    else:
        stop()