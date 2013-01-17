
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
        self.on_ground = True
        
    def draw(self):
        self.image.blit(self.pos[0], self.pos[1])
        
    def jemp(self):
        if self.on_ground == True:
            self.vel[1] +=50
        
        
    def update(self):
        
        self.pp2 = [self.pos[0], self.pos[1] + self.height]
        self.pp3 = [self.pos[0] + self.width, self.pp2[1] ]
        self.pp4 = [self.pp3[0], self.pos[1]]
        
        self.pos[0] = (self.pos[0] + self.vel[0]) #% window.width
        self.pos[1] = (self.pos[1] + self.vel[1]) % window.height
                 
        self.vel[0] *= .90 #friction, h66rdej6ud
        
        # POS [1] ON TEGELIKULT OBJEKTI ALUMISEST SERVAST, tee korda
        
        if self.on_ground == True:        
            self.vel[1] = 0
            if self.pos[1] < platform.pp2[1]:
                self.pos[1] = platform.pp2[1]                    
        elif self.on_ground == False:
            if self.vel[1] > -10:
                self.vel[1] -= 0.5    
 
        self.image.blit(self.pos[0], self.pos[1])      


class room:
    def __init__(self, width, height):
        self.width = 0
        self.height = 0
        
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
        self.image.blit(self.pos[0], self.pos[1])
        self.pp2 = [self.pos[0], self.pos[1] + self.height]
        self.pp3 = [self.pos[0] + self.width, self.pp2[1] ]
        self.pp4 = [self.pp3[0], self.pos[1]]
        
def collide(ob1, ob2):
    if ob1.pos[0] >= ob2.pp3[0] or ob1.pp3[0] <=  ob2.pos[0] or ob1.pp4[1] > ob2.pp2[1] :
        ob1.on_ground = False
    else:
        ob1.on_ground = True   
        #print "lel"

player_1=player([200, 0], pimage)
platform = sprite([50,0], platform_imag)
platvorme = []
#platvorme = 4

for i in range(4):
    i = sprite([i,i], platform_imag)
    platvorme.append(i)
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
    
    collide(player_1, platform)
    player_1.draw()
    platform.update()
    
    #1.update()
    
    
   # for i in range(4):
       # i.update()
        #i.draw()
    
    #pass
    pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
    ('v2i', (int(player_1.pp4[0]), int(player_1.pp4[1]), 30, 35))
    )

        
pyglet.app.run()