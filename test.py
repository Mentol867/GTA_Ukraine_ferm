import ctypes
import time

# Імпорт потрібних функцій
SetCursorPos = ctypes.windll.user32.SetCursorPos
mouse_event = ctypes.windll.user32.mouse_event
time.sleep(3)
# Константи подій миші
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

# Координати
x, y = 786, 341

# Переміщення курсора
SetCursorPos(x, y)
time.sleep(0.1)  # коротка затримка для стабільності

# Клік
mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
time.sleep(0.05)