#the files needed for the math and key inputs
import curses; import math; import fractions; import setup; import RoboPiLib as RPL
#to set starting coordinates for curses to track
x = 10; y = 10
#to define the lengths of the arm
d_one = 10
d_two = 10
s_pin = 0
e_pin = 1
height_of_robot = 5
#to account for errors in calculations later
d_one = d_one + 0.0000000001; d_two = d_two + 0.0000000001
#gear ratios for motors
fraction_shoulder = fractions.Fraction(1, 1); fraction_elbow = fractions.Fraction(1, 1)
#to enter into the curses screen
screen = curses.initscr()
#so important text can stand out
curses.start_color(); curses.use_default_colors(); curses.init_pair(1, curses.COLOR_RED, -1); curses.init_pair(2, curses.COLOR_GREEN, -1); curses.init_pair(3, curses.COLOR_BLUE, -1)
#so the only things that print are the returned values
curses.noecho()
#so the screen will update every tenth of a second (from 1 to 225)
curses.halfdelay(5)
#to set key value to be read later
key = ''
#to enter into the curses screen
screen = curses.initscr()
#so important text can stand out
curses.start_color(); curses.use_default_colors(); curses.init_pair(1, curses.COLOR_RED, -1); curses.init_pair(2, curses.COLOR_GREEN, -1)
#so the only things that print are the returned values
curses.noecho()
#so the screen will update every tenth of a second (from 1 to 225)
curses.halfdelay(1)
#to set key value to be read later
key = ''
def ik(x, y):
    d_three = (y ** 2 + x ** 2) ** 0.5 #determining distance from shoulder to wrist
    if d_three >= d_one + d_two or d_three <= d_one - d_two:
        return False
    else:
        return True
#to end loop if 'q' is hit
while key != ord('q'):
    #math for the kinimatics
    d_arm = (y ** 2 + x ** 2) ** 0.5
    a_three = math.acos((d_one ** 2 + d_two ** 2 - y ** 2 - x ** 2) / (2 * d_one * d_two))
    a_two = math.asin((d_two * math.sin(a_three) / d_arm)) #angle between shoulder and wrist
    a_four = math.atan2(y , x) #angle between 0 line and wrist
    #define angles of joints
    if y >= 0:
        a_shoulder = (a_four + a_two) * 180/math.pi
    elif a_two >= math.fabs(a_four):
        a_shoulder = (a_two - a_four) * 180/math.pi
    elif a_two < math.fabs(a_four):
        a_shoulder = (a_two - math.fabs(a_four)) * 180/math.pi
    a_elbow = a_three * 180 / math.pi
    #give motor values
    input_elbow = int(fraction_elbow * a_three * 2000 / math.pi + 400); input_shoulder = int(fraction_shoulder * a_shoulder * 2000 / math.pi + 400)
    #print angles of joints
    angle_shoulder = '%d' %a_shoulder; angle_elbow = '%d' %(a_elbow + 1); screen.addstr(1, 0, 'Shoulder angle:'); screen.addstr(1, 21, 'Elbow angle:'); screen.addstr(1, 16, angle_shoulder, curses.color_pair(2)); screen.addstr(1, 34, angle_elbow, curses.color_pair(2))
    #so the keys can be read
    key = screen.getch()
    #to reformat the screen every time something is hit
    screen.clear()
    screen.addstr(0, 0, 'Hit   to quit. Use  ,  ,  , and   to move the arm.'); screen.addstr(0, 4, 'Q', curses.color_pair(1)); screen.addstr(0, 19, 'W', curses.color_pair(2)); screen.addstr(0, 22, 'A', curses.color_pair(2)); screen.addstr(0, 25, 'S', curses.color_pair(2)); screen.addstr(0, 32, 'D', curses.color_pair(2)); screen.addstr(0, 51, 'Detected key:')
    #to show the point the arm is at
    screen.addstr(2, 0, 'Point:'); screen.addstr(3, 0, '(   ,   )'); x_coordinate = '%d' %x; y_coordinate = '%d' %y; screen.addstr(3, 1, x_coordinate, curses.color_pair(3)); screen.addstr(3, 5, y_coordinate, curses.color_pair(3))
    #so the varaibles can't go out of their range
    if x <= 0:
        x = 0
    if y < -height_of_robot:
        y = -height_of_robot
    #to move the motors
    RPL.servoWrite(s_pin, input_shoulder)
    RPL.servoWrite(e_pin, input_elbow)
    #to define what keys preform commands
    if key != curses.ERR: #to read if the user presses something
        if key == ord('w'):
            screen.addstr(0, 65, 'w key', curses.color_pair(2))
            y = y + 0.1
            ik(x, y)
            if ik(x, y) == False:
                y = y - 0.1
        elif key == ord('s'):
            screen.addstr(0, 65, 's key', curses.color_pair(2))
            y = y - 0.1
            ik(x, y)
            if ik(x, y) == False:
                y = y + 0.1
        elif key == ord('d'):
            screen.addstr(0, 65, 'a key', curses.color_pair(2))
            x = x + 0.1
            ik(x, y)
            if ik(x, y) == False:
                x = x - 0.1
        elif key == ord('a'):
            screen.addstr(0, 65, 'd key', curses.color_pair(2))
            x = x - 0.1
            ik(x, y)
            if ik(x, y) == False:
                x = x + 0.1
        else:
            screen.addstr(0, 65, 'invalid', curses.color_pair(1))
        #to reformat the terminal after the curses file closes
        curses.endwin()
