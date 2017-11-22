from BANKACCOUNT import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate, minimum_balance,check_number = 0):
        BankAccount.__init__(self, account_number, balance, interest_rate, minimum_balance)
        self.__check_number = check_number

    def get_check_number(self):
        return self.__check_number

    def set_check_number(self, check_number):
        self.__check_number = check_number

    def write_check(self, check_amount):
        self.withdraw(check_amount)
        self.__check_number += 1



      #  BankAccount.set_balance(BankAccount.get_balance() - check_amount)

class ServiceChargeChecking(CheckingAccount):
    def __init__(self, account_number, balance, interest_rate, minimum_balance, check_limit, check_number = 0):
        CheckingAccount.__init__(self, account_number, balance, interest_rate, minimum_balance, check_number)
        self.__check_limit = check_limit

    def write_check(self, check_amount):
        if self.get_check_number() == self.__check_limit:
            print('You cannot write any more checks this month.')
        else:
            self.withdraw(check_amount)
            self.set_check_number(self.get_check_number()+1)


class NoServiceChargeChecking(CheckingAccount):
    def __init__(self, account_number, balance, interest_rate, minimum_balance):
        CheckingAccount.__init__(self, account_number, balance, interest_rate, minimum_balance)

class HighInterestChecking(NoServiceChargeChecking):
    def __init__(self, account_number, balance, interest_rate, minimum_balance):
        NoServiceChargeChecking.__init__(self, account_number, balance, interest_rate, minimum_balance)

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate, minimum_balance):
        BankAccount.__init__(self, account_number, balance, interest_rate, minimum_balance)

class HighInterestSavings(SavingsAccount):
    def __init__(self, account_number, balance, interest_rate, minimum_balance):
        SavingsAccount.__init__(self, account_number, balance, interest_rate, minimum_balance)

class CertificateOfDeposit(BankAccount):
    def __init__(self, account_number, balance, interest_rate, minimum_balance, maturity_month, current_month):
        BankAccount.__init__(self, account_number, balance, interest_rate, minimum_balance)
        self.__maturity_month = maturity_month
        self.__current_month = current_month

    def set_maturity_month(self, maturity_month):
        self.__maturity_month = maturity_month
    def get_maturity_month(self):
        return self.__maturity_month

    def set_current_month(self, current_month):
        self.__current_month = current_month
    def get_current_month(self):
        return self.__current_month

    def __str__(self):
        s = 'Account: {} Balance: {:<4.2f}, Minimum Balance: {:<6.2f}, Interest rate (%): {:<2.2f} Maturity Months: {:<2.0f}, Current Month: {:<2.0f}'
        return s.format(self.get_account_number(), self.get_balance(), self.get_minimum_balance(), self.get_interest_rate(), self.__maturity_month, self.__current_month)
        #s = 'account: {}, balance: {}, minimum balance {}, interest: {}'
        #return s.format(self.__account_number, self.__balance, self.__minimum_balance, self.__interest_rate)
