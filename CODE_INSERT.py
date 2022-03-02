import tkinter
import os


def click():
    a = entry.get()
    if a == 'phone':
        window.destroy()
        import CAGE
    elif a == '1':
        window.destroy()
        os.system('INTRO_SCREEN.py')


window = tkinter.Tk(className='Insert code.')
window.rowconfigure(0, minsize= 50, weight=1)
frame = tkinter.Frame(master=window)
entry = tkinter.Entry(master=frame, width=36)
entry.insert(0, "Enter 1 to return")
button = tkinter.Button(master=window, text='Check code', command=click)
frame.grid(row=0, column=0, padx=5)
entry.grid(row=0, column=0, sticky='n')
button.grid(row=1, column=0, pady=5)

window.mainloop()
