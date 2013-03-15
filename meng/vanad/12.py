
import pyglet
from pyglet.window import key

    
window = pyglet.window.Window(vsync = False)
pimage =  pyglet.image.load('lel.jpg')
i_pp1 = pyglet.image.load('pp1.jpg')
i_pp2 = pyglet.image.load('pp2.jpg')
i_pp3 = pyglet.image.load('pp3.jpg')
i_pp4 = pyglet.image.load('pp4.jpg')
platform_imag = pyglet.image.load('platform.jpg')

keys = key.KeyStateHandler()
window.push_handlers(keys)
fps_display = pyglet.clock.ClockDisplay()
image =  pyglet.image.load('lel.jpg')

def update(dt):
    return 0


pyglet.clock.schedule_interval(update, 1.0/90.0)
pyglet.clock.set_fps_limit(90)   

class player:
    def __init__(self, pp1, image):
        self.pp1=[int(pp1[0]),int(pp1[1])]
        self.vel=[0,0]
        self.image = pimage
        self.width = 118
        self.height = 125
        self.pp2 = [self.pp1[0], self.pp1[1] + self.height]
        self.pp3 = [self.pp1[0], self.pp2[1]]
        self.pp4 = [self.pp2[0], self.pp3[1]]
        self.collision = False
        self.collisions = []
        self.jump = False
        #self.statuses = ["can_jump"]
        self.can_jump = False
        #self.vel[1] = 50
    def draw(self):
        #self.image.blit(self.pp1[0], self.pp1[1])
        self.image.blit(room_1.view(self.pp1)[0], room_1.view(self.pp1)[1])
        i_pp1.blit(room_1.view(self.pp1)[0], room_1.view(self.pp1)[1])
        i_pp2.blit(room_1.view(self.pp2)[0], room_1.view(self.pp2)[1])
        i_pp3.blit(room_1.view(self.pp3)[0], room_1.view(self.pp3)[1])
        i_pp4.blit(room_1.view(self.pp4)[0], room_1.view(self.pp4)[1])
        
    def jemp(self):
        if self.can_jump == True:
            self.jump = True
            
            if self.jump == True:
                if "_on_top" not in str(self.collisions):
                    self.vel[1] += 10
                    #        self.jump = False
                else: #"_on_top" in str(self.collisions):
                    self.jump = False
                    self.can_jump = False
                            #self.vel[1] = -100     
        
    def update(self):
        
        if "_on_top" in str(self.collisions) and "_on_ground" not in str(self.collisions): # <- TAHTIS, JALGI SEDA
                self.vel[1] = -1
                self.can_jump = False

        #if self.jump == True:
            #print self.collisions
            #self.vel[1] += 10
            #self.jump = False
            #if "_on_top" not in str(self.collisions):
            #    if self.vel[1] < 10:
            #        if "_on_top" not in str(self.collisions):
            #            self.vel[1] += 1
                #        self.jump = False
           #         if "_on_top" in str(self.collisions):
           #             self.jump = False
           #             self.can_jump = False
           #             self.vel[1] = -100
                  
                #else:
                    #self.jump = False
            #if "_on_top" in str(self.collisions):
            #    self.vel[1] = 0
            #    self.jump = False
            #else:    
            #    self.vel[1] += 10
            #    self.jump = False
            
        # katsetus ###################################    
        #    if self.vel[1] < 5:
        #        if self.vel[1] == 0:
        #            self.vel[1] = 1
        #        else:
        #            self.vel[1] += self.vel[1]*0.5
        #    else:    
        #        self.jump = False
                
        #if "_on_top" in str(self.collisions) and "_on_ground" not in str(self.collisions):
           # self.vel[1] = 1
         #% window.width
        self.pp1[1] = (self.pp1[1] + self.vel[1]) #% (window.height +100)
        if (self.vel[0] > 0 and "_right_side" in str(self.collisions)) or (self.vel[0] < 0 and "_left_side" in str(self.collisions)):
            self.vel[0] = 0
        self.pp1[0] = (self.pp1[0] + self.vel[0])
        self.vel[0] *= 0.90 #friction, h66rdej6ud
                 
        self.pp2 = [self.pp1[0], self.pp1[1] + self.height]
        self.pp3 = [self.pp1[0] + self.width, self.pp2[1] ]
        self.pp4 = [self.pp3[0], self.pp1[1]]
        #print self.collisions       

        collision_group()
        gravity(self)

        in_screen(player_1, room_1)             
        #pyglet.clock.schedule_interval(update, 1.0/90.0)
        
