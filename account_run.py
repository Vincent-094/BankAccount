import accounts
from accountsF import *
def main():
    #print('Enter the following data: ')
    #account_number = input('Account number: ')
    #balance = input('Balance: ')
    #interest_rate = input('Interest rate: ')
    #minimum_balance = input('Minimum balance: ')


#no interest, and no minimum balance
    SC_checking_object = accounts.ServiceChargeChecking(1, 1000, 0, 0)
#interest, checks, min balance
    NSC_checking_object = accounts.NoServiceChargeChecking(2, 1000, 1, 100)
#high interest and higher min balance.
    HighInterest_checking_object = accounts.HighInterestChecking(3, 1000, 2, 200)
#pays interest
    Savings_object = accounts.SavingsAccount(4, 1000, 1, 0)
#higher interest savings, also minimum balance
    High_savings_object = accounts.HighInterestSavings(5, 1000, 2, 100)
#account_number, balance, interest_rate, minimum_balance, maturity_month, current_month
#it has instance variables to store the number of CD maturity months, interest rate, and the current CD month.
    CD_object = accounts.CertificateOfDeposit(6, 1000, 5, 0, 60, 30)

    action = menu()
    account = submenu()
    amount = int(input('What is the amount? '))
    if action == 1 and account == 1:
        money(action,amount, SC_checking_object)
    elif action == 2 and account == 1:
        money(action,amount, SC_checking_object)
    elif action == 3 and account == 1:
        counter = 0
        while counter <= 5:
            if counter > 5:
                print('You have exceeded the check writing limits for this month.')
            counter += 1
            money(action,amount, SC_checking_object)
            action = menu()

    elif action == 1 and account == 2:
        money(action, amount, NSC_checking_object)
    elif action == 2 and account == 2:
        money(action,amount, NSC_checking_object)
    elif action == 3 and account == 2:
        money(action,amount, NSC_checking_object)

    elif action == 1 and account == 3:
        money(action, amount, HighInterest_checking_object)
    elif action == 2 and account == 3:
        money(action,amount, HighInterest_checking_object)
    elif action == 3 and account == 3:
        money(action,amount, HighInterest_checking_object)

    elif action == 1 and account == 4:
        money(action, amount, Savings_object)
    elif action == 2 and account == 4:
        money(action,amount, Savings_object)

    elif action == 1 and account == 5:
        money(action, amount, High_savings_object)
    elif action == 2 and account == 5:
        money(action,amount, High_savings_object)

    elif action == 1 and account == 6:
        money(action, amount, CD_object)
    elif action == 2 and account == 6:
        money(action,amount, CD_object)

    print()
    print(SC_checking_object)
    print(NSC_checking_object)
    print(HighInterest_checking_object)
    print(Savings_object)
    print(High_savings_object)
    print(CD_object)
    print()

main()
