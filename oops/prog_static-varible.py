# withdrawal,deposit, balanceEnquery, createAcount
from datetime import datetime
class Bank:
    bank_name='SBI'
    def __init__(self,acno,person_name,min_balance):
        self.acno=acno
        self.personanme=person_name
        self.balance=min_balance


    def deposit(self,amount):
        self.balance=amount
        print(Bank.bank_name,'your account',self.acno,'has been credited with amount',amount ,'on',datetime.today(),'avalable bal',self.balance)

    def withdrawal(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print(Bank.bank_name,'your account', self.acno, 'has been debited with amount', amount, 'on', datetime.today(),
                  'avalable bal', self.balance)
        else:
            print("transaction cancelled with error code,because of insufficient balance")

    def balance_enq(self):
        print(self.balance)

person=Bank(100,'shaneeba',3000)

person.withdrawal(1000)