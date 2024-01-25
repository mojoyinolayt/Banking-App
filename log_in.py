import bcrypt
from db import my_database
a = my_database()
conn = a.connect()
mycursor = conn.cursor()

class log_in:
    def account_login(self):
        try:
            email = (str(input("email:")))
            password = (str(input("password:")))
            self.check_if_user_exist(email, password)
        except Exception as e:
             print(f"failed request: {e}")
    def check_if_user_exist(self, email, password):
        salt = bcrypt.gensalt()
        hashed_password  = bcrypt.hashpw(password.encode('utf-8'), salt)
        sql = "SELECT * FROM user WHERE email = %s"
        val = (email,)
        exec = mycursor.execute(sql, val)
        user = mycursor.fetchone()
        if user:
            print("WORLD BANK")
            print(user[4])
        else:
            print('user does not exist')            
create_account = log_in()
create_account.account_login()

