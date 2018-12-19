import curses, math, setup, RoboPiLib as RPL #to pull all the files needed to run the code

d_one = 14.0 #distance from shoulder to elbow
d_two = 14.0 #distance from elbow to wrist
height_of_robot = 6.0 #distance from floor to point (x, 0, z)

el_pin = 0 #set pin numbers
sh_pin = 1
sw_pin = 2

screen = curses.initscr() #setting up the curses file
curses.halfdelay(1)
curses.noecho()
curses.start_color()
curses.use_default_colors()
curses.init_pair(1, curses.COLOR_RED, -1)
curses.init_pair(2, curses.COLOR_GREEN, -1)
curses.init_pair(3, curses.COLOR_BLUE, -1)

speed = 1 #so the values of the changing variables will not return errors
x = 14.0
y = 14.0
z = 0.0
key = ''

def test(x, y, z): #function to test if the arm is in the range of possible motion
    d_three = (round(x, 2) ** 2 + round(y, 2) ** 2 + round(z, 2) ** 2) ** 0.5
    if round(x, 1) == 0.0 and round(y, 1) == 0.0 and round(z, 1) == 0:
        return True
    if d_three > d_one + d_two or d_three < d_one - d_two:
        return False

while key != ord('z'): #to end loop if 'q' is hit
    key = screen.getch()
    screen.clear()

    if x <= 0.0: #so the varaibles can't go out of their range
        x = 0.0

    if y <= -height_of_robot: #so the robot's arm can't run into the ground
        y = -height_of_robot

    if round(y, 1) == 0.0: #so the code doesn't read "-0.0" at y = 0.0
        y = 0.0
    if round(z, 1) == 0.0: #so the code doesn't read "-0.0" at z = 0.0
        z = 0.0

    if round(z, 1) == 0.0:
        z = 0.0

    if test(x, y, z) != True: #to calculate all angle values for motors except at point (0, 0, 0)
        a_elbow = math.acos((d_one ** 2 + d_two ** 2 - round(x, 2) ** 2 - round(y, 2) ** 2 - round(z, 2) ** 2) / (2 * d_one * d_two))
        a_shoulder = math.asin((d_two * math.sin(a_elbow) / (round(y, 2) ** 2 + round(x, 2) ** 2 + round(z, 2) ** 2) ** 0.5)) + math.atan2(round(y, 2), (round(x, 2) ** 2 + round(z, 2) ** 2) ** 0.5)
        a_swivel = math.atan2(round(z, 2), round(x, 2)) + math.pi / 2
    else: #to give the motor values at (0, 0, 0)
        a_elbow = 0
        a_shoulder = math.pi
        x = 0.0
        y = 0.0
        z = 0.0
        
    screen.addstr(0, 0, 'Hit   to quit. Use the   and   keys for verticle movement, the   and   keys to')
    screen.addstr(1, 0, 'extend and retract the arm, and the   and   keys for horizontle movement. Use')
    screen.addstr(2, 0, 'and   to speed up and slow down the robot. Key detected:')
    screen.addstr(0, 4, 'Z', curses.color_pair(1))
    screen.addstr(0, 23, 'W', curses.color_pair(3))
    screen.addstr(0, 29, 'S', curses.color_pair(3))
    screen.addstr(0, 63, 'Q', curses.color_pair(3))
    screen.addstr(0, 69, 'E', curses.color_pair(3))
    screen.addstr(1, 36, 'A', curses.color_pair(3))
    screen.addstr(1, 42, 'D', curses.color_pair(3))
    screen.addstr(1, 78, '1', curses.color_pair(2))
    screen.addstr(2, 4, '2', curses.color_pair(2))

    screen.addstr(4, 0, 'Shoulder angle:') #to print shoulder angle value
    angle_shoulder = a_shoulder * 180 / math.pi
    screen.addstr(4, 16, str(round(angle_shoulder, 1)), curses.color_pair(1))

    screen.addstr(4, 22, 'Elbow angle:') #to print elbow angle value
    angle_elbow = a_elbow * 180 / math.pi
    screen.addstr(4, 35, str(round(angle_elbow, 1)), curses.color_pair(1))

    screen.addstr(4, 41, 'Swivel angle:') #to print swivel angle value
    angle_swivel = a_swivel * 180 / math.pi
    screen.addstr(4, 55, str(round(angle_swivel, 1)), curses.color_pair(1))

    screen.addstr(5, 0, 'Point: (     ,     ,     )') #to print the coordinate the arm is at
    screen.addstr(5, 8, str(round(x, 1)), curses.color_pair(3))
    screen.addstr(5, 14, str(round(y, 1)), curses.color_pair(3))
    screen.addstr(5, 20, str(round(z, 1)), curses.color_pair(3))

    screen.addstr(6, 27, 'Max arm extention:')
    screen.addstr(6, 46, str(round(d_one + d_two, 1)), curses.color_pair(3))
    screen.addstr(6, 0, 'Distance from origin:')
    screen.addstr(6, 22, str(round((x ** 2 + y ** 2 + z ** 2) ** 0.5, 1)), curses.color_pair(3))

    screen.addstr(7, 0, 'Speed:') #to print speed value
    screen.addstr(7, 7, str(round(speed, 1),), curses.color_pair(2))

    screen.addstr(8, 0, 'Elbow motor value:') #to give elbow motor value
    input_elbow = int(a_elbow * 2000 / math.pi + 400)
    screen.addstr(8, 19, str(input_elbow))
    RPL.servoWrite(el_pin, input_elbow)

    screen.addstr(9, 0, 'Shoulder motor value:') #to give shoulder motor value
    input_shoulder = int(a_shoulder * 2000 / math.pi + 400)
    screen.addstr(9, 22, str(input_shoulder))
    RPL.servoWrite(sh_pin, input_shoulder)

    screen.addstr(10, 0, 'Swivel motor value:') #to give swivel motor value
    input_swivel = int(a_swivel * 2000 / math.pi + 400)
    screen.addstr(10, 20, str(input_swivel))
    RPL.servoWrite(sw_pin, input_swivel)

    if input_shoulder < 400 or input_elbow < 400 or input_swivel < 400: #to inform users if the point is reachable with the motors
        screen.addstr(11, 0, 'Domain error: point outside of motor range', curses.color_pair(1))

    if key != curses.ERR: #to read if the user is pressing a key
        if key == ord('w'): #to increase y value
            screen.addstr(2, 57, 'w key', curses.color_pair(2))
            y = y + 0.1 * speed
            if test(x, y, z) == False:
                y = y - 0.1 * speed
        elif key == ord('s'): #to decrease y value
            screen.addstr(2, 57, 's key', curses.color_pair(2))
            y = y - 0.1 * speed
            if test(x, y, z) == False:
                y = y + 0.1 * speed
        elif key == ord('e'): #to increase x value
            screen.addstr(2, 57, 'e key', curses.color_pair(2))
            x = x + 0.1 * speed
            if test(x, y, z) == False:
                x = x - 0.1 * speed
        elif key == ord('q'): #to decrease x value
            screen.addstr(2, 57, 'q key', curses.color_pair(2))
            x = x - 0.1 * speed
            if test(x, y, z) == False:
                x = x + 0.1 * speed
        elif key == ord('d'): #to increase z value
            screen.addstr(2, 57, 'd key', curses.color_pair(2))
            z = z + 0.1 * speed
            if test(x, y, z) == False:
                z = z - 0.1 * speed
        elif key == ord('a'): #to decrease z value
            screen.addstr(2, 57, 'a key', curses.color_pair(2))
            z = z - 0.1 * speed
            if test(x, y, z) == False:
                z = z + 0.1 * speed
        elif key == ord('2'): #to increase speed
            screen.addstr(2, 57, '2 key', curses.color_pair(2))
            speed = int(speed + 1)
            if speed >= 4:
                speed = 4
        elif key == ord('1'): #to decrease speed
            screen.addstr(2, 57, '1 key', curses.color_pair(2))
            speed = int(speed - 1)
            if speed <= 1:
                speed = 1
        elif key == ord('z'): #to end the program and reformat the terminal
            curses.endwin()
        else: #so if an invalid key is hit, the user is alerted
            screen.addstr(2, 57, 'invalid', curses.color_pair(1))
            curses.beep()
