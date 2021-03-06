import RoboPiLib_pwm as RPL, time #to pull all the files needed to run the code
RPL.RoboPiInit("/dev/ttyAMA0", 115200) #connect to RoboPi

RPL.pinMode(0, RPL.PWM) #set shoulder_pul pin as a pulse-width modulation output
RPL.pinMode(1, RPL.OUTPUT) #set shoulder_dir pin to an output and write 1 to it

motor_speed = 1000

def stop(): #stop the motors
  RPL.pwmWrite(0, 0, 1)

def shoulder(dir, run_for, motor_speed):
  if (dir):
    RPL.digitalWrite(1, 1) #set pin to 1
  else:
    RPL.digitalWrite(1, 0) #set pin to 0
  RPL.pwmWrite(0, motor_speed, motor_speed * 2) #RPL.pwmWrite(pin value, on duration, off duration)
  time.sleep(run_for)
  stop()
while True:
    print "Hit 'y' or 'x' to run motor. Hit 'q' to quit."
    run = raw_input('- ')
    if run == 'y':
        shoulder(True, 26, 1000)
    elif run == 'x':
        shoulder(False, 26, 1000)
    elif run == 'q':
      break
    continue
