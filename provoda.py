import pyautogui
import keyboard
import time
from PIL import ImageGrab
import os

# координати лівих і правих точок (x, y)
left_points = [
    (786, 341),
    (786, 405),
    (786, 474),
    (786, 538),
    (786, 608),
    (786, 673),
    (786, 738)
]

right_points = [
    (1136, 341),
    (1136, 405),
    (1136, 474),
    (1136, 538),
    (1136, 608),
    (1136, 673),
    (1136, 738)
]

# ---------------------- допоміжні функції ----------------------

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_color(x, y):
    img = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    return img.getpixel((0, 0))

def colors_close(c1, c2, tolerance=15):
    """Перевіряє, чи схожі кольори з певним допуском"""
    return all(abs(a - b) <= tolerance for a, b in zip(c1, c2))

def find_matchings(left_points, right_points):
    left_colors = [get_color(x, y) for x, y in left_points]
    right_colors = [get_color(x, y) for x, y in right_points]

    matchings = []
    for i, color in enumerate(left_colors):
        for j, color2 in enumerate(right_colors):
            if colors_close(color, color2):
                matchings.append((left_points[i], right_points[j]))
                break
    return matchings

def connect_wires():
    print("\n🔧 З’єдную дроти...")
    matches = find_matchings(left_points, right_points)

    if not matches:
        print("⚠️ Не знайдено збігів!")
        return

    for start, end in matches:
        pyautogui.dragTo(start, duration=0.1)
        pyautogui.leftClick(start)
        time.sleep(0.2)
        end_x, end_y = end

        pyautogui.dragTo(end_x, end_y,0.3, button="right")  # тягнемо
        time.sleep(0.3)
        pyautogui.leftClick(end)
        time.sleep(0.15)

        print(f"✅ З'єднано {start} ➜ {end}")

    print("✨ Готово!")

# ---------------------- головний цикл ----------------------

clear_console()
print("🎧 Програма слухає клавіші...\n")
print("➡ Натисни [Alt] — щоб запустити з’єднання")
print("➡ Натисни [Esc] — щоб завершити програму\n")

while True:
    if keyboard.is_pressed('alt'):
        connect_wires()
        time.sleep(0.8)
    elif keyboard.is_pressed('esc'):
        print("\n🛑 Програму завершено користувачем.")
        break
