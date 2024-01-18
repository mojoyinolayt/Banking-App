import random;
import sys;

class BankingSystem:
        def __init__(self):
        
            self.name = []
            self.email = []
            self.password = []
            self.re_enter_password = []
            self.account_number = []
    
        def main_welcom_screen(self):
                print(
                    "1. Create an account\n"
                    "2. Log into account\n"
                    "0. Exit"
                )
                selection_option = str(input("Select an option (1 or 2 or 3):"))
                if selection_option == "1":
                    self.create_account()
                if selection_option == "2":
                    self.account_login()
                if selection_option == "0":
                    print("\n")
                    return "Bye!"
                

        
        def create_account(self):
                    #username input
                    name = ((str)(input(" Name :")))

                    #email input
                    email = ((str)(input("Email :")))

                    #password input
                    password = ((str)(input("Password :")))

                    #re-enter password input
                    re_enter_password = ((str)(input("Re-enter password :")))

                    self.check_if_password_correct(password, re_enter_password)


                    #account number generator
                    account_number = random.randrange(10**9, 10**10)
            
                    # adding/appending the constructors into the arrays
                    self.name.append(name)
                    self.email.append(email)
                    self.password.append(password)
                    self.re_enter_password.append(re_enter_password)
                    self.account_number.append(account_number)

            
                    print("\n")     
                    print("Your account has been created")
                    print("Your account number:")
                    print(account_number)
                    print("Your account name:")
                    print(name)
                    print("Your email:")
                    print(email)
                    print("Your password:")
                    print(password)
                    print("\n")
                    self.main_welcom_screen()
        def account_login(self):
                    print("\n")
                    print("Enter your username:")
                    name = str(input())
            
                    print("Enter your Password:")
                    password = str(input())
            
                    if str(name) in self.name and str(password) in self.password:
                        print("\n")
                        print("Welcome")
                        print("WORLD BANK")
                        
                        # self.show_balance(self,user)
                        # self.deposit(self,user)
                        # self.withdraw(self,user)
                    else:
                        print("\n")
                        print("Wrong user inputs")
                        print("\n")
                        self.main_welcom_screen()

                # this is where the error was.
        # def account_balance(self):
        #              print("hello")
            
            # function to check if the password is the same
        def check_if_password_correct(self, password, re_enter_password):
            if password == re_enter_password:
                print("it is correct")
            else:
                print("incorrect password.")
                exit()
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


        
BankingSystem().main_welcom_screen()