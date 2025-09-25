# imports
import tkinter as tk
from tkinter import messagebox

# import functions from data_manager
from data_manager import signup, login, get_account, load_accounts, save_accounts


#variables
username = ""
name = ""
balance = 0.0

# functions |
#           V            

# signup window popup
def signup_window():
    signup_win = tk.Toplevel(root)
    signup_win.title("Sign Up")
    signup_win.geometry("300x250")

    tk.Label(signup_win, text="Username").pack()
    username_entry = tk.Entry(signup_win)
    username_entry.pack()

    tk.Label(signup_win, text="Password").pack()
    password_entry = tk.Entry(signup_win, show="*")
    password_entry.pack()

    tk.Label(signup_win, text="Name").pack()
    name_entry = tk.Entry(signup_win)
    name_entry.pack()

    # logic for signup (used for button)
    def submit_signup():
        username = username_entry.get()
        password = password_entry.get()
        name = name_entry.get()
        if not username or not password or not name:
            messagebox.showerror("Error", "All fields are required.")
            return
        if signup(username, password, name):
            messagebox.showinfo("Success", "Account created! You can now log in.")
            signup_win.destroy()
        else:
            messagebox.showerror("Error", "Username already exists.")
    
    tk.Button(signup_win, text="Sign Up", command=submit_signup).pack(pady=10)

# logic for login (used for button)
def auth_login():
    global username, name, balance
    userid = username_entry.get()
    password = password_entry.get()
    accounts = load_accounts()
    if userid not in accounts:
        messagebox.showerror("Login Failed", "Username does not exist.")
        return
    user = login(userid, password)
    if user is None:
        messagebox.showerror("Login Failed", "Incorrect password.")
        return
    username = userid
    name = user['name']
    balance = user['balance']
    show_main_menu(user)

# mainmenu (clears login widgets)
def show_main_menu(user):
    for widget in root.winfo_children():
        widget.destroy()
    # greeting
    greeting = tk.Label(root, text=f"Hello, {user['name']}!", font=("Arial", 16))
    greeting.pack(pady=10)
    # show balance
    global balancelabel
    balancelabel = tk.Label(root, text=f"Balance: {user['balance']}", font=("Arial", 14))
    balancelabel.pack(pady=10)
    # top up button
    topup_button = tk.Button(root, text="Top Up 100", command=topup)
    topup_button.pack(pady=10)

# top up 100
def topup():
    global balance
    balance += 100
    accounts = load_accounts()
    accounts[username] = {
        **accounts[username],
        'balance': balance
    }
    save_accounts(accounts)
    balancelabel.config(text=f"Balance: {balance}")

# root (always take you to login)
root = tk.Tk()
root.title("PayAja - Log In")
root.geometry("400x300")

logintitle_label = tk.Label(root, text="PayAja - Log In")

username_label = tk.Label(root, text="Username")
username_entry = tk.Entry(root)

password_label = tk.Label(root, text="Password")
password_entry = tk.Entry(root, show="*")

login_button = tk.Button(root, text="Login", command=auth_login)

signup_label = tk.Label(root, text="Don't have an account yet?")
signup_button = tk.Button(root, text="Sign Up", command=signup_window)

# packs
logintitle_label.pack()
username_entry.pack()
password_entry.pack()
login_button.pack()
signup_button.pack()

# start
root.mainloop()


def mainmenu():
    print("Welcome to PayAja")
    print("Your Balance:")
    print("Balance")
    print("1. Transfer")
    print("2. History")
    print("3. Top Up")

