# imports
import tkinter as tk
from tkinter import messagebox

# import functions from data_manager
from data_manager import signup, login, get_account, load_accounts, save_accounts


#variables
balance = float(0)

# functions
def add_100():
    global balance
    balance += 100
    balancelabel.config(text=f"Balance: {balance}")


# login screen
login = tk.Tk()
login.title("PayAja - Log In")
login.geometry("400x300")

logintitle_label = tk.Label(login, text="PayAja - Log In")

username_label = tk.Label(login, text="Username")
username_entry = tk.Entry(login)

password_label = tk.Label(login, text="Password")
password_entry = tk.Entry(login, show="*")

login_button = tk.Button(login, text="Login", command=login)

signup_label = tk.Label(login, text="Don't have an account yet?")
signup_button = tk.Button(login, text="Sign Up", command=signup)

#signup screen

# packs
logintitle_label.pack()
username_entry.pack()
password_entry.pack()
login_button.pack()
signup_button.pack()

# start
login.mainloop()


def mainmenu():
    print("Welcome to PayAja")
    print("Your Balance:")
    print("Balance")
    print("1. Transfer")
    print("2. History")
    print("3. Top Up")

