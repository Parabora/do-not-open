class UltimateHorrorSim:
    def __init__(self):
        self.simulation_active = True  
        self.root = tk.Tk()
        self.setup_main_window()
        self.setup_audio()
        self.setup_ui()
        self.phase = 0
        self.start_simulation()

    def setup_main_window(self):
        self.root.title("SYSTEM FAILURE")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        self.root.bind("<F11>", lambda e: None)
        self.root.bind("<Escape>", lambda e: None)
        self.root.protocol("WM_DELETE_WINDOW", self.disable_event)

    def disable_event(self):
        pass  # لا تسمح بالإغلاق

    def setup_audio(self):

        def play_horror_sounds():
            while self.simulation_active:

                sound_file = random.choice(['sound1.wav', 'sound2.wav', 'sound3.wav']) 
                os.system(f"aplay {sound_file}")  
                time.sleep(random.uniform(0.1, 0.5))  
                
        threading.Thread(target=play_horror_sounds, daemon=True).start()

    def setup_ui(self):

        self.canvas = tk.Canvas(self.root, bg='black', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)


        self.tv_noise()


        self.horror_text = self.canvas.create_text(
            self.root.winfo_screenwidth()//2, 
            self.root.winfo_screenheight()//2,
            text="",
            font=('Courier New', 24),
            fill='red',
            justify='center'
        )


        self.draw_demon_face()

    def tv_noise(self):

        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        
        for _ in range(1000):
            x = random.randint(0, width)
            y = random.randint(0, height)
            size = random.randint(1, 3)
            color = random.choice(['#111111', '#222222', '#333333'])
            self.canvas.create_rectangle(x, y, x+size, y+size, fill=color, outline='')
        
        if self.simulation_active:
            self.root.after(50, self.tv_noise)

    def draw_demon_face(self):

        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        

        eye_size = width // 10
        self.canvas.create_oval(
            width//2 - eye_size*2, height//2 - eye_size,
            width//2 - eye_size, height//2 + eye_size,
            fill='red', outline='black'
        )
        self.canvas.create_oval(
            width//2 + eye_size, height//2 - eye_size,
            width//2 + eye_size*2, height//2 + eye_size,
            fill='red', outline='black'
        )
        

        mouth_width = width // 3
        self.canvas.create_arc(
            width//2 - mouth_width//2, height//2 + eye_size,
            width//2 + mouth_width//2, height//2 + eye_size*3,
            start=0, extent=180, fill='black', outline='red', width=5
        )

    def start_simulation(self):

        messages = [
            "WARNING: SYSTEM BREACH DETECTED",
            "CRITICAL FAILURE IN PROGRESS",
            "YOUR SOUL HAS BEEN HACKED",
            "DEMONIC PRESENCE DETECTED",
            "DON'T TURN AROUND...",
            "THEY ARE COMING FOR YOU",
            "IT'S INSIDE YOUR COMPUTER",
            "YOUR DATA BELONGS TO US NOW",
            "WE SEE YOU THROUGH THE CAMERA",
            "PREPARE FOR TERROR"
        ]
        

        def change_text():
            if not self.simulation_active:
                return
            
            self.canvas.itemconfig(
                self.horror_text,
                text=random.choice(messages),
                font=('Courier New', random.randint(20, 40)),
                fill=random.choice(['red', '#FF0000', '#880000', '#FF3333'])
            )
            

            x = random.randint(100, self.root.winfo_screenwidth()-100)
            y = random.randint(100, self.root.winfo_screenheight()-100)
            self.canvas.coords(self.horror_text, x, y)
            
            self.root.after(random.randint(500, 2000), change_text)
        
        change_text()
        

        self.horror_effects()
        

        self.next_horror_phase()

    def horror_effects(self):

        def red_flash():
            if not self.simulation_active:
                return
            
            self.canvas.config(bg='red')
            self.root.after(100, lambda: self.canvas.config(bg='black'))
            self.root.after(random.randint(1000, 5000), red_flash)
        
        red_flash()
        

        def hidden_messages():
            if not self.simulation_active:
                return
            
            msg = random.choice(["HELP ME", "RUN AWAY", "THEY ARE HERE", "LOOK BEHIND YOU"])
            x = random.randint(0, self.root.winfo_screenwidth())
            y = random.randint(0, self.root.winfo_screenheight())
            color = random.choice(['#330000', '#110000', '#550000'])
            
            text_id = self.canvas.create_text(
                x, y, text=msg, font=('Courier New', 12),
                fill=color, angle=random.randint(0, 360)
            )
            
            self.root.after(2000, lambda: self.canvas.delete(text_id))
            self.root.after(random.randint(3000, 8000), hidden_messages)
        
        hidden_messages()

    def next_horror_phase(self):

        self.phase += 1
        
        if self.phase == 1:

            self.show_hacking_animation()
            self.root.after(10000, self.next_horror_phase)
        
        elif self.phase == 2:

            self.show_scary_messages()
            self.root.after(15000, self.next_horror_phase)
        
        elif self.phase == 3:

            self.advanced_horror_effects()
            self.root.after(20000, self.next_horror_phase)
        
        elif self.phase == 4:

            self.final_scare()

    def show_hacking_animation(self):

        hacking_text = [
            "INITIATING SYSTEM PENETRATION...",
            "BYPASSING SECURITY PROTOCOLS...",
            "ACCESSING CAMERA FEED...",
            "DOWNLOADING DARK SOULS...",
            "CONNECTING TO OTHER SIDE...",
            "SUMMONING DEMONIC ENTITIES..."
        ]
        
        x, y = self.root.winfo_screenwidth()//2, self.root.winfo_screenheight()//3
        
        for i, text in enumerate(hacking_text):
            self.canvas.create_text(
                x, y + i*30,
                text=text,
                font=('Courier New', 14),
                fill='red',
                tags="hacking_text"
            )
            time.sleep(0.5)
            self.root.update()
        
        self.root.after(5000, lambda: self.canvas.delete("hacking_text"))

    def final_scare(self):

        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        

        self.canvas.delete('all')
        self.canvas.config(bg='red')
        

        self.canvas.create_text(
            width//2, height//2,
            text="☠",
            font=('Arial', 300),
            fill='black'
        )
        

        self.canvas.create_text(
            width//2, height - 100,
            text="GAME OVER",
            font=('Courier New', 50, 'bold'),
            fill='black'
        )
        

        self.exit_btn = tk.Button(
            self.root, text="EXIT (10)", 
            command=self.close_app,
            bg='black', fg='red',
            font=('Courier New', 20, 'bold'),
            state='disabled'
        )
        self.exit_btn.place(relx=0.5, rely=0.8, anchor='center')
        

        def countdown(sec=10):
            if sec > 0:
                self.exit_btn.config(text=f"EXIT ({sec})")
                self.root.after(1000, countdown, sec-1)
            else:
                self.exit_btn.config(state='normal', text="EXIT NOW")
        
        countdown()

    def close_app(self):

        self.simulation_active = False
        self.root.destroy()

if __name__ == "__main__":
    app = UltimateHorrorSim()
    app.root.mainloop()

