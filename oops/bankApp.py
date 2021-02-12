# withdrawal,deposit, balanceEnquery, createAcount
from datetime import datetime
class Bank:
    def create_acount(self,acno,person_name,min_balance,bank_name):
        self.acno=acno
        self.personanme=person_name
        self.balance=min_balance
        self.bankname=bank_name

    def deposit(self,amount):
        self.balance=amount
        print('your account',self.acno,'has been credited with amount',amount ,'on',datetime.today(),'avalable bal',self.balance)

    def withdrawal(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print('your account', self.acno, 'has been debited with amount', amount, 'on', datetime.today(),
                  'avalable bal', self.balance)
        else:
            print("transaction cancelled with error code,because of insufficient balance")

    def balance_enq(self):
        print(self.balance)

person=Bank()
person.create_acount(100,'shaneeba',3000,'SBI')
person.withdrawal(5000)