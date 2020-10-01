#we_are_using_snake_case, not camelCase in this file. 


class Worker:

    #name : worker name
    #contract: number of hours per day (per week?)
    #avails: list of hours during which the worker is available

    def __init__(self,name: str,contract: int,avails: list):
       self.name = name
       self.contract = contract
       self.avails = avails


    def __repr__(self):
        return self.name + ", " + str(self.contract) +" hour contract, available " + str(self.avails)

    #determine worker's availibilities
    def determine_avail(self,avail = None):
        if avail is not None:
            avails = avail
        else:
            looking = True
            while looking :
                h = input("please enter an hour where " + str(self.name) + " is available.   ")
                print("to exit this loop, please enter 0")
                while not h.isnumeric():
                    h = input("please enter an interger  ")
                h = int(h)
                if not h > 0:
                    looking = False
                else:
                    self.avails.append(h)
            self.avails.sort()



class Day:

    #we'll start by fixing the available times, then make it modifiable 

    def __init__(self,name):
        self.timetable = { i : [0,[]] for i in range(8,20) }
        self.name = name

    def __repr__(self):
        return self.name + "\n " + " \n ".join(str(i) +  str(self.timetable[i]) for i in self.timetable) + "\n \n" 

    def print_time_table(self):
        print(str(self.timetable))

    def determine_needs(self):
        for i in self.timetable:
           self.timetable[i][0] = int(input("How many workers are need at hour " + str(i) + "?  ")) 


class Workforce:

    def __init__(self):
        staff_number = int(input("How many total workers are there?  "))
        self.staff = []
        for i in range(staff_number):
            name = input("Please input worker name:  ")
            contract = int(input("Please enter number of hours in "+ name + "'s contract:   "))
            avails = []
            self.staff.append(Worker(name,contract,avails))



    def __repr__(self):
        return str(self.staff)

    def determine_all_avail(self):
        
        for i in self.staff:

            i.determine_avail()

class Week:

    #the week is seven days. Always. 
    def __init__(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.week = []
        for d in days:
            self.week.append(Day(d))

    def __repr__(self):
        return " ".join(str(d) for d in self.week)




week51 = Week()
print(week51)



