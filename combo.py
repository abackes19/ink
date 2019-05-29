# using arrow keys!
# notes: can use continuously, but use one key at a time in an orderly fashion

import RoboPiLib3 as RPL
import setup3
import pygame, math, fractions, time
from pygame.locals import *


pygame.init()

######################################
#setup
######################################


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (39, 147, 52)
blue = (102, 136, 214)
pink = (232, 13, 119)
grey = (203, 206, 214)

display_width = 500
display_height = 500
gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay.fill(white)
clock = pygame.time.Clock()

step = 4
originx = 250
originy = 250
d_one = 62.0 #distance from shoulder to elbow
d_two = 48.0 #distance from elbow to wrist
pixel_one = d_one # the distance from shoulder to elbow
pixel_two = d_two # distance from elbow to wrist

pygame.draw.circle(gameDisplay, grey, (originx, originy), (pixel_one + pixel_two), 0)
pygame.draw.circle(gameDisplay, white, (originx, originy), (pixel_one - pixel_two), 0)
xm, ym = originx+pixel_two, originy-pixel_one
pygame.draw.line(gameDisplay, blue, (originx, originy), (xm, ym),5)
pygame.display.update()

x, y = originx+pixel_two, originy-pixel_one
xo = x
yo = y
x_change = 0
y_change = 0


# ^^^ that all would be the setup

done = False
clock = pygame.time.Clock()

######################################
#display functions
######################################

def ik(xm, ym): # here is where we do math
    y = originy - ym
    x = xm - originx

    sqd_one = pixel_one ** 2
    sqd_two = pixel_two ** 2

    pixel_three = math.sqrt((y**2) + (x**2)) # determining distance from shoulder to wrist ^
    if pixel_one - pixel_two < pixel_three < pixel_one + pixel_two and y > -24:
        a_three = math.acos((sqd_one + sqd_two - ((y**2) + (x ** 2))) / (2 * pixel_one * pixel_two))
        a_two = math.asin((pixel_two * math.sin(a_three) / pixel_three)) # angle between shoulder and wrist
        a_four = math.atan2(y , x) # angle between 0 line and wrist
        a_shoulder = (a_four + a_two)  # shoulder angle?
        a_elbow = a_three

        return a_shoulder, a_elbow
    else:
        return False

    pygame.display.flip()


def pos(x, y):
    x_change = 0
    y_change = 0

    if event.type == pygame.KEYDOWN:
        # what key are they pressing? move accordingly
        if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
            done=True
            return done
        elif event.key == pygame.K_a:
            x_change = -step
        elif event.key == pygame.K_d:
            x_change = step
        elif event.key == pygame.K_w:
            y_change = -step
        elif event.key == pygame.K_s:
            y_change = step

    return x_change, y_change


######################################
#display loop
######################################

def display():
    while not done:
        clock.tick(60)
        # determine where want to be
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            else: # did something other than close
                x_change, y_change = pos(x,y) # figure out the change
        # move
        x += x_change
        y += y_change

        if ik(x, y) != False:
            # determine elbow point
            a_shoulder, a_elbow = ik(x,y)
            xe = pixel_one * math.cos(a_shoulder) + originx
            ye = originy - (pixel_one * math.sin(a_shoulder))

            xo = x; yo = y
            # draw line
            pygame.draw.lines(gameDisplay, blue, False, [[originx,originy], [xe, ye], [xo, yo]], 5)

        else: # out of range so stay
            pygame.draw.lines(gameDisplay, pink, False, [[originx,originy], [xe, ye], [xo, yo]], 5)
            x = xo; y = yo
            pygame.draw.circle(gameDisplay, pink, (x, y), (5), 0)
        
        global x
        x = x 
        global y
        y = y

        pygame.display.update()
        gameDisplay.fill(grey)
        pygame.draw.circle(gameDisplay, white, (originx, originy), (pixel_one + pixel_two), 0)
        pygame.draw.circle(gameDisplay, grey, (originx, originy), (pixel_one - pixel_two), 0)
        pygame.draw.rect(gameDisplay, grey, [0, (originy + 24), display_width, display_width])


####
pygame.quit()

######################################
######################################
# Conner's code
######################################
######################################



######################################
# Variables
######################################

d_one = 62.0 #distance from shoulder to elbow
d_two = 48.0 #distance from elbow to wrist

x = 0.0 #starting x value
y = 110.0 #starting y value
z = 0.0 #starting z value
speed = 1 #starting speed (whole number between 1 and 4)


######################################
# movement functions
######################################

# rip

######################################
# setup apple vs mcsft
######################################

try: #if running on apple
    import sys, tty, termios #imports for no return command

    fd = sys.stdin.fileno() #unix file descriptor to define the file type
    old_settings = termios.tcgetattr(fd) #records the existing console settings

    tty.setcbreak(sys.stdin) #sets the style of input

    apple = True #computer type

except: #if running on microsoft
    import msvcrt #microsoft file for key input

    microsoft = True #computer type

######################################
# read keys
######################################

# rip

######################################
# motor setup
######################################

