import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "admin" and password == "password123":
        messagebox.showinfo("Login Success", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

def clear_fields():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

btn_login = tk.Button(root, text="Login", command=login)
btn_login.pack(pady=5)

btn_clear = tk.Button(root, text="Clear", command=clear_fields)
btn_clear.pack(pady=5)

root.mainloop()