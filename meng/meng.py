
import pyglet
from pyglet.window import key

x = 5
y = 6

window = pyglet.window.Window()
pimage =  pyglet.image.load('lel.jpg')
platform_imag = pyglet.image.load('platform.jpg')

keys = key.KeyStateHandler()
window.push_handlers(keys)
t = 1
fps_display = pyglet.clock.ClockDisplay()
image =  pyglet.image.load('lel.jpg')

class player:
    def __init__(self, pos, image):
        self.pos=[pos[0],pos[1]]
        self.vel=[0,0]
        self.image = pimage
        self.width = 125
        self.height = 118
        self.pp2 = [self.pos[0] + self.width, self.pos[1]]
        self.pp3 = [self.pos[0], self.pos[1] - self.height]
        self.pp4 = [self.pp2[0], self.pp3[1]]
        
    def draw(self):
        self.image.blit(self.pos[0], self.pos[1])
        
        
    def update(self):
        
        self.pp2 = [self.pos[0] + self.width, self.pos[1]]
        self.pp3 = [self.pos[0], self.pos[1] - self.height]
        self.pp4 = [self.pp2[0], self.pp3[1]]
        
        self.pos[0] = (self.pos[0] + self.vel[0]) % window.width
        
        self.vel[0] *= .90 #friction, h66rdej6ud
        # POS [1] ON TEGELIKULT OBJEKTI ALUMISEST SERVAST, tee korda
        
        if self.pos[0] >= platform.pp2[0] or self.pp2[0] <=  platform.pos[0] or self.pp3[1] > platform.pos[1] :
            self.pos[1]-=0.5
            print platform.pos
            print platform.pp2
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
        self.pp2 = [self.pos[0] + self.width, self.pos[1]]
        self.pp3 = [self.pos[0], self.pos[1] - self.height]
        self.pp4 = [self.pp2[0], self.pp3[1]]
        

player_1=player([200, 0], pimage)
print player_1.pp3[1]
platform = sprite([50,0], platform_imag)

print player_1.pos
print player_1.pos[1]
print player_1.pp3[1]
#print platform.pos[0]
#@window.event
def controls():
    if keys == {}:
        pass
    elif keys[key.W]:
        player_1.pos[1]+=10
    elif keys[key.A]:
        #player_1.pos[0]-=10
        player_1.vel[0] -=1
    elif keys[key.S]:
        player_1.pos[1]-=10
    elif keys[key.D]:
        player_1.vel[0] +=1    
    elif keys[key.ENTER]:
        pyglet.app.exit()
    #pass
    #keys = {}


def progress():
    pass    
 
def update(dt):
    return 0

 
@window.event            
def on_draw():
    print player_1.pos[1]
    global t
    window.clear()
    fps_display.draw()
    controls()
    player_1.update()
    player_1.draw()
    platform.update()
    pass
    t +=1

#@window.event       
#def on_key_press(symbol, modifiers): 
#    if symbol == key.A:
#        player_1.vel[0] -=1   
#        player_1.vel[0] -=1   
#        player_1.vel[0] -=1   
#@window.event       
#def on_key_release(symbol, modifiers):
#    if symbol == key.A:
#        player_1.vel[0] +=1
#        
#        pass   
   
pyglet.clock.schedule_interval(update, 1/60.0)    
    #pass
    #pyglet.app.run()    
        
pyglet.app.run()