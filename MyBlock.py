#Block properties

import pygame

pygame.init()

class Block:

    width = 50
    height = 22

    def __init__(self, x, y, color):
        self.x = x
        self.y = y

        self.isHit = 1

        if(color == 1):
            colorImgName = 'Sprites/block_green.png'
        elif(color == 2):
            colorImgName = 'Sprites/block_blue.png'
        elif(color == 3):
            colorImgName = 'Sprites/block_red.png'
        elif(color == 0):
            colorImgName = 'Sprites/block_grey.png'
            self.isHit = 2

        self.blockImg = pygame.image.load(colorImgName)

    def draw(self, gameDisplay):
        gameDisplay.blit(self.blockImg, (self.x, self.y))

    def get_hit(self):
        self.isHit -= 1
        self.blockImg = pygame.image.load('Sprites/block_grey_hit.png')
