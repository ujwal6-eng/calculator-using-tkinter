from tkinter import *

# Global expression variable to store the sequence of inputs
expression = ""

# Function to handle button presses and update the expression
def press(key):
    global expression
    expression += str(key)
    display_var.set(expression)

# Function to evaluate the current expression and display the result
def equal():
    global expression
    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = ""
    except:
        display_var.set("error")
        expression = ""

# Function to clear the current expression
def clear():
    global expression
    expression = ""
    display_var.set("")

# Main GUI code
root = Tk()
root.configure(bg="light green")
root.title("Simple Calculator")
root.geometry("270x150")

display_var = StringVar()
entry = Entry(root, textvariable=display_var)
entry.grid(columnspan=4, ipadx=70)

# Number buttons
Button(root, text='1', command=lambda: press(1), height=1, width=7).grid(row=2, column=0)
Button(root, text='2', command=lambda: press(2), height=1, width=7).grid(row=2, column=1)
Button(root, text='3', command=lambda: press(3), height=1, width=7).grid(row=2, column=2)
Button(root, text='4', command=lambda: press(4), height=1, width=7).grid(row=3, column=0)
Button(root, text='5', command=lambda: press(5), height=1, width=7).grid(row=3, column=1)
Button(root, text='6', command=lambda: press(6), height=1, width=7).grid(row=3, column=2)
Button(root, text='7', command=lambda: press(7), height=1, width=7).grid(row=4, column=0)
Button(root, text='8', command=lambda: press(8), height=1, width=7).grid(row=4, column=1)
Button(root, text='9', command=lambda: press(9), height=1, width=7).grid(row=4, column=2)
Button(root, text='0', command=lambda: press(0), height=1, width=7).grid(row=5, column=0)

# Operator buttons
Button(root, text='+', command=lambda: press('+'), height=1, width=7).grid(row=2, column=3)
Button(root, text='-', command=lambda: press('-'), height=1, width=7).grid(row=3, column=3)
Button(root, text='', command=lambda: press(''), height=1, width=7).grid(row=4, column=3)
Button(root, text='/', command=lambda: press('/'), height=1, width=7).grid(row=5, column=3)

# Misc buttons
Button(root, text='=', command=equal, height=1, width=7).grid(row=5, column=2)
Button(root, text='Clear', command=clear, height=1, width=7).grid(row=5, column=1)
Button(root, text='.', command=lambda: press('.'), height=1, width=7).grid(row=6, column=0)

root.mainloop()