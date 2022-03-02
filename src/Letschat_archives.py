import pyglet
import os
window = pyglet.window.Window(fullscreen = 1)
batch = pyglet.graphics.Batch()
backbackground = pyglet.graphics.OrderedGroup(1)
background = pyglet.graphics.OrderedGroup(2)
foreground = pyglet.graphics.OrderedGroup(3)
foreforeground = pyglet.graphics.OrderedGroup(4)
screen_list =[]
exit_tech = 0
dialoge = 1
orange_image = pyglet.image.load('cursor_orange.png')
orange = pyglet.sprite.Sprite(orange_image,
                              x = -100,
                              y = - 100,
                              batch = batch,
                              group = foreground)
background_image = pyglet.image.load('background.png')
bacKground = screen = pyglet.sprite.Sprite(background_image,
                              x = window.width // 4,
                              y = window.height //10,
                              batch = batch,
                              group = backbackground)

screen_image = pyglet.image.load('Letschat_screen.png')
screen = pyglet.sprite.Sprite(screen_image,
                              x = window.width // 4,
                              y = window.height //10,
                              batch = batch,
                              group = background)
green_image = pyglet.image.load('Green_Button.png')
green = pyglet.sprite.Sprite(green_image,
                              x = -100,
                              y = -100,
                              batch = batch,
                              group = foreforeground)
dialog_image = pyglet.image.load('dialog.png')
dialog1_image = pyglet.image.load('dialog1.png')
dialog2_image = pyglet.image.load('dialog2.png')
dialog= pyglet.sprite.Sprite(dialog_image,
                              x = -700,
                              y = -700,
                              batch = batch,
                              group = background)

dialog1 = pyglet.sprite.Sprite(dialog1_image,
                              x = -700,
                              y = -700,
                              batch = batch,
                              group = background)

dialog2 = pyglet.sprite.Sprite(dialog2_image,
                              x = -700,
                              y = -700,
                              batch = batch,
                              group = background)
eXit_image = pyglet.image.load('cursor_exit_tech.png')
eXit = pyglet.sprite.Sprite(eXit_image,
                            x = -200,
                            y=-200,
                            batch = batch,
                            group = foreforeground)
tech_image = pyglet.image.load('Technical_works.png')
tech = pyglet.sprite.Sprite(tech_image,
                            x = -200,
                            y=-200,
                            batch = batch,
                            group = foreground)

@window.event
def on_draw():
    batch.draw()
    
@window.event
def on_mouse_motion(x,y,dx,dy):
    global dialoge
    if dialoge == 1:        
        if x > window.width // 4 and x < window.width // 4+229:
            if y > window.height // 10+78 and y < window.height //10+146:
                green.update(x = window.width // 4,y = window.height //10+78)
            elif y > window.height // 10+156 and y < window.height //10+224:
                green.update(x = window.width // 4,y = window.height //10+156)
            elif y > window.height // 10+589 and y < window.height //10+657:
                green.update(x = window.width // 4,y = window.height //10+589)
            elif y > window.height // 10+661 and y < window.height //10+729:
                green.update(x = window.width // 4,y = window.height //10+661)
            elif y > window.height // 10+733 and y < window.height //10+801:
                green.update(x = window.width // 4,y = window.height //10+733)
            else:
                green.update(x = -100, y = -100)
        else:
            green.update(x = -100, y = -100)

        if exit_tech == 1:
            if x > window.width//4+286 and x < window.width//4 + 345:
                if y > window.height//10+127 and y < window.height//10 + 200:
                    eXit.update(x = window.width//4+288, y = window.height//10+127)
                else:
                    eXit.update(x = -200, y = -200)
            else:
                eXit.update(x = -200, y = -200)

    elif dialoge == 0:
        if x > window.width // 4+480 and x < window.width // 4+705:
            if y >window.height//10+400 and y < window.height // 10+473:
                orange.update(x = window.width //4+487, y = window.height//10+407)
            else:
                orange.update(x=-100, y = - 100)

        else:
            orange.update(x=-100, y = - 100)



@window.event
def on_mouse_press(x,y,button,modifiers):
    global exit_tech
    global dialoge
    if dialoge == 1:
        if x > window.width // 4 and x < window.width // 4+229:
            if y > window.height // 10+78 and y < window.height //10+146:
                tech.update(x = window.width//4+250, y=window.height//10+100)
                exit_tech = 1
            elif y > window.height // 10+156 and y < window.height //10+224:
                window.close()
                os.system('DekaOS_Main_Menu.py')

                
            elif y > window.height // 10+589 and y < window.height //10+657:
                dialog2.update(x = window.width // 4+250,y = window.height //10)
                if screen_list != []:
                    for i in screen_list:
                        i.update(x=-700,y=-700)
                    screen_list.clear()
                screen_list.append(dialog2)
                screen.update(x = -1000, y = -1000)
                dialoge = 0
                tech.delete()
                green.delete()
                
                
                
            elif y > window.height // 10+661 and y < window.height //10+729:
                dialog1.update(x = window.width // 4+250,y = window.height //10)
                if screen_list != []:
                    for i in screen_list:
                        i.update(x=-700,y=-700)
                    screen_list.clear()
                screen_list.append(dialog1)

                
            elif y > window.height // 10+733 and y < window.height //10+801:
                dialog.update(x = window.width // 4+260,y = window.height //10-10)
                if screen_list != []:
                    for i in screen_list:
                        i.update(x=-700,y=-700)
                    screen_list.clear()
                screen_list.append(dialog)

        elif x > window.width//4+286 and x < window.width//4 + 345:
            if y > window.height//10+127 and y < window.height//10 + 200:
                eXit.update(x = -200, y = -200)
                tech.update(x=-200, y = -200)
                exit_tech = 0

    elif dialoge == 0:
        if x > window.width // 4+480 and x < window.width // 4+705:
            if y >window.height//10+400 and y < window.height // 10+473:
                window.close()
                os.system('Game_Loading.py')

pyglet.app.run()
