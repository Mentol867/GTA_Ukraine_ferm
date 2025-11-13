from pynput import keyboard
import pyautogui
import threading
import random
import time

stop_flag = False

def click_with_random_intervals(action, total_clicks=20):
    global stop_flag
    for i in range(total_clicks):
        if stop_flag:
            print(f"{action.upper()} кліки зупинено!")
            break

        if action in ('left', 'right'):
            pyautogui.click(button=action)
        elif action == 'space':
            pyautogui.press('space')

        remaining_clicks = total_clicks - (i + 1)
        if remaining_clicks > 0:
            interval = random.uniform(0.005, 0.01)
            time.sleep(interval)

def on_key_press(key):
    global stop_flag

    if key == keyboard.Key.enter:
        threading.Thread(target=click_with_random_intervals, args=('left',), daemon=True).start()
        threading.Thread(target=click_with_random_intervals, args=('right',), daemon=True).start()
        threading.Thread(target=click_with_random_intervals, args=('space',), daemon=True).start()

    if key == keyboard.Key.esc:
        stop_flag = True
        print("ESC натиснуто — зупинка всіх кліків")
        return False

keyboard_listener = keyboard.Listener(on_press=on_key_press)
keyboard_listener.start()
keyboard_listener.join()
