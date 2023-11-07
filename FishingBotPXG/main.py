import pyautogui as pg
import keyboard as key
import random

fishingSpots = [(543, 209, 90, 94),(358, 394, 90, 94),(358, 301, 90, 94)]
def startFishing(): #throws the bait and push it in the right time
    randomSpot = random.choice(fishingSpots)
    x, y = pg.center(randomSpot)
    pg.moveTo(x, y)
    key.press_and_release('capslock') #throws the bait
    while (pg.locateOnScreen("pictures/bubbles.png", region= randomSpot,confidence=0.8) == None):
        print("waiting for fish")    
    key.press_and_release('capslock') #push the bait
    
battleListRegion = (1716, 388, 204, 352)
def checkCreatures(): #checks if there's creatures in the battle list
    if (pg.locateOnScreen("pictures/magikarp.png", region= battleListRegion, confidence= 0.8) != None):
        return True
    else:
        return False

singleTargetRegion = (1721, 421, 33, 261)  
def checkTargetedCreature():#check if there's a targeted creature
    if (pg.locateOnScreen("pictures/redTarget.png", region= singleTargetRegion, confidence= 0.8) != None):
        return True
    else:
        return False

attackList = ('1','2','3','4','5','6')
def killCreatures():
    while(checkCreatures() == True):
        key.press_and_release('tab')
        killSingleTarget()

def killSingleTarget():#uses the preset skills and stop if there's no targets
    for i in attackList:
        key.press_and_release(i)
        pg.sleep(0.8)
        if(checkCreatures() == False or checkTargetedCreature() == False):
            break

hungryIconRegion = (165, 77, 14, 17)
def checkHungry(): #gives food for the pokemon when necessary
    if(pg.locateOnScreen("pictures/hungryIcon.png",region=hungryIconRegion, confidence=0.9) != None):
        key.press_and_release('F3')
    else:
        print("Não está com fome!")
   

def checkHeal(): #use potion when necessary
    if (pg.pixelMatchesColor(199, 58,(16,16,16)) == True):
        key.press_and_release('F1')
        

puzzleRegion = (952, 496, 14, 344)
def solvePuzzle():#solve the fishing minigame
    if(pg.pixelMatchesColor(958, 822, (68, 145, 252)) == True):
        while True:
            if (checkCreatures() == True):
                break
            blueBar = pg.locateOnScreen("pictures/blueBar.png",region=puzzleRegion, confidence=0.9)
            fishPuzzle = pg.locateOnScreen("pictures/fishPuzzle.png",region=puzzleRegion, confidence=0.8, grayscale=True)
            while(blueBar == None or fishPuzzle == None):
                blueBar = pg.locateOnScreen("pictures/blueBar.png",region=puzzleRegion, confidence=0.9)
                fishPuzzle = pg.locateOnScreen("pictures/fishPuzzle.png",region=puzzleRegion, confidence=0.8, grayscale=True)
                key.release('space')
                if (checkCreatures() == True):
                    break
            if (checkCreatures() == True):
                    break
            if (blueBar.top > fishPuzzle.top):
                key.press('space')
            else:
                key.release('space')

key.wait('h')
checkHungry()

#while True:
    #checkHungry()
#    checkHeal()
    #pg.displayMousePosition()
    #checkHungry()
#    startFishing()
#    pg.sleep(1)
#    solvePuzzle()
#    pg.sleep(1)
#    killCreatures()
#    pg.sleep(1)
#    key.press_and_release('F12') #autoloot    
   


    



#while True:
#    startFishing()
#    pg.sleep(1) #if it's too fast, won't work
#    killCreatures()
#    pg.sleep(1)
#    key.press_and_release('F12') #autoloot