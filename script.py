# imports
import tkinter as tk
from tkinter import messagebox
from camera import QRscanner

# import functions from data_manager
from data_manager import signup, login, get_account, load_accounts, save_accounts, transaction, topup


#variables
username = ""
name = ""
balance = 0.0
receiver = ""
amount = 0.0
password = ""

# functions |
#           V            

# signup window popup
def signup_window():
    # signup window setup
    signup_win = tk.Toplevel(root)
    signup_win.title("PayAja - Sign Up")
    signup_win.geometry("300x300")
    signup_win.configure(bg="#f5f6fa")
    frame = tk.Frame(signup_win, bg="#f5f6fa")
    frame.pack(expand=True, fill="both")
    # signup title
    tk.Label(frame, text="Sign Up", font=("Arial", 20, "bold"), bg="#f5f6fa", fg="#273c75").pack(pady=(15, 20))

    tk.Label(frame, text="Username", font=("Arial", 12), bg="#f5f6fa").pack(anchor="w", padx=20)
    username_entry = tk.Entry(frame, font=("Arial", 12), width=25)
    username_entry.pack(padx=20, pady=(0, 10))

    tk.Label(frame, text="Password", font=("Arial", 12), bg="#f5f6fa").pack(anchor="w", padx=20)
    password_entry = tk.Entry(frame, show="*", font=("Arial", 12), width=25)
    password_entry.pack(padx=20, pady=(0, 10))

    tk.Label(frame, text="Name", font=("Arial", 12), bg="#f5f6fa").pack(anchor="w", padx=20)
    name_entry = tk.Entry(frame, font=("Arial", 12), width=25)
    name_entry.pack(padx=20, pady=(0, 20))

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
    
    tk.Button(frame, text="Sign Up", command=submit_signup, font=("Arial", 12), bg="#44bd32", fg="white", width=20).pack(pady=10)

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
    root.title("PayAja - Main Menu")
    # clears login widgets
    for widget in root.winfo_children():
        widget.destroy()
    # setting frame
    menu_frame = tk.Frame(root, bg="#f5f6fa")
    menu_frame.pack(expand=True, fill="both")
    # greeting
    greeting = tk.Label(menu_frame, text=f"Hello, {user['name']}!", font=("Arial", 18, "bold"), bg="#f5f6fa", fg="#273c75")
    greeting.pack(pady=(30, 10))
    # show balance
    global balance_label
    balance_label = tk.Label(menu_frame, text=f"Balance: {user['balance']}", font=("Arial", 14), bg="#f5f6fa")
    balance_label.pack(pady=(0, 20))
    # top up button
    topup_button = tk.Button(menu_frame, text="Top Up", command=topup_window, font=("Arial", 12), bg="#44bd32", fg="white", width=20)
    topup_button.pack(pady=10)
    # transfer button
    transfer_button = tk.Button(menu_frame, text="Transfer", command=transfer_window, font=("Arial", 12), bg="#40739e", fg="white", width=20)
    transfer_button.pack(pady=10)

def transfer_window():
    #setup transfer frame
    transfer_win = tk.Toplevel(root)
    transfer_win.title("PayAja - Transfer Funds")
    transfer_win.geometry("350x300")
    transfer_win.configure(bg="#f5f6fa")
    frame = tk.Frame(transfer_win, bg="#f5f6fa")
    frame.pack(expand=True, fill="both")
    #trasnfer title
    transfer_title = tk.Label(frame, text="Transfer Funds", font=("Arial", 18, "bold"), bg="#f5f6fa", fg="#273c75")
    transfer_title.pack(pady=(20, 20))
    #receiver entry
    tk.Label(frame, text="Receiver Username", font=("Arial", 12), bg="#f5f6fa").pack(anchor="w", padx=20)
    receiver_entry = tk.Entry(frame, font=("Arial", 12), width=25)
    receiver_entry.pack(padx=20, pady=(0, 10))
    #amount entry
    tk.Label(frame, text="Amount", font=("Arial", 12), bg="#f5f6fa").pack(anchor="w", padx=20)
    amount_entry = tk.Entry(frame, font=("Arial", 12), width=25)
    amount_entry.pack(padx=20, pady=(0, 20))
    def scan_qr():
        user = QRscanner()
        receiver_entry.insert(0, user)
    #submit button
    def submit_transfer():
        global balance
        receiver = receiver_entry.get()
        #validate amount data type
        try:
            amount = float(amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")
            return
        #validate ammount positive
        if amount <= 0:
            messagebox.showerror("Error", "Amount must be positive.")
            return
        #show success message
        success, msg = transaction(username, receiver, amount)
        if success:
            messagebox.showinfo("Success", msg)
            #refresh balance
            user = get_account(username)
            global balance_label
            balance_label.config(text=f"Balance: {user['balance']}")
            show_main_menu(user)
        else:
            messagebox.showerror("Error", msg)
        transfer_win.destroy()

    #QR scanner button
    tk.Button(transfer_win, text="Use QR Scanner", command=scan_qr, font=("Arial", 12), bg="#44bd32", fg="white", width=20).pack(pady=10)
    #submit button
    tk.Button(frame, text="Submit", command=submit_transfer, font=("Arial", 12), bg="#40739e", fg="white", width=20).pack(pady=10)

# top up
def topup_window():
    # setup topup frame
        topup_win = tk.Toplevel(root)
        topup_win.title("PayAja - Top Up Funds")
        topup_win.geometry("350x300")
        topup_win.configure(bg="#f5f6fa")
        frame = tk.Frame(topup_win, bg="#f5f6fa")
        frame.pack(expand=True, fill="both")
        # topup title
        topup_title = tk.Label(frame, text="Top Up Funds", font=("Arial", 18, "bold"), bg="#f5f6fa", fg="#273c75")
        topup_title.pack(pady=(20, 20))
        # amount entry
        tk.Label(frame, text="Top Up Amount", font=("Arial", 12), bg="#f5f6fa").pack(anchor="w", padx=20)
        amount_entry = tk.Entry(frame, font=("Arial", 12), width=25)
        amount_entry.pack(padx=20, pady=(0, 10))
        # password entry
        tk.Label(frame, text="Password", font=("Arial", 12), bg="#f5f6fa").pack(anchor="w", padx=20)
        password_entry = tk.Entry(frame, show="*", font=("Arial", 12), width=25)
        password_entry.pack(padx=20, pady=(0, 20))

        def submit_topup():
            global balance
            try:
                amount = float(amount_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid amount.")
                return
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be positive.")
                return
            pwd = password_entry.get()
            user = get_account(username)
            if user['password'] != pwd:
                messagebox.showerror("Error", "Incorrect password.")
                return
            success, msg = topup(username, amount)
            if success:
                balance = get_account(username)['balance']
                balance_label.config(text=f"Balance: {balance}")
                messagebox.showinfo("Success", msg)
                topup_win.destroy()
                show_main_menu(get_account(username))
            else:
                messagebox.showerror("Error", msg)
        #submit button
        tk.Button(frame, text="Submit", command=submit_topup, font=("Arial", 12), bg="#44bd32", fg="white", width=20).pack(pady=10)

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