import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("Books.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS booktable (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.connection.commit()
        



    #THIS IS FOR THE ADD ENTRY BUTTON
    def insert(self,title, author, year, isbn):
        self.cursor.execute("INSERT INTO booktable VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        self.connection.commit()
        


    #THIS IS FOR THE VIEW ALL BUTTON
    def view(self):
        self.cursor.execute("SELECT * FROM booktable")
        rows = self.cursor.fetchall()
        return rows


    #THIS IS FOR THE SEARCH ENTRY BUTTON - blank default arguments are so error doesnt occur when all arguments arent entered
    def search(self,title = "", author = "", year = "", isbn = ""):
        self.cursor.execute("SELECT * FROM booktable WHERE title =? OR author =? OR year =? OR isbn =?",(title, author, year, isbn))
        rows = self.cursor.fetchall()
        return rows

    #THIS IS FOR THE UPDATE ENTRY BUTTON
    def update(self,id, title, author, year, isbn):
        self.cursor.execute("UPDATE booktable SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?" , (title, author, year, isbn, id))
        self.connection.commit()
        

    #THIS IS FOR THE DELETE ENTRY BUTTON
    def delete(self,id):
        self.cursor.execute("DELETE FROM booktable WHERE id=?" , (id, ))
        self.connection.commit()
        
    def __del__(self):
        self.connection.close()

