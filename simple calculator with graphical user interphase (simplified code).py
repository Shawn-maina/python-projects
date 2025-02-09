import tkinter as tk  

root = tk.Tk()
root.config(bg="#333333")

calculations = ""

def add_to_calculations(symbol):
    global calculations
    calculations += symbol
    T_entry.delete(0, tk.END)
    T_entry.insert(0, calculations)

def calculate():
    global calculations
    try:
        calculations = str(eval(calculations))
        T_entry.delete(0, tk.END)
        T_entry.insert(0, calculations)
    except ZeroDivisionError:
        T_entry.delete(0, tk.END)
        T_entry.insert(0, "Error: Division by zero")
        calculations = ""
    except Exception:
        T_entry.delete(0, tk.END)
        T_entry.insert(0, "Error!")
        calculations = ""

def clear():
    global calculations
    calculations = ""
    T_entry.delete(0, tk.END)

T_entry = tk.Entry(root, font=("arial", 18), width=15, bd=5, relief="ridge")
T_entry.grid(row=0, columnspan=4, sticky="news")

buttons = [
    ('C', clear, "orange"), ('%', lambda: add_to_calculations("%"), "grey"),
    ('/', lambda: add_to_calculations("/"), "grey"), ('*', lambda: add_to_calculations("*"), "grey"),
    ('7', lambda: add_to_calculations("7"), "light grey"), ('8', lambda: add_to_calculations("8"), "light grey"),
    ('9', lambda: add_to_calculations("9"), "light grey"), ('-', lambda: add_to_calculations("-"), "grey"),
    ('4', lambda: add_to_calculations("4"), "light grey"), ('5', lambda: add_to_calculations("5"), "light grey"),
    ('6', lambda: add_to_calculations("6"), "light grey"), ('+', lambda: add_to_calculations("+"), "grey"),
    ('1', lambda: add_to_calculations("1"), "light grey"), ('2', lambda: add_to_calculations("2"), "light grey"),
    ('3', lambda: add_to_calculations("3"), "light grey"), ('(', lambda: add_to_calculations("("), "grey"),
    ('0', lambda: add_to_calculations("0"), "light grey"), ('.', lambda: add_to_calculations("."), "grey"),
    (')', lambda: add_to_calculations(")"), "grey"), ('=', calculate, "orange")
]

row_val, col_val = 1, 0
for text, cmd, color in buttons:
    button = tk.Button(root, text=text, command=cmd, font=("arial", 14), bd=1, width=6, background=color)
    button.grid(row=row_val, column=col_val, sticky="news")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
