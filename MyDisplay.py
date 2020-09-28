import pygame

pygame.init()

class Display():

    displayWidth = 800
    displayHeight = 600

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    gameDisplay = pygame.display.set_mode((displayWidth, displayHeight)) #Init display

    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.white)                #AA - True
        return textSurface, textSurface.get_rect()

    def message_display(self, text, size, x, y):
        textDesc = pygame.font.Font('retro.ttf', size)
        textSurf, textRect = self.text_objects(text, textDesc)          #textSurf contains text, color and AA
        textRect.center = (x, y)
        self.gameDisplay.blit(textSurf, textRect)

