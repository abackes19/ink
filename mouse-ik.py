import math, fractions
import pyautogui, sys

# 1365 by 767
#



height_of_robot = 6.0 #distance from floor to point (0, 0)
d_one = 150 #distance from shoulder to elbow
d_two = 150 #distance from elbow to wrist

xmbase = 682
ymbase = 382

x, y = pyautogui.position()

def test(x, y): #function to test if the arm is in the range of possible motion
    d_three = (round(y, 1) ** 2 + round(x, 1) ** 2) ** 0.5
    if d_three > d_one + d_two or d_three < d_one - d_two or (math.fabs(round(x, 1)) == 0.0 and math.fabs(round(y, 1)) == 0.0):
        return False

if x <= 0.0: #so the varaibles can't go out of their range
    x = 0.0
if y <= -height_of_robot:
    y = -height_of_robot
if round(y, 1) == 0.0:
    y = 0.0

a_elbow = math.acos((d_one ** 2 + d_two ** 2 - round(y, 1) ** 2 - round(x, 1) ** 2) / (2 * d_one * d_two))
a_two = math.asin((d_two * math.sin(a_elbow) / (round(y, 1) ** 2 + round(x, 1) ** 2) ** 0.5))
a_four = math.atan2(round(y, 1) , round(x, 1)) #calculate all angle values
a_shoulder = a_four + a_two
angle_elbow = a_elbow * 180 / math.pi
angle_shoulder = a_shoulder * 180 / math.pi


print angle_elbow
print angle_shoulder
