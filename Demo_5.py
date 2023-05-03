# Import the relevant modules
import pyautogui
import time

# Spiral drawing using pyautogui

time.sleep(3)   # temps d execution

distance = 300   # la longueur initiale

while distance > 0:

    #  pyautogui.dragRel permet de déplacer la souris en maintenant un bouton enfoncé

    pyautogui.dragRel(distance, 0,5, button="left")
    distance = distance - 20
    pyautogui.dragRel(0,5 , distance, button="left")
    pyautogui.dragRel(-distance, 0,5, button="left")
    distance = distance - 20
    pyautogui.dragRel(0,5 , -distance, button="left")
    
    time.sleep(2)