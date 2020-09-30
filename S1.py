
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



class Day:

    #we'll start by fixing the available times, then make it modifiable 

    def __init__(self):
        self.timetable = { i : [0,[]] for i in range(8,20) }

    def __repr__(self):
        return str(self.timetable)


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






w = Workforce()
print(w)
