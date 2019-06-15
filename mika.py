#this is an experimental file, an attempt at making a scheduling program
#which, when given a list of people with availablilites, 
#and time zone to fill, with a mininum number of people required at
#each hourly zone, 
#will fill them automatically. 

#I guess we should objectify the people O.o

class Vendeur:

    def __init__(self):
        self.nom = input("nom?")
        self.dispo = input("quands est il/elle disponible? entrer une liste s'il vous plait ^_^")
        self.contract = input("comien d'heures de travaille aujourdui?")


    def showinfo(self):
        print(self.nom)
        print(self.dispo)
        print(self.contract)


class Floor:

    def __init__(self):
        self.ouvre = int(input("on ouvre a quelle heure aujour'dui?"))
        self.ferme = int(input("on ferme a quelle heure aujourdui?"))
        #we'll now proceed to generate the time zone
        self.tz = list(range(self.ouvre,self.ferme))
        self.needed = []

    def show(self):
        print(self.tz)

    def make(self):
        dance = {i:input("combien de gens a "+str(i)+"h?") for i in tz}
        
floor = Floor()
floor.show()
floor.ask()

