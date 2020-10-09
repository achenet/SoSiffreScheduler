#this is where we try and make the GUI

import Logic

import tkinter as tk

class Window(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.initialize_window()

    def initialize_window(self):
        self.title("Scheduler")
        self.frame1 = tk.Frame(self)
        self.quit_button = tk.Button(self,  text = "Quit", command = self.quit)
        self.entry = tk.Entry(self.frame1)
        self.frame1.grid(row = 0, column = 0)
        self.quit_button.grid(row=2, column = 2)
        self.entry.grid(row = 1)
        self.show_text = ""
        self.output = tk.Text(self.frame1, height = 2, width = 50) 
        self.output.grid(row = 3)
        self.enter_text_button = tk.Button(self.frame1, text = "enter", command =self.read_entry())
        self.enter_text_button.grid(row = 2)
        self.enter_text_label = tk.Label(self.frame1, text = "Employee Name")
        self.enter_text_label.grid(row = 0)

    
    
    
    def read_entry(self):
        self.show_text = self.entry.get()
        
        self.output.insert(tk.END,self.show_text)
    



if __name__ == '__main__':
    w = Window()
    w.mainloop()
