class Reg:
    def create_account (self):
         name = (str(input("name :")))
         email = (str(input("email :")))
         password = (str(input("email :")))
         re_enter_password = (str(input("re_enter_password :")))
         self.confirm_password(password,re_enter_password)
         
    def confirm_password (self, password, re_enter_password):
        if password == password:
            print("password match")
        else:
            print("incorrect password")
registration = Reg()
registration.create_account()
    
    
   