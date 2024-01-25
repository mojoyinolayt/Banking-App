import bcrypt
from db import my_database
import random
a = my_database()
conn = a.connect()
mycursor = conn.cursor()

class Reg:
    def create_account (self):
        name = (str(input("name :")))
        email = (str(input("email :")))
        check_email = self.check_if_email_is_taken(email)
        
        if check_email:
            print("email is already taken")
            return
           
        password = (str(input("password :")))
        re_enter_password = (str(input("re_enter_password :")))
        try:
            self.confirm_password(password,re_enter_password)
            self.save_to_db(name,email,password)
            print("user saved")
        except Exception as e:
            print(f"user not saved: {e}")
        
    def confirm_password (self, password, re_enter_password):
        if password == re_enter_password:
            print("password match")
        else:
            print("incorrect password")
            
    def save_to_db(self, name, email, password):
        sql = "INSERT INTO user (name, email, password, account_number, account_bal) VALUES (%s, %s, %s, %s, %s)"
        account_number = random.randrange(10**9, 10**10)
        account_bal = 0
        salt = bcrypt.gensalt()
        hashed_password  = bcrypt.hashpw(password.encode('utf-8'), salt)
        val = (name, email, hashed_password, account_number, account_bal)
        mycursor.execute(sql, val)
        conn.commit()
        
    def check_if_email_is_taken(self, email):
        try:
            sql = "SELECT * FROM user WHERE email = %s"
            val = (email,)
            exec = mycursor.execute(sql, val)
            return mycursor.fetchone()
        except Exception as e:
            print(f"error : {e}")
            
registration = Reg()
registration.create_account()
