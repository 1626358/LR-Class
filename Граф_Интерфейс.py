from cProfile import *
from random import random
from tkinter import *
import random
def print_hello():
    print('Привет')

root = Tk()
root.geometry('800x600')
root.title('Hello')
root.configure(bg = 'blue')

def switch(event):
    colors = ['blue','red','white']
    root.configure(bg = random.choice(colors))

label_1 = Label(text = 'Hello, im glad to see you', font = ('Arial', 14))
label_1.pack(pady =10)

button_1 = Button(text = 'Print', font = ('Arial', 14), bg = '#FFFAFA', command = print_hello)
button_1.pack()

button_2 = Button(text = 'exit', font = ('Arial', 14), bg = '#FFFAFA', command =  root.destroy)
button_2.pack(pady = 150)

button_3 =Button(text= 'Смена фона',font = ('Arial', 14), bg = '#FFFAFA')
button_3.pack()
button_3.bind('<Button-1>',switch)

root.mainloop()


