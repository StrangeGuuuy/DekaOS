import tkinter

window = tkinter.Tk()
window.wm_attributes('-fullscreen',True)
def handle_keypress(event):
    window.destroy()
    import INTRO_SCREEN

window.title('Introduction.')
window['bg'] = 'black'
window.iconphoto(False, tkinter.PhotoImage(file='project_icon.png'))
frame = tkinter.Frame(master = window)
label = tkinter.Label(master = frame, font = 'Arial 50', text = "Hello.\nThis is the game project.\nIt's really raw, so be careful.\nHave fun.\n(press Enter to continue)", background = 'black', foreground = 'white')
frame.pack()
label.pack()
window.bind('<Return>', handle_keypress)
window.mainloop()
