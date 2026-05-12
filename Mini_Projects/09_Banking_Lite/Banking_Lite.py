class Account:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance
        self.history = []

    def show_balance(self):
        print(35 * '=', f'{self.username}, your account balance is:', self.balance, 35 * '=', sep='\n')

    def transfer(self, recipient_account, amount):
        if amount <= 0:
            print('\nThe sum must be positive.')
            return

        if amount > self.balance:
            print(f'\nThe amount cannot be greater than the balance.\nYour account balance is: {self.balance}.')
            return

        self.balance -= amount
        recipient_account.balance += amount

        self.history.append(f'Transferred {amount} to {recipient_account.username}')
        recipient_account.history.append(f'Received {amount} from {self.username}')

    def show_history(self):
        if not self.history:
            print(f'\nYour transaction history is empty.')
            return

        print(35 * '~', f'\n{self.username}, your transaction history:')
        for operation in self.history:
            print(operation)

account1 = Account('Bohdan', 1000)
account2 = Account('Victoria', 1500)

account1.show_balance()
account2.show_balance()

account1.transfer(account2, 100)
account1.transfer(account2, 900)

account1.show_balance()
account2.show_balance()

account1.show_history()
account2.show_history()
