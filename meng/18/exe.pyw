
import pyglet
import zipfile
import math
from pyglet.window import key
from pyglet.gl import *

from funktsioonid import *
    
window = pyglet.window.Window(vsync = False)
keys = key.KeyStateHandler()
window.push_handlers(keys)
fps_display = pyglet.clock.ClockDisplay()

glEnable(GL_BLEND) # labipaistvate png jaoks

pyglet.gl.glClearColor(0, 255, 0, 255)


#-------------failide-laadimine-------------#
resources =  pyglet.resource.ZIPLocation(zipfile.ZipFile('resources.zip'), '')

class image_storage:
    def  __init__(self):

        #self.image_locl = pyglet.resource.ZIPLocation(resources, 'images/')
        #self.image_locl = pyglet.resource.ZIPLocation(resources, 'images/right/weapons/spear')
        self.debug()
        self.player()
        self.weapons()
        self.environment()
        
    def debug(self):
        open_file = resources.open('debug/kast.png')
        self.kast = pyglet.image.load('kast.png', open_file)
        
        open_file = resources.open('debug/pp1.png')
        self.i_pp1 = pyglet.image.load('pp1.png', open_file)
        open_file = resources.open('debug/pp2.png') 
        self.i_pp2 = pyglet.image.load('pp2.png', open_file)
        open_file = resources.open('debug/pp3.png')
        self.i_pp3 = pyglet.image.load('pp3.png', open_file)
        open_file = resources.open('debug/pp4.png')   
        self.i_pp4 = pyglet.image.load('pp4.png', open_file)
        
        
    def player(self):
        a_player_legs_right = []
        a_player_legs_left = []
        open_file = resources.open('images/right/player/pl_torso.png')
        self.i_pl_torso_right = pyglet.image.load('pl_torso.png', open_file)
        self.i_pl_torso_right = pyglet.sprite.Sprite(self.i_pl_torso_right)

        open_file = resources.open('images/left/player/pl_torso.png')
        self.i_pl_torso_left = pyglet.image.load('pl_torso.png', open_file)
        self.i_pl_torso_left = pyglet.sprite.Sprite(self.i_pl_torso_left)
        
        i_r_l_arm_20 = resources.open('images/right/player/arms/l_arm/l_20.png')
        self.i_r_l_arm_20 = pyglet.image.load('images/right/player/arms/l_arm/l_20.png', i_r_l_arm_20)
        
                
        
        
        for i in range(20, -25, -5): #laeb sisse k2te pildifailid iga rynnaku nurga jaoks
            #strng = str(i)
            #strng.replace('-', 'm')
            strng = str(i).replace('-', 'm')
                #strng = 'm' + str(-1*i)
            file_directory = 'images/right/player/arms/' + strng + '.png'
            open_file = resources.open(file_directory)
            #setattr(images, 'i_player_arms_' + strng, pyglet.image.load(dir))
            
            setattr(self, 'i_player_arms_' + strng, pyglet.image.load(file_directory, open_file))
            
            
            #setattr(self, 'i_player_arms_' + strng, pyglet.resource.image(dir, file))
            
        for i in range(4): # lisab attribuudi self.i_player_legs_i
            
            file_directory = 'images/right/player/legs/pl_l_' + str(i) + '.png'
            open_file = resources.open(file_directory) 
            
            setattr(self, 'i_player_legs_right' + str(i), pyglet.image.load(file_directory, open_file))
            #setattr(self, ('a_player_legs[' + str(i) + ']'), pyglet.image.load(file_directory, open_file))
            a_player_legs_right.append(getattr(self, 'i_player_legs_right' + str(i)))
           
        self.a_player_legs_right = pyglet.image.Animation.from_image_sequence(a_player_legs_right, 0.2, loop=True)    
        self.a_player_legs_right = pyglet.sprite.Sprite(self.a_player_legs_right)
        
        for i in range(4): # lisab attribuudi self.i_player_legs_i
            
            file_directory = 'images/left/player/legs/pl_l_' + str(i) + '.png'
            open_file = resources.open(file_directory) 
            
            setattr(self, 'i_player_legs_left' + str(i), pyglet.image.load(file_directory, open_file))
            #setattr(self, ('a_player_legs[' + str(i) + ']'), pyglet.image.load(file_directory, open_file))
            a_player_legs_left.append(getattr(self, 'i_player_legs_left' + str(i)))
           
        self.a_player_legs_left = pyglet.image.Animation.from_image_sequence(a_player_legs_left, 0.2, loop=True)    
        self.a_player_legs_left = pyglet.sprite.Sprite(self.a_player_legs_left)       
    def weapons(self):
        #global resources
        file = resources.open('images/right/weapons/spear/sper.png')
        self.i_spear_r = pyglet.image.load('sper.png', file)
        
        
    def environment(self):
        file = resources.open('debug/platform.png')
        self.i_platform = pyglet.image.load('platform.png', file)    
        
    
    
