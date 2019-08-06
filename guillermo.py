#simple "how does gui work" test kit

#many tanks to python-course.eu/tkinter_entry_widgets.php

import tkinter




#we create the window
w = tkinter.Tk()

def showEntryFields():
    print("First Name: %s \n Last Name: %s" % (e1.get(),e2.get()))

#testing copy paste in vim across files

tkinter.Label(w, text= "Entry One").grid(row=0)
tkinter.Label(w, text= "Entry Two").grid(row=1)

e1 = tkinter.Entry(w)
e2 = tkinter.Entry(w)

e1.grid(row=0, column = 1)
e2.grid(row=1, column = 1)

tkinter.Button(w, text = 'Quit', command = w.quit).grid(row=3,column=0,pady=4,sticky= tkinter.S)

tkinter.Button(w, text = 'Show', command= showEntryFields).grid(row=3, column=1, pady=4, sticky= tkinter.S)

w.mainloop()

