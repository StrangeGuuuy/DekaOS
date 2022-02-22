import pyglet
from pyglet import clock
from pyglet.window import key
window = pyglet.window.Window(fullscreen = True) #основное окно
change = open('DEKA_OS.txt','w')
background = pyglet.graphics.OrderedGroup(0) #задний план
foreground = pyglet.graphics.OrderedGroup(1) #передний план
batch = pyglet.graphics.Batch() #список с будущими спрайтами
dt = clock.tick() #тик-так из модуля pyglet.clock
i = 0 # количество действий
loading_image = pyglet.image.load('Loading_game.png') # картинка с загрузкой
loading = pyglet.sprite.Sprite(loading_image,
                            x = window.width //4,
                            y = window.height // 10,    #спрайт загрузки
                            batch = batch,
                            group = background)

black_image = pyglet.image.load('black.png') # картинка чёрной полосочки для перекрывания полоски с загрузкой, так как я ленивая жопа, не умеющая нормально показывать загрузку
black = pyglet.sprite.Sprite(black_image,   #чёрная полосочка
                            x =loading.x+50,
                            y =loading.y+250,
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
    black.x = black.x+20  #полосочку перемещаем направо
    if i == 50: #когда переменная будет равно двадцати, то
        window.close()
        change.write('GAME = 1')
        change.close()
        import DekaOS_Main_Menu #закрыть окно и импортировать Главное Меню
        
        

    
clock.schedule_interval(move, 0.07) #выполнять вышеупомянутое действие каждые 0.4 секунды

pyglet.app.run()
