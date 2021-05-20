from tkinter import *



root = Tk()

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def click(num):
    e.delete(0, END)
    e.insert(0, num)


def add():
    global f_num
    global math
    math = '+'
    f_num = int(e.get())
    e.delete(0, END)


def substract():
    global f_num
    global math
    math = '-'
    f_num = int(e.get())
    e.delete(0, END)


def multiple():
    global f_num
    global math
    math = '*'
    f_num = int(e.get())
    e.delete(0, END)


def divide():
    global f_num
    global math
    math = '/'
    f_num = int(e.get())
    e.delete(0, END)


def equal():
    second_num = int(e.get())
    e.delete(0, END)

    if math == '+':
        e.insert(0, f_num + second_num)
    if math == '-':
        e.insert(0, f_num - second_num)
    if math == '*':
        e.insert(0, f_num * second_num)
    if math == '/':
        e.insert(0, f_num // second_num)


def clear():
    e.delete(0, END)


button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: click('1'))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: click('2'))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: click('3'))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: click('4'))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: click('5'))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: click('6'))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: click('7'))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: click('8'))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: click('9'))
button_0 = Button(root, text='0', padx=40, pady=40, command=lambda: click('0'))

button_plus = Button(root, text='+', padx=39, pady=20, command=add)
button_minus = Button(root, text='-', padx=41, pady=20, command=substract)
button_product = Button(root, text='*', padx=40, pady=20, command=multiple)
button_divide = Button(root, text='/', padx=41, pady=20, command=divide)

button_equal = Button(root, text='=', padx=89, pady=20, command=equal)
button_clear = Button(root, text='CLEAR', padx=75, pady=40, command=clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_plus.grid(row=5, column=0)
button_minus.grid(row=6, column=0)
button_product.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

root.mainloop()
