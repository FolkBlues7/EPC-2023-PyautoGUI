import pyautogui
import keyboard

#This are is responsable for fiding the waypoint and moving the character
miniMapRegion = [1752, 1, 106, 110]
def moveMinimapSimbol_1():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_01.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_2():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_02.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_3():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_03.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_4():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_04.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_5():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_05.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_6():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_06.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_7():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_07.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_8():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_08.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_9():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_09.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_10():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_10.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_11():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_11.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_12():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_12.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_13():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_13.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_14():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_14.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_15():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_15.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_16():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_16.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_17():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_17.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_18():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_18.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_19():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_19.png", region=miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

def moveMinimapSimbol_20():
    coordinate = pyautogui.locateCenterOnScreen("imagens/miniMapIcon_20.png", region= miniMapRegion , confidence= 0.8)
    pyautogui.leftClick(coordinate.x, coordinate.y)

#responsable for taking loot from the bodies, not done yet! PRE ALPHA
lootRegion = {764, 379, 206, 209}
def loot():
    pyautogui.rightClick(875, 571) #sul
    pyautogui.rightClick(953, 571) #suldeste
    pyautogui.rightClick(953, 493) #oeste
    pyautogui.rightClick(954, 415) #nordeste
    pyautogui.rightClick(876, 415) #norte
    pyautogui.rightClick(798, 415) #noroeste
    pyautogui.rightClick(798, 493) #leste
    pyautogui.rightClick(789, 571) #sudoeste

#responsabel to heal the character if needed
def checkHeal():
    while(pyautogui.pixelMatchesColor(853, 9, (41,41,41)) == True):
        pyautogui.press("2")
        print("healing")

#responsabel to eat if the character is hungry
statusBar = [820, 37, 105, 13]
def checkHungry():
    result = pyautogui.locateOnScreen("imagens/hungryIcon.png", confidence=0.8)
    print(result)
    if (result != None):
        print(result)
        pyautogui.press('4')

#check if there is wasps in the battle list
battleListCoordinate = [1569, 0, 175,463]
def checkCombat():
    if(pyautogui.locateOnScreen("imagens/wasp.png", region= battleListCoordinate, confidence=0.8)!=None):
        return True
    else:
        return False

def killMonsters():
    while(checkCombat() == True):
        pyautogui.press('space')
        pyautogui.sleep(4)

#drop to the next floor
def holeDown():
    result = pyautogui.locateOnScreen("imagens/holeDown.png", confidence = 0.8)
    x, y = pyautogui.center(result)
    pyautogui.leftClick(x,y)   
    pyautogui.sleep(10)

#use hope when the floor is wiped
def useHopeSecondeFloor():
    result = pyautogui.locateCenterOnScreen("imagens/anchorSecondFloor.png", confidence= 0.8)
    pyautogui.moveTo(result.x - 470, result.y -320)
    pyautogui.press('F3')
    pyautogui.leftClick()
    pyautogui.sleep(1)

def doLure():
    killMonsters()
    loot()
    checkHeal()
    checkHungry()

def firstFloor():
    #lure1
    doLure()#funcionando
    #lure2
    moveMinimapSimbol_2()
    pyautogui.sleep(5)
    doLure()#funcionando
    #lure3
    moveMinimapSimbol_3()
    pyautogui.sleep(5)
    doLure()#funcionando
    #lure4
    moveMinimapSimbol_4()
    pyautogui.sleep(9)
    doLure()
    #lure5
    moveMinimapSimbol_5()
    pyautogui.sleep(8)
    doLure()
    #lure6
    moveMinimapSimbol_6()
    pyautogui.sleep(5)
    doLure()
    #lure7
    moveMinimapSimbol_7()
    pyautogui.sleep(8)
    doLure()
    #lure8
    moveMinimapSimbol_8()
    pyautogui.sleep(8)
    doLure()
    #dropHole and lure
    holeDown()
    pyautogui.sleep(8)
    doLure()

def secondFloor():
    #lure9
    doLure()
    moveMinimapSimbol_9()
    pyautogui.sleep(8)
    doLure()#ok
    #lure10
    moveMinimapSimbol_10()
    pyautogui.sleep(5)
    doLure()#ok
    #lure11
    moveMinimapSimbol_11()
    pyautogui.sleep(8)
    doLure()#ok
    #lure12
    moveMinimapSimbol_12()
    pyautogui.sleep(11)
    doLure()
    #lure13
    moveMinimapSimbol_16()
    pyautogui.sleep(5)
    doLure()
    #lure14
    moveMinimapSimbol_13()
    pyautogui.sleep(5)
    doLure()
    #lure15
    moveMinimapSimbol_14()
    pyautogui.sleep(10)
    doLure()
    #lure16
    moveMinimapSimbol_15()
    pyautogui.sleep(5)
    doLure()
    #lure17
    moveMinimapSimbol_16()
    pyautogui.sleep(10)
    doLure()
    #lure17
    moveMinimapSimbol_12()
    pyautogui.sleep(5)
    doLure()
    #use rope
    useHopeSecondeFloor()
    doLure()
    #lure0
    moveMinimapSimbol_1()
    pyautogui.sleep(7)
    doLure()


keyboard.wait('h')
while True:
    
    firstFloor()
    secondFloor()


    

