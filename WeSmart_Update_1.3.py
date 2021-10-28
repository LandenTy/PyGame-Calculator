"""
SMART Caluclator

Description: This is a test of me making a smart calculator, that can
detect key presses; and uses them to make equations. Then it will solve
said equations.
"""

#---- Variables ----#
opperation = ""
equation = ""
choose = "x"
x = ""
y = ""

#---- Libraries ----#
import tsk
import pygame

#---- Prerequisites ----#
running = True
pygame.init()

#---- PyGame_Variables ----#
screen_height = 1920
screen_width = 1080

screen = pygame.display.set_mode((screen_height, screen_width)) 

#---- Program ----#

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        #Keyboard Input
        if event.type == pygame.KEYDOWN:
            
            #Number Input
            if event.key == pygame.K_1:
                
                if choose == "x":
                    x = x + str(1)
                    print("1")
                else:
                    y = y + str(1)
                    print("1")
            if event.key == pygame.K_2:
                
                if choose == "x":
                    x = x + str(2)
                    print("2")
                else:
                    y = y + str(2)
                    print("2")
                    
            if event.key == pygame.K_3:
                
                if choose == "x":
                    x = x + str(3)
                    print("3")
                else:
                    y = y + str(3)
                    print("3")
                    
            if event.key == pygame.K_4:
                
                if choose == "x":
                    x = x + str(4)
                    print("4")
                else:
                    y = y + str(4)
                    print("4")
            
            if event.key == pygame.K_5:
                
                if choose == "x":
                    x = x + str(5)
                    print("5")
                else:
                    y = y + str(5)
                    print("5")
            
            if event.key == pygame.K_6:
                
                if choose == "x":
                    x = x + str(6)
                    print("6")
                else:
                    y = y + str(6)
                    print("6")
            
            if event.key == pygame.K_7:
                
                if choose == "x":
                    x = x + str(7)
                    print("7")
                else:
                    y = y + str(7)
                    print("7")
            
            if event.key == pygame.K_8:
                
                if choose == "x":
                    x = x + str(8)
                    print("8")
                else:
                    y = y + str(8)
                    print("8")
            
            if event.key == pygame.K_9:
                
                if choose == "x":
                    x = x + str(9)
                    print("9")
                else:
                    y = y + str(9)
                    print("9")
            
            if event.key == pygame.K_0:
                
                if choose == "x":
                    x = x + str(0)
                    print("0")
                else:
                    y = y + str(0)
                    print("0")
            
            #Checks for Plus Key
            if event.key == 61:
                print(" + ")
                choose = "y"
                oppertion = "+"
            
            if event.key == pygame.K_MINUS:
                print(" - ")
                choose = "y"
                oppertion = "-"
                
            #Checks for Enter Key
            if event.key == pygame.K_RETURN:
                
                # ---- Calculation Storage ---- #
                if oppertion == "+":
                    print()
                    print(int(x) + int(y))
                    
                if oppertion == "-":
                    print()
                    print(int(x) - int(y))
                
screen.fill((0,0,1))
pygame.display.flip() 
