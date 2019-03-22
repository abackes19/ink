import RoboPiLib_pwm as RPL #to pull all the files needed to run the motors
from time import sleep
RPL.RoboPiInit("/dev/ttyAMA0", 115200) #connect to RoboPi

a_shoulder = 200
motor_speed = 500

shoulder_pul = 1
shoulder_dir = 2

print shoulder_pul, " shoulder_pul"
print shoulder_dir, " shoulder_dir"

RPL.pinMode(shoulder_pul, RPL.PWM) #set shoulder_pul pin as a pulse-width modulation output
RPL.pinMode(shoulder_dir, RPL.OUTPUT) #set shoulder_dir pin to an output and write 1 to it

RPL.pwmWrite(shoulder_pul, 0, 1)

ppin = 7

while True:
    p1 = RPL.analogRead(ppin) * 145 / 512 - 55
    print("p = ", int(p1))
    while abs(p1 - a_shoulder) > 5: #so there is a margin of error of max 3 degrees
        if p1 > a_shoulder:
            RPL.digitalWrite(shoulder_dir, 1) #turn clockwise
        if p1 < a_shoulder:
            RPL.digitalWrite(shoulder_dir, 0) #turn counterclockwise
        RPL.pwmWrite(shoulder_pul, motor_speed, motor_speed * 2) #RPL.pwmWrite(pin value, number of on pulses, total pulses duration)
        p1 = RPL.analogRead(ppin) * 145 / 512 - 55
        if abs(p1 - a_shoulder) < 5:
            RPL.pwmWrite(shoulder_pul, 0, 1)
            break