def in_screen(ob, room):
        if ob.pp1[0] - room.offset[0] != room.clearance[0]:
            room.offset[0] = ob.pp1[0] - room.clearance[0]
        if ob.pp3[0] - room.offset[0] > room.clearance[1]:
            room.offset[0] = ob.pp3[0] - room.clearance[1]
            
        if ob.pp1[1] - room.offset[1] != room.clearance[2]:
            room.offset[1] = ob.pp1[1] - room.clearance[2]
            
        
class room:
    def __init__(self, width, height):
        self.width = 0
        self.height = 0
        self.clearance = [200, 200, 200, 300]
        self.offset = [0,0]
        
    def view(self, pos):
        return [pos[0] - self.offset[0], pos[1] - self.offset[1]]
        
class sprite:
    def __init__(self, pp1, image):
        self.pp1=[pp1[0],pp1[1]]
        self.image = platform_imag
        self.width = 188
        self.height = 35
        self.pp2 = [self.pp1[0] +self. width, self.pp1[1]]
        self.pp3 = [self.pp1[0], self.pp1[1] - self.height]
        self.pp4 = [self.pp2[0], self.pp3[1]]
        
        
        self.pp2 = [self.pp1[0], self.pp1[1] + self.height]
        self.pp3 = [self.pp1[0] + self.width, self.pp2[1] ]
        self.pp4 = [self.pp3[0], self.pp1[1]]
        
        player_1.collisions.append(str(self) + "_False")
        
    def draw(self):
        self.image.blit(room_1.view(self.pp1)[0], room_1.view(self.pp1)[1])
        
        
    
    def update(self):
        #self.image.blit(-player_1.pos[0]+self.pos[0], player_1.pos[1]+self.pos[1]) 
        #self.image.blit(self.pos[0], self.pos[1])
        #self.pp2 = [self.pp1[0], self.pp1[1] + self.height]
        #self.pp3 = [self.pp1[0] + self.width, self.pp2[1] ]
        #self.pp4 = [self.pp3[0], self.pp1[1]]
        
        collide(player_1, self)
        
        
#-----------------------------Funktsioonid-----------------------------#
def gravity(ob):
    if "_on_ground" in str(ob.collisions):
        ob.can_jump = True
        ob.jump = False
        ob.vel[1] = 0
    else:
        ob.can_jump = False
        if ob.vel[1] > -20:   
            ob.vel[1] -= 0.5        
        
