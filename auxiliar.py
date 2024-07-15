import time
import pyautogui

# captura o local exato do cursor do mouse
time.sleep(5)
print(pyautogui.position())

# sobe a tela
pyautogui.scroll(200)