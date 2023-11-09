import keyboard
#Instalação: "pip install pyautogui"
import pyautogui

#------------------------------------

#Segurança:
#pyautogui.FAILSAFE = True

#------------------------------------

#Printar posição do mouse:
#pyautogui.position()
#print(pyautogui.position())

#------------------------------------

#Printar tamanho do monitor
#print(pyautogui.size())

#------------------------------------

#Comando de pausa de x segundos a cada chamada da pyautogui()
#pyautogui.PAUSE = 2.5

#------------------------------------





#AQUI COMEÇA A FICAR INTERESSANTE MOUSE FUNCTIONS!

#move até a coordenada x y por determinado tempo em segundos
#pyautogui.moveTo(100, 100, duration=num_seconds)
#pyautogui.moveRel(xOffset, yOffset, duration=num_seconds) #move relativo a onde está

#------------------------------------

#arrasta com o mouse:
#keyboard.wait('h')
#pyautogui.dragTo(x, y, duration=num_seconds)
#pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)  #move relativo a onde está

#------------------------------------

#move e clica com o mouse:
#pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
#buttom: left, right ou middle

#------------------------------------

#pyautogui.rightClick(x=moveToX, y=moveToY)
#pyautogui.middleClick(x=moveToX, y=moveToY)
#pyautogui.doubleClick(x=moveToX, y=moveToY)
#pyautogui.tripleClick(x=moveToX, y=moveToY)

#------------------------------------
#pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)
#pyautogui.scroll(-10000)
#pyautogui.scroll(+10000)

#------------------------------------
#Escrever na tela?
#pyautogui.typewrite('Sim, eu jogo de malphite, como adivinhou ?\n', interval=0)

#------------------------------------
#mostra uma popup na tela e pausa a aplicação até que você clique em OK
#pyautogui.alert('Você pode criar um PopUP?')
#print("Clicou em OK")




#------------------------------------
#AQUI FICA MUITO MAIS LEGAL AINDA!!!!
#instalação: pip install Pillow
region = (10, 100, 90, 30)
#pyautogui.locateOnScreen("CaminhoImagem.PNG",confidence=0.0,region=(x,y,z,w) grayscale=False)
#pyautogui.locateAllOnScreen("CaminhoImagem.PNG",confidence=0.0,region=(x,y,z,w) grayscale=False)
#pyautogui.locateCenterOnScreen("CaminhoImagem.PNG",confidence=0.0,region=(x,y,z,w) grayscale=False)
#pyautogui.locateAllOnScreen("CaminhoImagem.PNG",confidence=0.0,region=(x,y,z,w) grayscale=False)

#------------------------------------

#e acabou!

