import stepper_control as SC, curses

screen = curses.initscr() #setting up curses file
curses.halfdelay(1)
curses.noecho()

key = ''

while key != ord('q'):

    key = screen.getch()
    screen.clear()

    screen.addstr('Hit Q to quit. Use A and D to move the motor')
    if key == ord('a'):
        SC.elbow(True, 0.1, 1000)
    if key == ord('d'):
        SC.elbow(False, 0.1, 1000)
    if key == ord('q'):
        curses.endwin()
