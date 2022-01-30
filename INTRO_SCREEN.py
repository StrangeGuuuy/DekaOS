import pyglet
from pyglet.window import key

window = pyglet.window.Window(1000,800, 'Project: SHELL')

img=pyglet.resource.image('project_icon.png')
window.set_icon(img)
batch = pyglet.graphics.Batch()
label = pyglet.text.Label('PROJECT: SHELL',
                          font_name='Times New Roman',
                          font_size=40,
                          x=500, y=400, batch = batch)
label1 = pyglet.text.Label('Press z to start new game',
                          font_name='Times New Roman',
                          font_size=18,
                          x=500, y=300, batch = batch)
label2 = pyglet.text.Label('Press x to go to "insert savepoint code" place',
                          font_name='Times New Roman',
                          font_size=18,
                          x=500, y=250, batch = batch)
label.anchor_x = 'center'
label1.anchor_x = 'center'
label2.anchor_x = 'center'
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.Z:
        window.close()
        import Introduction
    elif symbol == key.X:
        window.close()
        import CODE_INSERT
@window.event
def on_draw():
    window.clear()
    batch.draw()
pyglet.app.run()
