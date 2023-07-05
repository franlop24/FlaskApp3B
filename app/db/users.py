from db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash

mydb = get_connection()

class User:

    def __init__(self, 
                 username, 
                 password,
                 first_name = '',
                 last_name = '',
                 email = '',
                 image = '',
                 role='',
                 id = None):
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.role = role
        self.image = image

    def save(self):
        # Create a New Object in DB
        if self.id is None:
            with mydb.cursor() as cursor:
                self.password = generate_password_hash(self.password)
                sql = "INSERT INTO users(username, password) VALUES(%s, %s)"
                val = (self.username, self.password)
                cursor.execute(sql, val)
                mydb.commit()
                self.id = cursor.lastrowid
                return self.id
        else:
            with mydb.cursor() as cursor:
                sql = 'UPDATE users SET first_name = %s, last_name = %s, email = %s, image = %s '
                sql += 'WHERE id = %s'
                val = (self.first_name, self.last_name, self.email, self.image, self.id)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM users WHERE id = { self.id }"
            cursor.execute(sql)
            mydb.commit()
            return self.id

    @staticmethod
    def __get__(id):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM users WHERE id = { id }"
            cursor.execute(sql)

            user = cursor.fetchone()

            if user:
                user = User(username=user["username"], #username
                            password=user["password"], #password
                            first_name=user["first_name"], #first_name
                            last_name=user["last_name"], #last_name
                            email=user["email"], #email
                            image=user["image"], #image
                            role=user["role"],
                            id=id)
                return user
            
            return None
    
    @staticmethod
    def get_by_password(username, password):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT id, username, password FROM users WHERE username = %s"
            val = (username,)
            cursor.execute(sql, val)
            user = cursor.fetchone()
            
            if user != None:
                if check_password_hash(user["password"], password):
                    return User.__get__(user["id"])
            return None

    @staticmethod
    def get_all():
        users = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM users"
            cursor.execute(sql)
            result = cursor.fetchall()
            for user in result:
                users.append(
                    User(username=user["username"],
                         password=user["password"],
                         email=user["email"],
                         first_name=user["first_name"],
                         last_name=user["last_name"],
                         role=user["role"],
                         id=user["id"])
                )
            return users

    def __str__(self):
        return f"{ self.username } { self.first_name } { self.last_name }"