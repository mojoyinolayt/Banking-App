class Reg:
    def __init__(self, name,email,password,re_enter_password)
        self.name = name
        self.email = email
        self.password = password
        self.re_enter_password = re_enter_password
    # def __str__(self):
    #     return(
    #             F"name : ((str)(input(" name :")))/n
    #             "email = ((str)(input("email :"))/n)"
    #             "password = ((str)(input("password :")))/n"
    #             "re_enter_password = ((str)(input("re-enter password :")))/n"      
    def create_account:
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