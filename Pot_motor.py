import RoboPiLib_pwm as RPL #to pull all the files needed to run the motors
from time import sleep
RPL.RoboPiInit("/dev/ttyAMA0", 115200) #connect to RoboPi

a_shoulder = 200
motor_speed = 500

RPL.pinMode(0, RPL.PWM) #set shoulder_pul pin as a pulse-width modulation output
RPL.pinMode(1, RPL.OUTPUT) #set shoulder_dir pin to an output and write 1 to it

ppin = 7
while True:
    p1 = RPL.analogRead(ppin) * 145 / 512 - 55
    print("p = ", int(p1))
    sleep(0.1)
    if abs(round(p1, 0) - round(a_shoulder, 0)) > 5: #so there is a margin of error of max 3 degrees
        if p1 > a_shoulder:
            RPL.digitalWrite(1, 1) #turn clockwise
        else:
            RPL.digitalWrite(1, 0) #turn counterclockwise
        while abs(round(p1, 0) - round(a_shoulder, 0)) > 5:
            p1 = RPL.analogRead(ppin) * 145 / 512 - 55
            RPL.pwmWrite(0, motor_speed, motor_speed * 2) #RPL.pwmWrite(pin value, number of on pulses, total pulses duration)
            print("running")
            sleep(0.1)
    if abs(round(p1, 0) - round(a_shoulder, 0)) < 5:
        RPL.pwmWrite(0, 0, 1)
