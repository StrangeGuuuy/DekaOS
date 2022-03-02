import pyglet
from pyglet import clock
import random
import os
dt = clock.tick()
i = 0
window = pyglet.window.Window(fullscreen = True)
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
batch = pyglet.graphics.Batch()
loading_screen_image = pyglet.image.load('Letschat_loading.png')
loading_screen = pyglet.sprite.Sprite(loading_screen_image,
                                      x = window.width //4,
                                      y = window.height//10,
                                      batch = batch,
                                      group = background)
triangle = pyglet.shapes.Polygon((window.width//4+500,
                       window.height//10+400),
                       (window.width//4+550,
                       window.height//10+450),
                       (window.width//4+600,
                       window.height//10+400),
                       color = (50,150,50),
                       batch=batch,
                       group=foreground)



@window.event
def on_draw():
    batch.draw()

def move(self):
    global i
    i+=1
    triangle.rotation = 90*i
    if i > random.randint(5,15):
        window.close()
        os.system('Letschat_archives.py')

clock.schedule_interval(move, 0.4)
             

pyglet.app.run()
