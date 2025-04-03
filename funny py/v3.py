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


def update_hack_text():
    while True:

        hack_text.config(fg=random.choice(["red", "green", "blue", "yellow", "magenta", "cyan", "white"]))
        hack_text.place(x=random.randint(0, root.winfo_screenwidth() - 250), y=random.randint(0, root.winfo_screenheight() - 50))
        root.update()
        time.sleep(0.5)


def random_text_fill():
    while True:
        random_text = "You were hacked by Hicham"
        x = random.randint(0, root.winfo_screenwidth() - 250)
        y = random.randint(0, root.winfo_screenheight() - 50)
        hack_text.config(text=random_text, fg=random.choice(["red", "green", "blue", "yellow", "magenta", "cyan", "white"]))
        hack_text.place(x=x, y=y)
        root.update()
        time.sleep(0.1)


def screen_flicker():
    while True:
        root.configure(bg=random.choice(["black", "white", "red", "blue", "green", "purple", "yellow"]))
        root.update()
        time.sleep(0.1)


def mouse_cursor_change():
    while True:
        root.config(cursor=random.choice(["arrow", "circle", "pirate", "plus", "watch"]))
        root.update()
        time.sleep(0.3)


def moving_text():
    while True:
        text = tk.Label(root, text="You were hacked by Hicham", font=("Arial", 20, "bold"), fg=random.choice(["red", "green", "blue", "yellow", "magenta", "cyan", "white"]), bg="black")
        text.place(x=random.randint(0, root.winfo_screenwidth() - 250), y=random.randint(0, root.winfo_screenheight() - 50))
        root.update()
        time.sleep(0.5)


def text_animation():
    while True:
        hack_text.config(text="You were hacked by Hicham", fg=random.choice(["red", "green", "blue", "yellow", "magenta", "cyan", "white"]))
        hack_text.place(x=random.randint(0, root.winfo_screenwidth() - 250), y=random.randint(0, root.winfo_screenheight() - 50))
        root.update()
        time.sleep(0.3)


threading.Thread(target=move_devil_face, daemon=True).start()
threading.Thread(target=update_hack_text, daemon=True).start()
threading.Thread(target=random_text_fill, daemon=True).start()
threading.Thread(target=screen_flicker, daemon=True).start()
threading.Thread(target=mouse_cursor_change, daemon=True).start()
threading.Thread(target=moving_text, daemon=True).start()
threading.Thread(target=text_animation, daemon=True).start()

root.mainloop()
