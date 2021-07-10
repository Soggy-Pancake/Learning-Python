import tkinter as tk
import time

def second():
    print('function called!')

Main = tk.Tk()

Main.title('Test')

screen_height = Main.winfo_screenheight()
screen_width = Main.winfo_screenwidth()

Main.geometry(f'500x500+{int(screen_width/2)}+{int(screen_height/2)}')

box1 = tk.Label(
    Main,
    text="Box 1",
    bg="green",
    fg="white"
)

button = tk.Button(Main, text='Press', command=lambda: print('pressed!'))
button2 = tk.Button(Main, text='Press me too!', command=second)

box1.pack(
    ipadx=10,
    ipady=10,
    side='left'
)

button.pack() #places on screen
button.place(x=10, y=10) #forces specific spot
button2.pack()
button2.place(x=20, y=20)

Main.mainloop()