quit = False #for breaking the motor loop with the '1' key command
try: #if not connected to a RoboPi, it can still run
    import RoboPiLib_pwm as RPL #to pull all files needed to run the motors
    RPL.RoboPiInit("/dev/ttyAMA0", 115200) #connect to RoboPi

    motor_speed = 500

    max_error = 5 #max distance arm can be away from intended point (multiply by sqrt(3) to get max distance away)

    shoulder_pul = 1 #shoulder pulse pin
    shoulder_dir = 2 #shoulder direction pin
    elbow_pul = 3 #elbow pulse pin
    elbow_dir = 4 #elbow direction pin
    swivel_continuous = 1 #pin for swivel motor
    ppin_shoulder = 7 #pin number for shoulder potentiometer
    ppin_elbow = 8 #pin number for elbow potentiomenter
    ppin_swivel = 9 #pin number for swivel potentiomenter

    print "shoulder_pul", shoulder_pul
    print "shoulder_dir", shoulder_dir
    print "elbow_pul", elbow_pul
    print "elbow_dir", elbow_dir
    print "swivel_continuous", swivel_continuous
    print "ppin_shoulder", ppin_shoulder
    print "ppin_elbow", ppin_elbow
    print "ppin_swivel", ppin_swivel

    RPL.pinMode(shoulder_pul, RPL.PWM) #set shoulder_pul pin as a pulse-width modulation output
    RPL.pinMode(shoulder_dir, RPL.OUTPUT) #set shoulder_dir pin to an output and write 1 to it
    RPL.pinMode(elbow_pul, RPL.PWM) #set elbow_pul pin as a pulse-width modulation output
    RPL.pinMode(elbow_dir, RPL.OUTPUT) #set elbow_dir pin to an output and write 1 to it

except:
    print 'Motors unrunnable: unable to reach RoboPiLib_pwm'

######################################
# run motors
######################################

import math #to calculate all angle values
def motor_runner(): #sends signals to all the motors based on potentiometer readings
    while quit == False:
        reach_length = (x ** 2 + y ** 2 + z ** 2) ** 0.5
        a_elbow = math.acos(round(((d_one ** 2 + d_two ** 2 - reach_length ** 2) / (2 * d_one * d_two)), 2))
        a_shoulder = math.asin(round((d_two * math.sin(a_elbow) / reach_length), 2)) + math.asin(round((y / reach_length), 2))
        a_swivel = math.atan2(round(x, 2), round(z, 2))

        try:
            pot_shoulder = RPL.analogRead(ppin_shoulder) * 29 * math.pi / 18432
            error_s = abs(pot_shoulder - a_shoulder) #how many degrees off the intended value the arm is
            calculated_error_s = error_s * d_one
            if pot_shoulder > a_shoulder and calculated_error_s > max_error:
                RPL.digitalWrite(shoulder_dir, 1) #turn clockwise
                RPL.pwmWrite(shoulder_pul, motor_speed, motor_speed * 2)
            elif pot_shoulder < a_shoulder and calculated_error_s > max_error:
                RPL.digitalWrite(shoulder_dir, 0) #turn counterclockwise
                RPL.pwmWrite(shoulder_pul, motor_speed, motor_speed * 2)
            elif calculated_error_s < max_error:
                RPL.pwmWrite(shoulder_pul, 0, motor_speed * 2) #stops running while in range

            pot_elbow = RPL.analogRead(ppin_elbow) * 29 * math.pi / 18432
            error_e = abs(pot_elbow - a_elbow) #how many degrees off the intended value the arm is
            calculated_error_e = error_e * d_two
            if pot_elbow > a_elbow and calculated_error_e > max_error:
                RPL.digitalWrite(elbow_dir, 1) #turn clockwise
                RPL.pwmWrite(elbow_pul, motor_speed, motor_speed * 2)
            elif pot_elbow < a_elbow and calculated_error_e > max_error:
                RPL.digitalWrite(elbow_dir, 0) #turn counterclockwise
                RPL.pwmWrite(elbow_pul, motor_speed, motor_speed * 2)
            elif calculated_error_e < max_error:
                RPL.pwmWrite(elbow_pul, 0, motor_speed * 2) #stops running while in range

            pot_swivel = RPL.analogRead(ppin_swivel) * 29 * math.pi / 18432
            error_sw = abs(pot_swivel - a_swivel) #how many degrees off the intended value the arm is
            if pot_swivel > a_swivel and error_sw > max_error:
                RPL.servoWrite(swivel_continuous, 2000) #turn clockwise
            elif pot_swivel < a_swivel and error_sw > max_error:
                RPL.servoWrite(swivel_continuous, 1000) #turn counterclockwise
            elif error_sw < max_error:
                RPL.servoWrite(swivel_continuous, 0) #stops running while in range

        except: #to show the values of the motor arm
            import time
            time.sleep(1)
            print('[elbow, shoulder, swivel]:', [round(a_elbow, 4), round(a_shoulder, 4), round(a_swivel, 4)], '[Speed]:', [speed], '[x, y, z]:', [round(x, 2), round(y, 2), round(z, 2)])

######################################
# threading!
######################################

import threading #runs both functions simultanously
threading.Thread(target = motor_runner, name = 'motor_runner').start()
threading.Thread(target = key_reader, name = 'key_reader').start()

