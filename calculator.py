# Inspired by https://youtu.be/oq3lJdhnPp8
from tkinter import *

root = Tk()

# Create an entry gui and place it on a grid
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=8, padx=10, pady=10)


def button_click(number):  # Number is the button input
    current = e.get()
    e.delete(0, END)  # Clear
    e.insert(0, str(current) + str(number))  # Insert previous input and new input


def button_clear():
    e.delete(0, END)  # Clear


def button_add():
    first_num = e.get()  # Get first number
    global f_num  # Global num
    global math  # Another variable
    math = "addition"
    f_num = float(first_num)  # Global num is equal to float of first num
    e.delete(0, END)  # Clear


def button_subtract():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_num)
    e.delete(0, END)


def button_multiply():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_num)
    e.delete(0, END)


def button_divide():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_num)
    e.delete(0, END)


def button_decimal():
    current = e.get()
    e.delete(0, END)  # Clear
    e.insert(0, str(current) + ".")  # Get previous input and input a decimal point at the end


def button_equal():
    second_num = e.get()  # get second number and store into second_num
    e.delete(0, END)

    if math == "addition":  # If we are adding, then first it adds both numbers and puts a value into variable answer
        answer = f_num+float(second_num)
        if answer.is_integer():  # If answer is a integer, then convert from float to integer
            answer = int(answer)
        e.insert(0, answer)  # Output answer!
    elif math == "subtraction":
        answer = f_num - float(second_num)
        if answer.is_integer():
            answer = int(answer)
        e.insert(0, answer)
    elif math == "multiplication":
        answer = f_num * float(second_num)
        if answer.is_integer():
            answer = int(answer)
        e.insert(0, answer)
    elif math == "division":
        answer = f_num / float(second_num)
        if answer.is_integer():
            answer = int(answer)
        e.insert(0, answer)


# Create button gui... 16 in total (0-9 have a lamba calling button_click)
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_clr = Button(root, text="AC", padx=35, pady=20, command=button_clear)
button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)
button_decimal = Button(root, text=".", padx=41, pady=20, command=button_decimal)
button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="x", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)


# ***** GRID DISPLAY *******
# ROW 4
button_clr.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_decimal.grid(row=4, column=2)
button_equal.grid(row=4, column=3)
button_add.grid(row=4, column=4)
# ROW 3
button_1.grid(row=3, column=1)
button_2.grid(row=3, column=2)
button_3.grid(row=3, column=3)
button_subtract.grid(row=3, column=4)
# ROW 2
button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)
button_multiply.grid(row=2, column=4)
# ROW 1
button_7.grid(row=1, column=1)
button_8.grid(row=1, column=2)
button_9.grid(row=1, column=3)
button_divide.grid(row=1, column=4)

root.mainloop()