images = image_storage()
#print images.a_player_legs
#print images
#i_arms_20
#i_arms_15
#i_arms_10
#i_arms_5
#i_arms_0
#i_arms_5



#i_spear_r_1 = pyglet.image.load('images/player/right/1.png')
#i_spear_r_2 = pyglet.image.load('images/player/right/2.png')
#ispear_3 = pyglet.image.load('images/player/right/3.png')
#i_spear_r_4 = pyglet.image.load('images/player/right/4.png')
#i_spear_r_5 = pyglet.image.load('images/player/right/5.png')

#i_sl_ud_1 = pyglet.image.load('images/player/_sl_ud_1.jpg')
#i_sl_ud_2 = pyglet.image.load('images/player/_sl_ud_2.jpg')
#i_sl_ud_3 = pyglet.image.load('images/player/_sl_ud_3.jpg')
#i_sl_ud_4 = pyglet.image.load('images/player/_sl_ud_4.jpg')
#i_sl_ud_5 = pyglet.image.load('images/player/_sl_ud_5.jpg')
#i_sl_ud_6 = pyglet.image.load('images/player/_sl_ud_6.jpg')
#i_sl_ud_7 = pyglet.image.load('images/player/_sl_ud_7.jpg')
#i_sl_ud_8 = pyglet.image.load('images/player/_sl_ud_8.jpg')
#i_sl_ud_9 = pyglet.image.load('images/player/_sl_ud_9.jpg')

#------------------------------------------------#


#-----------------------------Funktsioonid-----------------------------#             

def collision_group():
    global current_room                  # uuendatakse ning joonistatakse k6ik platvormid nimekirjas platvormid, kokkupuutekontrolli kasutatakse platvormide uuenduses
    for i in range(len(current_room.platvormid)):
        current_room.platvormid[i].update()
        current_room.platvormid[i].draw()    
           
def controls():                                                     # nupuvajutused
    global current_room
    if keys[key.W]:                 
        if player_1.jump == True:
            pass
        else:
            if "_on_top" not in str(player_1.collisions):
                player_1.jemp()
        
    elif keys[key.A]:
        player_1.vel[0] -=1                                 
        player_1.facing = "left"

    elif keys[key.S]:
        player_1.pp1[1]-=10
        
    elif keys[key.D]:
        player_1.vel[0] +=1                                          # suurendab horisontaalset kiirust 1 v6rra
        player_1.facing = "right"
        
    elif keys[key._1]:
        current_room = room_1
        
    elif keys[key._2]:
        current_room = room_2
                
        
            
    elif keys[key.ENTER]:
        pyglet.app.exit()                                            # sulgeb programmi
            
            
#----------------------------------------------------------------------#            

pyglet.clock.schedule_interval(update, 1.0/90.0) # programmi kiirus
pyglet.clock.set_fps_limit(90)                   # kaadrisageduse piirang 
    
#--------------------------------klassid-------------------------------# 
        
