import mysql.connector
import random
import bcrypt

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="mojoyin"
)
mycursor = mydb.cursor()

sql = "INSERT INTO user (name,email,password,account_number,account_bal) VALUES (%s,%s,%s,%s,%s)"
account_number = random.randrange(10**9, 10**10)
password = "peter"
password = password.encode('utf-8')
hashedPwd = bcrypt.hashpw(password, bcrypt.gensalt())
val = ("peter","peter",hashedPwd,account_number,"500")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
