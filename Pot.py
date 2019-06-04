import RoboPiLib_pwm as RPL
RPL.RoboPiInit("/dev/ttyAMA0", 115200)
from time import sleep

apin = 0
ppin = 7  #potentiomenter pin line

while True:
  p1 = RPL.analogRead(ppin)
  print("p = ", int(pl))
  sleep(0.05)
