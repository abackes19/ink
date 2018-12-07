#the files needed for the math and key inputs
import curses
import math
import fractions
#to set starting coordinates for curses to track
x = 10; y = 10
#distance from shoulder to elbow and elbow to shoulder
d_one = 15; d_two = 5
#gear ratios for motors
fraction_shoulder = fractions.Fraction(1, 1); fraction_elbow = fractions.Fraction(1, 1)
#for defining the lengths of the arm
d_one = 10; d_two = 10
#to enter into the curses screen
screen = curses.initscr()
#so important text can stand out
curses.start_color(); curses.use_default_colors(); curses.init_pair(1, curses.COLOR_RED, -1); curses.init_pair(2, curses.COLOR_GREEN, -1); curses.init_pair(3, curses.COLOR_BLUE, -1)
#so the only things that print are the returned values
curses.noecho()
#so the screen will update every tenth of a second (from 1 to 225)
curses.halfdelay(1)
#to set key value to be read later
key = ''
#to end loop if 'q' is hit
while key != ord('q'):
    key = screen.getch()
    #to reformat the screen every time something is hit
    screen.clear()
    #fine angle and motor values
    d_three = (y ** 2 + x ** 2) ** 0.5 #determine distance from shoulder to wrist
    max_radius_squared = (d_one + d_two) ** 2 #so we can plug in this function later
    min_radius_squared = (d_one - d_two) ** 2

    #domain errors
    # a_three = math.acos((d_one ** 2 + d_two ** 2 - int(y) ** 2 - int(x) ** 2) / (2 * d_one * d_two)) #angle for elbow
    #domain errors

    # if d_three > 0:
    #    a_two = math.asin(d_two * math.sin(int(a_three)) / int(d_three)) #angle between shoulder and wrist
    # if d_three <= 0:
    #    a_two = d_two
    # a_four = math.atan2(y,x) # angle between 0 line and wrist
    #check if values are possible or not
    # if y >= 0:
    #    a_shoulder = a_four + a_two
    # if a_two >= math.fabs(a_four):
    #    a_shoulder = a_two - a_four
    # if a_two < math.fabs(a_four):
    #    a_shoulder = a_two - math.fabs(a_four)
    #to give outputs
    # input_elbow = int(fraction_elbow * a_three * 2000 / math.pi + 400)
    # input_shoulder = int(fraction_shoulder * a_shoulder * 2000 / math.pi + 400)
    # print_shoulder = a_shoulder * 180 / math.pi; print_shoulder = '%d' %print_shoulder; print_elbow = a_three * 180 / math.pi; print_elbow = '%d' %print_elbow
    #tell the user how to use the code
    screen.addstr(0, 0, 'Hit   to quit. Use  ,  ,  , and   to move the arm.'); screen.addstr(0, 4, 'Q', curses.color_pair(1)); screen.addstr(0, 19, 'W', curses.color_pair(2)); screen.addstr(0, 22, 'A', curses.color_pair(2)); screen.addstr(0, 25, 'S', curses.color_pair(2)); screen.addstr(0, 32, 'D', curses.color_pair(2)); screen.addstr(0, 51, 'Detected key:')
    #to give the angle values
    screen.addstr(1, 0, 'Shoulder angle:')
    screen.addstr(1, 20, 'Elbow angle:')
    # screen.addstr(1, 15, print_elbow, curses.color_pair(2))
    # screen.addstr(1, 32, print_shoulder, curses.color_pair(2))
    #to show the point the arm is at
    screen.addstr(2, 0, 'Point:'); screen.addstr(3, 0, '(   ,   )'); x_coordinate = '%d' %x; y_coordinate = '%d' %y; screen.addstr(3, 1, x_coordinate, curses.color_pair(3)); screen.addstr(3, 5, y_coordinate, curses.color_pair(3))
    #the math for the calculations
    #so the varaibles can't go out of their range
    if x <= 0:
        x = 0
    #to define what keys preform commands
    if key != curses.ERR: #to read if the user presses something
        if key == ord('w'):
            screen.addstr(0, 65, 'w key', curses.color_pair(2))
            y = min(y + 0.1, (max_radius_squared - x ** 2) ** 0.5)

        #negative value squareroot
        elif key == ord('s'):
            screen.addstr(0, 65, 's key', curses.color_pair(2))
            y = y - 0.1 #(max_radius_squared - x ** 2) ** 0.5)

        elif key == ord('d'):
            screen.addstr(0, 65, 'd key', curses.color_pair(2))
            x = min(x + 0.1, (max_radius_squared - y ** 2) ** 0.5)

        #negative value squareroot
        elif key == ord('a'):
            screen.addstr(0, 65, 'a key', curses.color_pair(2))
            x = x - 0.1 #(max_radius_squared - y ** 2) ** 0.5)

        else:
            screen.addstr(0, 65, 'invalid', curses.color_pair(1))
            #to signify that there is an invalid input
            curses.beep()
        #to reformat the terminal after the curses file closes
        curses.endwin()
