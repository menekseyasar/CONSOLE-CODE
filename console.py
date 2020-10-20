import pygame

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()


leftxaxis = 0
leftyaxis = 0
rightxaxis = 0
rightyaxis = 0
hatx = 0
haty = 0

while True:
    yuvarlak = 0
    ucgen = 0
    L1 = 0
    R1 = 0
    L2 = 0
    R2 = 0
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0:
                leftxaxis = event.value
            if event.axis == 1:
                leftyaxis = event.value
            if event.axis == 2:
                rightxaxis = event.value
            if event.axis == 3:
                rightyaxis = event.value
        if event.type == pygame.JOYHATMOTION:
            if event.value == (0,1):
                haty = 1
            elif event.value == (0,-1):
                haty = -1
            elif event.value == (1,0):
                hatx = 1
            elif event.value == (-1,0):
                hatx = -1
            if event.value == (0,0):
                hatx = 0
                haty = 0
        if event.type == pygame.JOYBUTTONDOWN:
            if j.get_button(1):
                yuvarlak = 1
            if j.get_button(2):
                ucgen = 1
            if j.get_button(4):
                L1 = 1
            if j.get_button(5):
                R1 = 1
            if j.get_button(6):
                L2 = 1
            if j.get_button(7):
                R2 = 1