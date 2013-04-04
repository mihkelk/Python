from printerid import *

import Tkinter


from Tkinter import *
aktiv = "1"
#active_table = tyhjad
#master = Tk()

class menyy:
    def __init__(self, master):
        self.master = master
        self.var = StringVar(self.master)
        options = ["t2is", "tyhjad"]
        option = OptionMenu(master, self.var, *options)
        option.grid(row=20, column=20)
        button = Button(master, text="OK", command=self.ok)
        #button.pack()
        button.grid(row=21, column=20)
        self.tabel = "1"
        

    def t2is(self):
        global t2is
        self.tabel = t2is
        joonista_tabel(self.master, t2is)
        #self.create_lables(t2is)
        
    def tyhi(self):
        global tyhjad
        self.tabel = tyhjad
        joonista_tabel(self.master, tyhjad)    
       
    def ok(self):
        global aktiv
        if aktiv != "1":
            for c in range(len(aktiv.read[0].labels)):
                for i in range(aktiv.k6rgus):
                    aktiv.read[i].labels[c].grid_forget()
        #self.master.quit()
        #self.master.
        print "ok"
        #global master, t2is, tyhjad, var
        value = self.var.get()
        print value
        if value == "t2is":
            #active_table = t2is
            self.t2is()
        elif value == "tyhjad":
            #active_table = tyhjad
            self.tyhi()
            #print active_table    
        
def joonista_tabel(master, active_table):
    global aktiv
    aktiv = active_table
    #c = 1
    master = master
    active_table = active_table

    for c in range(len(active_table.read[0].labels)):#range(4):
        for i in range(active_table.k6rgus):  

            active_table.read[i].labels[c].grid(row=i, column=c, sticky=W+E, padx = 1) 

    

menuu = menyy(master)

mainloop()