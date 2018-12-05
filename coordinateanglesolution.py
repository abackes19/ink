# inverse kinematics take 1!
# math syntax: https://docs.python.org/2/library/math.html
# distance from center of hole to hole: 8mm


import math
import fractions
import sys
import time


d_one = 10 # the distance from shoulder to elbow
d_two = 10 # distance from elbow to wrist
sqd_one = math.pow(d_one, 2)
sqd_two = math.pow(d_two, 2)

print 'Enter x value'
x = input('- ') # given x input- how we tell robot where to go
print 'Enter y value'
y = input('- ') # given y input- how we tell robot where to go

start = time.time()

d_three = math.sqrt(math.pow(y, 2) + math.pow(x, 2)) # determining distance from shoulder to wrist ^

o_reach = d_one + d_two
if d_three > o_reach:
    sys.exit("Out of reach: too far away.")
i_reach = d_one - d_two
if d_three < i_reach:
    sys.exit("Out of reach: too close.")

a_three = math.acos((sqd_one + sqd_two - (math.pow(y, 2) + math.pow(x, 2))) / (2 * d_one * d_two))
a_two = math.asin((d_two * math.sin(a_three) / d_three)) # angle between shoulder and wrist
a_four = math.atan2(y , x) # angle between 0 line and wrist

if y >= 0:
    print "Point above x axis"
    a_shoulder = (a_four + a_two) * 180/math.pi
elif a_two >= math.fabs(a_four):
    print "Point below x axis, elbow is not"
    a_shoulder = (a_two - a_four) * 180/math.pi
elif a_two < math.fabs(a_four):
    print "All of arm below x axis"
    a_shoulder = -(math.fabs(a_four) - a_two) * 180/math.pi
else:
    print "guess I'll die"

print "Angle between shoulder and wrist:"
print a_two * 180/math.pi
print "Angle directly to wrist:"
print math.atan2(y, x) * 180/math.pi
#print a_three * 180/math.pi
 # angle the shoulder joint should be at from the 0 line
a_elbow = a_three * 180/math.pi # elbow angle, flush back to shoulder is 0

print "Distance from base: %i units" % d_three
print "Shoulder: %i degrees" % a_shoulder
print "Elbow: %i degrees" % a_elbow

print time.time()
print time.time() - start
