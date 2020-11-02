# SoSiffreScheduler
An attempt to automate the process of making schedules for salesteams, which my manager at H&M had to do by hand. This is actually a specific case of the Nurse Scheduling Problem.

update 2 Nov 2020
The GUI is currently not functional, and I have decided to momentarily stop working on it at the moment as I am stumped by the current bug
The Logic portion of the program is capable of more or less correctly filling out a day, although the worker availibilites will have to 
be modified to be viewed as a weekly table, not a daily one. 


update 9 Oct 2020
run into a rather frustrating bug - when trying to build a simple functionality to display an entered text, run into
"AttributeError - 'tkinter.tkapp' object has no attribute 'output' ". 
Which is rather odd, because I have initialized a 'self.output' field.
but I initialized it AFTER refering to it, hence Python's confusion. 
Fixed. 
  

update 27 Sept 2020
starting again, with a more Object Oriented approach this time. 

update 1 Sept 2020
Well I've been completely neglecting this project for a looooong time, and will likely continue to do so for the near future. 


update 29 June 2019
well basically it works - unless it doesn't.
And one of the times it doesn't work is when a member of the salesteam with few   hours is free and in the list before a member of the salesteam with many hours. 
The solution to this would probably be to sort the salesteam by hours.

update 17 July 2019
So it seems to work. Have yet to test in a bunch of weird cases. Gunna go work on a GUI.  
