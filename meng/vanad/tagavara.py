
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
        self.image = pimage
        self.width = 0
        self.height = 0
        
    def update(self):
        
        
        if self.pos[1] > 1:
            self.pos[1]-=0.5
        self.image.blit(200, 100)      

class room:
    def __init__(self, width, height):
        self.width = 0
        self.height = 0
        
class sprite:
    def __init__(self, pos, image):
        self.pos=[pos[0],pos[1]]
        self.image = platform_imag
        self.width = 4
        self.height = 4
    
    def update(self):
        self.image.blit(-player_1.pos[0]+self.pos[0], player_1.pos[1]+self.pos[1]) 



player_1=player([200, 0], pimage)
platform = sprite([50,0], platform_imag)


#@window.event
def controls():
    if keys == {}:
        pass
    elif keys[key.W]:
        player_1.pos[1]+=10
    elif keys[key.A]:
        player_1.pos[0]-=1
    elif keys[key.S]:
        player_1.pos[1]-=1
    elif keys[key.D]:
        player_1.pos[0]+=1       
    elif keys[key.ENTER]:
        pyglet.app.exit()
    #pass
    #keys = {}

def progress():
    pass    
 
@window.event            
def on_draw():
    
    global t
    window.clear()
    fps_display.draw()
    controls()
    player_1.update()
    platform.update()
    pass
    t +=1
    
    #pass
    #pyglet.app.run()    
        
pyglet.app.run()