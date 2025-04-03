import tkinter as tk
import time
import random
import threading
import os


root = tk.Tk()
root.attributes('-fullscreen', True)  
root.attributes('-topmost', True)  
root.configure(bg='black')


root.bind("<Alt-F4>", lambda e: "break")
root.bind("<Escape>", lambda e: "break")
root.bind("<Control-w>", lambda e: "break")


label = tk.Label(root, text="🔥 اختراق كامل جارٍ! 🔥", font=("Arial", 50, "bold"), fg="red", bg="black")
label.pack(expand=True)


messages = [
    "الوصول إلى النظام...",
    "تنزيل ملفات خطيرة...",
    "تجاوز جدار الحماية...",
    "تحليل بيانات المستخدم...",
    "محو البيانات (مزحة فقط)...",
    "اتصال بالسيرفر الخارجي...",
    "إرسال بيانات المستخدم...",
    "تعطيل الحماية...",
    "تحميل فيروسات خطيرة..."
]

hack_text = tk.Label(root, text="", font=("Courier", 20, "bold"), fg="green", bg="black")
hack_text.pack()

def update_text():
    start_time = time.time()
    duration = 30  # مدة التأثيرات
    while time.time() - start_time < duration:
        message = random.choice(messages)
        for i in range(len(message) + 1):
            hack_text.config(text=message[:i])
            root.update()
            time.sleep(0.05)
        time.sleep(random.uniform(0.5, 1.5))
    root.destroy()

def flicker_effect():
    for _ in range(100):
        root.configure(bg=random.choice(["black", "darkred", "darkblue", "darkgreen", "darkorange", "purple"]))
        label.config(fg=random.choice(["red", "white", "yellow", "purple", "blue"]))
        hack_text.config(fg=random.choice(["green", "lightgreen", "cyan", "magenta", "white"]))
        root.update()
        time.sleep(0.02)

def moving_text_effect():
    x, y = 100, 100
    direction_x, direction_y = 20, 20
    for _ in range(200):
        x += direction_x
        y += direction_y
        if x >= root.winfo_screenwidth() - 200 or x <= 0:
            direction_x *= -1
        if y >= root.winfo_screenheight() - 100 or y <= 0:
            direction_y *= -1
        label.place(x=x, y=y)
        root.update()
        time.sleep(0.02)

def screen_shake():
    for _ in range(50):
        root.geometry(f"+{random.randint(0, 100)}+{random.randint(0, 100)}")
        time.sleep(0.02)
        root.update()
    root.geometry("+0+0")

def beep_sound():
    for _ in range(30):
        os.system("echo \a")  
        time.sleep(0.3)

def loading_bar():
    progress = tk.Label(root, text="[                    ]", font=("Courier", 20, "bold"), fg="white", bg="black")
    progress.pack()
    for i in range(1, 21):
        progress.config(text=f"[{('=' * i).ljust(20)}]")
        root.update()
        time.sleep(0.05)

def fake_system_crash():
    time.sleep(10)
    os.system("cls" if os.name == "nt" else "clear")
    print("ERROR: SYSTEM FAILURE DETECTED\nCRITICAL SYSTEM MALFUNCTION\nAUTO SHUTDOWN INITIATED")
    time.sleep(5)

def final_message():
    time.sleep(30)
    root.withdraw()
    tk.messagebox.showinfo("😱 مفاجأة مرعبة! 😱", "لقد تم خداعك!\nكل شيء كان مجرد خدعة!\nلكن تذكر، لا تثق بأي شيء على جهازك دون التحقق منه!\n😂😂😂")
    root.destroy()
    shutdown()

def shutdown():
    if os.name == "nt":
        os.system("shutdown /s /t 5")  
    else:
        os.system("shutdown -h now")  

def screen_flicker():
    for _ in range(100):
        root.configure(bg=random.choice(["black", "white", "red", "blue", "green", "purple"]))
        label.config(fg=random.choice(["yellow", "white", "cyan", "blue"]))
        hack_text.config(fg=random.choice(["green", "lightgreen", "red", "yellow"]))
        root.update()
        time.sleep(0.02)

def random_text_alert():
    alert_texts = [
        "SYSTEM ERROR!", "WARNING: HACK DETECTED!", "SHUTDOWN INITIATED!", "DISCONNECTING...", "FILE DELETED",
        "DATA CORRUPTED!", "ACCESS DENIED!", "HACKING IN PROGRESS!", "SECURITY BREACH!"
    ]
    for _ in range(50):
        label.config(text=random.choice(alert_texts))
        root.update()
        time.sleep(0.1)
        root.configure(bg=random.choice(["darkred", "purple", "black"]))
        time.sleep(0.2)

def mouse_cursor_change():
    for _ in range(50):
        root.config(cursor="pirate") 
        time.sleep(0.3)
        root.config(cursor="arrow")
        time.sleep(0.3)

def random_windows_open():
    for _ in range(5):
        os.system("start cmd")  
        time.sleep(1)


threading.Thread(target=update_text, daemon=True).start()
threading.Thread(target=flicker_effect, daemon=True).start()
threading.Thread(target=moving_text_effect, daemon=True).start()
threading.Thread(target=screen_shake, daemon=True).start()
threading.Thread(target=beep_sound, daemon=True).start()
threading.Thread(target=loading_bar, daemon=True).start()
threading.Thread(target=fake_system_crash, daemon=True).start()
threading.Thread(target=final_message, daemon=True).start()
threading.Thread(target=screen_flicker, daemon=True).start()
threading.Thread(target=random_text_alert, daemon=True).start()
threading.Thread(target=mouse_cursor_change, daemon=True).start()
threading.Thread(target=random_windows_open, daemon=True).start()

root.mainloop()
