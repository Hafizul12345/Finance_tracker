# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 09:44:56 2022

@author: Muhamad Hafizul
"""
#import essential library
from decimal import * #for accuracy and presicion of currency calculation
import matplotlib.pyplot as plt #visualize data
import numpy as np
import pickle

#constant for quantize() method for fixed decimal point
TWOPLACE = Decimal(10) ** -2 #Decimal(0.01)

class Budget_Tracker:
    def __init__(self,username = "0"):
        self.username = username
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
        
#-----------------------------------------------------------------------------------
      
    def set_income(self,i_source = '000',income = 0):
        #function to update income(s) 
        stop = False
        for key in self.source_income_dict:
            if key == '0' and self.source_income_dict[key] == 0:
                self.source_income_dict = {}
        while stop == False:
            if i_source == '000' and income == 0:
                i_source = input("\nPlease enter your income source (ex: salary, bonus, etc):\n")
                income = input("Please enter your income value(RM):\n")
                
            try:
                income = int(income)
                income = Decimal(income).quantize(TWOPLACE)
                self.source_income_dict |= {i_source:income}
                stop = True
            except (TypeError,ValueError) as e:
                i_source = '000'
                income = 0
                print("Invalid income value!\n")
                continue

    def set_total_income(self):
        #function to calculate total income
        self.set_total_income = 0
        for income in self.source_income_dict:
            self.total_income = self.total_income + self.source_income_dict[income]
    
    def set_expense(self,e_source = '000',expense = 0):
        #function to update expense(s)
        stop = False
        for key in self.source_expense_dict:
            if key == '0' and self.source_expense_dict[key] == 0:
                self.source_expense_dict = {}
        while stop == False:
            if e_source == '000' and expense == 0:
                e_source = input("\nPlease enter your expense source (ex: rent, food, etc):\n")
                expense = input("Please enter your expense value(RM):\n")
            try:
                expense = int(expense)
                expense = Decimal(expense).quantize(TWOPLACE)
                self.source_expense_dict |= {e_source:expense}
                stop = True
            except (TypeError,ValueError) as e:
                e_source = '000'
                expense = 0
                print("Invalid input!\n")
                continue      
  
    def set_total_expense(self):
        #calculate total expense
        self.total_expense = 0
        for expense in self.source_expense_dict:
            self.total_expense = self.total_expense + self.source_expense_dict[expense]
    
    def set_balance(self):
        #calculate balance
        self.balance = self.total_income - self.total_expense
        if self.balance < 0:
            self.balance = 0
#--------------------------------------------------------------------
    def get_income_list(self):
        #display income and total income in 'tabulated' form
        print("*"*40)
        print(f"{'Income(s)': <20} |{'Value': <20}")
        for income in self.source_income_dict:
            print(f"{income: <20} |RM {self.source_income_dict[income]: <20}")
        print("-"*40)
        print(f"{'Total income': <20} |RM {self.total_income: <20}")
        print(f"{'*'*40}\n")
        
    def get_expense_list(self):
        #display expense and total expense in 'tabulated' form
        print("*"*40)
        print(f"{'Expense(s)': <20} |{'Value': <20}")
        for expense in self.source_expense_dict:
            print(f"{expense: <20} |RM {self.source_expense_dict[expense]: <20}")
        print("-"*40)
        print(f"{'Total expense': <20} |RM {self.total_expense: <20}")
        print(f"{'*'*40}\n")
        
    def get_balance(self):
        #display total income, total expense and balance
        print("*"*40)
        print(f"{'Total income': <20} |RM {self.total_income: <20}")
        print(f"{'Total expense': <20} |RM {self.total_expense: <20}")
        print("-"*40)
        print(f"{'Total balance': <20} |RM {self.balance: <20}")
        print(f"{'*'*40}\n")

#---------------------------------------------------------------------   
    def pie_chart(self):
        #to make income, expense, and overall pie chart
        self.income_label = []
        self.income_value = []
        for label in self.source_income_dict:
            self.income_label.append(label)
            self.income_value.append(int(self.source_income_dict[label]))

        x = []
        for i in range(0,len(self.source_income_dict)):
            x.append(0.01)
        
        #plot income pie chart
        plt.subplot(2,2,1)

        #figure_1 = plt.figure(1)
        plt.title("Income Percentage")
        plt.pie(
            self.income_value,
            labels=self.income_label, #label of value
            startangle=90, #the start angle is at 90deg (start at 12 o'clock)
            explode=x, #seperate from pie centre by dictated length (each value for each segment)
            autopct= '%1.1f%%' #display percentage via string formatting
            )
        #Put source and value from dict into seperate list because pie cannot accept dict
        self.expense_label = [] #to make sure list do not append duplicate
        self.expense_value = [] #to make sure list do not append duplicate
        for label in self.source_expense_dict:
            self.expense_label.append(label)
            self.expense_value.append(int(self.source_expense_dict[label]))

        #this is to make variable number of segment can be 'explode'
        x = []
        for i in range(0,len(self.source_expense_dict)):
            x.append(0.01) #explode size of 0.01

        #plot expense pie
        plt.subplot(2,2,2) #figure is 2x2, at position 2 (x=2,y=1)
        plt.title("Expenses Percentage")
        plt.pie(
            self.expense_value,
            labels=self.expense_label, #label of value
            startangle=90, #the start angle is at 90deg (start at 12 o'clock)
            explode=x, #seperate from pie centre by dictated length (each value for each segment)
            autopct= '%1.1f%%' #display percentage via string formatting
            )

        #variable for overall pie
        self.overall_value = [] #to make sure duplicate do not append.exist
        self.overall_value.append(self.total_expense)
        self.overall_value.append(self.balance)

        #plot for overall pie
        plt.subplot(2,2,3)
        plt.title("Total Percentage")
        plt.pie(
            self.overall_value,
            labels=self.overall_label,
            startangle=90,
            explode=[0.01,0.01],
            autopct='%1.1f%%'
        )

        plt.show()
        #plt.show can only used once, to generate 2 or more figures simultaneously, plt.show() at the end only
    
#---------------------------------------------------------------------------------------------
    def save_data(self): #save function for when user not exist yet
        if not self.source_expense_dict: #if there is no expense data, store expense as {0:0}
            self.source_expense_dict = {'0':0} #to avoid error when action(3)
        if not self.source_income_dict: #if there is no income data, store income as {0:0}
            self.source_income_dict = {'0':0} #to avoid error when action(3)
        self.data_base = [self.username,self.source_income_dict,self.source_expense_dict]
        try:
            with open("finance_tracker_data","rb") as save_file:
                data = pickle.load(save_file)
            print(f"this is data (save_data) {data}")
            user_exist = True
            
        except (EOFError,FileNotFoundError) as e:
            user_exist = False

        if user_exist == False:
            with open("finance_tracker_data","ab") as save_file:
                pickle.dump(self.data_base,save_file)
        elif user_exist == True:
            self.rewrite_save_file() #save function for when user already exist

    def rewrite_save_file(self): #save function for when user already exist
        temp_data_list = []
        
        with open("finance_tracker_data","rb") as save_file:
            while True:
                try:
                    data = pickle.load(save_file)
                    temp_data_list.append(data)
                except EOFError:
                    break
            #pickle only pickle one at a time 
            #ex: if there are several list,pickleload only pickle one list
        
        num = len(temp_data_list)
        matching_user = False
        for x in range(num):
            print(temp_data_list[x])
            if self.username == temp_data_list[x][0]:
                temp_data_list[x] = self.data_base
                matching_user = True

        if matching_user == False:
            temp_data_list.append(self.data_base)
        
        num = len(temp_data_list)

        with open("finance_tracker_data","wb") as save_file:
            for x in range(num):
                pickle.dump(temp_data_list[x],save_file)

#Test Run #########################################################################

#initialise user-------------------------------------------------
username = input("Hello, what is your name?\n")
user = Budget_Tracker(username)

def load_user_data(): 
    #load user data if there is any
    temp_data_list = []
    with open("finance_tracker_data","rb") as save_file:
        while True:
            try:
                data = pickle.load(save_file)
                temp_data_list.append(data)
            except EOFError:
                break
    for x in range(len(temp_data_list)):
        if user.username == temp_data_list[x][0]:
            user.source_income_dict = temp_data_list[x][1]
            user.source_expense_dict = temp_data_list[x][2]
            user.set_total_income()
            user.set_total_expense()
            user.set_balance()
        
def input_promt(): 
    #ask if user want to continue set_input()
    promt = "y"
    while promt != "n":
        promt = input("\nDo you want to add another income?[y/n]\n")
        if promt == "y":
            user.set_income()
            user.set_total_income()
            user.set_balance()
            user.save_data()
        elif promt == "n":
            break
        else:
            print("Invalid input!!\n")

def expense_promt(): 
    #in case user need to continue to add expense(s)
    promt = "y"
    while promt != "n":
        promt = input("\nDo you want to add another expense?[y/n]\n")
        if promt == "y":
            user.set_expense()
            user.set_total_expense()
            user.set_balance()
            user.save_data()
        elif promt == "n":
            break
        else:
            print("Invalid input!!!\n")

def action(): #User choose what to do
    action_promt = 0 #trigger to stay in while loop
    while action_promt ==0:
        print("\n\n~~~FINANCIAL TRACKER~~~\n\n")
        print("[1]Update income\n[2]Update expense\n[3]Show financial stat\n[4]Quit\n")
        action_promt = input("What do you want to do?[1/2/3/4]\n")
        
        if action_promt == "1":
            #to update the income(s)
            user.set_income()
            user.set_total_income()
            user.set_balance()
            user.save_data()
            input_promt()
            action_promt = 0 #to stay in loop after 'action'

        elif action_promt == "2":
            #to update the expenses
            user.set_expense()
            user.set_total_expense()
            user.set_balance()
            user.save_data()
            expense_promt()
            action_promt = 0 #to stay in loop after 'action'
        
        elif action_promt == "3":
            #to display income,expense, total and balance, to display pie chart
            user.get_income_list()
            user.get_expense_list()
            user.get_balance()

            user.pie_chart()
         
            action_promt = 0 #to stay in loop after 'action'

        elif action_promt == "4":
            print("\nProgram closed successfully\n")
            break
        else:
            print("Invalid input!")
            action_promt = 0

load_user_data() #if user have data saved, load the user data
action() #call function in which user choose what to do
