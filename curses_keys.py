import curses; import math; import fractions; import setup; import RoboPiLib as RPL #the files needed for the math and key inputs
height_of_robot = 8 #distance from floor to point (0, 0)
d_one = 10 #distance from shoulder to elbow
d_two = 10 #distance from elbow to wrist
s_pin = 0 #shoulder pin
e_pin = 1 #elbow pin
fraction_shoulder = fractions.Fraction(1, 1); fraction_elbow = fractions.Fraction(1, 1) #gear ratios for motors
x = 10; y = 10 #to set starting coordinates for curses to track
d_one = d_one + 0.0000000001; d_two = d_two + 0.0000000001 #to account for the error in the imported math
screen = curses.initscr() #to enter into the curses screen
curses.start_color(); curses.use_default_colors(); curses.init_pair(1, curses.COLOR_RED, -1); curses.init_pair(2, curses.COLOR_GREEN, -1); curses.init_pair(3, curses.COLOR_BLUE, -1) #so important text can stand out
curses.noecho(); curses.halfdelay(5); screen = curses.initscr(); curses.noecho(); key = '' #to set up the curses file
def ik(x, y): #function to test if the arm is in the range of possible motion
    d_three = (y ** 2 + x ** 2) ** 0.5
    if d_three >= d_one + d_two or d_three <= d_one - d_two or (x <= 0.1 and math.fabs(y) <= 0.1):
        return False
while key != ord('q'): #to end loop if 'q' is hit
    d_arm = (y ** 2 + x ** 2) ** 0.5; a_three = math.acos((d_one ** 2 + d_two ** 2 - y ** 2 - x ** 2) / (2 * d_one * d_two)); a_two = math.asin((d_two * math.sin(a_three) / d_arm)); a_four = math.atan2(y , x) #calculate all angle values
    if y >= 0: #define angles of joints
        a_shoulder = a_four + a_two
    else:
        a_shoulder = math.fabs(a_two - a_four)
    angle_elbow = a_three * 180 / math.pi; angle_shoulder = a_shoulder * 180 / math.pi; input_elbow = int(fraction_elbow * a_three * 2000 / math.pi + 401); input_shoulder = int(fraction_shoulder * a_shoulder * 2000 / math.pi + 400) #angle and motor values
    print_angle_shoulder = '%d' %angle_shoulder; print_angle_elbow = '%d' %(angle_elbow + 0.01); screen.addstr(1, 0, 'Shoulder angle:'); screen.addstr(1, 21, 'Elbow angle:'); screen.addstr(1, 16, print_angle_shoulder, curses.color_pair(2)); screen.addstr(1, 34, print_angle_elbow, curses.color_pair(2)) #print angles of joints
    if x <= 0: #so the varaibles can't go out of their range
        x = 0
    if y < -height_of_robot:
        y = -height_of_robot
    key = screen.getch() #to reformat the screen every time something is hit
    screen.clear() #so the keys can be read
    screen.addstr(0, 0, 'Hit   to quit. Use  ,  ,  , and   to move the arm.'); screen.addstr(0, 4, 'Q', curses.color_pair(1)); screen.addstr(0, 19, 'W', curses.color_pair(2)); screen.addstr(0, 22, 'A', curses.color_pair(2)); screen.addstr(0, 25, 'S', curses.color_pair(2)); screen.addstr(0, 32, 'D', curses.color_pair(2)); screen.addstr(0, 51, 'Detected key:') #print key controls
    screen.addstr(2, 0, 'Point:'); screen.addstr(3, 0, '(   ,   )'); x_coordinate = '%d' %x; y_coordinate = '%d' %y; screen.addstr(3, 1, x_coordinate, curses.color_pair(3)); screen.addstr(3, 5, y_coordinate, curses.color_pair(3)) #to show the point the arm is at
    RPL.servoWrite(s_pin, input_shoulder); RPL.servoWrite(e_pin, input_elbow) #to move the motors
    print_input_elbow = '%d' %input_elbow; print_input_shoulder = '%d' %input_shoulder; screen.addstr(4, 0, 'Elbow motor value:'); screen.addstr(4, 19, print_input_elbow); screen.addstr(5, 0, 'Shoulder motor value:'); screen.addstr(5, 22, print_input_shoulder)
    if key != curses.ERR: #to read if the user presses something
        if key == ord('w'):
            screen.addstr(0, 65, 'w key', curses.color_pair(2)); y = y + 0.1; ik(x, y)
            if ik(x, y) == False:
                y = y - 0.1
        elif key == ord('s'):
            screen.addstr(0, 65, 's key', curses.color_pair(2)); y = y - 0.1; ik(x, y)
            if ik(x, y) == False:
                y = y + 0.1
        elif key == ord('d'):
            screen.addstr(0, 65, 'a key', curses.color_pair(2)); x = x + 0.1; ik(x, y)
            if ik(x, y) == False:
                x = x - 0.1
        elif key == ord('a'):
            screen.addstr(0, 65, 'd key', curses.color_pair(2)); x = x - 0.1; ik(x, y)
            if ik(x, y) == False:
                x = x + 0.1
        else:
            screen.addstr(0, 65, 'invalid', curses.color_pair(1))
        curses.endwin() #to reformat the terminal after the curses file closes

