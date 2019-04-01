import RoboPiLib_pwm as RPL #to pull all the files needed to run the motors
RPL.RoboPiInit("/dev/ttyAMA0", 115200) #connect to RoboPi

a_shoulder = 200

shoulder_pul = 1
shoulder_dir = 2
ppin = 7

print shoulder_pul, " shoulder_pul"
print shoulder_dir, " shoulder_dir"
print ppin, " ppin"

RPL.pinMode(shoulder_pul, RPL.PWM) #set shoulder_pul pin as a pulse-width modulation output
RPL.pinMode(shoulder_dir, RPL.OUTPUT) #set shoulder_dir pin to an output and write 1 to it

RPL.pwmWrite(shoulder_pul, 0, 1)

while True:
    p1 = RPL.analogRead(ppin) * 145 / 512 - 55
    print p1, " p1"
    error = abs(p1 - a_shoulder) #how many degrees off the intended value the arm is
    if p1 > a_shoulder and error > 5:
        RPL.digitalWrite(shoulder_dir, 1) #turn clockwise
        motor_speed = 500
    if p1 < a_shoulder and error > 5:
        RPL.digitalWrite(shoulder_dir, 0) #turn counterclockwise
        motor_speed = 500
    else:
        motor_speed = 0 #stop the motor
    RPL.pwmWrite(shoulder_pul, motor_speed, motor_speed * 2) #RPL.pwmWrite(pin value, number of on pulses, total pulses duration)
