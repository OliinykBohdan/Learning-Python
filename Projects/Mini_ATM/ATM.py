attempt_pin = 0
import sys

print('===== Welcome to the ATM =====')

# PIN authentication (max 3 attempts)
while attempt_pin < 3:
    pin = input('Please enter a pin: ')
    if pin == '1122':
        print('Access granted')
        break
    else:
        print('Pin not recognised')
        attempt_pin += 1

# Exit if authentication failed
if attempt_pin == 3:
    print('Access denied')
    sys.exit()


balance = 1000.0

# Main ATM menu loop
while True:
    print('\nChoose an option:\n1 - Check balance\n2 - Deposit\n3 - Withdraw\n4 - Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        print('Your balance: ' + str(balance))
    elif choice == '2':
        am_depos = float(input('Enter the amount to deposit: '))
        if am_depos <= 0:
            print('Amount must be positive.')
        else:
            balance += am_depos
            print('Deposit successful. Your new balance is: ' + str(balance))
    elif choice == '3':
        withdraw = float(input('Enter the withdrawal amount: '))
        if withdraw <= 0:
            print('Amount must be positive.')
        # Prevent overdraft
        elif balance < withdraw:
            print('Transaction failed: not enough balance.')
        else:
            balance -= withdraw
            print('Withdrawal successful. Your remaining balance is: ' + str(balance))
    elif choice == '4':
        print ('=== Thank you. Goodbye. ===')
        break
    else:
        print('Please enter a valid option.')
