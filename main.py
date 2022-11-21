import tkinter as tk
import math
from tkinter import messagebox


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value)==1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)

def add_operation(operation):
    value = calc.get()
    if value[-1] in "-=/*":
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value :
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)

def add_point(operation):
    value = calc.get()
    if value[-1] in "-=/*":
          value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)

def calculate():
    value = calc.get()
    if value[-1] in "-=/*":
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        k = eval(value)
        k = '{:g}'.format(k)
        calc.insert(0, k)
    except (NameError, SyntaxError):
        messagebox.showinfo('Need to enter numbers)
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Can not divide by zero')
        calc.insert(0, 0)

def calculatesqrt():
    value = calc.get()
    if value[-1] in "-=/*":
        value = value + value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value :
        calculate()
        value = calc.get()
    sqrt = int(value)
    calc.delete(0, tk.END)
    k = math.sqrt(sqrt)
    k = '{:g}'.format(k)
    calc.insert(0, k)
      
    

def calculateprocent():
    value = calc.get()
    if value[-1] in "-=/*":
        value = value + value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value :
        calculate()
        value = calc.get()
    procent = int(value)
    calc.delete(0, tk.END)
    i = procent/100
    i = '{:g}'.format(i)
    calc.insert(0, i)

def clear():
    calc.delete(0, tk.END)
    calc.insert(0, 0)
    


def make_digit_buttom(digit):
    return tk.Button(text=digit, bd=5, command=lambda: add_digit(digit))


def make_operation_buttom(operation):
    return tk.Button(text=operation, bd=5, command=lambda: add_operation(operation))


def make_calc_buttom(operation):
    return tk.Button(text=operation, bd=5, font=(15), command=calculate)

def make_calcsqrt_buttom(operation):
    return tk.Button(text=operation, bd=5, font=(15), command=calculatesqrt)

def make_calcprocent_buttom(operation):
    return tk.Button(text=operation, bd=5, font=(15), command=calculateprocent)

def make_clear_buttom(operation):
    return tk.Button(text=operation, bd=5, font=(15), command=clear)

def make_point_buttom(operation):
    return tk.Button(text=operation, bd=5, font=(15), command=lambda: add_point(operation))


def presskey(event):#Обработка ввода с клавиатуры
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif  event.char in '+-*/%':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    elif event.char == '.':
        add_operation(event.char)
    elif event.char == '\x08':
        clear()



win = tk.Tk()
win.geometry("300x260")
win.title("Calculator")
win.focus_force()
calc = tk.Entry(win, justify=tk.RIGHT, font=(15), width=15)
calc.insert(0,'0')
calc.grid(row=0, column=0, columnspan=6, stick="we", padx=10)


win.bind('<Key>', presskey)

make_digit_buttom('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_buttom('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_buttom('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_buttom('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_buttom('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_buttom('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_buttom('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_buttom('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_buttom('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_buttom('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation_buttom("+").grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_buttom("-").grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_buttom("/").grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_buttom("*").grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calcsqrt_buttom("\u221A").grid(row=1, column=5, stick='wens', padx=5, pady=5)
make_calcprocent_buttom("%").grid(row=2, column=5, stick='wens', padx=5, pady=5)
make_point_buttom(".").grid(row=3, column=5, stick='wens', padx=5, pady=5)

make_calc_buttom('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_buttom('c').grid(row=4, column=1, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)


win.mainloop()
