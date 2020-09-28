#The game has only 2 levels
#You can edit or add more levels in the "MyLevels" class

import pygame
import time
import random
import MyPlatform
import MyDisplay
import MyBlocksArray
import MyBall
import MyBonuses
import DrawObject
import MyLevels


backgroundGameImg = pygame.image.load('Sprites/Background_Game.png')
backgroundTitleImg = pygame.image.load('Sprites/Background_Title.png')
backgroundTutorialImg = pygame.image.load('Sprites/Background_Tutorial.png')



def game_over(finished):
    if(finished == 1):
        thisDisplay.message_display('Level Completed', 50, 400, 300)
    elif(finished == 0):
        thisDisplay.message_display('You Lost', 95, 400, 300)
    else:
        thisDisplay.message_display('You Won', 95, 400, 300)
    pygame.display.update()

    time.sleep(5)

def start_menu():

    showMessage = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return False
                
                
        thisDisplay.gameDisplay.blit(backgroundTitleImg, (0, 0))
        thisDisplay.message_display('Arkanoid', 90, 400, 200)

        if(showMessage):
            thisDisplay.message_display('Press Enter to Start', 20, 400, 450)
            showMessage = False
        else:
            showMessage = True

        pygame.display.update()
        clock.tick(2)

    return True

def show_tutorial():

    thisDisplay.gameDisplay.blit(backgroundTutorialImg, (0, 0))
    
    thisDisplay.message_display('Controls ', 50, 240, 150)

    pygame.display.update()

    time.sleep(5)
    

def game_loop(gameExit, currLevel):
    
    ballArray = []
    bonusArray = []

    # Add new first ball
    ballArray.append(MyBall.Ball(thisDisplay.displayWidth * 0.1, thisDisplay.displayHeight * 0.9 - 20, 0))

    # Add platform
    thisPlatform = MyPlatform.Platform(thisDisplay.displayWidth * 0.45, thisDisplay.displayHeight * 0.92)

    thisBlocksArray = MyBlocksArray.Blocks(len(MyLevels.levels[currLevel]), MyLevels.levels[currLevel], MyLevels.colors[currLevel])

    while not gameExit:

        for event in pygame.event.get():                                 #Grabs any event(button presses)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    thisPlatform.decrease_speed()
                if event.key == pygame.K_RIGHT:
                    thisPlatform.increase_speed()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    thisPlatform.stop()

            keys = pygame.key.get_pressed()  #checking pressed keys
            if keys[pygame.K_LEFT]:
                thisPlatform.decrease_speed()
            if keys[pygame.K_RIGHT]:
                thisPlatform.increase_speed()

        
        thisDisplay.gameDisplay.blit(backgroundGameImg, (0, 0))

        
        DrawObject.draw_all_bonuses(bonusArray, thisPlatform, ballArray, thisDisplay.gameDisplay)
        DrawObject.draw_all_blocks(thisBlocksArray, bonusArray, thisDisplay.gameDisplay)
        DrawObject.draw_and_move_platform(thisPlatform, thisDisplay.gameDisplay)
        DrawObject.draw_and_move_every_ball(ballArray, thisPlatform, thisBlocksArray, thisDisplay.gameDisplay)

        if(len(ballArray) == 0):
            gameExit = True
            game_over(0)
            return 0

        if(len(thisBlocksArray.blocksArray) == 0):
            if(currLevel != len(MyLevels.levels)-1):
                game_over(1)
            return 1


        pygame.display.update()                                          #Updates frame
        clock.tick(60)                                                   #Game speed


pygame.init()

pygame.display.set_caption('Arkanoid')                               #Set title

clock = pygame.time.Clock()                                          #Tracks time

thisDisplay = MyDisplay.Display()

currLevel = 0

start_menu()
show_tutorial()

while(True):
    finished = game_loop(False, currLevel)
    if(finished == 1):
        currLevel += 1
    if(currLevel == len(MyLevels.levels)):
        break

game_over(3)
pygame.quit()
quit()

