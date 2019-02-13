import RoboPiLib as RPL
import setup
from time import sleep
spin = 0  #servo pin
 
ppin = 7  #potentiomenter pin 
while True:
  p1 = RPL.analogRead(ppin) 
  s1 = p1 * 26.6
  RPL.servoWrite(spin,int(s1)) 
  print("p = ", int(p1), "  S = ",int(s1) )
  sleep(0.05)
