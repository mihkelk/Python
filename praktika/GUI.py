from printerid import *

import Tkinter


from Tkinter import *

#active_table = tyhjad
#master = Tk()

class menyy:
    def __init__(self, master):
        self.master = master
        mehneu = Menu(master)
        #mehneu.add_command(label = "t2is", command = self.t2is())
        #mehneu.add_command(label = "tyhi", command = self.tyhi())
        #nupp = Menubutton(master=master, menu = mehneu, text = "menuu")
        self.var = StringVar(self.master)
        options = ["t2is", "tyhjad"]
        option = OptionMenu(master, self.var, *options)
        option.pack()
        button = Button(master, text="OK", command=self.ok)
        button.pack()
        
        #nupp.pack()

    def t2is(self):
        global t2is
        joonista_tabel(self.master, t2is)
        
    def tyhi(self):
        global tyhjad
        joonista_tabel(self.master, tyhjad)    
       
    def ok(self):
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
    master = master
    active_table = active_table
    #global active_table
    group = Label(master)
    group.pack(padx=10, pady=0, fill=X)
    
    
    for i in range(active_table.k6rgus):
        
        if i %2:
            verv="white"
        else:
            verv="gray"
        
        labels = [
                  Label(group, text=active_table.read[i].printer, bg=verv)),
                  Label(group, text=active_table.read[i].tooner, bg=verv),
                  Label(group, text=active_table.read[i].tulp_c, bg=verv),
                  Label(group, text=active_table.read[i].tulp_e, bg=verv),
                  Label(group, text=active_table.read[i].tulp_f, bg=verv),
                  Label(group, text=active_table.read[i].tulp_g, bg=verv),
                  Label(group, text=active_table.read[i].kuu_algul, bg=verv)]
        
        for e in labels:
            for columns in range(1,7)
             labels[e].grid(row=i, column = columns, sticky=W+E, padx = 1)
             
            
        #Label(group, text=active_table.read[i].printer, bg=verv).grid(row=i, sticky=W+E, padx = 1)
        #Label(group, text=active_table.read[i].tooner, bg=verv).grid(row=i, column=2, sticky=W+E, padx = 1)
        #Label(group, text=active_table.read[i].tulp_c, bg=verv).grid(row=i, column=3, sticky=W+E, padx = 1)
        #Label(group, text=active_table.read[i].tulp_e, bg=verv).grid(row=i, column=4, sticky=W+E, padx = 1)
        #Label(group, text=active_table.read[i].tulp_f, bg=verv).grid(row=i, column=5, sticky=W+E, padx = 1)
        #Label(group, text=active_table.read[i].tulp_g, bg=verv).grid(row=i, column=6, sticky=W+E, padx = 1)
        #Label(group, text=active_table.read[i].kuu_algul, bg=verv).grid(row=i, column=7, sticky=W+E, padx = 1)
    
            
        Label(group, text=active_table.read[i].tooner, bg=verv  ).grid(row=i, column=2, sticky=W+E)
    
    
    
    

    #return active_table
    #master.quit()    
    
def tabelimenyy():
    global var
    var = StringVar(master)
    
    option = OptionMenu(master, var, "t2is", "tyhjad")
    print option
    option.pack()
    
    #
    # test stuff
    
    
    
    button = Button(master, text="OK", command=ok)
    button.pack()

#while True:
menuu = menyy(Tk())
#tabelimenyy()

#joonista_tabel(master, t2is)
#joonista_tabel(master, active_table)


mainloop()