import stepper_control as SC
while True:
    print 'Input time to run motor at 1000 speed. Hit Q to quit.'
    position = input('- ')
    SC.elbow(True, position, 1000)
    if position == 'Q':
        break
    else:
        continue
