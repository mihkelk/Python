
import pyglet

window = pyglet.window.Window(vsync = False)

class image_storage:
    def __init__(self):
        self.i_platform = pyglet.sprite.Sprite('platform.jpg')
        
images = image_storage        
        
      
#images.i_platform = pyglet.resource.image('platform.jpg')        
images.i_platform = pyglet.sprite.Sprite(pyglet.image.load('platform.jpg'))        
@window.event            
def on_draw():
    images.i_platform.draw()
    #on_mouse_press()
    #print "lel"

@window.event  
def on_mouse_press(x, y, button, modifiers):
    
    if button == pyglet.window.mouse.LEFT:
        images.i_platform.x = x
        images.i_platform.y = y
        #print "heh"
    
    pass      
    
pyglet.app.run()

    