class player:                                                   # mangjaklassi loomine
    def __init__(self, pp1, image):                             # mis tehakse kui mistahes seda klassi kasutav objekt luuakse, mis parameetreid on voimalik objekti loomisel maarata
        self.pp1=[pp1[0], pp1[1]]                               # esimesele nurga positsjoonile nimekirja andmetuubi andmine
        self.vel=[0,0]                                          # kiirusele nimekirja andmetuubi andmine    
        self.image = image                                      # objekti loomisel antud pildifaili sidumine objektiga
        
        
        #self.i_legs = images.i_player_legs_2
        
        
        
        
        
        
        self.width = 118                                        # laius
        self.height = 125                                       # k6rgus    
        self.pp2 = [self.pp1[0], self.pp1[1] + self.height]     # teise punkti koordinaadid
        self.pp3 = [self.pp1[0], self.pp2[1]]                   # kolmanda punkti koordinaadid        
        self.pp4 = [self.pp2[0], self.pp3[1]]                   # neljanda punkti koordinaadid 
        self.center = [self.pp1[0] + (self.width/2), self.pp1[1] + self.height/2]
                              
        self.collisions = []                                    # kokkupuutumiste nimekirja loomine
        self.jump = False                                       # objekti luues ta parasjagu ei hyppa
                                               
        self.can_jump = False                                   # loomise hetkel ei tohi objekt olema v6imeline hyppama
        self.facing = "right"                                   # luues on objekt naoga paremale  
        self.att = False
        
        
        self.att_pos = [0,0]
        self.att_angle = 0
        self.att_vel = [0, 0]
        self.first_dir_key = "none"
        self.spear_rad = 100
        
        
        self.step = 1
                                             
    def draw(self):
        

        
        
                                                               # objekti joonistamise funktsioon
        self.image.blit(room_1.view(self.pp1)[0], room_1.view(self.pp1)[1]) # joonistab pildifaili koordinaatidele
        #i_pp1.blit(room_1.view(self.pp1)[0], room_1.view(self.pp1)[1])     # need olid nurkade asukohakoordinaatide tapsuse kontrollimiseks   
        #i_pp2.blit(room_1.view(self.pp2)[0], room_1.view(self.pp2)[1])
        #i_pp3.blit(room_1.view(self.pp3)[0], room_1.view(self.pp3)[1])
        #i_pp4.blit(room_1.view(self.pp4)[0], room_1.view(self.pp4)[1])
        #i_pp4.blit(room_1.view(self.center)[0], room_1.view(self.center)[1])
        
        anglestring = str(self.att_angle).replace('-', 'm')
        if anglestring != 'm25' and anglestring != '25':
            self.image = getattr(images, "i_player_arms_" + str(anglestring))
    
       
        spear.x = room_1.view(self.pp1)[0] + self.width/2
        spear.y = room_1.view(self.pp1)[1] + self.height/2 #+ 12.5
        
        
        spear.rotation = -1 * self.att_angle
        
       # if keys[key.D] == True:
            
        #    if self.step == 1:
        #        self.i_legs = images.i_player_legs_0
        #        self.i_legs.blit(room_1.view(self.pp1)[0], room_1.view(self.pp1)[1])
        #    elif self.step == 2:
        #        self.i_legs = images.i_player_legs_1
        #    elif self.step == 3:
        #        self.i_legs = images.i_player_legs_2
        #    print self.step
        
        #20
        #15
        #10
        #5
        #0
        #-5
        #-10
        #-15
        #-20
        #images.a_player_legs.blit(room_1.view(self.pp1)[0], room_1.view(self.pp1)[1])
        
        self.i_torso.x = room_1.view(self.pp1)[0]
        self.i_torso.y = room_1.view(self.pp1)[1]
        self.i_torso.draw()
        
        
        self.a_legs.x = room_1.view(self.pp1)[0] #+ self.width/2
        self.a_legs.y = room_1.view(self.pp1)[1] #+ self.height/2
        
        self.a_legs.draw()
        
    def jemp(self):                                         # hyppamisfunktsioon
        if self.can_jump == True:                           # kas tohib hyppata?
            self.jump = True                                # hyppamine toimub
            
            if self.jump == True:                           # kas hyppamine toimub?
                if "_on_top" not in str(self.collisions):   # kas objekti ylemine serv ei puutu millegagi kokku?
                    self.vel[1] += 10                       
                    self.jump = False                       # hyppe l6ppeb
                else:
                    self.jump = False
                    self.can_jump = False
                    
    def attack(self):
        #first_dir_key = "none"
        #self.att = False
        #first_dir_key
       
        #if key.SPACE not in keys:
        #    self.att = False
        
        if self.facing == "right":
            mark = 1
        elif self.facing == "left":
            mark = -1
        keys_true = 0    
        directionals = [keys[key.UP], keys[key.DOWN], keys[key.LEFT], keys[key.RIGHT]]
        

        for i in range(len(directionals)):    
            if directionals[i]:
                keys_true += 1  
             
        #if keys_true == 1:
        if keys[key.UP]:
            self.first_dir_key = "up"
            
            if self.att == "stab_mid":
                player_1.att = "slash_mid_up"
            elif self.att == "stab_down":
                self.att = "slash_down_up"    
            else:
                if self.att != False:
                    pass
                else:    
                    player_1.att = "stab_up"
     
        elif keys[key.RIGHT]:
            self.first_dir_key = "right"
            if self.facing == "right":
                if self.att == "stab_down": 
                    self.att = "slash_down_mid"
                elif self.att == "stab_up":
                    self.att = "slash_up_mid"
                else:                      
                    player_1.att = "stab_mid"                        
                    
            else:
                self.att = "stab_back"
                                            
        elif keys[key.LEFT]:
            self.first_dir_key = "left"
            if self.facing == "left":
                player_1.att = "stab_mid"
            else:
                self.att = "stab_back"         
                
        elif keys[key.DOWN]:
            self.first_dir_key = "down"
            
            if self.att == "stab_mid":
                self.att = "slash_mid_down"
            elif self.att == "stab_up":
                self.att = "slash_up_down"
            
            else:
                if self.att != False:
                    pass
                else:    
                    player_1.att = "stab_down" 
 
            
        #if keys_true > 1:
        #    if (keys[key.RIGHT] and keys[key.UP]):
        #        
        #        if self.facing == "right":
        #            if self.first_dir_key == "right":
        #                player_1.att = "slash_mid_up"
    
        #            elif self.first_dir_key == "up":
        #                player_1.att = "slash_up_mid"
                        
                #elif self.facing == "left":        
   
        #    if keys[key.LEFT] and keys[key.UP]:
        #        if self.facing == "left":
        #            if self.first_dir_key == "left":
        #                player_1.att = "slash_mid_up"
    
        #           elif self.first_dir_key == "up":
        #                player_1.att = "slash_up_mid"
                        
        #    if keys[key.UP] and keys[key.DOWN]:
        #        if self.first_dir_key == "up":
        #            self.att = "slash_up_down"
        #        elif self.first_dir_key == "down":
        #            self.att = "slash_down_up"
                                    
                                 
        if self.att == False:
            self.att_pos = self.center
            images.i_pp1.blit(room_1.view(self.att_pos)[0], room_1.view(self.att_pos)[1])
            pass
        

        if self.att == "stab_up":
            self.att_angle = 20
        elif self.att == "stab_mid":
            self.att_angle = 0
        elif self.att == "stab_down":
            self.att_angle = -20
        elif self.att == "slash_down_up":
            if self.att_angle <= 20:
                self.att_angle +=5 
            else:
                self.att = "stab_up" #False       
        elif self.att == "slash_up_down":      
            if self.att_angle >= -20:
                self.att_angle -=5
            else:
                self.att = "stab_down"#False
        elif self.att == "slash_up_mid":
            if self.att_angle > 0:
                self.att_angle -=5
            else:
                self.att = "stab_mid"
        elif self.att == "slash_mid_up":
            if self.att_angle < 20:
                self.att_angle +=5
            else:
                self.att = "stab_up"         
        elif self.att == "slash_mid_down":
            if self.att_angle > -20:
                self.att_angle -=5
            else:
                self.att = "stab_down"            
        elif self.att == "slash_down_mid":
            if self.att_angle < 0:
                self.att_angle +=5
            else:
                self.att = "stab_mid"        
        if keys[key.SPACE] == False:
            self.att = False              
        self.att_vel[0] = angle(self.att_angle)[0]
        self.att_vel[1] = angle(self.att_angle)[1]  
        
        self.att_pos[0] = self.center[0] + mark * (self.spear_rad * self.att_vel[0]) #+ 100
        self.att_pos[1] = self.center[1] +(self.spear_rad * self.att_vel[1]) #+ 100

              
        images.i_pp1.blit(room_1.view(self.att_pos)[0], room_1.view(self.att_pos)[1]) # joonista ryndepunkt
        
        
        
        #if self.att_angle == 20:
           # i_sl_ud_1
        
        
        #20
        #15
        #10
        #5
        #0
        #-5
        #-10
        #-15
        #-20

        
        
    def update(self):   # mangja uuendamine
        
        if self.step >= 3:
            self.step = 1
        else:
            self.step +=1
        
        
        if "_on_top" in str(self.collisions) and "_on_ground" not in str(self.collisions): # kui objekti ylemine serv puudutab midagi ja alumine parasjagu ei puuduta
                self.vel[1] = -1
                self.can_jump = False

        self.pp1[1] = (self.pp1[1] + self.vel[1]) #% (window.height +100)
        if (self.vel[0] > 0 and "_right_side" in str(self.collisions)) or (self.vel[0] < 0 and "_left_side" in str(self.collisions)):
            self.vel[0] = 0
        self.pp1[0] = (self.pp1[0] + self.vel[0])
        self.vel[0] *= 0.90 # h66rdej6ud
                 
        self.pp2 = [self.pp1[0], self.pp1[1] + self.height]
        self.pp3 = [self.pp1[0] + self.width, self.pp2[1] ]
        self.pp4 = [self.pp3[0], self.pp1[1]] 
        
        self.center = [self.pp1[0] + (self.width/2), self.pp1[1] + self.height/2]     

        collision_group()
        gravity(self)

        in_screen(player_1, room_1)
        self.attack()             
        
        self.a_legs = getattr(images, ("a_player_legs_" + self.facing))
        self.i_torso = getattr(images, ("i_pl_torso_" + self.facing))
          
          
            
        
