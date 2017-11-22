def menu():
    print('Welcome')
    print('Select an option')
    print('1. Withdraw')
    print('2. Deposit')
    print('3. Write a check from checking accounts')
    option = int(input())
    return option

def money(option, amount, objectName):
    if option == 1:
        objectName.withdraw(amount)
    elif option == 2:
        objectName.deposit(amount)
    elif option == 3:
        objectName.write_check(amount)

def submenu():
    print('Which account would you like to use:')
    print('1. Service Charge Checking Account')
    print('2. No Service Charge Checking Account')
    print('3. High Interest Checking Account')
    print('4. Savings Account')
    print('5. High Interest Savings Account')
    print('6. Certificate of Deposit')

    suboption = int(input())
    return suboption