def collide(ob1, ob2):
    status = "_False"
    Vtime = 1
    RHtime = 1
    LHtime = 1
    UVtime = 1
    #print ob1.collisions
    if (str(ob2) + "_False") in ob1.collisions:
        i = ob1.collisions.index(str(ob2) + "_False")
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
    if Vspeed != 0:
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
        
                     
    #print time
     #or time == 0:
    #if ob1.pp1[1] <= ob2.pp2[1] and ob1.pp2[1] > ob2.pp2[1] and ob1.pp1[1] > ob2.pp2[1] - 10:
    if (ob1.pp1[0] <= ob2.pp3[0] and ob1.pp1[0] >= ob2.pp1[0])  or (ob1.pp3[0] >=  ob2.pp1[0] and ob1.pp3[0] <= ob2.pp3[0]):
        if Vtime >= 0 and Vtime < 1:
            status = "_on_ground"
        elif UVtime >= 0 and UVtime < 1:
        #if (ob1.pp1[0] <= ob2.pp3[0] and ob1.pp1[0] >= ob2.pp1[0])  or (ob1.pp3[0] >=  ob2.pp1[0] and ob1.pp3[0] <= ob2.pp3[0]):
            status = "_on_top"
            #ob1.vel[1] = 0
            #print ob1.collisions
            #print "el oh el"
    elif ob1.pp2[1] < ob2.pp1[1] or ob1.pp1[1] > ob2.pp2[1]: # Kui objekt asub teisest objektist korgemal voi madalamal polegi mottet edasi kontrollida.
        pass            
                
    #elif (ob1.pp1[1] >= ob2.pp1[1] and ob1.pp1[1] <= ob2.pp2[1]) or (ob1.pp2[1] <= ob2.pp2[1] and ob1.pp2[1] >= ob2.pp1[1]) or (ob2.pp1 >= ob1.pp1[1] and ob2.pp1[1] <= ob1.pp2[1]) or (ob2.pp2[1] <= ob1.pp2[1] and ob2.pp2[1] >= ob1.pp1[1]):
  
    #    #status = "_left_side"
    elif RHtime >=0 and RHtime <1:
    #    if (ob1.pp4[0] >= ob2.pp1[0]) and ob1.pp4[0] < (ob2.pp1[0] + 10): # or ob1.pp3 > ob2.pp3:
        status = "_right_side"
    #    elif(ob1.pp1[0] <= ob2.pp4[0]) and (ob1.pp1[0] > ob2.pp4[0] - 10):                
    #        status = "_left_side"
    #else:
        #status = "_False"
    elif LHtime >=0 and LHtime <1:
        status = "_left_side"    
        
    #speed = ob1.vel[1] + -0.5
    #distance = ob2.pp2[1] - ob1.pp1[1]
    #time = distance / speed    
    
    #if time > 0 and time < 1:
    ob1.collisions[i] = str(ob2) + status

def collision_group():
    for i in range(len(platvorme)):
        platvorme[i].update()
        platvorme[i].draw()
#----------------------------------------------------------------------#
#-----------------------------Loomine----------------------------------#        
player_1=player([200, 200], pimage)
room_1 = room(5,5)
platvorme = []
platvormod = 3

for i in range(platvormod):
    platvorme.append(i)
    platvorme[i] = sprite([(i+1) * 200,(i+1) * 50], platform_imag)
    #player_1.collisions.append(str(platvorme[i]) + "_False")
    
vasak_testiplatvorm = sprite([1,100], platform_imag)
ylemine_testiplatvorm = sprite([200,300], platform_imag)
platvorme.append(vasak_testiplatvorm)
platvorme.append(ylemine_testiplatvorm)  
print platvorme 
#----------------------------------------------------------------------#
def controls():

    if keys[key.W]:
        
        if player_1.jump == True:
            pass
        else:
            if "_on_top" not in str(player_1.collisions):
                player_1.jemp()
        
    elif keys[key.A]:
        player_1.vel[0] -=1
        if room_1.clearance[0] < 500:
            room_1.clearance[0] += 10
            room_1.clearance[1] += 10 

    elif keys[key.S]:
        player_1.pp1[1]-=10
    elif keys[key.D]:
        #print str(player_1.collisions)
        player_1.vel[0] +=1
        if room_1.clearance[0] > 300:
            room_1.clearance[0] -= 10
            room_1.clearance[1] -= 10 
            
    elif keys[key.ENTER]:
        pyglet.app.exit()

@window.event            
def on_draw():
    
    pyglet.clock.tick()
    window.clear()

    fps_display.draw()
    
    controls()
    
    player_1.update()
    #collision_group()
    
    player_1.draw()
    #player_1.vel[1] += 0.5
    #player_1.collisions = []
        
pyglet.app.run()