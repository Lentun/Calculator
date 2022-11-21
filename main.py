import tkinter as tk
import math
from tkinter import messagebox


def add_digit(digit):#Ввод цифр
    value = calc.get()
    if value[0] == '0' and len(value)==1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)

def add_operation(operation):#Ввод знаков
    value = calc.get()
    if value[-1] in "-=/*":
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value :
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)

def add_point(operation):#Ввод точки
    value = calc.get()
    if value[-1] in "-=/*":
          value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)

def calculate():#Выполнить дейстие + обработка ошибок
    value = calc.get()
    if value[-1] in "-=/*":
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        k = eval(value)
        k = '{:g}'.format(k)
        calc.insert(0, k)
    except (NameError, SyntaxError):
        messagebox.showinfo('Нужно ввести цифры')
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Нельзя делить на ноль')
        calc.insert(0, 0)

def calculatesqrt():#Корень
    value = calc.get()
    if value[-1] in "-=/*":
        value = value + value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value :
        calculate()
        value = calc.get()
    koren = int(value)
    calc.delete(0, tk.END)
    k = math.sqrt(koren)
    k = '{:g}'.format(k)
    calc.insert(0, k)
      
    

def calculateprocent():#Процент
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

def clear():#Очистить поле ввода
    calc.delete(0, tk.END)
    calc.insert(0, 0)
    

#Функции создания кнопок
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
win.title("Калькулятор")
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