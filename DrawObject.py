#Drawing objects on screen

import MyBonuses
import MyPlatform
import MyBall
import random

def draw_and_move_every_ball(ballArray, thisPlatform, thisBlocksArray, gameDisplay):

    for i in range(len(ballArray)-1, -1, -1):

            if(ballArray[i].lost == True):
                del ballArray[i]
            else:
                ballArray[i].move(thisPlatform, thisBlocksArray)
                ballArray[i].draw(gameDisplay)

def draw_all_bonuses(bonusArray, thisPlatform, ballArray, gameDisplay):

    for i in range(len(bonusArray)-1, -1, -1):

        if(bonusArray[i].lost == True):
            del bonusArray[i]
        else:
            bonusArray[i].draw(gameDisplay)
            bonusArray[i].move(thisPlatform)

            if(bonusArray[i].collided == True):
                bonusArray[i].lost = True
            
                if(bonusArray[i].bonusType == 1):
                    for i in range(len(ballArray)-1, -1, -1):
                        ballArray.append(MyBall.Ball(ballArray[i].x, ballArray[i].y, ballArray[i].xSpeed))
                    
                elif(bonusArray[i].bonusType == 2):
                    thisPlatform.shortenPlatform()
                    
                elif(bonusArray[i].bonusType == 3):
                    thisPlatform.lengthenPlatform()

def draw_all_blocks(thisBlocksArray, bonusArray, gameDisplay):
    
    for i in range(thisBlocksArray.numOfBlocks-1, -1, -1):

        random.seed()

        randomBonusAppereance = random.randrange(5)
        
        if(thisBlocksArray.blocksArray[i].isHit == 0):

            if(randomBonusAppereance == 4):
                random.seed()
                randomBonusType = random.randrange(3) + 1
                bonusArray.append(MyBonuses.Bonus(thisBlocksArray.blocksArray[i].x, thisBlocksArray.blocksArray[i].y, randomBonusType))
            
            del thisBlocksArray.blocksArray[i]
            thisBlocksArray.numOfBlocks -= 1

        else:
            thisBlocksArray.blocksArray[i].draw(gameDisplay)

def draw_and_move_platform(thisPlatform, gameDisplay):

    thisPlatform.draw(gameDisplay)
    thisPlatform.move()
