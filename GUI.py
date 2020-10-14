#this is where we try and make the GUI

import Logic as lo

import tkinter as tk

class Window(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.initialize_workforce()
        self.initialize_window()

    
    
    
    def initialize_window(self):
        self.title("Scheduler")
        self.show_frame1() 
        self.quit_button = tk.Button(self,  text = "Quit", command = self.quit)
        self.quit_button.grid(row=2, column = 2)
        self.display_workforce()

    def show_frame1(self):
        self.frame1 = tk.Frame(self)
        self.frame1.grid(row = 0, column = 0)
        self.add_worker_button = tk.Button(self.frame1, text = "Add Employee", command = self.add_worker)
        self.add_worker_button.grid(row = 2, column = 1) 
        self.back_to_start_button = tk.Button(self, text = "Back to Start", command = self.back_to_start)

    def initialize_workforce(self):
        self.workforce = lo.Workforce()


    def add_worker(self):
        self.frame1.grid_remove()
        self.add_employee_frame = tk.Frame(self)
        self.add_employee_label = tk.Label(self.add_employee_frame, text = "Please Fill in Employee details")
        self.add_employee_label.grid()
        self.employee_name_frame = tk.LabelFrame(self.add_employee_frame, text = "Employee Name")
        self.employee_name_entry = tk.Entry(self.employee_name_frame)
        self.employee_name_frame.grid(row = 1, column = 0)
        self.employee_name_entry.grid()
        self.employee_hours_frame = tk.LabelFrame(self.add_employee_frame, text = "Contract Hours")
        self.employee_hours_entry = tk.Entry(self.employee_hours_frame)
        self.employee_hours_frame.grid(row = 1, column = 1)
        self.employee_hours_entry.grid()
        self.enter_employee_data_button = tk.Button(self.add_employee_frame, text = "Enter Worker Data", command = self.enter_worker_data)
        self.enter_employee_data_button.grid(row = 1, column = 2)        

        self.add_employee_frame.grid(row = 0)
        self.back_to_start_button.grid(row = 2)

    def enter_worker_data(self):
        self.worker_data_frame = tk.Frame(self)
        name = self.employee_name_entry.get()
        contract = self.employee_hours_entry.get()
        worker = lo.Worker(name,contract,[])
        self.workforce.staff.append(worker)
        self.worker_data_display = tk.Label(self.worker_data_frame, text = worker)
        self.worker_data_display.grid(row = 0)
        self.add_employee_frame.grid_remove()
        self.worker_data_frame.grid(row = 0)


    def back_to_start(self):
        for frame in self.grid_slaves():
            frame.grid_remove()
        self.initialize_window() 

    
    def display_workforce(self):
        self.workforce_frame = tk.Frame(self)
        self.workforce_frame.grid()
        self.workforce_label = tk.LabelFrame(self.workforce_frame, text = "Workforce")
        self.workforce_label.grid()
        self.workforce_display = tk.Label(self.workforce_frame, text = "\n ".join(str(i) for i in self.workforce.staff))
        self.workforce_display.grid()





if __name__ == '__main__':
    w = Window()
    w.mainloop()
