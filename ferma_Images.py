import pyautogui
import time

time.sleep(5)
# Регіони для пошуку
region1 = (918, 799, 20, 20)  # для двох перших картинок
region2 = (897, 799, 14, 19)  # для третьої картинки

# Списки картинок
images_region1 = ['l.png', 'p.png']
image_region2 = 's.png'

# Перевірка двох перших картинок
found = None
for img in images_region1:
    location = pyautogui.locateOnScreen(img, region=region1, confidence=0.7)
    if location:
        found = img
        x, y = pyautogui.center(location)
        pyautogui.click(x, y)
        print(f"Знайдено {found} у region1")
        break

# Перевірка третьої картинки, якщо перші не знайдено
if not found:
    location = pyautogui.locateOnScreen(image_region2, region=region2, confidence=0.5)
    if location:
        x, y = pyautogui.center(location)
        pyautogui.click(x, y)
        print(f"Знайдено {image_region2} у region2")
    else:
        print("Жодна картинка не знайдена")
