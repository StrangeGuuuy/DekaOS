import pyglet
from pyglet.window import key

window = pyglet.window.Window(fullscreen=True)

img=pyglet.resource.image('project_icon.png')
window.set_icon(img)
batch = pyglet.graphics.Batch()
label = pyglet.text.Label('PROJECT: SHELL',
                          font_name='Times New Roman',
                          font_size=40,
                          x=window.width//2, y=window.height//2, batch=batch, anchor_x='center')
label1 = pyglet.text.Label('Press z to start new game',
                          font_name='Times New Roman',
                          font_size=18,
                          x=window.width//2, y=window.height//2 - 50, batch=batch, anchor_x='center')
label2 = pyglet.text.Label('Press x to go to "insert savepoint code" place',
                          font_name='Times New Roman',
                          font_size=18,
                          x=window.width//2, y=window.height//2 - 100, batch=batch, anchor_x='center')

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
