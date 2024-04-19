import json
import difflib
from difflib import get_close_matches


data = json.load(open("data.json"))

word = input("please type word here: ")

def Search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]                                                           #this line of code is for nouns like places that only appear in dictionary with capital letter. (added later)
    elif word.upper() in data:
        return data[word.upper()]                                                           #this line of code is for Acronyms like USA that only appear in dictionary in full caps.(added later)
    elif len(get_close_matches(word, data.keys(), cutoff = 0.75)) > 1:
        YN = input("did you mean %s ? If yes, press enter Y, if no, enter N: " % get_close_matches(word, data.keys(), cutoff = 0.75)[0]) # the [0] returns the first index of this list which will be the most matched word
        if YN == "Y":
            return data[get_close_matches(word, data.keys(), cutoff = 0.75)[0]]
        elif YN == "N":
            return "Sorry, that word does not exist, please try again."
        else:
            return "Input not recognised, please enter a new word and try again."      
    else:
        return "Word does not exist, please try again"
        

finaloutput = Search(word)

if type(finaloutput) == list:
    for items in finaloutput:
        print(items)
else:
    print(finaloutput)

# this last section here iterates through the multiple outputs for words with more than one definition. This is so a List isnt just printed for the user to see. This looks better.
