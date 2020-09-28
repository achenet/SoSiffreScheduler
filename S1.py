
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



class Schedule:

    #we'll start by fixing the available times, then make it modifiable 

    def __init__(self):
        self.timetable = { 8: [] , 9 : [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], 20: []}







joe = Worker("Eric",35,[8,9,10,11,12,13])
print(joe)

