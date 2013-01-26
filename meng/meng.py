
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
        self.pp1=[pp1[0],pp1[1]]
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
        
    def update(self):
        #self.pp1[1] = (self.pp1[1] + self.vel[1]) 
        if self.jump == True:
            #if self.vel[1] < 10:
            self.vel[1] += 10
            self.jump = False
        # katsetus ###################################    
        #    if self.vel[1] < 5:
        #        if self.vel[1] == 0:
        #            self.vel[1] = 1
        #        else:
        #            self.vel[1] += self.vel[1]*0.5
        #    else:    
        #        self.jump = False
                
        
        self.pp1[0] = (self.pp1[0] + self.vel[0]) #% window.width
        self.pp1[1] = (self.pp1[1] + self.vel[1])
        self.vel[0] *= 0.90 #friction, h66rdej6ud
                 
        self.pp2 = [self.pp1[0], self.pp1[1] + self.height]
        self.pp3 = [self.pp1[0] + self.width, self.pp2[1] ]
        self.pp4 = [self.pp3[0], self.pp1[1]]
               
         
        if "on_ground" in self.collisions:
            self.can_jump = True
            self.jump = False
            self.vel[1] = 0
        else:
            self.can_jump = False
            if self.vel[1] > -10:
                self.vel[1] -= 0.5
                print self.vel[1]
                
        self.pp1[1] = (self.pp1[1] + self.vel[1])        
                
  
        in_screen(player_1, room_1)        
        
        self.collisions = []
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
        
        
        
    
    def update(self):
        #self.image.blit(-player_1.pos[0]+self.pos[0], player_1.pos[1]+self.pos[1]) 
        #self.image.blit(self.pos[0], self.pos[1])
        #self.pp2 = [self.pp1[0], self.pp1[1] + self.height]
        #self.pp3 = [self.pp1[0] + self.width, self.pp2[1] ]
        #self.pp4 = [self.pp3[0], self.pp1[1]]
        
        collide(player_1, self)

        self.image.blit(room_1.view(self.pp1)[0], room_1.view(self.pp1)[1])
        
def collide(ob1, ob2):
    
    if ob1.pp1[1] <= ob2.pp2[1] and ob1.pp2[1] > ob2.pp1[1]:
        if (ob1.pp1[0] <= ob2.pp4[0] and ob1.pp1[0] >= ob2.pp1[0])  or (ob1.pp4[0] >=  ob2.pp1[0] and ob1.pp4[0] <= ob2.pp4[0]):
            ob1.collision = "on_ground"
            
    else:
        ob1.collision = "false"        
            
            
        #if ob1.pp4[1] < ob2.pp3[1]:
            #ob1.pp1[1] = ob2.pp3[1]
            #ob1.collision = "submerged"
    #elif (((ob1.pp1[1] >= ob2.pp1[1]) and (ob1.pp1[1] <= ob2.pp2[1])) or ((ob1.pp2[1] <= ob2.pp3[1]) and (ob1.pp2[1] >= ob2.pp1[1]))) or (((ob2.pp1[1] >= ob1.pp1[1]) and (ob2.pp1[1] <= ob1.pp2[1])) or ((ob2.pp2[1] <= ob1.pp2[1]) and (ob2.pp2[1] >= ob1.pp1[1]))):
        #ob1.collision = "lel"    
        #if (ob1.pp4[0] > ob2.pp1[0]) and ob1.pp4[0] < (ob2.pp4[0]): # or ob1.pp3 > ob2.pp3:
            #ob1.collision = "right_side"        
    #else:
        #ob1.collision = "false"
        
    #if no ""    
    ob1.collisions.append(ob1.collision)
           
        #print "lel"

player_1=player([200, 200], pimage)
room_1 = room(5,5)
platvorme = []
platvormod = 5

for i in range(platvormod):
    platvorme.append(i)
    platvorme[i] = sprite([i * 200,i * 50], platform_imag)
    #print platvorme
    

def controls():
    #global jemp
    #if keys == {}:
        #pass
    if keys[key.W]:
        
        if player_1.jump == True:
            pass
        else:
            player_1.jemp()
        
    elif keys[key.A]:
        player_1.vel[0] -=1
        if room_1.clearance[0] < 500:
            room_1.clearance[0] += 10
            room_1.clearance[1] += 10 

    elif keys[key.S]:
        player_1.pp1[1]-=10
    elif keys[key.D]:
        player_1.vel[0] +=1
        if room_1.clearance[0] > 300:
            room_1.clearance[0] -= 10
            room_1.clearance[1] -= 10 
            
    elif keys[key.ENTER]:
        pyglet.app.exit()

def progress():
    pass    
 

@window.event            
def on_draw():
    pyglet.clock.tick()
    window.clear()
    fps_display.draw()
    
    controls()
    
    player_1.update()
    for i in range(4):
        platvorme[i].update()

    player_1.draw()
    
        
pyglet.app.run()