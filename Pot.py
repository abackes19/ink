import RoboPiLib as RPL
import setup
from time import sleep

spin = 0  #servo pin
ppin = 7  #potentiomenter pin

while True:
  p1 = RPL.analogRead(ppin)
  a1 = p1 * 580 / 77
  RPL.servoWrite(spin,int(s1))
  print("p = ", int(p1), "  a = ",int(a1 - 55) )
  sleep(1)
