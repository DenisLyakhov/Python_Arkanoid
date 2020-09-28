import pygame
import random
import MyBall

pygame.init()

class Bonus():

    width = 30
    height = 30

    constSpeed = 1

    def __init__(self, x, y, bonusType):
        self.x = x
        self.y = y

        self.bonusType = bonusType

        self.bonusImg = pygame.image.load('Sprites/Bonus.png')

        if(bonusType == 1):
            self.bonusColor = (255, 255, 0)
                
        elif(bonusType == 2):
            self.bonusColor = (255, 0, 0)
                
        elif(bonusType == 3):
            self.bonusColor = (0, 0, 255)

        elif(bonusType == 4):
            self.bonusColor = (0, 255, 0)

        self.lost = False
        self.collided = False


    def draw(self, gameDisplay):
        gameDisplay.blit(self.bonusImg, (self.x, self.y))

    def check_col_with_platform(self, thisPlatform):

        if(self.x + self.width >= thisPlatform.x and self.x <= thisPlatform.x + thisPlatform.width):
            if(self.y + self.height >= thisPlatform.y and self.y <= thisPlatform.y + thisPlatform.height):
                self.collided = True

    
    def move(self, thisPlatform):

        if(self.y > 600):
            self.lost = True
        else:
            self.y += self.constSpeed

        self.check_col_with_platform(thisPlatform)
                    
                
        
