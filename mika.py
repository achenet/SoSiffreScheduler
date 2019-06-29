#this is an experimental file, an attempt at making a scheduling program
#which, when given a list of people with availablilites, 
#and time zone to fill, with a mininum number of people required at
#each hourly zone, 
#will fill them automatically. 

#I guess we should objectify the people O.o

import re

class Vendeur:

    def __init__(self):
        self.nom = input("nom?")
       # self.dispo = list(range(8,20))
        self.dispoInput = input("quands est il/elle disponible? entrer une liste s'il vous plait séparer d'espace s'il vous plait ^_^")
        self.dispo = self.dispoInput.split()
        self.dispo = list(map(int,self.dispo))
        self.contract = int(input("comien d'heures de travaille aujourdui?"))



    def showinfo(self):
        print(self.nom)
        print(self.dispo)
        print(self.contract)


class Floor:

    def __init__(self):
       # self.ouvre = 8
        self.ouvre = int(input("on ouvre a quelle heure aujour'dui?"))
       # self.ferme = 10
        self.ferme = int(input("on ferme a quelle heure aujourdui?"))
        #we'll now proceed to generate the time zone
        self.tz = list(range(self.ouvre,self.ferme))
        self.needed = []

    def show(self):
        print(self.tz)

    def make(self):
        self.dance = {str(i)+"h":int(input("combien de gens a "+str(i)+"h?")) for i in self.tz}
        print("juste pour vérifier")
        print(self.dance)
        return self.dance


def fillMinimum(dancefloor,salesteam):
    planning = {x:[] for x in dancefloor}
    i = 0
    for x in planning:
        while len(planning[x]) < dancefloor[x] and i < dancefloor[x]:

            addVendeur(salesteam,planning[x],x)
            print(len(planning[x]))
            i +=1
        i = 0
    print(planning)
    return 0

def addVendeur(salesteam,planninglist,heure):
    i = 0
    h = int(re.search(r'\d+',heure).group()) 
    while i<len(salesteam) : 
      #  print(type(salesteam[i].dispo))
      #  print(type(heure))
      #  print(type(h))
        if h in salesteam[i].dispo and salesteam[i].contract > 0:
            planninglist.append(salesteam[i].nom)
       #     print("L sucks hella good dick <3")
            #we need to add the person for all hours...
            #so we'll modify his hours left and time spent working
            salesteam[i].dispo.remove(h)
            salesteam[i].contract -=1 
            return 0
        i+=1

    return 0

floor = Floor()
floor.show()

dancefloor = floor.make()
salesteam = []
for i in range(int(input("combien de vendeurs?"))):
    salesteam.append(Vendeur())

for i in range(len(salesteam)):
    print(salesteam[i].nom)

fillMinimum(dancefloor,salesteam)


