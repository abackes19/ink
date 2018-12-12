#the file that reads key inputs
import curses
import math
import fractions
#import setup
#import RoboPiLib as RPL

print 'Enter x value'
x = input('- ') # given x input- how we tell robot where to go
print 'Enter y value'
y = input('- ') # given y input- how we tell robot where to go

e_pin = 0
s_pin = 1

#for defining the lengths of the arm
d_one = 14
d_two = 14

sqd_one = math.pow(d_one, 2)
sqd_two = math.pow(d_two, 2)
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
    screen.addstr(4, 0, "Elbow angle: "); screen.addstr(4, 20, str(a_elbow))
    screen.addstr(5, 0, "Shoulder angle:"); screen.addstr(5, 20, str(a_shoulder))


#RPL.servoWrite(e_pin, a_elbow)
#RPL.servoWrite(s_pin, a_shoulder)

while key != ord('q'):
    #so key presses can be read
    key = screen.getch()
    #to reformat the screen every time something is hit
    screen.clear()
    #to format and give instructions for the arm use
    screen.addstr(0, 0, 'Hit   to quit. Use  ,  ,  , and   to move the arm.');
    screen.addstr(0, 4, 'Q', curses.color_pair(1));
    screen.addstr(0, 19, 'W', curses.color_pair(2))
    screen.addstr(0, 22, 'A', curses.color_pair(2))
    screen.addstr(0, 25, 'S', curses.color_pair(2))
    screen.addstr(0, 32, 'D', curses.color_pair(2))
    screen.addstr(0, 51, 'Detected key:')
    screen.addstr(2, 0, str(x))
    screen.addstr(2, 10, str(y))
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
#        RPL.servoWrite(e_pin, a_elbow)
#        RPL.servoWrite(s_pin, a_shoulder)
        #to reformat the terminal after the curses file closes
        curses.endwin()
