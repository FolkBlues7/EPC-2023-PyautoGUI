import pyautogui as pg
import keyboard as key
battleListCoordinate = [1569, 0, 175,463]
lootRegion = [756, 368, 232, 251]
miniMapRegion = [1752, 1, 106, 110]

def checkCombat():
    if(pg.locateOnScreen("imagens/wasp.png", region= battleListCoordinate, confidence=0.8)!=None):
        return True
    else:
        return False

def killMonsters():
    while(checkCombat() == True):
        pg.press('space')
        pg.sleep(4)

def lootMonsters():
    pg.sleep(2)
    pg.rightClick(875, 571) #sul
    pg.rightClick(953, 571) #suldeste
    pg.rightClick(953, 493) #oeste
    pg.rightClick(954, 415) #nordeste
    pg.rightClick(876, 415) #norte
    pg.rightClick(798, 415) #noroeste
    pg.rightClick(798, 493) #leste
    pg.rightClick(789, 571) #sudoeste
        

def checkHeal(): #check if heal is needed, if it is, heals until 100% hp.
    while(pg.pixelMatchesColor(853, 9, (41,41,41)) == True):
        pg.press("2")
        print("healing")

def lure0():
    result = pg.locateOnScreen("imagens/lure0.png", region = miniMapRegion, confidence = 0.8)
    x, y = pg.center(result)
    pg.leftClick(x,y)
    pg.sleep(5)

def lure1():
    result = pg.locateOnScreen("imagens/lure1.png", region = miniMapRegion, confidence = 0.8)
    x, y = pg.center(result)
    pg.leftClick(x,y)
    pg.sleep(8)
    
def lure2():
    result = pg.locateOnScreen("imagens/lure2.png", region = miniMapRegion, confidence = 0.8)
    x, y = pg.center(result)
    pg.leftClick(x,y)
    pg.sleep(5)

def lure3():
    result = pg.locateOnScreen("imagens/lure3.png", region = miniMapRegion, confidence = 0.8)
    x, y = pg.center(result)
    pg.leftClick(x,y)
    pg.sleep(15)

def lure4():
    result = pg.locateOnScreen("imagens/lure4.png", region = miniMapRegion, confidence = 0.8)
    x, y = pg.center(result)
    pg.leftClick(x,y)    
    pg.sleep(12)

def lure5():
    result = pg.locateOnScreen("imagens/lure5.png", region = miniMapRegion, confidence = 0.8)
    x, y = pg.center(result)
    pg.leftClick(x,y) 
    pg.sleep(12)

def lure6():
    result = pg.locateOnScreen("imagens/lure6.png", region = miniMapRegion, confidence = 0.8)
    x, y = pg.center(result)
    pg.leftClick(x,y)   
    pg.sleep(10)

def holeDown():
    result = pg.locateOnScreen("imagens/holeDown.png", confidence = 0.8)
    x, y = pg.center(result)
    pg.leftClick(x,y)   
    pg.sleep(10)

def lure7():
    result = pg.locateOnScreen("imagens/lure7.png", region = miniMapRegion, confidence = 0.8)
    x, y = pg.center(result)
    pg.leftClick(x,y)   
    pg.sleep(10)
    
def lure8():
    result = pg.locateOnScreen("imagens/lure8.png", region = miniMapRegion, confidence = 0.8)
    x, y = pg.center(result)
    pg.leftClick(x,y)   
    pg.sleep(5)

def lure9():
    result = pg.locateOnScreen("imagens/lure9.png", region = miniMapRegion, confidence = 0.8)
    x, y = pg.center(result)
    pg.leftClick(x,y)   
    pg.sleep(8)

def lure10():
    result = pg.locateOnScreen("imagens/lure6.png", region = miniMapRegion, confidence = 0.8)
    x, y = pg.center(result)
    pg.leftClick(x,y)   
    pg.sleep(20)

def lure11():
    result = pg.locateOnScreen("imagens/lure10.png", region = miniMapRegion, confidence = 0.8)
    x, y = pg.center(result)
    pg.leftClick(x,y)   
    pg.sleep(10)

def lure12():
    result = pg.locateOnScreen("imagens/lure12.png", region = miniMapRegion, confidence = 0.8)
    x, y = pg.center(result)
    pg.leftClick(x,y)   
    pg.sleep(10)

def lure13():
    result = pg.locateOnScreen("imagens/lure11.png", region = miniMapRegion, confidence = 0.8)
    x, y = pg.center(result)
    pg.leftClick(x,y)   
    pg.sleep(10)

def useHopeSecondeFloor():
    result = pg.locateCenterOnScreen("imagens/anchorSecondFloor.png", confidence= 0.8)
    pg.moveTo(result.x - 470, result.y -320)
    pg.press('F3')
    pg.leftClick()
    pg.sleep(1)

key.wait('h')
while True:
    killMonsters()
    lootMonsters() #até aqui OK
    lure1()
    killMonsters()
    lootMonsters() #até aqui OK
    lure2()
    killMonsters()
    lootMonsters() #até aqui OK
    lure3()
    killMonsters()
    lootMonsters() #até aqui OK
    lure4()
    killMonsters()
    lootMonsters() #até aqui OK
    lure5()
    killMonsters()
    lootMonsters() #até aqui OK
    lure6()
    killMonsters()
    lootMonsters() #até aqui OK
    holeDown()
    killMonsters()
    lootMonsters() #até aqui OK
    lure7()
    killMonsters()
    lootMonsters() #até aqui OK
    lure8()
    killMonsters()
    lootMonsters() #até aqui OK
    lure9()
    killMonsters()
    lootMonsters() #até aqui OK
    lure10()
    killMonsters()
    lootMonsters() #até aqui OK
    lure5()
    killMonsters()
    lootMonsters() #até aqui OK
    lure11()
    killMonsters()
    lootMonsters() #até aqui OK
    lure12()
    killMonsters()
    lootMonsters() #até aqui OK
    lure13()
    killMonsters()
    lootMonsters() #até aqui OK
    useHopeSecondeFloor()
    killMonsters()
    lootMonsters() #até aqui OK
    lure0()
    killMonsters()
    lootMonsters() #até aqui OK








