
import curses, math, fractions, setup, RoboPiLib as RPL
height_of_robot = 6.0 #distance from floor to point (0, 0)
d_one = 14.0 #distance from shoulder to elbow
d_two = 14.0 #distance from elbow to wrist
s_pin = 0 #shoulder pin
e_pin = 1 #elbow pin
fraction_shoulder = fractions.Fraction(1, 1); fraction_elbow = fractions.Fraction(1, 1) #gear ratio inputs
x = 10.0; y = 10.0
screen = curses.initscr(); curses.noecho(); curses.halfdelay(5); screen.keypad(True); screen = curses.initscr() #set up curses file
curses.start_color(); curses.use_default_colors(); curses.init_pair(1, curses.COLOR_RED, -1); curses.init_pair(2, curses.COLOR_GREEN, -1); curses.init_pair(3, curses.COLOR_BLUE, -1)
key = ''
def test(x, y): #function to test if the arm is in the range of possible motion
    d_three = (round(y, 1) ** 2 + round(x, 1) ** 2) ** 0.5
    if d_three > d_one + d_two or d_three < d_one - d_two or (math.fabs(round(x, 1)) == 0.0 and math.fabs(round(y, 1)) == 0.0):
        return False
while key != ord('q'): #to end loop if 'q' is hit
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
    input_elbow = int(fraction_elbow * a_elbow * 2000 / math.pi + 400)
    input_shoulder = int(fraction_shoulder * a_shoulder * 2000 / math.pi + 400) #angle and motor value calculations
    RPL.servoWrite(s_pin, input_shoulder)
    RPL.servoWrite(e_pin, input_elbow) #to move the motors
    key = screen.getch(); screen.clear()
    screen.addstr(0, 0, 'Hit   to quit. Use the            to move the arm.'); screen.addstr(0, 4, 'Q', curses.color_pair(1)); screen.addstr(0, 23, 'arrow keys', curses.color_pair(2)); screen.addstr(0, 51, 'Detected key:') #print code controls
    screen.addstr(1, 0, 'Shoulder angle:'); screen.addstr(1, 22, 'Elbow angle:'); screen.addstr(1, 16, str(round(angle_shoulder, 1)), curses.color_pair(2)); screen.addstr(1, 35, str(round(angle_elbow, 1)), curses.color_pair(2)) #print angles
    screen.addstr(2, 0, 'Point:'); screen.addstr(3, 0, '(    ,    )'); screen.addstr(3, 1, str(round(x, 1)), curses.color_pair(3)); screen.addstr(3, 6, str(round(y, 1)), curses.color_pair(3)) #print point
    screen.addstr(4, 0, 'Elbow motor value:'); screen.addstr(4, 19, str(input_elbow)); screen.addstr(5, 0, 'Shoulder motor value:'); screen.addstr(5, 22, str(input_shoulder)) #print all values
    if key != curses.ERR: #to read if the user is pressing a key
        if key == curses.KEY_UP:
            screen.addstr(0, 65, 'up arrow', curses.color_pair(2))
            y = y + 0.1; test(x, y)
            if test(x, y) == False:
                y = y - 0.1
        elif key == curses.KEY_DOWN:
            screen.addstr(0, 65, 'down arrow', curses.color_pair(2))
            y = y - 0.1; test(x, y)
            if test(x, y) == False:
                y = y + 0.1
        elif key == curses.KEY_RIGHT:
            screen.addstr(0, 65, 'right arrow', curses.color_pair(2))
            x = x + 0.1; test(x, y)
            if test(x, y) == False:
                x = x - 0.1
        elif key == curses.KEY_LEFT:
            screen.addstr(0, 65, 'left arrow', curses.color_pair(2))
            x = x - 0.1; test(x, y)
            if test(x, y) == False:
                x = x + 0.1
        else:
            screen.addstr(0, 65, 'invalid', curses.color_pair(1))
        curses.endwin() #to reformat the terminal after the curses file closes
