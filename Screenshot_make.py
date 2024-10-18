import time
import pyautogui
import pydirectinput




def screenshot():
    screen_width, screen_height = pyautogui.size()

    filename = f'screenshot_{int(time.time())}.png'
    center_x = screen_width // 2
    center_y = screen_height // 2

    # Делаем скриншот от центра экрана вверх (по ширине всего экрана)
    screenshot = pyautogui.screenshot(region=(0, 0, screen_width, center_y))
    screenshot.save(filename)


if __name__ == "__main__":
    try:
        while True:
            screenshot()
            time.sleep(2)
    except KeyboardInterrupt:
        print('Скрипт остановлен')