from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Calculator v.1.1")
root.iconbitmap("calculator.ico")
e = Entry(root, width=65, borderwidth=3)
e.grid(row=0, column=0, columnspan=4, pady=10, ipady=10)

def button_click(number):
    current = e.get()
    # Check if the current input is empty or if it already contains a dot
    if number == ".":
        if "." in current:
            return
    # Concatenate the new number to the current input
    e.delete(0, END)
    e.insert(0, current + number)

def clear_button():
    e.delete(0, END)

def sum_button():
    global f_num
    global math
    math = "+"
    f_num = float(e.get())
    e.delete(0, END)

def sub_button():
    global f_num
    global math
    math = "-"
    f_num = float(e.get())
    e.delete(0, END)

def mul_button():
    global f_num
    global math
    math = "*"
    f_num = float(e.get())
    e.delete(0, END)

def div_button():
    global f_num
    global math
    math = "/"
    f_num = float(e.get())
    e.delete(0, END)
def equal_button():
    second_number = float(e.get())
    e.delete(0, END)
    if math == "+":
        e.insert(0, f_num + second_number)
    elif math == "-":
        e.insert(0, f_num - second_number)
    elif math == "*":
        e.insert(0, f_num * second_number)
    elif math == "/":
        if second_number == 0:
            e.insert(0, "Error")
        else:
            e.insert(0, f_num / second_number)

button_brak1 = Button(root, text='(', padx=40, pady=20, command=lambda: button_click('('), border=3,bg='grey')
button_brak2 = Button(root, text=')', padx=40, pady=20, command=lambda: button_click(')'), border=3,bg='grey')
button_dot = Button(root, text='.', padx=43, pady=20, command=lambda: button_click('.'), border=3)
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click('1'), border=3)
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click('2'), border=3)
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click('3'), border=3)
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click('4'), border=3)
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click('5'), border=3)
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click('6'), border=3)
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click('7'), border=3)
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click('8'), border=3)
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click('9'), border=3)
button_0 = Button(root, text='0', padx=89, pady=20, command=lambda: button_click('0'), border=3)
button_clear = Button(root, text='C', padx=40, pady=20, command=clear_button, border=3, bg='grey')
button_equal = Button(root, text='=', padx=40, pady=20, command=equal_button, border=3,bg='orange')
button_sum = Button(root, text='+', padx=40, pady=20, command=sum_button, border=3,bg='orange')
button_sub = Button(root, text='-', padx=40, pady=20, command=sub_button, border=3,bg='orange')
button_mul = Button(root, text='*', padx=40, pady=20, command=mul_button, border=3,bg='orange')
button_div = Button(root, text='/', padx=40, pady=20, command=div_button, border=3,bg='orange')

button_brak1.grid(row=1, column=1)
button_brak2.grid(row=1, column=2)
button_dot.grid(row=5, column=2)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=0,columnspan=2)
button_clear.grid(row=1, column=0)
button_equal.grid(row=5, column=3)
button_sum.grid(row=4, column=3)
button_sub.grid(row=3, column=3)
button_mul.grid(row=2, column=3)
button_div.grid(row=1, column=3)

root.mainloop()
