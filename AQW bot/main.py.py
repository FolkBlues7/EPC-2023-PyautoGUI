import pyautogui as pg
import keyboard as key
import time        

liga = True

# Encontra na tela o ícone ou imagem e clica
def buscarEClicar(a):
    locate = pg.locateOnScreen('image\\' + a, confidence = 0.8)
    if (locate != None):
        pg.click(locate)

# Sempre que uma missão for completa, essa função vai perceber e entrega-la para receber suas recompensas, em seguida ela irá buscar pelo 
# botão de replay da luta
def turnIn():
    locate = pg.locateOnScreen('image\\questCompletedMessage.png', confidence = 0.7)
    if (locate != None):
        locate = pg.locateOnScreen('image\\questMenu.png', confidence = 0.9)
        if (locate != None):
            pg.click(locate)
            
            time.sleep(0.3)
            
            locate = pg.locateOnScreen('image\\questButton.png', confidence = 0.9)
            if (locate != None):
                pg.click(locate)
                
                time.sleep(0.3)
                
                locate = pg.locateOnScreen('image\\questNameComplete.png', confidence = 0.7)
                if (locate != None):
                    pg.click(locate)
                    
                    time.sleep(1)
                    
                    locate = pg.locateOnScreen('image\\turnIn.png', confidence = 0.7)
                    if (locate != None):
                        pg.click(locate)
                        
                        time.sleep(1)
                        
                        buscarEClicar('closeQuestTab.png')
                        
    buscarEClicar('repeatFight.png')
                       

# Espera 5 segundos para começar
time.sleep(5)

buscarEClicar('abrirDialogo.png')
    
time.sleep(1)

buscarEClicar('questIcon.png')
        
time.sleep(1)

buscarEClicar('questName.png')
    
time.sleep(1)

buscarEClicar('accept.png')
    
time.sleep(1)

buscarEClicar('closeQuestTab.png')

time.sleep(1)

buscarEClicar('battleIcon.png')
    
time.sleep(1)

buscarEClicar('battleName.png')

time.sleep(3)    
        
# Combate

 # Spamma os ícones de skill 5, 4, 3 e 2 (sendo o 1 automático), e caso você aperte h o loop em breve irá parar 
while liga:
    buscarEClicar('enemyImage.png')
    buscarEClicar('skill5.png')
    if (key.is_pressed("h")):
        liga = False
    buscarEClicar('skill4.png')
    if (key.is_pressed("h")):
        liga = False
    buscarEClicar('skill3.png')
    if (key.is_pressed("h")):
        liga = False
    buscarEClicar('skill2.png')
    if (key.is_pressed("h")):
        liga = False
    
    turnIn()