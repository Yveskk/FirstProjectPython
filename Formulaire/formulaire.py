import pyautogui
import time



time.sleep(3)
print(pyautogui.position())            # Recherche de la position
pyautogui.click(261,189)                # coordonnee du champs ou saisir
pyautogui.typewrite("kokou")             #  La saisi dans le champ

time.sleep(3)                         # Le temps de passer a autre saisi
 
print(pyautogui.position())
pyautogui.click(200,222)
pyautogui.typewrite("Yves")


time.sleep(3)
print(pyautogui.position())
pyautogui.click(244,253)
pyautogui.typewrite("kokou@gmail.com")

time.sleep(3) 
print(pyautogui.position())
pyautogui.click(289, 282, clicks=20)

time.sleep(3)
print(pyautogui.position())
pyautogui.click(109,312)

time.sleep(3)
print(pyautogui.position())
pyautogui.click(353,381)
pyautogui.typewrite("yveskokou")

time.sleep(3)
print(pyautogui.position())
pyautogui.click(141,408)
