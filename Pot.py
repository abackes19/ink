import RoboPiLib as RPL
import setup
from time import sleep

apin = 0
ppin = 7  #potentiomenter pin line

while True:
  p1 = RPL.analogRead(ppin)
  a1 = p1 * 145 / 512
  RPL.servoWrite(apin,int(a1))
  print("p = ", int(p1), "  a = ",int(a1 - 55) )
  sleep(0.05)
