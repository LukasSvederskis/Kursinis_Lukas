import json
import os

class ATM:
    def __init__(self, name):
        self.name = name.strip()
        self.personal_balance, self.sharing_balance = self.load_current_balances()
        self.user_accounts = self.load_user_accounts()
        self.sharing_account = None

    def load_user_accounts(self):
        try:
            with open("user_accounts.json", 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_user_accounts(self):
        with open("user_accounts.json", 'w') as file:
            json.dump(self.user_accounts, file)

    def deposit(self, amount):
        self.personal_balance += amount
        self.log_transaction(f"{self.name} deposited ${amount} to personal account (Balance: ${self.personal_balance})")
        print("Deposit to personal account successful.")

    def withdraw(self, amount):
        if amount > self.personal_balance:
            print("Insufficient funds in personal account.")
        else:
            self.personal_balance -= amount
            self.log_transaction(f"{self.name} withdrew ${amount} from personal account (Balance: ${self.personal_balance})")

    def check_balance(self):
        if self.sharing_account:
            transaction = f"{self.name} checked balance (Personal Account Balance: ${self.personal_balance}), Sharing Account Balance: ${self.sharing_balance}"
            self.log_transaction(transaction)
            print(f"Personal Account Balance: ${self.personal_balance}, Sharing Account Balance: ${self.sharing_balance}")
        else:
            transaction = f"{self.name} checked balance (Personal Account Balance: ${self.personal_balance})"
            self.log_transaction(transaction)
            print(f"Personal Account Balance: ${self.personal_balance}")

    def create_sharing_account(self):
        if self.sharing_account:
            print("You are already in a sharing account.")
            return

        if self.name in self.user_accounts:
            print("You are already in a sharing account.")
            return

        users = []
        print("Write names of users who will share the account. Enter '0' to finish.")
        while True:
            name = input("Write name: ").strip()
            if name == '0':
                break
            elif name:
                if name == self.name:
                    print("You are already in this sharing account.")
                    continue
                for account_name, account_users in self.user_accounts.items():
                    if name in account_users.split(', '):
                        print(f"{name} is already in a sharing account with {account_name}.")
                        break
                else:
                    users.append(name)
        if not users:
            print("At least one user is required.")
            return

        user_list = ', '.join(users)
        self.sharing_account = SharingAccount(users)
        self.log_transaction(f"{self.name} just created sharing account. Users: {user_list}")
        self.user_accounts[self.name] = user_list
        self.save_user_accounts()

    def load_sharing_account(self):
        if self.name in self.user_accounts:
            users = self.user_accounts[self.name].split(', ')
            self.sharing_account = SharingAccount(users)
            self.sharing_balance = self.sharing_account.get_sharing_balance()
        else:
            for account_name, account_users in self.user_accounts.items():
                if self.name in account_users.split(', '):
                    users = account_users.split(', ')
                    self.sharing_account = SharingAccount(users)
                    self.sharing_balance = self.sharing_account.get_sharing_balance()
                    return
            self.sharing_account = None
            self.sharing_balance = 0

    def sharing_account_actions(self):
        while True:
            print("\nWhat would you like to do for the sharing account?")
            print("1. Deposit money to sharing account")
            print("2. Withdraw money from sharing account")
            print("3. Check balance of sharing account")
            print("4. Go back to main menu")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.deposit_to_sharing_account()
            elif choice == '2':
                self.withdraw_from_sharing_account()
            elif choice == '3':
                print(f"Sharing account balance is: ${self.sharing_balance}")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    def deposit_to_sharing_account(self):
        try:
            amount = float(input("Enter the amount to deposit: $"))
            self.sharing_account.deposit(amount)
            self.sharing_balance += amount
            self.log_transaction(f"{self.name} deposited ${amount} to sharing account (Balance: ${self.sharing_balance})")
            print("Deposit to sharing account successful.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the deposit amount.")

    def withdraw_from_sharing_account(self):
        try:
            amount = float(input("Enter the amount to withdraw: $"))
            if amount > self.sharing_balance:
                print("Insufficient funds in sharing account.")
            else:
                self.sharing_account.withdraw(amount)
                self.sharing_balance -= amount
                self.log_transaction(f"{self.name} withdrew ${amount} from sharing account (Balance: ${self.sharing_balance})")
        except ValueError:
            print("Invalid input. Please enter a valid number for the withdrawal amount.")

    def log_transaction(self, transaction):
        with open("kita.txt", 'a') as file:
            file.write(transaction.strip() + "\n")

    def load_current_balances(self):
        personal_balance = 0
        sharing_balance = 0
        if not os.path.exists("kita.txt"):
            return personal_balance, sharing_balance
        
        with open("kita.txt", 'r') as file:
            for line in file:
                if line.strip().startswith(self.name):
                    parts = line.strip().split()
                    if "personal" in line:
                        balance_str = parts[-1][1:-1]  # Extracting balance from the last part of the line
                        try:
                            personal_balance = float(balance_str)
                        except ValueError:
                            pass
                    elif "sharing" in line:
                        balance_str = parts[-1][1:-1]  # Extracting balance from the last part of the line
                        try:
                            sharing_balance = float(balance_str)
                        except ValueError:
                            pass
        return personal_balance, sharing_balance

class SharingAccount:
    def __init__(self, users):
        self.users = users

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass
    
    def get_sharing_balance(self):
        # Load the sharing balance from the file or database
        sharing_balance = 0
        with open("kita.txt", 'r') as file:
            for line in file:
                if "sharing" in line:
                    parts = line.strip().split()
                    try:
                        sharing_balance = float(parts[-1][1:-1])
                    except ValueError:
                        pass
        return sharing_balance

def main():
    # Welcome message
    print("Welcome to the ATM Finance Tracker!")

    # Ask for the user's name
    name = input("Please enter your name: ")
    atm = ATM(name)
    atm.load_sharing_account()

    # Main menu
    while True:
        print("\nWhat would you like to do?")
        print("1. Deposit money to personal account")
        print("2. Withdraw money from personal account")
        print("3. Check balance of personal account")
        print("4. Create sharing account")
        print("5. Deposit, withdraw, or check balance for sharing account")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                atm.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number for the deposit amount.")
        elif choice == '2':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                atm.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number for the withdrawal amount.")
        elif choice == '3':
            atm.check_balance()
        elif choice == '4':
            atm.create_sharing_account()
        elif choice == '5':
            if atm.sharing_account:
                atm.sharing_account_actions()
            else:
                print("No sharing account exists. Please create one.")
        elif choice == '6':
            print("Thank you for using the ATM Finance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()