import pygame

pygame.init()

class Platform():

    width = 120
    height = 22

    x = 0
    y = 0

    Speed = 0

    color = (255, 255, 255)

    platformS1Img = pygame.image.load('Sprites/Platform_Short.png')
    platformStanImg = pygame.image.load('Sprites/Platform_Standard.png')
    platformL1Img = pygame.image.load('Sprites/Platform_Long.png')

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.platformImg = self.platformStanImg

    def draw(self, gameDisplay):
        gameDisplay.blit(self.platformImg, (self.x, self.y))

    def move(self):
        
        if self.x + self.Speed + self.width > 800 or self.x + self.Speed < 0:
            self.stop()
        
        self.x += self.Speed

    def increase_speed(self):
        self.Speed = 5
    def decrease_speed(self):
        self.Speed = -5
    def stop(self):
        self.Speed = 0

    def change_platform_image(self):
        if(self.width == 80):
            self.platformImg = self.platformS1Img
        elif(self.width == 120):
            self.platformImg = self.platformStanImg
        elif(self.width == 160):
            self.platformImg = self.platformL1Img


    def shortenPlatform(self):

        if(self.width > 80):
            self.width -= 40
            self.change_platform_image()

    def lengthenPlatform(self):

        if(self.width < 160):
            self.width += 40
            self.change_platform_image()



