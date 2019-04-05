d_one = 62.0 #distance from shoulder to elbow
d_two = 48.0 #distance from elbow to wrist

x = 10.0 #starting x value
y = 10.0 #starting y value
z = 0.0 #starting z value

import math
def test(): #function for angle domains
    d_three = (round(x, 2) ** 2 + round(y, 2) ** 2 + round(z, 2) ** 2) ** 0.5
    if round(x, 1) == 0.0 and round(y, 1) == 0.0 and round(z, 1) == 0:
        return True
    if d_three > d_one + d_two or d_three < d_one - d_two:
        return False

import RoboPiLib_pwm as RPL #to pull all the files needed to run the code
RPL.RoboPiInit("/dev/ttyAMA0", 115200) #connect to RoboPi

shoulder_pul = 1 #shoulde pulse pin
shoulder_dir = 2 #shoulde direction pin
elbow_pul = 3 #elbow pulse pin
elbow_dir = 4 #elbow direction pin
swivel_continuous = 1 #pin for swivel motor
ppin_shoulder = 7 #pin number for shoulder potentiometer
ppin_elbow = 8 #pin number for elbow potentiomenter
ppin_swivel = 9 #pint number for swivel potentiomenter

print 'shoulder_pul', shoulder_pul
print 'shoulder_dir', shoulder_dir
print 'elbow_pul', elbow_pul
print 'elbow_dir', elbow_dir
print 'swivel_continuous', swivel_continuous
print 'ppin_shoulder', ppin_shoulder
print 'ppin_elbow', ppin_elbow
print 'ppin_swivel', ppin_swivel

RPL.pinMode(shoulder_pul, RPL.PWM) #set shoulder_pul pin as a pulse-width modulation output
RPL.pinMode(shoulder_dir, RPL.OUTPUT) #set shoulder_dir pin to an output and write 1 to it
RPL.pinMode(elbow_pul, RPL.PWM) #set elbow_pul pin as a pulse-width modulation output
RPL.pinMode(elbow_dir, RPL.OUTPUT) #set elbow_dir pin to an output and write 1 to it

import sys, termios, tty
def getch(): #detect key presses
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

while True:

    if z <= 0.0: #limit the arm to the front side of the robot
        z = 0.0

    if test() != True: #calculate angle values for motors
        a_elbow = math.acos((d_one ** 2 + d_two ** 2 - round(x, 2) ** 2 - round(y, 2) ** 2 - round(z, 2) ** 2) / (2 * d_one * d_two))
        a_shoulder = math.asin((d_two * math.sin(a_elbow) / (round(x, 2) ** 2 + round(y, 2) ** 2 + round(z, 2) ** 2) ** 0.5)) + math.atan2(round(y, 2), (round(x, 2) ** 2 + round(z, 2) ** 2) ** 0.5)
        a_swivel = math.atan2(round(x, 2), round(z, 2)) + math.pi / 2
    else: #give motor values at (0, 0, 0)
        a_elbow = x = y = z = 0.0

    motor_speed = 500

    max_error = 2

    pot_shoulder = RPL.analogRead(ppin_shoulder) * 29 * math.pi / 18432
    error_s = abs(pot_shoulder - a_shoulder) #how many degrees off the intended value the arm is
    calculated_error_s = error_s / d_one
    if pot_shoulder > a_shoulder and calculated_error_s > max_error:
        RPL.digitalWrite(shoulder_dir, 1) #turn clockwise
        RPL.pwmWrite(shoulder_pul, motor_speed, motor_speed * 2)
    if pot_shoulder < a_shoulder and calculated_error_s > max_error:
        RPL.digitalWrite(shoulder_dir, 0) #turn counterclockwise
        RPL.pwmWrite(shoulder_pul, motor_speed, motor_speed * 2)
    if calculated_error_s < max_error:
        RPL.pwmWrite(shoulder_pul, 0, motor_speed * 2)

    pot_elbow = RPL.analogRead(ppin_elbow) * 29 * math.pi / 18432
    error_e = abs(pot_elbow - a_elbow) #how many degrees off the intended value the arm is
    calculated_error_e = error_e / d_two
    if pot_elbow > a_elbow and calculated_error_e > max_error:
        RPL.digitalWrite(elbow_dir, 1) #turn clockwise
        RPL.pwmWrite(elbow_pul, motor_speed, motor_speed * 2)
    if pot_elbow < a_elbow and calculated_error_e > max_error:
        RPL.digitalWrite(elbow_dir, 0) #turn counterclockwise
        RPL.pwmWrite(elbow_pul, motor_speed, motor_speed * 2)
    if calculated_error_e < max_error:
        RPL.pwmWrite(elbow_pul, 0, motor_speed * 2)

    pot_swivel = RPL.analogRead(ppin_swivel) * 29 * math.pi / 18432
    error_sw = abs(pot_swivel - a_swivel)
    if pot_swivel > a_swivel and error_sw > max_error:
        RPL.servoWrite(swivel_continuous, 2000)
    if pot_swivel < a_swivel and error_sw > max_error:
        RPL.servoWrite(swivel_continuous, 1000)
    if error_sw < max_error:
        RPL.servoWrite(swivel_continuous, 0)

    key = getch() #read when a key is presses

    speed = 1 #set starting step value

    if key == 'd': #increase x value
        x += 0.1 * speed
        if test() == False:
            x -= 0.1 * speed
    elif key == 'a': #decrease x value
        x -= 0.1 * speed
        if test() == False:
            x += 0.1 * speed
    elif key == 'w': #increase y value
        y += 0.1 * speed
        if test() == False:
            y -= 0.1 * speed
    elif key == 's': #decrease y value
        y -= 0.1 * speed
        if test() == False:
            y += 0.1 * speed
    elif key == 'e': #increase z value
        z += 0.1 * speed
        if test() == False:
            z -= 0.1 * speed
    elif key == 'q': #decrease z value
        z -= 0.1 * speed
        if test() == False:
            z += 0.1 * speed
    elif key == 'x': #increase step length
        speed += 1
        if speed >= 4:
            speed = 4
    elif key == 'z': #decrease step length
        speed -= 1
        if speed <= 1:
            speed = 1
    elif key == '1': #quit the program
        RPL.pwmWrite(shoulder_pul, 0, 1)
        RPL.pwmWrite(elbow_pul, 0, 1)
        RPL.servoWrite(swivel_continuous, 0)
        exit(0)
