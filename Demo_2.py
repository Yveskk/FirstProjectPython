import pyautogui
import time

# Ouvrir le menu Applications
pyautogui.hotkey('super')
time.sleep(5)

# Rechercher l'application
pyautogui.typewrite('firefox')
time.sleep(5)

# Sélectionner l'application dans les résultats de recherche
pyautogui.press('enter')
time.sleep(5)


# Fermer l'application
pyautogui.hotkey('ctrl', 'shift', 'q')


'''Dans ce programme, nous utilisons la fonction hotkey pour simuler l'appui sur la touche "Super" (la touche Windows ou Command sur d'autres systèmes d'exploitation) afin d'ouvrir le menu Applications. Nous attendons ensuite 1 seconde à l'aide de la fonction sleep.

Nous utilisons ensuite typewrite pour saisir le nom de l'application que nous voulons ouvrir, en l'occurrence "firefox". Nous appuyons sur Entrée avec la fonction press, ce qui ouvre l'application Firefox. Nous attendons 5 secondes à l'aide de sleep pour laisser l'application se charger.

Nous ouvrons ensuite une autre application, le terminal, en utilisant les mêmes fonctions que précédemment. Nous utilisons sleep pour attendre 2 secondes avant de fermer l'application en utilisant la combinaison de touches "Ctrl+Shift+Q".'''