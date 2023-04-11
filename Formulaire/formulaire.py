import pyautogui
import time


time.sleep(3)
print(pyautogui.position())
pyautogui.click(268,193)
pyautogui.typewrite("Yves")

time.sleep(3)
print(pyautogui.position())
pyautogui.click(206,226)
pyautogui.typewrite("kokou")

time.sleep(3)
print(pyautogui.position())
pyautogui.click(251,261)
pyautogui.typewrite("kokou@gmail.com")

time.sleep(3)
print(pyautogui.position())
pyautogui.click(290, 285, clicks=20)

time.sleep(3)
print(pyautogui.position())
pyautogui.click(109,321)

time.sleep(3)
print(pyautogui.position())
pyautogui.click(389,389)
pyautogui.typewrite("yveskokou")

time.sleep(3)
print(pyautogui.position())
pyautogui.click(133,425)