class room:
    def __init__(self, width, height):
        self.width = 0
        self.height = 0
        
        self.clearance = [200, 200, 200, 300]
        self.offset = [0,0]
        
        self.platvormid = []
        self.platvorme = 0
        
    def view(self, pos):
        return [pos[0] - self.offset[0], pos[1] - self.offset[1]]
    
    def update(self):   # muudab vaatevalja vastavalt mangja suunale
        if player_1.facing == "right" and self.clearance[0] > 300 :
            self.clearance[0] -= 15
            self.clearance[1] -= 15 
        elif player_1.facing == "left" and self.clearance[0] < 500:
            self.clearance[0] += 15
            self.clearance[1] += 15
            
    def creation (self):
        self.platvormid = []
        if self == room_1:
            self.platvorme = 3                                         
            for i in range(self.platvorme):  # luuakse teatud hulk platvorme, trepina
                self.platvormid.append(i)
                self.platvormid[i] = sprite([(i+1) * 200,(i+1) * 50], images.i_platform)
                
            vasak_testiplatvorm = sprite([1,100], images.i_platform)
            ylemine_testiplatvorm = sprite([200,300], images.i_platform)
            self.platvormid.append(vasak_testiplatvorm)
            self.platvormid.append(ylemine_testiplatvorm)
            
        if self == room_2:
            platvorm_1 = sprite([0,0], images.i_platform)
            self.platvormid.append(platvorm_1)
            for i in range(4):
                maa = sprite([i * platvorm_1.width, 0 ], images.i_platform)
                self.platvormid.append(maa)
                
                
                         
        
