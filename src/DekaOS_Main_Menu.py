import pyglet
import os
window = pyglet.window.Window(fullscreen = True) #основное окно
change = open('../DEKA_OS.txt','r')
f = change.read()
print(f)
background = pyglet.graphics.OrderedGroup(0) # задний фон
foreground = pyglet.graphics.OrderedGroup(1)# передний фон
foreforeground = pyglet.graphics.OrderedGroup(2)# перепередний фон
batch = pyglet.graphics.Batch()# лень объяснять повторяющиеся вещи
game_image = pyglet.image.load('../imgs/game.eze.png')
yellow_image = pyglet.image.load('../imgs/cursor_yellow.png')
deka_image = pyglet.image.load('../imgs/DekaOS_screen.png')
deka = pyglet.sprite.Sprite(deka_image,
                            x = window.width //4,
                            y = window.height // 10,        #спрайт-экран
                            batch = batch,
                            group = background)
settings_image = pyglet.image.load('../imgs/Settings.png')
settings = pyglet.sprite.Sprite(settings_image,
                                x = window.width //4 + 617,
                                y = window.height // 10 + 612,        #кнопка с настройками
                                batch = batch,
                                group = foreforeground)
letschat_image = pyglet.image.load('../imgs/Letschat.png')
if f == 'GAME = 0':
     letschat = pyglet.sprite.Sprite(letschat_image,
                                     x = window.width // 4+160,  
                                     y = window.height // 10+252,
                                     batch = batch,
                                     group = foreground)
blue_image = pyglet.image.load('../imgs/cursor.png')
green_image = pyglet.image.load('../imgs/cursor_green.png')         # шутучки вместо названий программ при наведении мышкой
settings_blue = pyglet.sprite.Sprite(blue_image,
                                    x = window.width //4 + 617,       #их
                                    y = window.height //10+612,
                                    batch = batch,
                                    group = foreground)

letschat_blue = pyglet.sprite.Sprite(green_image,
                                        x = -100,        #спрайты
                                        y = -100,
                                        batch = batch,
                                        group = foreforeground)
if f == 'GAME = 1':
     game = pyglet.sprite.Sprite(game_image,
                                   x = window.width //4 + 500,
                                   y = window.height // 10 + 300,        #кнопка с игрой
                                   batch = batch,
                                   group = foreground)
yellow = pyglet.sprite.Sprite(yellow_image,
                              x = -100,
                              y = -100,
                              batch = batch,
                              group = foreforeground)
     
@window.event
def on_mouse_motion(x,y,dx,dy):
     if x > window.width //4 + 617 and x < window.width // 4+737:          #мой главный геморрой. При наведении мышкой на текст с программой текст исчезает и показывает окошко
        if y > window.height // 10+612 and y < window.height //10+638:
            settings.update(x = -100,y = -100)
        else:
            settings.update(x = window.width //4 + 617, y = window.height //10+612)       #иначе оставляет на месте
     else:
         settings.update(x = window.width //4 + 617, y = window.height //10+612)
            
     if x > window.width // 4+160 and x < window.width // 4+280:
          if y > window.height // 10+252 and y < window.height // 10+280:     #то же самое, но с летсчатом
               if f == 'GAME = 0': 
                    letschat_blue.update(x = window.width // 4+160, y = window.height // 10+252)
          else:
              letschat_blue.update(x = -100, y = -100)       
     else:
          letschat_blue.update(x = -100, y = -100) 

     if x > window.width // 4 + 500 and x < window.width // 4 + 620:
          if y > window.height // 10 + 300 and y < window.height // 10 + 324:
               if f == 'GAME = 1':
                    yellow.update(x = window.width //4 + 500, y = window.height // 10 + 300)
          else:
               yellow.update(x = -100, y = -100)
     else:
          yellow.update(x = -100, y = -100)
   
@window.event
def on_mouse_press(x,y,button,modifiers):
     if button == pyglet.window.mouse.LEFT:
          if x > window.width //4 + 617 and x < window.width // 4+737:       #при нажатии на настройки
               if y > window.height // 10+612 and y < window.height //10+638:
                    window.close()
                    os.system('DekaOS_Settings.py')        #ведёт на экран с настройками
                     
          if x > window.width // 4+160 and x < window.width // 4+280:
               if y > window.height // 10+252 and y < window.height // 10+280:         #летсчат
                    if f == 'GAME = 0':
                         window.close()
                         os.system('Letschat_Loading.py')

          if x > window.width // 4 + 500 and x < window.width // 4 + 620:
               if y > window.height // 10 + 300 and y < window.height // 10 + 324:
                    if f == 'GAME = 1':
                         window.close()
                         os.system('Start_game.py')
        
        
@window.event
def on_draw():
    batch.draw()         

pyglet.app.run()
