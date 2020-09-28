#Ball physics and properties

import pygame
import random
import math


pygame.init()

class Ball():

    sound_block_hit = pygame.mixer.Sound("Sounds/block_hit.wav")

    lost = False

    radius = 10

    x = 0
    y = 0

    xSpeed = 0
    ySpeed = 0

    constSpeed = 0

    ballImg = pygame.image.load('Sprites/Ball.png')

    def __init__(self, x, y, vSpeed):
        self.x = x
        self.y = y

        self.constSpeed = 3

        if(vSpeed > 0):
            self.xSpeed = -self.constSpeed
        else:
            self.xSpeed = self.constSpeed

        self.ySpeed = -(self.constSpeed)

    def draw(self, gameDisplay):
        gameDisplay.blit(self.ballImg, (self.x, self.y))

    def move(self, thisPlatform, thisBlocksArray):

        if (self.x + self.xSpeed < 0) or (self.x + self.xSpeed + 2*self.radius > 800):
            self.inverseXSpeed()
        if (self.y + self.ySpeed < 0) or (self.y > 600):
            self.inverseYSpeed()

        self.check_col_with_platform(thisPlatform)
        self.check_col_with_all_blocks(thisBlocksArray)

        self.x += self.xSpeed
        self.y += self.ySpeed

        if(self.y > 600 or self.x + 2*self.radius < 0 or self.x > 800):
            self.lost = True

    def check_col_with_all_blocks(self, thisBlocksArray):
        
        for i in range(thisBlocksArray.numOfBlocks-1, -1, -1):
            self.check_col_with_one_block(thisBlocksArray.blocksArray[i])

    def check_col_with_one_block(self, thisBlock):

        if(self.y + 2*self.radius + self.ySpeed > thisBlock.y and self.y + self.ySpeed <= thisBlock.y + thisBlock.height):
            if(self.x + 2*self.radius + self.xSpeed >= thisBlock.x and self.x + self.xSpeed < thisBlock.x + thisBlock.width):

                pygame.mixer.Sound.play(self.sound_block_hit)
                 
                angle = self.angle(self.x + self.radius + self.xSpeed, self.y + self.radius + self.ySpeed , thisBlock.x + thisBlock.width/2, thisBlock.y + thisBlock.height/2)
                blockAngle = math.fabs(self.angle(thisBlock.x, thisBlock.y, thisBlock.x + thisBlock.width/2, thisBlock.y + thisBlock.height/2))
                

                if((angle >= -blockAngle and angle <= blockAngle) or (angle >= 180 - blockAngle and angle <= 180 + blockAngle)):
                    self.inverseXSpeed()
                else:
                    self.inverseYSpeed()
                    

                thisBlock.get_hit()

    def check_col_with_platform(self, thisPlatform):

        if(self.y + 2*self.radius + self.ySpeed >= thisPlatform.y):
            if(self.x + 2*self.radius + self.xSpeed >= thisPlatform.x + thisPlatform.Speed and self.x + self.xSpeed <= thisPlatform.x + thisPlatform.width + thisPlatform.Speed):

                
                if(self.y + 2*self.radius + self.ySpeed <= thisPlatform.y + (thisPlatform.height/2)):
                  self.inverseYSpeed()
                  self.y += self.ySpeed

                  if(thisPlatform.Speed > 0 and self.xSpeed < 3):
                      self.xSpeed += 2
                  elif(thisPlatform.Speed < 0 and self.xSpeed > -3):
                      self.xSpeed -= 2

                elif(self.x + self.xSpeed < thisPlatform.x + thisPlatform.width + thisPlatform.Speed or self.x + 2*self.radius + self.xSpeed > thisPlatform.x + thisPlatform.Speed):
                  self.inverseXSpeed()
                  self.x += self.xSpeed
                  if((thisPlatform.Speed > 0 and self.xSpeed > 0) or (thisPlatform.Speed < 0 and self.xSpeed < 0)):
                      self.xSpeed = thisPlatform.Speed
                      self.x += thisPlatform.Speed

    def angle(self, x, y, Cx, Cy):

        a = math.fabs(y - Cy)
        c = math.sqrt((x - Cx)*(x - Cx) + (y - Cy)*(y - Cy))

        result = math.asin(a/c) * 180 / math.pi

        return result
                

    def inverseXSpeed(self):
        self.xSpeed = -(self.xSpeed)
    def inverseYSpeed(self):
        self.ySpeed = -(self.ySpeed)

        
