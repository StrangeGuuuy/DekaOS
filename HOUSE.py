import pyglet
from pyglet.gl import *
from pyglet.window import key
batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
foreforeground = pyglet.graphics.OrderedGroup(2)
house_image = pyglet.image.load('house.png')
house = pyglet.sprite.Sprite(house_image, x=0, y=0, batch=batch, group = background)
light_image = pyglet.image.load('light.png')
light = pyglet.sprite.Sprite(light_image, x=725, y=135, batch=batch, group = background)
boy_image = pyglet.image.load('A_slightly_broken_boy(you).png')
boy = pyglet.sprite.Sprite(boy_image, x=350, y=130, batch=batch, group = foreground)
button_image = pyglet.image.load('button.png')
button = pyglet.sprite.Sprite(button_image, x=-100, y=-100, batch=batch, group = foreground)
button1_image = pyglet.image.load('button.png')
button1 = pyglet.sprite.Sprite(button1_image, x=-100, y=-100, batch=batch, group = foreground)
text_1_image = pyglet.image.load('text_1.png')
text_1 = pyglet.sprite.Sprite(text_1_image, x=-100, y=-100, batch=batch, group = foreforeground)
text_2_image = pyglet.image.load('text_2.png')
text_2 = pyglet.sprite.Sprite(text_2_image, x=-100, y=-100, batch=batch, group = foreforeground)
print(house.position)
window = pyglet.window.Window(width = 1000, height = 800)
gl.glClearColor(0.8,0.52,0.256, 1.0)

gl.glClear(gl.GL_COLOR_BUFFER_BIT)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        boy.update(x=boy.x - 10)
        print(boy.x)
    elif symbol == key.RIGHT:
        boy.update(x=boy.x + 10)
        print(boy.x)
    elif symbol == key.X:
        if boy.x > 120 and boy.x < 280:
            button1.update(x = -100, y = -100)
            text_1.update(x=170, y=300)
        if boy.x > 420 and boy.x < 560:
            button.update(x = -100, y = -100)
            text_2.update(x=490, y = 300)  
    if boy.x < 0:
        boy.x = 0

@window.event
def on_draw():
    batch.draw()
    if boy.x > 120 and boy.x < 280:
        button1.update(x = 170, y = 300)
    if boy.x < 120 or boy.x > 280:
        button1.update(x = -100, y = -100)
        text_1.update(x=-100, y=-100)
    if boy.x > 420 and boy.x < 560:
        button.update(x = 490, y = 300)
    if boy.x < 420 or boy.x > 560:
        button.update(x = -100, y = -100)
        text_2.update(x=-100, y = -100)


    
pyglet.app.run()
