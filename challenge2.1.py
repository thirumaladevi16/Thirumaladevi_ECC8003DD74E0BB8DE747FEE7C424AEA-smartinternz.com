class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.account_number = account_number
    self.account_holder_name = account_holder_name
    self.account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.account_balance += amount
      print(f'Deposited Rs{amount}. New balance: Rs{self.account_balance}')
    else:
      raise ValueError(
          'Invalid deposit amount. Please deposit a positive amount.')

  def withdraw(self, amount):
    if amount > 0 and amount <= self.account_balance:
      self.account_balance -= amount
      print(f'Withdrew Rs{amount}. New balance: Rs{self.account_balance}')
    else:
      raise ValueError('Invalid withdrawal amount or insufficient balance.')

  def display_balance(self):
    print(
        f'Account balance for {self.account_holder_name} (Account {self.account_number}): Rs{self.account_balance}'
    )


# Example usage:
account = BankAccount(account_number='123456789',
                      account_holder_name='Anonymous',
                      initial_balance=5000.0)
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()
