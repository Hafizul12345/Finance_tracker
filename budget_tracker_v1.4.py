# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 09:44:56 2022

@author: Muhamad Hafizul
"""

from decimal import *
TWOPLACE = Decimal(10) ** -2

class Budget_Tracker:
    def __init__(self):
        self.source_income_dict = {}
        self.source_expense_dict = {}
        self.total_income = Decimal(0.00).quantize(TWOPLACE)
        self.total_expense = Decimal(0.00).quantize(TWOPLACE)
        self.balance = Decimal(0.00).quantize(TWOPLACE)
        
    def set_income(self,i_source,income):
        income = Decimal(income).quantize(TWOPLACE)
        self.source_income_dict |= {i_source:income}
        
    def set_expense(self,e_source,expense):
        expense = Decimal(expense).quantize(TWOPLACE)
        self.source_expense_dict |= {e_source:expense}
    
    def set_total_income(self):
        for income in self.source_income_dict:
            self.total_income = (self.total_income 
                                + self.source_income_dict[income])
        
    def set_total_expense(self):
        for expense in self.source_expense_dict:
            self.total_expense = (self.total_expense 
                                  + self.source_expense_dict[expense])
            #print(self.total_expense)
    
    def set_balance(self):
        self.balance = self.total_income - self.total_expense

#Test Run            
hafizul = Budget_Tracker()

hafizul.set_income("Salary",1980)
hafizul.set_income("Parent",200)

print(f"{'Income(s)': <20} |{'Value': <20}")
for income in hafizul.source_income_dict:
    print(f"{income: <20} |RM {hafizul.source_income_dict[income]: <20}")
print("")

hafizul.set_total_income()
print(f"{'Total income': <20} :RM {hafizul.total_income}\n")

hafizul.set_expense("Rent",450)
hafizul.set_expense("Pant",600)
hafizul.set_expense("Ticket",250)
hafizul.set_expense("Food",400)
hafizul.set_expense("Shopee",250)

print(f"{'Expense(s)': <20} |{'Value': <20}")
for expense in hafizul.source_expense_dict:
    print(f"{expense: <20} |RM {hafizul.source_expense_dict[expense]: <20}")
print("")

hafizul.set_total_expense()
print(f"{'Total expense': <20} :RM {hafizul.total_expense}\n")

hafizul.set_balance()
print(f"{'Total balance': <20} :RM {hafizul.balance}")
