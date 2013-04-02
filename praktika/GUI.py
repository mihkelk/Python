from printerid import *

import Tkinter


from Tkinter import *

active_table = tyhjad


master = Tk()

#group = LabelFrame(master, padx=5, pady=5)# text="Group", padx=5, pady=5)
group = Label(master)
group.pack(padx=10, pady=0, fill=X)

for i in range(active_table.k6rgus):
    
    if i %2:
        verv="white"
    else:
        verv="gray"
    Label(group, text=active_table.read[i].printer, bg=verv).grid(row=i, sticky=W+E, padx = 1)
    Label(group, text=active_table.read[i].tooner, bg=verv).grid(row=i, column=2, sticky=W+E, padx = 1)
    Label(group, text=active_table.read[i].tulp_c, bg=verv).grid(row=i, column=3, sticky=W+E, padx = 1)
    Label(group, text=active_table.read[i].tulp_e, bg=verv).grid(row=i, column=4, sticky=W+E, padx = 1)
    Label(group, text=active_table.read[i].tulp_f, bg=verv).grid(row=i, column=5, sticky=W+E, padx = 1)
    Label(group, text=active_table.read[i].tulp_g, bg=verv).grid(row=i, column=6, sticky=W+E, padx = 1)
    Label(group, text=active_table.read[i].kuu_algul, bg=verv).grid(row=i, column=7, sticky=W+E, padx = 1)

        
    Label(group, text=active_table.read[i].tooner, bg=verv  ).grid(row=i, column=2, sticky=W+E)
    

mainloop()