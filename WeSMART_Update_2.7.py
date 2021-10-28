"""
WeSMART Online Calculator ~ Update 2.71

Description: Update 2.71 to the WeSMART Online Calculator.
    -Decreased lines used for performance
    -Allows for equations of unlimited length
    -Small Bug Fixes
"""

# ---- Arrays ---- #
keyCodes_num = [49, 50, 51, 52, 53, 54, 55, 56, 57, 48, 32]

#Opperations array, keeps track of ALL opperations used in equation
Opperations = [61]

# ---- Configures ALL Numbers used in Equation. ---- #
equation = ['']

#---- Libraries ----#
import tsk
import pygame

#---- Prerequisites ----#
running = False
pygame.init()

#---- PyGame_Variables ----#
screen_height = 1920
screen_width = 1080
screen = pygame.display.set_mode((screen_height, screen_width)) 

# ---- Variables ---- #
item = ""

#---- Program ----#
print("Starting the SMART Calculator. V.2.1")
print()
running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        #Keyboard Input
        if event.type == pygame.KEYDOWN:
            
            # Numbers
            if event.key == keyCodes_num[0]:
                
                item += str(1)
                
            if event.key == keyCodes_num[1]:
                
                item += str(2)
                
            if event.key == keyCodes_num[2]:
                
                item += str(3)
                
            if event.key == keyCodes_num[3]:
                
                item += str(4)
            
            if event.key == keyCodes_num[4]:
                
                item += str(5)
            
            if event.key == keyCodes_num[5]:
                
                item += str(6)
            
            if event.key == keyCodes_num[6]:
                
                item += str(7)
            
            if event.key == keyCodes_num[7]:
                
                item += str(8)
            
            if event.key == keyCodes_num[8]:
                
                item += str(9)
            
            if event.key == keyCodes_num[9]:
                
                item += str(0)
                
            #Opperations
            if event.key == Opperations[0]:
                #+ Key
                
                item += "+"
                
            if event.key == pygame.K_MINUS:
                #- Key
                
                item += "-"
                
            # Space
            if event.key == keyCodes_num[10]:
                print(item)
                equation.append(item)
                item = ""
                
            if event.key == pygame.K_RETURN:
                print()
                print(*equation)
