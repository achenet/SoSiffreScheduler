#we_are_using_snake_case, notCamelCase in this file. 

class Worker:

    #name : worker name
    #contract: number of hours per day (per week?)
    #avails: list of hours during which the worker is available

    def __init__(self,name: str,contract: int,avail: dict = { day : { i : False for i in range(8,21)} for day in 
        ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] } ):
       self.name = name
       self.contract = contract
       self.avail = avail


    def __repr__(self):
        repr_list = []
        for i in self.avail:
            if self.avail[i] is True:
                repr_list.append(i)
        return self.name + ", " + str(self.contract) +" hour contract, available " + str(repr_list)

    #determine worker's availibilities
    def determine_avail(self,avail = None):
        if avail is not None:
            self.avail = avail
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
                    self.avail.append(h)
            self.avail.sort()
            
        


class Day:

    #we'll start by fixing the available times, then make it modifiable 

    def __init__(self,name):
        self.timetable = { i : [0,[]] for i in range(8,21) }
        self.name = name

    def __repr__(self):
        return self.name + "\n " + " \n ".join(str(i) +  str(self.timetable[i]) for i in self.timetable) + "\n \n" 

    def print_time_table(self):
        print(str(self.timetable))

    def determine_needs(self,preset_needs: list = None):
        if preset_needs:
            self.update_needs(preset_needs)
        
        else: 
            for i in self.timetable:
                self.timetable[i][0] = int(input("How many workers are need at hour " + str(i) + "?  ")) 

    def update_needs(self, new_needs: list):
        if len(new_needs) != len(self.timetable):
            raise ValueError("New timetable is not the correct length, need length "+ str(len(self.timetable)) + " but have length "
                    + str(len(new_needs)))
        j = 0
        for i in self.timetable:
            self.timetable[i][0] = new_needs[j]
            j += 1

    #probably one of the least elegant ways to solve this problem, but hey
    #it's something.
    #it would actually be wiser to make a local copy of each worker's availibilites
    def fill_timetable(self, workforce):
        staff = workforce.staff
        staff.sort(key = lambda x : len(x.avail))

        for hour in self.timetable:
            still_workers = True
            while self.timetable[hour][0] > 0 and still_workers:
                for worker in staff:
                    avail = worker.avail
                    if avail[hour]:
                        still_workers = True
                        self.timetable[hour][1].append(worker)
                        avail[hour] = False
                        self.timetable[hour][0] -= 1
                still_workers = False
                    
       
        if False:
            raise RuntimeError("could not fill out timetable properly")


class Workforce:

    def __init__(self):
#        staff_number = int(input("How many total workers are there?  "))
        self.staff = []
 #       for i in range(staff_number):
 #           name = input("Please input worker name:  ")
 #           contract = int(input("Please enter number of hours in "+ name + "'s contract:   "))
 #           avails = []
 #           self.staff.append(Worker(name,contract,avails))



    def __repr__(self):
        return "Staff: " + str(self.staff)

    def determine_full_staff_avail(self):
        
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

    def determine_weekly_needs(self, preset_needs: list = None):
        if preset_needs:
            i = 0
            for day in self.week:
                day.determine_needs(preset_needs[i])
                i += 1
        else:
            for day in self.week:
                day.determine_needs()
    
if __name__ == '__main__':
    week51 = Week()
    week51.determine_weekly_needs([[i for i in range(8,21)]for j in range(7)])
    team = Workforce()
    team.staff.append(Worker("Eric",35,{ i: True for i in range(8,21)}))
    team.staff.append(Worker("Margot",35,{ i: i > 12 for i in range(8,21)}))
    team.staff.append(Worker("Pauline",35,{ i: i < 13 for i in range(8,21)}))

    for day in week51.week:
        day.fill_timetable(team)
        print(day)


