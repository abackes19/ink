# an attempt to integrate the codes that didn't work
# ignore this

import curses
import math
import fractions
import sys
import time

print 'Enter x value'
x = input('- ') # given x input- how we tell robot where to go
print 'Enter y value'
y = input('- ') # given y input- how we tell robot where to go


#for defining the lengths of the arm
d_one = 10
d_two = 10

sqd_one = math.pow(d_one, 2)
sqd_two = math.pow(d_two, 2)
#to enter into the curses screen
screen = curses.initscr(); curses.start_color(); curses.use_default_colors(); curses.init_pair(1, curses.COLOR_RED, -1); curses.init_pair(2, curses.COLOR_GREEN, -1); curses.init_pair(3, curses.COLOR_BLUE, -1); curses.noecho(); curses.halfdelay(5); screen = curses.initscr(); curses.noecho(); key = '' #to set up the curses file
#to set key value to be read later
key = ''
#to end loop if 'q' is hit

def ik(x, y):
    d_three = math.sqrt(math.pow(y, 2) + math.pow(x, 2)) # determining distance from shoulder to wrist

    o_reach = d_one + d_two
    if d_three > o_reach:
        return False
    i_reach = d_one - d_two
    if d_three < i_reach:
        return True
    else:
        a_three = math.acos((sqd_one + sqd_two - (math.pow(y, 2) + math.pow(x, 2))) / (2 * d_one * d_two))
        a_two = math.asin((d_two * math.sin(a_three) / d_three)) # angle between shoulder and wrist
        a_four = math.atan2(y , x) # angle between 0 line and wrist
        a_elbow = a_three * 180/math.pi
        if y >= 0:
            a_shoulder = (a_four + a_two) * 180/math.pi
        elif a_two >= math.fabs(a_four):
            a_shoulder = (a_two - a_four) * 180/math.pi
        elif a_two < math.fabs(a_four):
            a_shoulder = -(math.fabs(a_four) - a_two) * 180/math.pi
    screen.addstr(4, 0, "Elbow motor angle: "); screen.addstr(4, 20, str(a_elbow))
    screen.addstr(5, 0, "Shoulder motor angle:"); screen.addstr(5, 20, str(a_shoulder))


def screenadd():
    a_elbow = a_three * 180 / math.pi
    a_shoulder = a_shoulder * 180 / math.pi
    input_elbow = int(fraction_elbow * a_three * 2000 / math.pi + 401)
    input_shoulder = int(fraction_shoulder * a_shoulder * 2000 / math.pi + 400) #angle and motor value calculations
    screen.addstr(1, 0, 'Shoulder angle:'); screen.addstr(1, 21, 'Elbow angle:');
    screen.addstr(1, 16, print_angle_shoulder, curses.color_pair(2));
    screen.addstr(1, 34, print_angle_elbow, curses.color_pair(2)) #print above calculations
    screen.addstr(0, 0, 'Hit   to quit. Use the            to move the arm.');
    screen.addstr(0, 4, 'Q', curses.color_pair(1)); screen.addstr(0, 23, 'arrow keys', curses.color_pair(2))
    screen.addstr(0, 51, 'Detected key:') #print code controls
    screen.addstr(2, 0, 'Point:'); screen.addstr(3, 0, '(   ,   )')
    x_coordinate = '%d' %x; y_coordinate = '%d' %y;
    screen.addstr(3, 1, str(x), curses.color_pair(3))
    screen.addstr(3, 5, str(y), curses.color_pair(3))
    screen.addstr(4, 0, "Elbow motor angle: "); screen.addstr(4, 22, str(a_elbow))
    screen.addstr(5, 0, "Shoulder motor angle:"); screen.addstr(5, 22, str(a_shoulder))

ik(x,y)

while key != ord('q'):
    #so key presses can be read
    key = screen.getch()
    #to reformat the screen every time something is hit
    screen.clear()
    #to format and give instructions for the arm use
    key = screen.getch(); screen.clear(); screen.keypad(True) #to set up the curses files

    ik(x,y)
    if key != curses.ERR:
        if key == ord('w'):
            screen.addstr(0, 65, 'w key', curses.color_pair(2))
            y = y + 0.2
            ik(x,y)
            if ik(x,y) == False:
                y = y - 0.2
            elif ik(x,y) == True:
                y = y + 0.2
        elif key == ord('s'):
            screen.addstr(0, 65, 's key', curses.color_pair(2))
            y = y - 0.2
            ik(x,y)
            if ik(x,y) == False:
                y = y + 0.2
            elif ik(x,y) == True:
                y = y - 0.2
        elif key == ord('a'):
            screen.addstr(0, 65, 'a key', curses.color_pair(2))
            x = x - 0.2
            ik(x,y)
            if ik(x,y) == False:
                x = x + 0.2
            elif ik(x,y) == True:
                x = x - 0.2
        elif key == ord('d'):
            screen.addstr(0, 65, 'd key', curses.color_pair(2))
            x = x + 0.2
            ik(x,y)
            if ik(x,y) == False:
                x = x - 0.2
            elif ik(x,y) == True:
                x = x + 0.2

        else:
            screen.addstr(0, 65, 'invalid', curses.color_pair(1))
            #to signify that there is an invalid input
            curses.beep()
        #to reformat the terminal after the curses file closes
        curses.endwin()
