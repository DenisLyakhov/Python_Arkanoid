import pygame
import MyBlock

pygame.init()

class Blocks:

    def __init__(self, numOfBlocks, blocksLocationArray, colorArray):

        self.blocksArray = []

        for i in range(0, len(blocksLocationArray)):
            x, y = convertTo(blocksLocationArray[i])
            newBlock = MyBlock.Block(x, y, colorArray[i])
            
            self.blocksArray.append(newBlock)

        self.numOfBlocks = numOfBlocks

def convertTo(number):
    k = int(number/15)

    if(number >= 15):
        number = number % 15

    return (int(number*52)+10), (k*24 + 50)

    
