import pyglet


class images:
    def __init__(self):
        lel = self
        #i_player_arms_20 = "lel" 
        

lol = pyglet.image

i_player_arms_20 = "lel"           
    
for i in range(20, -20, -5):
    dir = 'images/right/player/arms/' + str(i) + '.jpg'
    setattr(lol, 'i_player_arms_' + str(i), pyglet.image.load(dir))
    print "ok"
print lol.i_player_arms_0
    
lell = "-hueuheuhue+hehueuhe-"
print lell
lell.replace("h", 'm')
print lell