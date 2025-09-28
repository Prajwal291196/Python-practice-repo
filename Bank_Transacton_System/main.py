# # Bank Transaction System:
# # Allow deposit, withdrawal, check balance
# # Handle insufficient funds
# # Maintain transaction history
'''
class BankAccount:
    def __init__(self,initial_balance=0, transaction_history=None, account_number=None, account_name=None):
        self.balance = initial_balance
        self.transaction_history = transaction_history if transaction_history is not None else []
        self.account_number = account_number
        self.account_name = account_name
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount:.2f}")
            print(f"✅ Deposit successful: ${amount:.2f}")
        else:
            print("❌ Deposit amount must be positive.")
            
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew: ${amount:.2f}")
                print(f"✅ Withdrawal successful: ${amount:.2f}")
            else:
                print("❌ Insufficient funds for withdrawal.")
        else:
            print("❌ Withdrawal amount must be positive.")
    
    def check_balance(self):
        print(f"💰 Current balance: ${self.balance:.2f}")
        return self.balance
    
    def print_transaction_history(self):
        if self.transaction_history:
            print("📜 Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")
            
    def set_account_details(self, account_number, account_name):
        self.account_number = account_number
        self.account_name = account_name
        print(f"Account details set: {self.account_name} (Account No: {self.account_number})")
    
if __name__ == "__main__":
    # Example usage
    account = BankAccount(initial_balance=100.0)
    account.set_account_details("123456789", "John Doe")
    
    account.check_balance()
    account.deposit(50.0)
    account.withdraw(30.0)
    account.withdraw(150.0)  # Should show insufficient funds
    account.print_transaction_history()
    
    account.check_balance()  # Check balance after transactions
'''
import json
from datetime import datetime
import os


class BankAccount:
    def __init__(self, initial_balance=0, account_number=None, account_name=None, data_file="bank_account.json"):
        self.balance = initial_balance
        self.transaction_history = []
        self.account_number = account_number
        self.account_name = account_name
        self.data_file = data_file
        try:
            self.load_account()
        except Exception as e:
            print(f"Error loading account data: {e}")

    # ---------------- HELPER FUNCTIONS ----------------
    def _record_transaction(self, action, amount):
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.transaction_history.append(f"{timestamp} - {action}: ${amount:.2f}")
            self.save_account()
        except Exception as e:
            print(f"Error recording transaction: {e}")

    def _validate_amount(self, amount):
        if not isinstance(amount, (int, float)):
            print("❌ Amount must be a number.")
            return False
        if amount <= 0:
            print("❌ Amount must be greater than zero.")
            return False
        return True

    # ---------------- MAIN OPERATIONS ----------------
    def deposit(self, amount):
        try:
            if not self._validate_amount(amount):
                return False
            self.balance += amount
            self._record_transaction("Deposited", amount)
            print(f"✅ Deposit successful: ${amount:.2f}")
            return True
        except Exception as e:
            print(f"Error during deposit: {e}")
            return False

    def withdraw(self, amount):
        try:
            if not self._validate_amount(amount):
                return False
            if amount <= self.balance:
                self.balance -= amount
                self._record_transaction("Withdrew", amount)
                print(f"✅ Withdrawal successful: ${amount:.2f}")
                return True
            else:
                print("❌ Insufficient funds for withdrawal.")
                return False
        except Exception as e:
            print(f"Error during withdrawal: {e}")
            return False

    def check_balance(self):
        try:
            print(f"💰 Current balance: ${self.balance:.2f}")
            return self.balance
        except Exception as e:
            print(f"Error checking balance: {e}")
            return None

    def print_transaction_history(self):
        try:
            if self.transaction_history:
                print("📜 Transaction History:")
                for transaction in self.transaction_history:
                    print(transaction)
            else:
                print("No transactions yet.")
        except Exception as e:
            print(f"Error printing transaction history: {e}")

    def set_account_details(self, account_number, account_name):
        try:
            self.account_number = account_number
            self.account_name = account_name
            print(f"Account details set: {self.account_name} (Account No: {self.account_number})")
            self.save_account()
        except Exception as e:
            print(f"Error setting account details: {e}")

    # ---------------- FILE HANDLING ----------------
    def save_account(self):
        try:
            data = {
                "account_number": self.account_number,
                "account_name": self.account_name,
                "balance": self.balance,
                "transaction_history": self.transaction_history
            }
            with open(self.data_file, "w") as f:
                json.dump(data, f, indent=4)
        except (OSError, json.JSONDecodeError) as e:
            print(f"Error saving account data: {e}")

    def load_account(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    self.account_number = data.get("account_number")
                    self.account_name = data.get("account_name")
                    self.balance = data.get("balance", 0)
                    self.transaction_history = data.get("transaction_history", [])
                print("📂 Account data loaded successfully.")
            except (OSError, json.JSONDecodeError) as e:
                print(f"Error loading account data: {e}")
        else:
            print("No existing account file found. Starting fresh.")


if __name__ == "__main__":
    try:
        account_two = BankAccount(initial_balance=120.0)
        account_two.set_account_details("123456789", "John Cena")

        account_two.check_balance()
        account_two.deposit(50.0)
        account_two.withdraw(30.0)
        account_two.withdraw(150.0)  # Should show insufficient funds
        account_two.print_transaction_history()
        account_two.check_balance()
    except Exception as e:
        print(f"An error occurred in the main execution: {e}")