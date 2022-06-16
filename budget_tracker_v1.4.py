# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 09:44:56 2022

@author: Muhamad Hafizul
"""

class Budget_Tracker:
    def __init__(self):
        self.source_income_dict = {}
        self.source_expense_dict = {}
        self.total_income = 0
        self.total_expense = 0
        self.balance = 0
        
    def set_income(self,i_source,income):
        income = int(income)
        self.source_income_dict |= {i_source:income}
        
    def set_expense(self,e_source,expense):
        expense = int(expense)
        self.source_expense_dict |= {e_source:expense}
        
    def get_income_list(self):
        print(f"{'Income source': <20} |{'Income value': <20} ")
        print("-"*40)
        for income in self.source_income_dict:
            print(f"{income: <20} |RM {self.source_income_dict[income]: <20}")
        print("\n")
            
    def get_expense_list(self):
        print(f"{'Expense source': <20} |{'Expense list': <20} ")
        print("-"*40)
        for expense in self.source_expense_dict:
            print(f"{expense: <20} |RM {self.source_expense_dict[expense]: <20}")
        print("\n")
    
    def get_total_income(self):
        for income in self.source_income_dict:
            self.total_income = (self.total_income 
                                + self.source_income_dict[income])
        print(f"Total income: RM {self.total_income}\n")
        
    def get_total_expense(self):
        for expense in self.source_expense_dict:
            self.total_expense = (self.total_expense 
                                  + self.source_expense_dict[expense])
        print(f"Total expense: RM {self.total_expense}\n")
    
    def set_balance(self):
        self.balance = self.total_income - self.total_expense
        
    def get_balance(self):
        print(f"The balance: RM {self.balance}")

#Test Run            
hafizul = Budget_Tracker()
hafizul.set_income("Salary",1980)
hafizul.set_income("Parent",200)
hafizul.get_income_list()
hafizul.get_total_income()
hafizul.set_expense("Rent",450)
hafizul.set_expense("Pant",600)
hafizul.set_expense("Ticket",250)
hafizul.set_expense("Food",400)
hafizul.set_expense("Shopee",250)
hafizul.get_expense_list()
hafizul.get_total_expense()
hafizul.set_balance()
hafizul.get_balance()