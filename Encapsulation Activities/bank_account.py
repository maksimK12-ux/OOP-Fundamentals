class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

def get_account_number(self):
    return self.account_number

def get_balance(self):
    return self.balance

def get_owner_name(self):
    return self.owner_name

def set_account_number(self, new_number):
    if isinstance(new_number, int):
        self.account_number = new_number
    else:
        raise ValueError("Number must be integer")
    
def set_balance(self, new_balance):
    if isinstance(new_balance, int):
        self.balance = new_balance
    else:
        raise ValueError("Balance must be integer")

def set_owner_name(self, new_owner):
    if isinstance(new_owner, int):
        self.owner_name = new_owner
    else:
        raise ValueError("Name must be string")