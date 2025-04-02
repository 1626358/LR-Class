from tkinter import *
root = Tk()
root.geometry('1366x768')
root.title('auauauauau')
conva = Canvas(width=500,height=500,background = 'green')
conva.pack()
'''
conva.create_line(0,0,1300,700,width=20, fill='#FF69B4')
conva.create_rectangle(0,0,100,100,fill='#FF0000', width=10, outline='#ADFF2F')
conva.create_oval(250,250,600,300,fill =  '#4682B4', width=11, outline='#FFFAFA')
'''
for i in range(10):
    if  i%3==0:
        color = 'white'
    elif i%2 == 0:
        color = 'red'
    else:
        color = 'green'
    conva.create_rectangle(150+i*10,150+i*10,350-i*10,350-i*10,fill=color,width=2)
root.mainloop()