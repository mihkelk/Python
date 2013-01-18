
import pyglet
from pyglet.window import key

x = 5
y = 6

    
window = pyglet.window.Window(vsync = False)
pimage =  pyglet.image.load('lel.jpg')
platform_imag = pyglet.image.load('platform.jpg')

keys = key.KeyStateHandler()
window.push_handlers(keys)
fps_display = pyglet.clock.ClockDisplay()
image =  pyglet.image.load('lel.jpg')
#collisions = []

def update(dt):
    return 0


pyglet.clock.schedule_interval(update, 1.0/60.0)
pyglet.clock.set_fps_limit(80)   

class player:
    def __init__(self, pos, image):
        self.pos=[pos[0],pos[1]]
        self.vel=[0,0]
        self.image = pimage
        self.width = 118
        self.height = 125
        self.pp2 = [self.pos[0], self.pos[1] + self.height]
        self.pp3 = [self.pos[0], self.pp2[1]]
        self.pp4 = [self.pp2[0], self.pp3[1]]
        self.collision = False
        self.collisions = []
        
    def draw(self):
        #self.image.blit(self.pos[0], self.pos[1])
        self.image.blit(room_1.view(self.pos)[0], room_1.view(self.pos)[1])
        
    def jemp(self):
        #if self.collision == "on_ground":
        if "on_ground" in self.collisions:    
            self.vel[1] +=50
        
        
    def update(self):
        #global offset
        
        self.pp2 = [self.pos[0], self.pos[1] + self.height]
        self.pp3 = [self.pos[0] + self.width, self.pp2[1] ]
        self.pp4 = [self.pp3[0], self.pos[1]]
        
        self.pos[0] = (self.pos[0] + self.vel[0]) #% window.width
        self.pos[1] = (self.pos[1] + self.vel[1]) #% window.height
                 
        self.vel[0] *= .90 #friction, h66rdej6ud
        if self.vel[1] > -10:
            self.vel[1] -= 0.5 
        
        # POS [1] ON TEGELIKULT OBJEKTI ALUMISEST SERVAST, tee korda
        
        if "on_ground" in self.collisions:
            self.vel[1] = 0    

        if self.pos[0] - room_1.offset[0] < room_1.clearance[0]:
            room_1.offset[0] = self.pos[0] - room_1.clearance[0]
        if self.pp3[0] - room_1.offset[0] > room_1.clearance[1]:
            room_1.offset[0] = self.pp3[0] - room_1.clearance[1]
        
        
        
        
        
        
             
        print self.collisions
        self.collisions = []
class room:
    def __init__(self, width, height):
        self.width = 0
        self.height = 0
        self.clearance = [300, 300]
        self.offset = [0,0]
        
    def view(self, pos):
        return [pos[0] - self.offset[0], pos[1] - self.offset[1]]
        
class sprite:
    def __init__(self, pos, image):
        self.pos=[pos[0],pos[1]]
        self.image = platform_imag
        self.width = 188
        self.height = 35
        self.pp2 = [self.pos[0] +self. width, self.pos[1]]
        self.pp3 = [self.pos[0], self.pos[1] - self.height]
        self.pp4 = [self.pp2[0], self.pp3[1]]
        
        
    
    def update(self):
        #self.image.blit(-player_1.pos[0]+self.pos[0], player_1.pos[1]+self.pos[1]) 
        #self.image.blit(self.pos[0], self.pos[1])
        self.pp2 = [self.pos[0], self.pos[1] + self.height]
        self.pp3 = [self.pos[0] + self.width, self.pp2[1] ]
        self.pp4 = [self.pp3[0], self.pos[1]]
        
        self.image.blit(room_1.view(self.pos)[0], room_1.view(self.pos)[1])
        
        collide(player_1, self)
        
def collide(ob1, ob2):
    #global collisions
    
    if (ob1.pos[0] <= ob2.pp4[0] and ob1.pos[0] >= ob2.pos[0]  or ob1.pp4[0] >=  ob2.pos[0] and ob1.pp4[0] <= ob2.pp4[0]) and ob1.pp4[1] <= ob2.pp2[1] and ob1.pp2[1] > ob2.pp4[1] :
        ob1.collision = "on_ground"
        if ob1.pp4[1] < ob2.pp3[1]:
            ob1.pos[1] = ob2.pp3[1]
            #ob1.collision = "submerged"
    else:
        ob1.collision = "false"
        
    #if no ""    
    ob1.collisions.append(ob1.collision)
           
        #print "lel"

player_1=player([200, 0], pimage)
room_1 = room(5,5)
platvorme = []
platvormod = 5

for i in range(platvormod):
    platvorme.append(i)
    platvorme[i] = sprite([i * 200,i * 50], platform_imag)
    print platvorme 
    


    

#@window.event
def controls():
    global jemp
    if keys == {}:
        pass
    elif keys[key.W]:
        player_1.jemp()
        
    elif keys[key.A]:
        player_1.vel[0] -=1
    elif keys[key.S]:
        player_1.pos[1]-=10
    elif keys[key.D]:
        player_1.vel[0] +=1    
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
    
    player_1.draw()

    
    
    for i in range(4):
        platvorme[i].update()

    pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
    ('v2i', (int(player_1.pp4[0]), int(player_1.pp4[1]), 30, 35)))
        
pyglet.app.run()