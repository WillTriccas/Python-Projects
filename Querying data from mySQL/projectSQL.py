import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student" ,
password = "ardit700_student" , 
host = "108.167.140.122" , 
database = "ardit700_pm1database"
)

cursor = con.cursor()

query = cursor.execute("SELECT * FROM Dictionary ")

output = cursor.fetchall()

print(output)


# this is a basic outline of how to connect to a database and the variables needed to manipulate data within that database and use it within python
# this script when run will output the whole dictionary in one, to see a more specified version look at advanced version of file.