


nimekiri = []

nimekiri.append(str(1) + "_lel")
nimekiri.append(str(1) + "_br")
nimekiri.append(str(1) + "_br")
nimekiri.append(str(1) + "_test")
nimekiri.append(str(1) + "_br")
nimekiri.append(str(1) + "_br")
toopel = tuple(nimekiri)
print nimekiri

l = "d"
#for e in nimekiri:
    #print "huehue"
    
#if "lel" in nimekiri[0]:
    #print "lol"
print toopel   
#print nimekiri[0].find("l")    
for i in range (len(nimekiri)):
    indoks = nimekiri.index(str(1) + "_lel")
    nimekiri[indoks] = str(1) + "_test"
    print nimekiri
    if "test" in nimekiri[i]:
        print "lol"
    else:
        print "hue"