from mmap import mmap,ACCESS_READ
from xlrd import open_workbook, cellname
from Tkinter import *
#from GUI import *

wb = open_workbook('printerid_uus.xls')
sheet = wb.sheets()[8]
#ToonerV = 1
master = Tk()

class printer():
    def __init__(self, name, order, tabel):
        self.name = name
        self.order = order        
        self.row = tabel.begin + self.order
        
        #self.tooner = sheet.cell(self.row, 1).value
        #self.tulp_c = sheet.cell(self.row, 2).value
        
        #self.tabel = tabel
        
class rida():
    def __init__(self, order, tabel):#(self, printer, order, tabel):   
        #self.printer = printer
        self.order = order
        self.tabel = tabel
        self.number = self.tabel.begin + self.order
        self.printer = sheet.cell(self.number, 0).value
        self.tooner = sheet.cell(self.number, 1).value
        self.tulp_c = sheet.cell(self.number, 2).value
        #self.tulp_e = sheet.cell(self.number, 4).value
        self.tulp_f = sheet.cell(self.number, 5).value
        self.tulp_g = sheet.cell(self.number, 6).value  
        self.kuu_algul = sheet.cell(self.number, 7).value
        self.create_labels()
        
    def create_labels(self):
        global master
        if self.order %2:
            verv="white"
        else:
            verv="gray"    
        self.labels = [
                       Label(master, text=self.printer, anchor = W, bg=verv),      
                       Label(master, text=self.tooner, anchor = W, bg=verv),
                       Label(master, text=self.tulp_c, anchor = W, bg=verv),
                       #Label(master, text=self.tulp_e, anchor = W, bg=verv),
                       Label(master, text=self.tulp_f, anchor = W, bg=verv),
                       Label(master, text=self.tulp_g, anchor = W, bg=verv),
                       Label(master, text=self.kuu_algul, anchor = W, bg=verv),
                       ]
class tabel():
    def __init__(self, name, begin, laius, k6rgus):#, second, third):
        self.name = name
        self.laius = laius
        self.k6rgus = k6rgus
        self.begin = begin
        self.read = []
        #self.first = sheet.cell(first,0).value
        
        for i in range(self.k6rgus):
                #print i
            #r = rida(sheet.cell(i+self.begin ,0).value, i+self.begin, self)
            r = rida(i+self.begin, self)
            self.read.append(r)
            #if i != 0:
                #print self.read[i].printer

        
        
        #self.printer_1 = printer(sheet.cell(1,0).value, 1, self)
        #self.printer_2 = printer(sheet.cell(2,0).value, 2, self)
        #self.printer_3 = printer(sheet.cell(3,0).value, 3, self)
        
        
        
        
        
tyhjad = tabel("Tyhjad kassetid", 1, 8 ,17 )#,2,3)   
#print tyhjad.first

t2is = tabel("T2is kassetid", 22, 8, 17)#),29,20)


#print tyhjad.printer_3.tooner
#print t2is.printer_3.tooner

#print t2is.printer_1.tulp_c

#print tyhjad.printer_1.name
#print tyhjad.read[1].kuu_algul
#print tyhjad.read[0].printer
#print tyhjad.name

print t2is.begin
#print t2is.