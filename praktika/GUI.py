from printerid import *

import Tkinter


from Tkinter import *

active_table = tyhjad


master = Tk()

#group = LabelFrame(master, padx=5, pady=5)# text="Group", padx=5, pady=5)
group = Label(master)
group.pack(padx=10, pady=0, fill=X)

lahtrid = []
lahter = []
#e = Label(master, text="Hello, world!")

for i in range(active_table.k6rgus):
    #lahtrid.append("1")
    #lahter.append("1")
  
    if i %2:
        verv="white"
    else:
        verv="gray"
    Label(group, text=active_table.read[i].printer, bg=verv).grid(row=i, sticky=W+E, padx = 1)
    
for i in range(active_table.k6rgus):    
    if i %2:
        verv="white"
    else:
        verv="gray"
        
    Label(group, text=active_table.read[i].tooner, bg=verv  ).grid(row=i, column=2, sticky=W+E)
    

mainloop()