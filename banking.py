import random;
import sys;

print("WORLD BANK")

class BankingSystem:
        def __init__(self):
            self.users = []
    
        def main_welcom_screen(self):
            print(
                "1. Create an account\n"
                "2. Log into account\n"
                "0. Exit"
            )
            selection_option = int(input(("Input: ")))
            if selection_option == 1:
                self.reg()
            elif selection_option == 2:
                self._login()
            else:
                print("\n")
                return "Bye!"
            
                
        def reg(self):
           
        def add_user(self,name, email, password):
            account_number = random.randrange(10**9, 10**10)
            account_balance = 0
            new_user = {'name':name, 'email':email, 'password':password, 'account_number':account_number, 'account_balance': account_balance,}
            self.users.append(new_user)
            
            # question = input(("Do you want to sign in:?"))
            # print(question)
            # if (question == 'yes'):
            #     print("you are logged in!")
            # else:
            #     sys.exit()
         
            email = ((str)(input("Email :")))
            password = ((str)(input(" Password :")))
            
            self.about()
           
        # def check_if_user_exist(self, email, password):
        def _login(self):
            if len(self.users) == 0:
                print("no user found")
            else :  
                for user in self.users:
                    if user["email"] == email and user["password"] == password:
                        print("You are logged in !!!")
                        print("Account Number: ", user["account_number"])
                        self.show_balance(user)
                        self.deposit(user)
                        self.withdraw(user)
                    else: 
                        print("Incorrect details")
                        
        def check_if_user_exist(email, password):
             for user in self.users:
                if user["email"] == email and user["password"] == password:
                    print("you are logged in")
                    print("Account Number: ", user['account_number'])
                    show_balance(user)
                    deposit(user)
                    withdraw(user)
                else:
                    print("incorrect details")
           
        def check_if_password_correct(self,password, re_enter_password):
           if password == re_enter_password:
            print("You have successfully created an account                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ")
           else:
             print("incorrect password.")
             
             
        def show_balance(self,user):
                print(user["account_balance"])
                question = (input("Do you want to make a withdrawal?"))
                x = "question"
                print(question)
                if (question =="yes"):
                     print("continue")
                else:
                       sys.exit()
          
        def deposit(self,user):
            amount = int(input("enter deposit amount :"))
            user["account_balance"] += amount
            print("Acount Balance: ", user["account_balance"])
        def withdraw(self,user):
            amount = int(input("enter withdrawal amount :"))
            user["account_balance"] -= amount
            print("Account Balance:", user["account_balance"])

        def about(self):
            print("==================")
            print("World bank")
            print('version 2.0')
            print("===================")
        def address(self):
            print("112 AVENUE,NEW YORK.")      
# about()
# address()
print(BankingSystem().main_welcom_screen())



