# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 09:44:56 2022

@author: Muhamad Hafizul
"""
#import essential library
from decimal import * #for accuracy and presicion of currency calculation
import matplotlib.pyplot as plt #visualize data
import numpy as np

#constant for quantize() method for fixed decimal point
TWOPLACE = Decimal(10) ** -2 #Decimal(0.01)

class Budget_Tracker:
    def __init__(self,):
        self.source_income_dict = {} #list of all income source and value
        self.source_expense_dict = {} #list of all expenses and value
        self.total_income = Decimal(0.00).quantize(TWOPLACE) #total income
        self.total_expense = Decimal(0.00).quantize(TWOPLACE) #total expense
        self.balance = Decimal(0.00).quantize(TWOPLACE) #end balance
        self.income_label = []
        self.income_value = []
        self.expense_label = []
        self.expense_value = []
        self.overall_label = ['Total expenses','Balance']
        self.overall_value = []
        self.data_base = []

    #input income and append    
    def set_income(self,i_source,income):
        income = Decimal(income).quantize(TWOPLACE)
        self.source_income_dict |= {i_source:income}

    #input expense and append    
    def set_expense(self,e_source,expense):
        expense = Decimal(expense).quantize(TWOPLACE)
        self.source_expense_dict |= {e_source:expense}
    
    #calculate total income
    def set_total_income(self):
        for income in self.source_income_dict:
            self.total_income = (self.total_income 
                                + self.source_income_dict[income])

    #calculate total expense    
    def set_total_expense(self):
        for expense in self.source_expense_dict:
            self.total_expense = (self.total_expense 
                                  + self.source_expense_dict[expense])
    
    #calculate balance
    def set_balance(self):
        self.balance = self.total_income - self.total_expense

    def pie_income(self):
        for label in self.source_income_dict:
            self.income_label.append(label)
            self.income_value.append(int(self.source_income_dict[label]))

        x = []
        for i in range(0,len(self.source_income_dict)):
            x.append(0.01)
        
        #plot a pie chart
        figure_1 = plt.figure(1)
        plt.pie(
            self.income_value,
            labels=self.income_label, #label of value
            startangle=90, #the start angle is at 90deg (start at 12 o'clock)
            explode=x, #seperate from pie centre by dictated length (each value for each segment)
            autopct= '%1.1f%%' #display percentage via string formatting
            )

    def pie_expense(self):
        #Put source and value from dict into seperate list because pie cannot accept dict
        for label in self.source_expense_dict:
            self.expense_label.append(label)
            self.expense_value.append(int(self.source_expense_dict[label]))

        #this is to make variable number of segment can be 'explode'
        x = []
        for i in range(0,len(self.source_expense_dict)):
            x.append(0.01) #explode size of 0.01

        #plot a pie chart
        figure_2 = plt.figure(2)
        plt.pie(
            self.expense_value,
            labels=self.expense_label, #label of value
            startangle=90, #the start angle is at 90deg (start at 12 o'clock)
            explode=x, #seperate from pie centre by dictated length (each value for each segment)
            autopct= '%1.1f%%' #display percentage via string formatting
            )

    def pie_overall(self):
        self.overall_value.append(self.total_expense)
        self.overall_value.append(self.balance)
        figure_3 = plt.figure(3)
        plt.pie(
            self.overall_value,
            labels=self.overall_label,
            startangle=90,
            explode=[0.01,0.01],
            autopct='%1.1f%%'
        )
        plt.show()
        #plt.show can only used once, to generate 2 or more figures simultaneously, plt.show() at the end only

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

hafizul.pie_income()
hafizul.pie_expense()
hafizul.pie_overall()
