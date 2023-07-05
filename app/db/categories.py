from .db import get_connection

mydb = get_connection()

class Category:

    def __init__(self, category, description, id=None):
        self.id = id
        self.category = category
        self.description = description

    def save(self):
        # Create a New Object in DB
        if self.id is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO categories(category, description) VALUES(%s, %s)"
                val = (self.category, self.description)
                cursor.execute(sql, val)
                mydb.commit()
                self.id = cursor.lastrowid
                return self.id
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE categories SET category = %s, description = %s WHERE id = %s"
                val = (self.category, self.description, self.id)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM categories WHERE id = { self.id }"
            cursor.execute(sql)
            mydb.commit()
            return self.id
            
    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT category, description FROM categories WHERE id = { id }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            category = Category(result["category"], result["description"], id)
            return category
        
    @staticmethod
    def get_all():
        categories = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id, category, description FROM categories"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                categories.append(Category(item["category"], item["description"], item["id"]))
            return categories
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id) FROM categories"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id } - { self.category }"