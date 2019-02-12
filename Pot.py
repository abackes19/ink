import RoboPiLib_pwm as RPL
import time
RPL.RoboPiInit("/dev/ttyAMA0", 115200)

RPL.pinMode(0, RPL.PWM)
RPL.pinMode(1, RPL.OUTPUT)

while True:
    print 'Potentiometer value: %d\n', analogRead(1)
    time.sleep(1)
    continue
