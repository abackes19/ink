import math, fractions
import pyautogui, sys, curses

# 1366 by 768
#
# math syntax: https://docs.python.org/2/library/math.html

screen = curses.initscr(); curses.noecho(); curses.halfdelay(1); screen.keypad(True); curses.start_color(); curses.use_default_colors()
curses.init_pair(1, curses.COLOR_RED, -1); curses.init_pair(2, curses.COLOR_GREEN, -1); curses.init_pair(3, curses.COLOR_BLUE, -1)

xmbase, ymbase = pyautogui.size()
xmbase = xmbase / 2
ymbase = ymbase / 2

d_one = 150 #distance from shoulder to elbow
d_two = 150 #distance from elbow to wrist

pyautogui.moveTo(xmbase, ymbase, duration=.1)

while True: #to end loop if 'q' is hit
    key = screen.getch(); screen.clear()
    xread, yread = pyautogui.position()
    x = xread - xmbase
    y = yread - ymbase
    sqd_one = math.pow(d_one, 2)
    sqd_two = math.pow(d_two, 2)

    d_three = math.sqrt(math.pow(y, 2) + math.pow(x, 2)) # determining distance from shoulder to wrist ^
    screen.addstr(1, 1, "Press q to quit")

    if key != curses.ERR: #to read if the user is pressing a key
        if key == ord('q'):
            curses.endwin()
            break
    elif x == 0 and y == 0:
        a_shoulder = 90
        a_elbow = 0


    elif d_three > d_one + d_two:
        screen.addstr(2, 1, "Too far away; move closer to the origin")

    else:
        a_three = math.acos((sqd_one + sqd_two - (math.pow(y, 2) + math.pow(x, 2))) / (2 * d_one * d_two))
        a_two = math.asin((d_two * math.sin(a_three) / d_three)) # angle between shoulder and wrist
        a_four = math.atan2(y , x) # angle between 0 line and wrist

        a_shoulder = (a_four + a_two) * 180/math.pi


         # angle the shoulder joint should be at from the 0 line
        a_elbow = a_three * 180/math.pi # elbow angle, flush back to shoulder is 0

        screen.addstr(2, 1, "Distance from base: "); screen.addstr(2, 50, str(round(d_three, 1)))
        screen.addstr(3, 1, "Shoulder angle: "); screen.addstr(3, 50, str(round(a_shoulder, 1)))
        screen.addstr(4, 1, "Elbow angle: "); screen.addstr(4, 50, str(round(a_elbow, 1)))
