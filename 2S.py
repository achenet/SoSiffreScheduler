#this is where we try and make the GUI

import 1S

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
     #   self.enter_text = tk.Button(self.entry, text = "enter", command =self.entry.get())
     #   self.enter_text.grid()
    



if __name__ == '__main__':
    w = Window()
    w.mainloop()
