import pyautogui
import time

time.sleep(5)
screenshot = pyautogui.screenshot(region=(897, 799, 14, 19))
screenshot.save("s.png")
