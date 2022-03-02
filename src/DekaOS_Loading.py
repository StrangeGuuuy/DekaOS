import pyglet
from pyglet import clock
from pyglet.window import key
window1=pyglet.window.Window(fullscreen = True) #окно, что прячет переходы между экранами. Надо как-то убрать в будущем. 
window = pyglet.window.Window(fullscreen = True) #основное окно
background = pyglet.graphics.OrderedGroup(0) #задний план
foreground = pyglet.graphics.OrderedGroup(1) #передний план
batch = pyglet.graphics.Batch() #список с будущими спрайтами
dt = clock.tick() #тик-так из модуля pyglet.clock
i = 0 # количество действий
deka_image = pyglet.image.load('DekaOS_loading.png') # картинка с загрузкой
deka = pyglet.sprite.Sprite(deka_image,
                            x = window.width //4,
                            y = window.height // 10,    #спрайт загрузки
                            batch = batch,
                            group = background)
black_image = pyglet.image.load('black.png') # картинка чёрной полосочки для перекрывания полоски с загрузкой, так как я ленивая жопа, не умеющая нормально показывать загрузку
black = pyglet.sprite.Sprite(black_image,   #чёрная полосочка
                            x =deka.x+50,
                            y =deka.y+250,
                            batch = batch,
                            group = foreground)
@window.event
def on_draw(): # нарисовать их
    batch.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.ESCAPE: # блокировка кнопки ESCAPE (ну, чтобы при нажатии не удалялся экран)
        return pyglet.event.EVENT_HANDLED
    
def move(self): #функция с передвижением полосочки.
    global i #вытаскиваем переменную сюда
    i += 1 #увеличиваем переменную на единицу после каждого действия
    black.x = black.x+50  #полосочку перемещаем направо
    if i == 20: #когда переменная будет равно двадцати, то
        window.close()
        import DekaOS_Main_Menu #закрыть окно и импортировать Главное Меню

    
clock.schedule_interval(move, 0.4) #выполнять вышеупомянутое действие каждые 0.4 секунды


pyglet.app.run()
