from BANKACCOUNT import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate, minimum_balance):
        BankAccount.__init__(self, account_number, balance, interest_rate, minimum_balance)

    def write_check(self, check_amount):
        self.__balance = self.__balance - check_amount

    #def __str__(self):
        #s = 'account: {}, balance: {}, minimum balance {}, interest: {}'
        #return s.format(self.__account_number, self.__balance, self.__minimum_balance, self.__interest_rate)
        #return 'For the '+ str(self.__account_number) +\
        #'your balance is ' + str(self.__balance) +\
        #'your interest is ' + str(self.__interest_rate) +\
        #'with a minimum balance of ' + str(self.__minimum_balance)

class ServiceChargeChecking(CheckingAccount):
    def __init__(self, account_number, balance, interest_rate, minimum_balance):
        CheckingAccount.__init__(self, account_number, balance, interest_rate, minimum_balance)
    #def __str__(self):
        #s = 'account: {}, balance: {}, minimum balance {}, interest: {}'
        #return s.format(self.__account_number, self.__balance, self.__minimum_balance, self.__interest_rate)

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