class sprite:
    def __init__(self, pp1, image):
        self.pp1=[pp1[0],pp1[1]]
        #self.image = images.i_platform
        self.image = pyglet.sprite.Sprite(images.i_platform)
        self.width = 188
        self.height = 35
        self.pp2 = [self.pp1[0] +self. width, self.pp1[1]]
        self.pp3 = [self.pp1[0], self.pp1[1] - self.height]
        self.pp4 = [self.pp2[0], self.pp3[1]]
        
        
        self.pp2 = [self.pp1[0], self.pp1[1] + self.height]
        self.pp3 = [self.pp1[0] + self.width, self.pp2[1] ]
        self.pp4 = [self.pp3[0], self.pp1[1]]
        
        player_1.collisions.append(str(self) + "_False")    # loomisel lisatakse k6ik selle klassi objektid mangja kokkupuudete nimekirja
        
    def draw(self):
        self.image.x = room_1.view(self.pp1)[0]
        self.image.y = room_1.view(self.pp1)[1]
        self.image.draw()
        #self.image.blit(room_1.view(self.pp1)[0], room_1.view(self.pp1)[1])
        #self.image.draw(room_1.view(self.pp1)[0], room_1.view(self.pp1)[1])
        
        
    
    def update(self):
        #self.image.x = self.
        #self.image.blit(-player_1.pos[0]+self.pos[0], player_1.pos[1]+self.pos[1]) 
        #self.image.blit(self.pos[0], self.pos[1])
        #self.pp2 = [self.pp1[0], self.pp1[1] + self.height]
        #self.pp3 = [self.pp1[0] + self.width, self.pp2[1] ]
        #self.pp4 = [self.pp3[0], self.pp1[1]]
        
        collide(player_1, self)
        
        


#-----------------------------Loomine----------------------------------#        
player_1=player([200, 100], images.kast) # loob mangja, kasutades player klassi ning maarates ara alutsamiskoordinaadid ning kasutatava pildifaili

spear = pyglet.sprite.Sprite(images.i_spear_r, x=player_1.pp1[0], y=player_1.pp1[1])
spear.image.anchor_x += player_1.image.width/2 #- player_1.height/2
spear.image.anchor_y += player_1.image.height/2 #- player_1.width/2
room_1 = room(5,5)
room_2 = room(5,5)



room.creation(room_1)
room.creation(room_2)


current_room = room_1
 
spear.draw()
#----------------------------------------------------------------------#

#@window.event

                                                                        

@window.event            
def on_draw():  # mis toimub iga kaadri jooksul
    
    pyglet.clock.tick()
    window.clear()
    fps_display.draw()
    
    controls()
    room_1.update()
    player_1.update() 
    player_1.draw()
    spear.draw()
#@window.event
#def on_key_release(symbol):#,# modifier):
#    if symbol == key.SPACE:
#        print "heh"   
#        player_1.att = False
        
pyglet.app.run() # Programm kaivitatakse