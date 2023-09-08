import tkinter as tk

class View:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x600")
        self.window.title("Puzzle")
        self.menu_frame = tk.Frame(self.window)
        self.menu_frame.pack(side="top")
        self.restart_button = tk.Button(self.menu_frame, text="Restart")
        self.restart_button.pack(side="top")
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(side="top", pady=100)
        self.nb_start_case = 7
        self.buttons_tab = [None]*self.nb_start_case
        for i in range(self.nb_start_case):
            self.buttons_tab[i] = [None]*self.nb_start_case
            for j in range(self.nb_start_case):
                self.buttons_tab[i][j] = tk.Button(self.button_frame, bg="cyan", height=2, width=4, fg="blue")
                self.buttons_tab[i][j].grid(row=i, column=j)
