import tkinter


def handle_keypress(event) -> None:
    window.destroy()
    import INTRO_SCREEN


window = tkinter.Tk(className='Introduction.')
window.wm_attributes('-fullscreen',True)

window.config(bg='black')
window.iconphoto(False, tkinter.PhotoImage(file='../imgs/project_icon.png'))
frame = tkinter.Frame(master=window)
label = tkinter.Label(master=frame, font='Arial 50', text="Hello.\nThis is the game project.\nIt's really raw, so be careful.\nHave fun.\n(press Enter to continue)",
                    background='black', foreground='white')
frame.pack()
label.pack()
window.bind('<Return>', handle_keypress)
window.mainloop()
