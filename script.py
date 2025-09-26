# imports
import tkinter as tk
from tkinter import messagebox

# import functions from data_manager
from data_manager import signup, login, get_account, load_accounts, save_accounts


#variables
username = ""
name = ""
balance = 0.0
receiver = ""
amount = 0.0

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

# mainmenu
def show_main_menu(user):
    # clears login widgets
    for widget in root.winfo_children():
        widget.destroy()
    # setting frame
    menu_frame = tk.Frame(root, bg="#f5f6fa")
    menu_frame.pack(expand=True)
    # greeting
    greeting = tk.Label(menu_frame, text=f"Hello, {user['name']}!", font=("Arial", 16))
    greeting.pack(pady=10)
    # show balance
    global balance_label
    balance_label = tk.Label(menu_frame, text=f"Balance: {user['balance']}", font=("Arial", 14))
    balance_label.pack(pady=10)
    # top up button
    topup_button = tk.Button(menu_frame, text="Top Up 100", command=topup)
    topup_button.pack(pady=10)

# top up 100
def topup():
    global balance
    user = get_account(username)
    balance = user['balance'] + 100
    accounts = load_accounts()
    accounts[username] = {
        **accounts[username],
        'balance': balance
    }
    # refresh balance
    save_accounts(accounts)
    balance_label.config(text=f"Balance: {balance}")

# root (always take you to login)
root = tk.Tk()
root.title("PayAja - Log In")
root.geometry("400x300")
root.configure(bg="#f5f6fa")

login_frame = tk.Frame(root, bg="#f5f6fa")
login_frame.pack(expand=True)

logintitle_label = tk.Label(
    login_frame, text="PayAja - Log In",
    font=("Arial", 20, "bold"),
    bg="#f5f6fa", fg="#273c75"
)
logintitle_label.pack(pady=(10, 20))

username_label = tk.Label(login_frame, text="Username", font=("Arial", 12), bg="#f5f6fa")
username_label.pack(anchor="w", padx=10)
username_entry = tk.Entry(login_frame, font=("Arial", 12), width=25)
username_entry.pack(padx=10, pady=(0, 10))

password_label = tk.Label(login_frame, text="Password", font=("Arial", 12), bg="#f5f6fa")
password_label.pack(anchor="w", padx=10)
password_entry = tk.Entry(login_frame, show="*", font=("Arial", 12), width=25)
password_entry.pack(padx=10, pady=(0, 20))

login_button = tk.Button(
    login_frame, text="Login", command=auth_login,
    font=("Arial", 12), bg="#44bd32", fg="white", width=20
)
login_button.pack(pady=(0, 10))

signup_label = tk.Label(
    login_frame, text="Don't have an account yet?", font=("Arial", 10), bg="#f5f6fa"
)
signup_label.pack()
signup_button = tk.Button(
    login_frame, text="Sign Up", command=signup_window,
    font=("Arial", 10), bg="#40739e", fg="white", width=15
)
signup_button.pack(pady=(0, 10))

# start
root.mainloop()


def mainmenu():
    print("Welcome to PayAja")
    print("Your Balance:")
    print("Balance")
    print("1. Transfer")
    print("2. History")
    print("3. Top Up")

