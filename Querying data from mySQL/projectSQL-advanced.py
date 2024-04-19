# THIS IS THE  SAME SCRIPT AS THE Dictionary Program, however, all of the data is retrieved from a database and is not directly stored within Python

import mysql.connector
import difflib
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student" ,
password = "ardit700_student" , 
host = "108.167.140.122" , 
database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("Please enter a word you wish to search for: ").lower()

def Search(word):
   
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)    
    results = cursor.fetchall()

    if results:
        return results
        # dont need to do an elif for upper and lowercase letters in words and SQL isnt case sensitive
    else:
        query = cursor.execute("SELECT * FROM Dictionary")
        results = cursor.fetchall()
        list_of_expressions = [item[0] for item in results]
        
        similar_word = get_close_matches(word, list_of_expressions, cutoff = 0.75)

        if len(similar_word) > 0:

            YN = input("did you mean '%s' ? if yes, please type Y, if not, please type N" % similar_word[0])
        
            if YN.upper() == "YES" or "Y":
                query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % similar_word[0])
                results = cursor.fetchall()
                return results
            elif YN.upper() == "NO" or "N":
                return "Sorry, we cant find your word, please try typing it again"
            else:
                return "Sorry, we didnt understand that, please try typing your word again"
        else:
            return "Sorry, we could not find the word you were looking for, please try again"

output = Search(word)    

if type(output) == list:
    for item in output:
        print(item[1])
else:
    print(output[1])

            

        



    

      


    