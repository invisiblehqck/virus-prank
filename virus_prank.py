import os
import random
import time
import tkinter as tk
from ctypes import windll

# Safety lock - make script read-only
os.chmod(__file__, 0o444)

def matrix_effect():
    for _ in range(50):
        print(''.join(random.choice('01') for _ in range(80)))
        time.sleep(0.05)

def glitch_screen():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')

    root.bind("<Escape>", lambda e: root.destroy())

    for _ in range(20):
        canvas = tk.Canvas(root)
        canvas.pack(fill='both', expand=True)
        for _ in range(100):
            x = random.randint(0, root.winfo_screenwidth())
            y = random.randint(0, root.winfo_screenheight())
            size = random.randint(10, 100)
            color = f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}'
            canvas.create_rectangle(x, y, x+size, y+size, fill=color, outline='')
        root.update()
        time.sleep(0.2)
        canvas.destroy()

    root.destroy()


def fake_bsod():
    windll.user32.MessageBoxW(0, 
        "CRITICAL_PROCESS_DIED\n\nYour PC ran into a problem and needs to restart.",
        "Windows", 0x00000010)

def invert_mouse():
    for _ in range(30):
        windll.user32.SetCursorPos(
            random.randint(0, windll.user32.GetSystemMetrics(0)),
            random.randint(0, windll.user32.GetSystemMetrics(1))
        )
        time.sleep(0.1)

def self_destruct():
    os.remove(__file__)
    print("Prank complete! File self-destructed.")

if __name__ == "__main__":
    try:
        matrix_effect()
        glitch_screen()
        fake_bsod()
        invert_mouse()
    finally:
        self_destruct()
