#this is where we try and make the GUI

import Logic

import tkinter as tk

class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Scheduler")
        self.geometry("800x600")
        self.initialize_window()

    def initialize_window(self):

        self.quit_button = tk.Button(self,  text = "Quit", command = self.quit)
        self.quit_button.grid(row=2, column = 2)
        self.entry = tk.Entry(self)
        self.entry.grid(row = 1, column = 1)
        self.show_text = ""
        self.enter_text_button = tk.Button(self, text = "enter", command =self.read_entry())
        self.enter_text_button.grid()
        self.enter_text_label = tk.Label(self.entry, text = "Employee Name")
        self.enter_text_label.grid()
        self.output = tk.Text(self) 
        self.output.grid()
    
    
    
    def read_entry(self):
        self.show_text = self.entry.get()
        
        self.output.insert(tk.END,self.show_text)
    



if __name__ == '__main__':
    w = Window()
    w.mainloop()
