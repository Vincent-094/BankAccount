class BankAccount:
    def __init__(self, account_number, balance, interest_rate, minimum_balance):
        self.__account_number = account_number
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__minimum_balance = minimum_balance

    def set_account_number(self, account_number):
        self.__account_number = account_number
    def set_balance(self, balance):
        self.__balance = balance
    def set_interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate
    def set_mininum_balance(self, minimum_balance):
        self.__minimum_balance = minimum_balance

    def get_account_number(self):
        return self.__account_number
    def get_balance(self):
        return self.__balance
    def get_interest_rate(self):
        return self.__interest_rate
    def get_minimum_balance(self):
        return self.__minimum_balance

    def deposit(self, amount):
        self.set_balance((self.get_balance() + amount)*(1+self.__interest_rate/100))
    def withdraw(self, amount):
        if self.__balance - amount < 0:
            print('You cannot withdraw more than you have in the account')
        else:
            self.__balance = self.__balance - amount

    def __str__(self):
        #return 'For the '+str(self.__account_number)+' your balance is: ' + str(self.__balance)
        s = 'account: {}, balance: {:4d}, minimum balance {:3d}, interest rate(%): {:2d}'
        return s.format(self.__account_number, self.__balance, self.__minimum_balance, self.__interest_rate)
