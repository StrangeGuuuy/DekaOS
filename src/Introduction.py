import tkinter


def handle_keypress(event) -> None:
    window.destroy()
    import HOUSE
    

window = tkinter.Tk(className='Beginning.')
window.iconphoto(False, tkinter.PhotoImage(file='../imgs/project_icon.png'))
frame = tkinter.Frame(master=window)
label = tkinter.Label(master=frame, font='Arial 40', text="I'm a little broken boy.\nI lost my animation because of something.\nIam going to the king so he can heal me,\n because we are friends.\nIt will be difficult, but I can do it with your help.", background = 'black', foreground = 'white')
frame.pack()
label.pack()
window.bind('<Return>', handle_keypress)
window.mainloop()
