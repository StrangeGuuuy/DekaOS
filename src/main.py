#!/usr/bin/env python3
import pyglet
from pyglet import clock
from pyglet.window import key


window = pyglet.window.Window(fullscreen=True) 
background = pyglet.graphics.OrderedGroup(0) # задний план
foreground = pyglet.graphics.OrderedGroup(1) # передний план
batch = pyglet.graphics.Batch() # список с будущими спрайтами
dt = clock.tick() # тик-так из модуля pyglet.clock
loading_percent: int = 0
deka_image = pyglet.image.load('../imgs/DekaOS_loading.png') # картинка с загрузкой
deka = pyglet.sprite.Sprite(deka_image,
                            x=window.width //4,
                            y=window.height // 10,    #спрайт загрузки
                            batch=batch,
                            group=background)
black_image = pyglet.image.load('../imgs/black.png') # картинка чёрной полосочки для перекрывания полоски с загрузкой, так как я ленивая жопа, не умеющая нормально показывать загрузку
black = pyglet.sprite.Sprite(black_image,   #чёрная полосочка
                            x=deka.x+50,
                            y=deka.y+250,
                            batch=batch,
                            group=foreground)
                            
                            
@window.event
def on_draw() -> None:
    batch.draw()

@window.event
def on_key_press(symbol, modifiers):
    '''Блокировка кнопки ESCAPE'''
    if symbol == pyglet.window.key.ESCAPE:
        return pyglet.event.EVENT_HANDLED
    

def move_loading_bar() -> None: 
    '''функция с передвижением полосочки.'''
    global loading_percent
    loading_percent += 1 
    black.x += 50
    if loading_percent == 20:
        window.close()
        import DekaOS_Main_Menu

    
clock.schedule_interval(move_loading_bar, 0.4) #выполнять вышеупомянутое действие каждые 0.4 секунды


pyglet.app.run()
