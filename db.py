import mysql.connector
import random
import bcrypt
class  my_database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "mojoyin"
                
    def connect(self):
        try:
            return mysql.connector.connect(
                host = self.host,
                user = self.user,               
                password = self.password,
                database = self.database
            )
        except Exception as e:
            print(f"Not connected to database: {e}")  
    
        