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


class tabel():
    def __init__(self, name, begin):#, second, third):
        self.name = name
        #self.first = sheet.cell(first,0).value
        
        self.begin = begin
        self.printer_1 = printer(sheet.cell(1,0).value, 1, self)
        self.printer_2 = printer(sheet.cell(2,0).value, 2, self)
        self.printer_3 = printer(sheet.cell(3,0).value, 3, self)
        
        
        
        
        
tyhjad = tabel("Tyhjad kassetid", 0)#,2,3)   
#print tyhjad.first

t2is = tabel("T2is kassetid", 17)#),29,20)

#print tyhjad.printer_3.tooner
#print t2is.printer_3.tooner

#print t2is.printer_1.tulp_c

print tyhjad.printer_1.name