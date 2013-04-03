from mmap import mmap,ACCESS_READ
from xlrd import open_workbook, cellname

wb = open_workbook('printimise_kulu.xls')
sheet = wb.sheets()[8]
#ToonerV = 1

class printer():
    def __init__(self, name, order, tabel):
        self.name = name
        self.order = order        
        self.row = tabel.begin + self.order
        
        self.tooner = sheet.cell(self.row, 1).value
        self.tulp_c = sheet.cell(self.row, 2).value
        
        #self.tabel = tabel
        
class rida():
    def __init__(self, printer, order, tabel):   
        self.printer = printer
        self.order = order
        self.tabel = tabel
        self.number = tabel.begin + self.order
        self.tooner = sheet.cell(self.number, 1).value
        self.tulp_c = sheet.cell(self.number, 2).value
        self.tulp_e = sheet.cell(self.number, 4).value
        self.tulp_f = sheet.cell(self.number, 5).value
        self.tulp_g = sheet.cell(self.number, 6).value  
        self.kuu_algul = sheet.cell(self.number, 7).value  

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
            r = rida(sheet.cell(i+self.begin ,0).value, i+self.begin, self)
            self.read.append(r)
            #if i != 0:
                #print self.read[i].printer

        
        
        self.printer_1 = printer(sheet.cell(1,0).value, 1, self)
        self.printer_2 = printer(sheet.cell(2,0).value, 2, self)
        self.printer_3 = printer(sheet.cell(3,0).value, 3, self)
        
        
        
        
        
tyhjad = tabel("Tyhjad kassetid", 0, 8 ,13 )#,2,3)   
#print tyhjad.first

t2is = tabel("T2is kassetid", 17, 8, 12)#),29,20)

#print tyhjad.printer_3.tooner
#print t2is.printer_3.tooner

#print t2is.printer_1.tulp_c

print tyhjad.printer_1.name
print tyhjad.read[1].kuu_algul
print tyhjad.read[0].printer