import pyglet
import os
window = pyglet.window.Window(fullscreen = True)
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
foreforeground = pyglet.graphics.OrderedGroup(2)
batch = pyglet.graphics.Batch()
numbers = ['0.png','1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png']
number0_image = pyglet.image.load('0.png')
number0_1 = pyglet.sprite.Sprite(number0_image,
                                 x = -100,#window.width//4 + 220,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number0_2 = pyglet.sprite.Sprite(number0_image,
                                 x = -100,#window.width//4 + 250,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number0_3 = pyglet.sprite.Sprite(number0_image,
                                 x = -100,#window.width//4 + 280,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number0_4 = pyglet.sprite.Sprite(number0_image,
                                 x = -100,#window.width//4 + 310,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number0_5 = pyglet.sprite.Sprite(number0_image,
                                 x = -100,#window.width//4 + 340,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number0_6 = pyglet.sprite.Sprite(number0_image,
                                 x = -100,#window.width//4 + 370,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number1_image = pyglet.image.load('1.png')
number1_1 = pyglet.sprite.Sprite(number1_image,
                                 x = -100,#window.width//4 + 220,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number1_2 = pyglet.sprite.Sprite(number1_image,
                                 x = -100,#window.width//4 + 250,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number1_3 = pyglet.sprite.Sprite(number1_image,
                                 x = -100,#window.width//4 + 280,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number1_4 = pyglet.sprite.Sprite(number1_image,
                                 x = -100,#window.width//4 + 310,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number1_5 = pyglet.sprite.Sprite(number1_image,
                                 x = -100,#window.width//4 + 340,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number1_6 = pyglet.sprite.Sprite(number1_image,
                                 x = -100,#window.width//4 + 370,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number2_image = pyglet.image.load('2.png')

number2_1 = pyglet.sprite.Sprite(number2_image,
                                 x = -100,#window.width//4 + 220,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number2_2 = pyglet.sprite.Sprite(number2_image,
                                 x = -100,#window.width//4 + 250,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number2_3 = pyglet.sprite.Sprite(number2_image,
                                 x = -100,#window.width//4 + 280,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number2_4 = pyglet.sprite.Sprite(number2_image,
                                 x = -100,#window.width//4 + 310,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number2_5 = pyglet.sprite.Sprite(number2_image,
                                 x = -100,#window.width//4 + 340,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number2_6 = pyglet.sprite.Sprite(number2_image,
                                 x = -100,#window.width//4 + 370,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number3_image = pyglet.image.load('3.png')
number3_1 = pyglet.sprite.Sprite(number3_image,
                                 x = -100,#window.width//4 + 220,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number3_2 = pyglet.sprite.Sprite(number3_image,
                                 x = -100,#window.width//4 + 250,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number3_3 = pyglet.sprite.Sprite(number3_image,
                                 x = -100,#window.width//4 + 280,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number3_4 = pyglet.sprite.Sprite(number3_image,
                                 x = -100,#window.width//4 + 310,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number3_5 = pyglet.sprite.Sprite(number3_image,
                                 x = -100,#window.width//4 + 340,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number3_6 = pyglet.sprite.Sprite(number3_image,
                                 x = -100,#window.width//4 + 370,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number4_image = pyglet.image.load('4.png')
number4_1 = pyglet.sprite.Sprite(number4_image,
                                 x = -100,#window.width//4 + 220,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number4_2 = pyglet.sprite.Sprite(number4_image,
                                 x = -100,#window.width//4 + 250,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number4_3 = pyglet.sprite.Sprite(number4_image,
                                 x = -100,#window.width//4 + 280,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number4_4 = pyglet.sprite.Sprite(number4_image,
                                 x = -100,#window.width//4 + 310,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number4_5 = pyglet.sprite.Sprite(number4_image,
                                 x = -100,#window.width//4 + 340,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number4_6 = pyglet.sprite.Sprite(number4_image,
                                 x = -100,#window.width//4 + 370,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number5_image = pyglet.image.load('5.png')
number5_1 = pyglet.sprite.Sprite(number5_image,
                                 x = -100,#window.width//4 + 220,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number5_2 = pyglet.sprite.Sprite(number5_image,
                                 x = -100,#window.width//4 + 250,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number5_3 = pyglet.sprite.Sprite(number5_image,
                                 x = -100,#window.width//4 + 280,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number5_4 = pyglet.sprite.Sprite(number5_image,
                                 x = -100,#window.width//4 + 310,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number5_5 = pyglet.sprite.Sprite(number5_image,
                                 x = -100,#window.width//4 + 340,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number5_6 = pyglet.sprite.Sprite(number5_image,
                                 x = -100,#window.width//4 + 370,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number6_image = pyglet.image.load('6.png')
number6_1 = pyglet.sprite.Sprite(number6_image,
                                 x = -100,#window.width//4 + 220,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number6_2 = pyglet.sprite.Sprite(number6_image,
                                 x = -100,#window.width//4 + 250,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number6_3 = pyglet.sprite.Sprite(number6_image,
                                 x = -100,#window.width//4 + 280,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number6_4 = pyglet.sprite.Sprite(number6_image,
                                 x = -100,#window.width//4 + 310,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number6_5 = pyglet.sprite.Sprite(number6_image,
                                 x = -100,#window.width//4 + 340,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number6_6 = pyglet.sprite.Sprite(number6_image,
                                 x = -100,#window.width//4 + 370,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number7_image = pyglet.image.load('7.png')
number7_1 = pyglet.sprite.Sprite(number7_image,
                                 x = -100,#window.width//4 + 220,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number7_2 = pyglet.sprite.Sprite(number7_image,
                                 x = -100,#window.width//4 + 250,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number7_3 = pyglet.sprite.Sprite(number7_image,
                                 x = -100,#window.width//4 + 280,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number7_4 = pyglet.sprite.Sprite(number7_image,
                                 x = -100,#window.width//4 + 310,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number7_5 = pyglet.sprite.Sprite(number7_image,
                                 x = -100,#window.width//4 + 340,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number7_6 = pyglet.sprite.Sprite(number7_image,
                                 x = -100,#window.width//4 + 370,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number8_image = pyglet.image.load('8.png')
number8_1 = pyglet.sprite.Sprite(number8_image,
                                 x = -100,#window.width//4 + 220,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number8_2 = pyglet.sprite.Sprite(number8_image,
                                 x = -100,#window.width//4 + 250,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number8_3 = pyglet.sprite.Sprite(number8_image,
                                 x = -100,#window.width//4 + 280,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number8_4 = pyglet.sprite.Sprite(number8_image,
                                 x = -100,#window.width//4 + 310,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number8_5 = pyglet.sprite.Sprite(number8_image,
                                 x = -100,#window.width//4 + 340,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number8_6 = pyglet.sprite.Sprite(number8_image,
                                 x = -100,#window.width//4 + 370,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number9_image = pyglet.image.load('9.png')
number9_1 = pyglet.sprite.Sprite(number9_image,
                                 x = -100,#window.width//4 + 220,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number9_2 = pyglet.sprite.Sprite(number9_image,
                                 x = -100,#window.width//4 + 250,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number9_3 = pyglet.sprite.Sprite(number9_image,
                                 x = -100,#window.width//4 + 280,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number9_4 = pyglet.sprite.Sprite(number9_image,
                                 x = -100,#window.width//4 + 310,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number9_5 = pyglet.sprite.Sprite(number9_image,
                                 x = -100,#window.width//4 + 340,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
number9_6 = pyglet.sprite.Sprite(number9_image,
                                 x = -100,#window.width//4 + 370,
                                 y = -100,#window.height//10 + 535,
                                 batch = batch,
                                 group = foreforeground)
code = []
settings_image = pyglet.image.load('Settings_screen.png')
settings = pyglet.sprite.Sprite(settings_image,
                                x = window.width//4,
                                y = window.height //10,
                                batch = batch,
                                group = background)

exit_image = pyglet.image.load('EXIT.png')
eXit =  pyglet.sprite.Sprite(exit_image,
                              x = window.width // 4+530,
                              y = window.height // 10+432,
                              batch = batch,
                              group = foreforeground)

debug_image = pyglet.image.load('debug.png')
debug = pyglet.sprite.Sprite(debug_image,
                             x = window.width //4+160,
                             y = window.height //10+132,
                             batch = batch,
                             group = foreforeground)

blue_image = pyglet.image.load('cursor.png')
X_image = pyglet.image.load('cursor_x.png')
number_blue_image = pyglet.image.load('cursor_numbers.png')

exit_blue = pyglet.sprite.Sprite(blue_image,
                                 x = window.width // 4+530,
                                 y = window.height // 10+432,
                                 batch = batch,
                                 group = foreground)

debug_blue = pyglet.sprite.Sprite(blue_image,
                                 x = window.width //4+160,
                                 y = window.height // 10+132,
                                 batch = batch,
                                 group = foreground)

password_image = pyglet.image.load('password_screen.png')
password = pyglet.sprite.Sprite(password_image,
                                 x = -300,
                                 y = -300,
                                 batch = batch,
                                 group = foreground)

exit_X = pyglet.sprite.Sprite(X_image,
                              x = -300,
                              y = -300,
                              batch = batch,
                              group = foreforeground)
number_blue = pyglet.sprite.Sprite(number_blue_image,
                                   x = -100,
                                   y = -100,
                                   batch = batch,
                                   group = foreforeground)

@window.event
def on_mouse_motion(x,y,dx,dy):
     if x > window.width // 4+530 and x < window.width // 4+650:
          if y > window.height // 10+432 and y < window.height //10+456:
              eXit.update(x = -100,y = -100)
          else:
              eXit.update(x = window.width // 4+530, y = window.height // 10+432)
     else:
          eXit.update(x = window.width // 4+530, y = window.height // 10+432)

     if x > window.width // 4+160 and x < window.width // 4+280:
          if y > window.height // 10+132 and y < window.height //10+160:
              debug.update(x = -100,y = -100)
          else:
              debug.update(x = window.width // 4+160, y = window.height // 10+132)
     else:
          debug.update(x = window.width // 4+160, y = window.height // 10+132)

     if password.x == window.width // 4+160 and password.y == window.height // 10+252:
          
          if x > window.width // 4+160 and x < window.width // 4+198:
               if y > window.height // 10+598 and y < window.height //10+655:
                    exit_X.update(x = -100, y = -100)
               else:
                    exit_X.update(x = window.width // 4+160, y = window.height // 10+597)
          else:
               exit_X.update(x = window.width // 4+160, y = window.height // 10+597)

          
          if x > window.width // 3+50 and x < window.width // 3+90:
               if y > window.height //3+214 and y < window.height // 3+260:
                    number_blue.update(x = window.width // 3+55 , y = window.height // 3+213)
               elif y > window.height // 3 + 154 and y < window.height // 3 +200:
                    number_blue.update(x = window.width // 3+55 , y = window.height // 3+154)
               elif y > window.height // 3 + 95 and y < window.height // 3 +131:
                    number_blue.update(x = window.width // 3+55 , y = window.height // 3+95)
               elif y > window.height // 3 + 36 and y < window.height // 3 +82:
                    number_blue.update(x = window.width // 3+55 , y = window.height // 3+37)
               else:
                    number_blue.update(x = -100, y = -100)
          else:
               number_blue.update(x = -100, y = -100)

          if x > window.width // 3+125 and x < window.width // 3+173:
               if y > window.height //3+214 and y < window.height // 3+260:
                    number_blue.update(x = window.width / 3+135 , y = window.height / 3+214)
               elif y > window.height // 3 + 154 and y < window.height // 3 +200:
                    number_blue.update(x = window.width // 3+135 , y = window.height // 3+154)
               elif y > window.height // 3 + 95 and y < window.height // 3 +131:
                    number_blue.update(x = window.width // 3+135 , y = window.height // 3+95)
               elif y > window.height // 3 + 36 and y < window.height // 3 +82:
                    number_blue.update(x = window.width // 3+135 , y = window.height // 3+37)

          if x > window.width // 3+210 and x < window.width // 3+250:
               if y > window.height //3+214 and y < window.height // 3+260:
                    number_blue.update(x = window.width // 3+215 , y = window.height // 3+214)
               elif y > window.height // 3 + 154 and y < window.height // 3 +200:
                    number_blue.update(x = window.width // 3+215 , y = window.height // 3+154)
               elif y > window.height // 3 + 95 and y < window.height // 3 +131:
                    number_blue.update(x = window.width // 3+215 , y = window.height // 3+95)
               elif y > window.height // 3 + 36 and y < window.height // 3 +82:
                    number_blue.update(x = window.width // 3+215 , y = window.height // 3+37)
                    
          
               
@window.event
def on_mouse_press(x,y,button,modifiers):
     if button == pyglet.window.mouse.LEFT:
          if x > window.width // 4+530 and x < window.width // 4+650:
               if y > window.height // 10+432 and y < window.height //10+456:
                    window.close()
                    os.system('DekaOS_Main_Menu.py')

          if x > window.width // 3 and x < window.width // 2.55:
               if y > window.height // 4.5 and y < window.height //4:
                    password.update(x = window.width // 4+160, y = window.height // 10+252)
                    exit_X.update(x = window.width // 4+160, y = window.height // 10+597)

          if password.x == window.width // 4+160 and password.y == window.height // 10+252:
               if x > window.width // 3 and x < window.width // 2.8:
                    if y > window.height // 1.53 and y < window.height //1.41:
                         password.update(x = -300, y = -300)
                         exit_X.update(x = -100, y = -100)
                         for i in code:
                              i.update(x = -100, y = -100)
                         code.clear()


               if x > window.width // 3+50 and x < window.width // 3+90:
                    if y > window.height //3+214 and y < window.height // 3+260:

                         if len(code) == 6:
                              pass
                         elif len(code) == 0:
                              code.append(number1_1)
                              number1_1.update(x = window.width//4 + 220, y = window.height//10 + 535)
                         elif len(code) == 1:
                              code.append(number1_2)
                              number1_2.update(x = window.width//4 + 250, y = window.height//10 + 535)
                         elif len(code) == 2:
                              code.append(number1_3)
                              number1_3.update(x = window.width//4 + 280, y = window.height//10 + 535)
                         elif len(code) == 3:
                              code.append(number1_4)
                              number1_4.update(x = window.width//4 + 310, y = window.height//10 + 535)
                         elif len(code) == 4:
                              code.append(number1_5)
                              number1_5.update(x = window.width//4 + 340, y = window.height//10 + 535)
                         elif len(code) == 5:
                              code.append(number1_6)
                              number1_6.update(x = window.width//4 + 370, y = window.height//10 + 535)
                              
                         
                    elif y > window.height // 3 + 154 and y < window.height // 3 +200:
                         
                         if len(code) == 6:
                              pass
                         elif len(code) == 0:
                              code.append(number4_1)
                              number4_1.update(x = window.width//4 + 220, y = window.height//10 + 535)
                         elif len(code) == 1:
                              code.append(number4_2)
                              number4_2.update(x = window.width//4 + 250, y = window.height//10 + 535)
                         elif len(code) == 2:
                              code.append(number4_3)
                              number4_3.update(x = window.width//4 + 280, y = window.height//10 + 535)
                         elif len(code) == 3:
                              code.append(number4_4)
                              number4_4.update(x = window.width//4 + 310, y = window.height//10 + 535)
                         elif len(code) == 4:
                              code.append(number4_5)
                              number4_5.update(x = window.width//4 + 340, y = window.height//10 + 535)
                         elif len(code) == 5:
                              code.append(number4_6)
                              number4_6.update(x = window.width//4 + 370, y = window.height//10 + 535)

                              
                    elif y > window.height // 3 + 95 and y < window.height // 3 +131:
                         if len(code) == 6:
                              pass
                         elif len(code) == 0:
                              code.append(number7_1)
                              number7_1.update(x = window.width//4 + 220, y = window.height//10 + 535)
                         elif len(code) == 1:
                              code.append(number7_2)
                              number7_2.update(x = window.width//4 + 250, y = window.height//10 + 535)
                         elif len(code) == 2:
                              code.append(number7_3)
                              number7_3.update(x = window.width//4 + 280, y = window.height//10 + 535)
                         elif len(code) == 3:
                              code.append(number7_4)
                              number7_4.update(x = window.width//4 + 310, y = window.height//10 + 535)
                         elif len(code) == 4:
                              code.append(number7_5)
                              number7_5.update(x = window.width//4 + 340, y = window.height//10 + 535)
                         elif len(code) == 5:
                              code.append(number7_6)
                              number7_6.update(x = window.width//4 + 370, y = window.height//10 + 535)

                              
                    elif y > window.height // 3 + 36 and y < window.height // 3 +82:
                         for i in code:
                              i.update(x = -100, y = -100)
                         code.clear()


               if x > window.width // 3+125 and x < window.width // 3+173:
                    if y > window.height //3+214 and y < window.height // 3+260:
                         if len(code) == 6:
                              pass
                         elif len(code) == 0:
                              code.append(number2_1)
                              number2_1.update(x = window.width//4 + 220, y = window.height//10 + 535)
                         elif len(code) == 1:
                              code.append(number2_2)
                              number2_2.update(x = window.width//4 + 250, y = window.height//10 + 535)
                         elif len(code) == 2:
                              code.append(number2_3)
                              number2_3.update(x = window.width//4 + 280, y = window.height//10 + 535)
                         elif len(code) == 3:
                              code.append(number2_4)
                              number2_4.update(x = window.width//4 + 310, y = window.height//10 + 535)
                         elif len(code) == 4:
                              code.append(number2_5)
                              number2_5.update(x = window.width//4 + 340, y = window.height//10 + 535)
                         elif len(code) == 5:
                              code.append(number2_6)
                              number2_6.update(x = window.width//4 + 370, y = window.height//10 + 535)

                              
                    elif y > window.height // 3 + 154 and y < window.height // 3 +200:
                         if len(code) == 6:
                              pass
                         elif len(code) == 0:
                              code.append(number5_1)
                              number5_1.update(x = window.width//4 + 220, y = window.height//10 + 535)
                         elif len(code) == 1:
                              code.append(number5_2)
                              number5_2.update(x = window.width//4 + 250, y = window.height//10 + 535)
                         elif len(code) == 2:
                              code.append(number5_3)
                              number5_3.update(x = window.width//4 + 280, y = window.height//10 + 535)
                         elif len(code) == 3:
                              code.append(number5_4)
                              number5_4.update(x = window.width//4 + 310, y = window.height//10 + 535)
                         elif len(code) == 4:
                              code.append(number5_5)
                              number5_5.update(x = window.width//4 + 340, y = window.height//10 + 535)
                         elif len(code) == 5:
                              code.append(number5_6)
                              number5_6.update(x = window.width//4 + 370, y = window.height//10 + 535)

                              
                    elif y > window.height // 3 + 95 and y < window.height // 3 +131:
                         if len(code) == 6:
                              pass
                         elif len(code) == 0:
                              code.append(number8_1)
                              number8_1.update(x = window.width//4 + 220, y = window.height//10 + 535)
                         elif len(code) == 1:
                              code.append(number8_2)
                              number8_2.update(x = window.width//4 + 250, y = window.height//10 + 535)
                         elif len(code) == 2:
                              code.append(number8_3)
                              number8_3.update(x = window.width//4 + 280, y = window.height//10 + 535)
                         elif len(code) == 3:
                              code.append(number8_4)
                              number8_4.update(x = window.width//4 + 310, y = window.height//10 + 535)
                         elif len(code) == 4:
                              code.append(number8_5)
                              number8_5.update(x = window.width//4 + 340, y = window.height//10 + 535)
                         elif len(code) == 5:
                              code.append(number8_6)
                              number8_6.update(x = window.width//4 + 370, y = window.height//10 + 535)

                              
                    elif y > window.height // 3 + 36 and y < window.height // 3 +82:
                         if len(code) == 6:
                              pass
                         elif len(code) == 0:
                              code.append(number0_1)
                              number0_1.update(x = window.width//4 + 220, y = window.height//10 + 535)
                         elif len(code) == 1:
                              code.append(number0_2)
                              number0_2.update(x = window.width//4 + 250, y = window.height//10 + 535)
                         elif len(code) == 2:
                              code.append(number0_3)
                              number0_3.update(x = window.width//4 + 280, y = window.height//10 + 535)
                         elif len(code) == 3:
                              code.append(number0_4)
                              number0_4.update(x = window.width//4 + 310, y = window.height//10 + 535)
                         elif len(code) == 4:
                              code.append(number0_5)
                              number0_5.update(x = window.width//4 + 340, y = window.height//10 + 535)
                         elif len(code) == 5:
                              code.append(number0_6)
                              number0_6.update(x = window.width//4 + 370, y = window.height//10 + 535)
                              

               if x > window.width // 3+210 and x < window.width // 3+250:
                    if y > window.height //3+214 and y < window.height // 3+260:
                         if len(code) == 6:
                              pass
                         elif len(code) == 0:
                              code.append(number3_1)
                              number3_1.update(x = window.width//4 + 220, y = window.height//10 + 535)
                         elif len(code) == 1:
                              code.append(number3_2)
                              number3_2.update(x = window.width//4 + 250, y = window.height//10 + 535)
                         elif len(code) == 2:
                              code.append(number3_3)
                              number3_3.update(x = window.width//4 + 280, y = window.height//10 + 535)
                         elif len(code) == 3:
                              code.append(number3_4)
                              number3_4.update(x = window.width//4 + 310, y = window.height//10 + 535)
                         elif len(code) == 4:
                              code.append(number3_5)
                              number3_5.update(x = window.width//4 + 340, y = window.height//10 + 535)
                         elif len(code) == 5:
                              code.append(number3_6)
                              number3_6.update(x = window.width//4 + 370, y = window.height//10 + 535)
                              


                    elif y > window.height // 3 + 154 and y < window.height // 3 +200:
                         if len(code) == 6:
                              pass
                         elif len(code) == 0:
                              code.append(number6_1)
                              number6_1.update(x = window.width//4 + 220, y = window.height//10 + 535)
                         elif len(code) == 1:
                              code.append(number6_2)
                              number6_2.update(x = window.width//4 + 250, y = window.height//10 + 535)
                         elif len(code) == 2:
                              code.append(number6_3)
                              number6_3.update(x = window.width//4 + 280, y = window.height//10 + 535)
                         elif len(code) == 3:
                              code.append(number6_4)
                              number6_4.update(x = window.width//4 + 310, y = window.height//10 + 535)
                         elif len(code) == 4:
                              code.append(number6_5)
                              number6_5.update(x = window.width//4 + 340, y = window.height//10 + 535)
                         elif len(code) == 5:
                              code.append(number6_6)
                              number6_6.update(x = window.width//4 + 370, y = window.height//10 + 535)
                              


                    elif y > window.height // 3 + 95 and y < window.height // 3 +131:
                         if len(code) == 6:
                              pass
                         elif len(code) == 0:
                              code.append(number9_1)
                              number9_1.update(x = window.width//4 + 220, y = window.height//10 + 535)
                         elif len(code) == 1:
                              code.append(number9_2)
                              number9_2.update(x = window.width//4 + 250, y = window.height//10 + 535)
                         elif len(code) == 2:
                              code.append(number9_3)
                              number9_3.update(x = window.width//4 + 280, y = window.height//10 + 535)
                         elif len(code) == 3:
                              code.append(number9_4)
                              number9_4.update(x = window.width//4 + 310, y = window.height//10 + 535)
                         elif len(code) == 4:
                              code.append(number9_5)
                              number9_5.update(x = window.width//4 + 340, y = window.height//10 + 535)
                         elif len(code) == 5:
                              code.append(number9_6)
                              number9_6.update(x = window.width//4 + 370, y = window.height//10 + 535)
                              


                    elif y > window.height // 3 + 36 and y < window.height // 3 + 82:
                         pass

@window.event
def on_draw():
    batch.draw()

pyglet.app.run()
