# imports
import tkinter as tk
from tkinter import messagebox


#variables
balance = float(0)

# functions

def validate_login():
    userid = username_entry.get()
    password = password_entry.get()
    
def add_100():
    global balance
    balance += 100
    balancelabel.config(text=f"Balance: {balance}")


# tkinter root settings
root = tk.Tk()
root.title("PayAja")
root.geometry("400x300")

# root elements
label = tk.Label(root, text="Welcome to PayAja")
button = tk.Button(root, text="Click Me", command=add_100)
balancelabel = tk.Label(root, text=f"Balance: {balance}")

# packs
label.pack()
button.pack()
balancelabel.pack()

# start
root.mainloop()


def mainmenu():
    print("Welcome to PayAja")
    print("Your Balance:")
    print("Balance")
    print("1. Transfer")
    print("2. History")
    print("3. Top Up")

