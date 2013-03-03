import pyglet
import zipfile

jeep = zipfile.ZipFile('kt.zip')
#zeep =  pyglet.resource.file(jeep, 'rt')
resources = pyglet.resource.ZIPLocation(jeep, 'images/right/weapons/spear')
#print resources.zip
#heh = resources.open('5.png')
heh = resources.open('5.png')
#i_spear_r = pyglet.image.load(heh)#'5.png', heh)