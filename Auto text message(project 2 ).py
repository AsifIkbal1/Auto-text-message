import pyautogui
import time
variable=5 # 5ta message jbe sudhu

while variable>0:
    time.sleep(2)
    pyautogui.typewrite("")
    pyautogui.press("Enter")
    time.sleep(5)
    variable=variable-1

