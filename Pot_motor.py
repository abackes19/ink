import RoboPiLib_pwm as RPL #to pull all the files needed to run the motors
RPL.RoboPiInit("/dev/ttyAMA0", 115200) #connect to RoboPi

print 'intended angle (degrees):'
a_shoulder = input('- ')
print 'arm length (length):'
arm_length = input('- ')
print 'max error (length):'
max_error = input('- ')
motor_speed = 500

shoulder_pul = 1
shoulder_dir = 2
ppin = 7

print shoulder_pul, ' shoulder_pul'
print shoulder_dir, ' shoulder_dir'
print ppin, ' ppin'

RPL.pinMode(shoulder_pul, RPL.PWM) #set shoulder_pul pin as a pulse-width modulation output
RPL.pinMode(shoulder_dir, RPL.OUTPUT) #set shoulder_dir pin to an output and write 1 to it

RPL.pwmWrite(shoulder_pul, 0, 1)

while True:
    p1 = RPL.analogRead(ppin) * 145 / 512 - 55
    print "p1: ", p1
    error = abs(p1 - a_shoulder) * 3.14159265358979323846264338 / 180 #how many degrees off the intended value the arm is
    calculated_error = error / arm_length
    if p1 > a_shoulder and calculated_error > max_error:
        RPL.digitalWrite(shoulder_dir, 1) #turn clockwise
        RPL.pwmWrite(shoulder_pul, motor_speed, motor_speed * 2)
    if p1 < a_shoulder and calculated_error > max_error:
        RPL.digitalWrite(shoulder_dir, 0) #turn counterclockwise
        RPL.pwmWrite(shoulder_pul, motor_speed, motor_speed * 2)
    if calculated_error < max_error:
        RPL.pwmWrite(shoulder_pul, 0, motor_speed * 2)
