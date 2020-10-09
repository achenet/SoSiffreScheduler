#this is where we try and make the GUI

import Logic

import tkinter as tk

class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Scheduler")
        self.geometry("800x600")
        self.quit_button = tk.Button(self,  text = "Quit", command = self.quit)
        self.quit_button.grid()
        self.entry = tk.Entry(self)
        self.entry.grid()
        self.text = ""
        self.enter_text_button = tk.Button(self.entry, text = "enter", command =self.entry.read_entry())
        self.enter_text.grid()
        self.enter_text_label = tk.Label(self.entry, text = "Employee Name")

    def read_entry(self):
        self.text = self.entry.get()

    



if __name__ == '__main__':
    w = Window()
    w.mainloop()
