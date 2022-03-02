import pyglet

window = pyglet.window.Window(632,454, "Where it belongs to be.")
image = pyglet.resource.image('This.png')

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

pyglet.app.run()
