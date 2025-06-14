import ctypes
import sys
import pyautogui
import cv2
import numpy as np
import keyboard
import time

# Проверка прав администратора
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

# Настройки
ORANGE_HSV_MIN = (5, 100, 100)    # Минимальный цвет апельсина (HSV)
ORANGE_HSV_MAX = (15, 255, 255)   # Максимальный цвет апельсина (HSV)
MIN_ORANGE_SIZE = 100             # Минимальный размер контура (пиксели)
CLICK_DELAY = 0.15                # Задержка между кликами (сек)
MIN_DISTANCE = 70                 # Минимальное расстояние между апельсинами (пиксели)

# Получаем размеры экрана
screen_width, screen_height = pyautogui.size()
print(f"Разрешение экрана: {screen_width}x{screen_height}")

# Определяем область поиска (центрированная по X, ограниченная по Y)
SEARCH_WIDTH = 1000
SEARCH_HEIGHT = 700
search_left = (screen_width - SEARCH_WIDTH) // 2
search_top = 0
search_right = search_left + SEARCH_WIDTH
search_bottom = search_top + SEARCH_HEIGHT

print(f"Область поиска: X({search_left}-{search_right}), Y(0-{SEARCH_HEIGHT})")

def find_oranges(screenshot):
    """Находит координаты апельсинов на изображении"""
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, ORANGE_HSV_MIN, ORANGE_HSV_MAX)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    oranges = []
    for cnt in contours:
        if cv2.contourArea(cnt) > MIN_ORANGE_SIZE:
            M = cv2.moments(cnt)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            # Преобразуем координаты в абсолютные (на весь экран)
            abs_x = search_left + cx
            abs_y = search_top + cy
            oranges.append((abs_x, abs_y))
    
    # Фильтруем слишком близкие апельсины
    filtered = []
    for x, y in oranges:
        keep = True
        for fx, fy in filtered:
            if abs(x - fx) < MIN_DISTANCE and abs(y - fy) < MIN_DISTANCE:
                keep = False
                break
        if keep:
            filtered.append((x, y))
    
    return filtered

def main():
    print("Управление:")
    print("  Нажмите и удерживайте 'X' - сбор апельсинов (история сбрасывается)")
    print("  Нажмите 'M' - полная остановка программы")
    print(f"  Область поиска: центр экрана ±500px по X (всего 1000px), Y: 0-{SEARCH_HEIGHT}px")
    
    last_positions = []
    active = False
    
    try:
        while True:
            # Проверка на выход по клавише M
            if keyboard.is_pressed('m'):
                print("Нажата клавиша 'M' - выход из программы")
                break
            
            # Ожидание нажатия X
            if keyboard.is_pressed('x'):
                if not active:
                    # Активация и сброс истории при новом нажатии
                    active = True
                    last_positions = []
                    print("\nАктивация! История сброшена. Начинаю сбор...")
                
                # Снимок только области поиска
                screenshot = pyautogui.screenshot(region=(search_left, search_top, SEARCH_WIDTH, SEARCH_HEIGHT))
                screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
                
                # Поиск апельсинов
                oranges = find_oranges(screenshot)
                
                # Кликаем по новым апельсинам
                for x, y in oranges:
                    # Проверяем расстояние до предыдущих кликов
                    new_orange = True
                    for lx, ly in last_positions:
                        if abs(x - lx) < MIN_DISTANCE and abs(y - ly) < MIN_DISTANCE:
                            new_orange = False
                            break
                    
                    if new_orange:
                        pyautogui.click(x, y)
                        last_positions.append((x, y))
                        time.sleep(CLICK_DELAY)
                
                # Обновляем историю позиций
                if len(last_positions) > 10:
                    last_positions.pop(0)
                
                time.sleep(0.05)
            else:
                if active:
                    active = False
                    print("Ожидание нового нажатия 'X'...")
                time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем.")
    
    print("Работа программы завершена.")

if __name__ == "__main__":
    main()