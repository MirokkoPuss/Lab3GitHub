from tkinter import *

import numpy as np
import matplotlib.pyplot as plt


def read():
    f=open("data.txt")
    x=f.readline()
    y=f.readline()
    x=x.split(' '); x = [float(i) for i in x]
    y=y.split(' '); y = [float(i) for i in y]
    f.close()
    for i in range(21):
        label = Label(master = window)
        label.grid(row = 1+i, column = 0)
        label.config(text = str(x[i]))
        label = Label(master = window)
        label.grid(row = 1+i, column = 1)
        label.config(text = str(y[i]))
    plt.plot(x,y,'o')
    plt.show()
    
window = Tk()
window.title('ex5')

labelx = Label(master = window, text = 'x')
labelx.grid(row = 0, column = 0)

labely = Label(master = window, text = 'y')
labely.grid(row = 0, column = 1)

button1 = Button(master = window, text = 'Выполнить', command = read)
button1.grid(row = 23, column = 0)

window.mainloop()

