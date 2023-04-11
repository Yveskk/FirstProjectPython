import pyautogui
import time

# Ouvrir le menu "éteindre"
pyautogui.hotkey('super')
time.sleep(5)
pyautogui.typewrite('power')
time.sleep(5)
pyautogui.press('enter')
time.sleep(5)

# Sélectionner "éteindre"
pyautogui.press('down')
time.sleep(5)
pyautogui.press('enter')
time.sleep(5)

# Confirmer l'extinction
pyautogui.press('enter')
