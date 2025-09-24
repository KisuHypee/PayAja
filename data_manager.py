# imports
import json
import os

# define data file path
data_file = os.path.join(os.path.dirname(__file__), '../accounts.json')

# load data file
def load_accounts():
    if not os.path.exists(data_file):
        return {}
    with open(data_file, 'r') as file:
        return json.load(file)

# save accounts for signup
def save_accounts(accounts):
    with open(data_file, 'w') as file:
        json.dump(accounts, file)

# signup function
def signup(username, password, name):
    accounts = load_accounts()
    if username in accounts:
        return False
    accounts[username] = {
        'password': password,
        'name': name,
        'balance': 0.0
    }
    save_accounts(accounts)
    return True

# login function
def login(username, password):
    accounts = load_accounts()
    if username in accounts and accounts[username]['password'] == password:
        return accounts[username]
    return None

# load account data
def get_account(username):
    accounts = load_accounts()
    return accounts.get(username)