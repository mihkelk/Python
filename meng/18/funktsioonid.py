import math

def angle(ang):
    cos = math.cos(math.radians(ang))
    sin = math.sin(math.radians(ang))    
    return [cos, sin]

def update(dt): # vajalik kella/kiiruse jaoks
    return 0

def gravity(ob):
    if "_on_ground" in str(ob.collisions):
        ob.can_jump = True
        ob.jump = False
        ob.vel[1] = 0
    else:
        ob.can_jump = False
        if ob.vel[1] > -20:   
            ob.vel[1] -= 0.5   
            
def collide(ob1, ob2): # kokkupuudete kontrolli funktsioon
    
    status = "_False"
    Vtime = 1   # vertikaalne aeg alla
    RHtime = 1  # vertikaalne aeg paremale
    LHtime = 1  # vertikaalne aeg vasakule
    UVtime = 1  # vertikaalne aeg ylesse
    
    if (str(ob2) + "_False") in ob1.collisions:         # kui teise objekti nimetus leitakse koos vastava liidesega esimese objekti kokkupuutumiste nimekirjast 
        i = ob1.collisions.index(str(ob2) + "_False")   # saab i vaartuseks mitmendal kohal objekt oma liidesega selles nimekirjas oli
    elif (str(ob2) + "_on_ground") in ob1.collisions:
        i = ob1.collisions.index(str(ob2) + "_on_ground")
    elif (str(ob2) + "_right_side") in ob1.collisions:
        i = ob1.collisions.index(str(ob2) + "_right_side")    
    elif (str(ob2) + "_left_side") in ob1.collisions:
        i = ob1.collisions.index(str(ob2) + "_left_side")
    elif (str(ob2) + "_on_top") in ob1.collisions:
        i = ob1.collisions.index(str(ob2) + "_on_top")          
               
    #----------Kiirused-kontrollideks----------#   
    Vspeed = ob1.vel[1] + -0.5
    Vdistance = ob2.pp2[1] - ob1.pp1[1]
    if Vspeed != 0:                         # nulliga ei saa jagada
        Vtime = Vdistance / Vspeed
        
    UVspeed = ob1.vel[1] + -100
    UVdistance = ob2.pp1[1] - ob1.pp2[1]
    if UVspeed != 0:
        UVtime = UVdistance / UVspeed    
        
    RHspeed = ob1.vel[0] + 1
    RHdistance = ob2.pp1[0] - ob1.pp4[0]
    if RHspeed != 0:
        RHtime = RHdistance / RHspeed
        
    LHspeed = ob1.vel[0] - 1    
    LHdistance = ob2.pp4[0] - ob1.pp1[0]    
    if LHspeed !=0:
        LHtime = LHdistance / LHspeed    
        
                     
    if (ob1.pp1[0] <= ob2.pp3[0] and ob1.pp1[0] >= ob2.pp1[0])  or (ob1.pp3[0] >=  ob2.pp1[0] and ob1.pp3[0] <= ob2.pp3[0]):
        if Vtime >= 0 and Vtime < 1:    # ennetav kokkupuutekontroll, tapsem kui punktide kasutamine
            status = "_on_ground"
            ob1.pp1[1] = ob2.pp2[1] + 0.05
        elif UVtime >= 0 and UVtime < 1:
            status = "_on_top"

    elif ob1.pp2[1] < ob2.pp1[1] or ob1.pp1[1] > ob2.pp2[1]: # Kui objekt asub teisest objektist korgemal
        pass                                                 # siis lopetatakse funktsioon siinsamas. 

    elif RHtime >=0 and RHtime <1:
            status = "_right_side"
    elif LHtime >=0 and LHtime <1:
            status = "_left_side"    
        

    ob1.collisions[i] = str(ob2) + status # esimese objekti kokkupuudete nimekirja kohal i asuv vaartus muudetakse stringiks mis koosneb objekti nimest ja kokkupuute tyybist            
        
def in_screen(ob, room):    # funktsioon mis t6lgendab koordinaate ekraanikoordinaatideks
        if ob.pp1[0] - room.offset[0] != room.clearance[0]:
            room.offset[0] = ob.pp1[0] - room.clearance[0]
        if ob.pp3[0] - room.offset[0] > room.clearance[1]:
            room.offset[0] = ob.pp3[0] - room.clearance[1]
            
        if ob.pp1[1] - room.offset[1] != room.clearance[2]:
            room.offset[1] = ob.pp1[1] - room.clearance[2]    