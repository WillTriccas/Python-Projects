import sqlite3

def conn_and_create():
    connection = sqlite3.connect("Books.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS booktable (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    connection.commit()
    connection.close()

conn_and_create()

#THIS IS FOR THE ADD ENTRY BUTTON
def insert(title, author, year, isbn):
    connection = sqlite3.connect("Books.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO booktable VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    connection.commit()
    connection.close()


#THIS IS FOR THE VIEW ALL BUTTON
def view():
    connection = sqlite3.connect("Books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM booktable")
    rows = cursor.fetchall()
    connection.close()
    return rows


#THIS IS FOR THE SEARCH ENTRY BUTTON - blank default arguments are so error doesnt occur when all arguments arent entered
def search(title = "", author = "", year = "", isbn = ""):
    connection = sqlite3.connect("Books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM booktable WHERE title =? OR author =? OR year =? OR isbn =?",(title, author, year, isbn))
    rows = cursor.fetchall()
    connection.close()
    return rows

#THIS IS FOR THE UPDATE ENTRY BUTTON
def update(id, title, author, year, isbn):
    connection = sqlite3.connect("Books.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE booktable SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?" , (title, author, year, isbn, id))
    connection.commit()
    connection.close()

#THIS IS FOR THE DELETE ENTRY BUTTON
def delete(id):
    connection = sqlite3.connect("Books.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM booktable WHERE id=?" , (id, ))
    connection.commit()
    connection.close()

#insert("Astrophysics for people", "Neil deGrasse Tyson", 2017, 9780393609394)
#update(3,"Astrophysics for People in a Hurry", "Neil deGrasse Tyson", 2017, 9780393609394)
#delete(4)
#print(search(title = "Life 3.0"))
print(view())