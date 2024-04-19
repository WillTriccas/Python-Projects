from tkinter import *
from Backend1 import Database

database = Database()

def get_selected_row(event):
    try:
        global selected_row
        index = List1.curselection()[0]
        selected_row = List1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_row[1])
        e2.delete(0,END)
        e2.insert(END,selected_row[2])
        e3.delete(0,END)
        e3.insert(END,selected_row[3])
        e4.delete(0,END)
        e4.insert(END,selected_row[4])
    except IndexError :
        pass

# Whenever the user pressed on the empty list box, the code 'List1.bind('<<ListboxSelect>>', get_selected_row)' was called, in turn using this above function
# To eliminate this error, we have added a try and except block - if the user clicks on the empty Listbox and the 'IndexError' is thrown, 'pass' will be executed, which means do nothing, hence the error is dealt with
    
def delete_command():
    database.delete(selected_row[0])

def update_command():
    database.update(selected_row[0],Title_Text.get(), Author_Text.get(), Year_Text.get(), ISBN_Text.get())

def view_command():
    List1.delete(0,END)
    for row in database.view():
        List1.insert(END, row)

def search_command():
    List1.delete(0,END)
    for row in database.search(Title_Text.get(), Author_Text.get(), Year_Text.get(), ISBN_Text.get()):
        List1.insert(END, row)

def add_command():
    database.insert(Title_Text.get(), Author_Text.get(), Year_Text.get(), ISBN_Text.get())
    display_addition = (Title_Text.get(), Author_Text.get(), Year_Text.get(), ISBN_Text.get())
    List1.delete(0,END)
    List1.insert(END,display_addition)
    

window = Tk()

window.wm_title("Will's Web Library")

l1 = Label(window, text = "Title")
l1.grid(row = 0,column = 0 )

l2 = Label(window, text = "Author")
l2.grid(row = 1,column = 0 )

l3 = Label(window, text = "Year")
l3.grid(row = 0,column = 2 )

l4 = Label(window, text = "ISBN Number")
l4.grid(row = 1,column = 2 )



Title_Text = StringVar()
e1 = Entry(window, textvariable = Title_Text )
e1.grid(row = 0, column = 1)

Author_Text = StringVar()
e2 = Entry(window, textvariable = Author_Text )
e2.grid(row = 1, column = 1)

Year_Text = StringVar()
e3 = Entry(window, textvariable = Year_Text )
e3.grid(row = 0, column = 3)

ISBN_Text = StringVar()
e4 = Entry(window, textvariable = ISBN_Text )
e4.grid(row = 1, column = 3)


List1 = Listbox(window, height =12, width = 70)
List1.grid(row =2, column = 0, columnspan = 4, rowspan = 12)


sb1 = Scrollbar(window)
sb1.grid(row = 2, column =4,rowspan = 12, sticky = 'ns') # Sticky makes the scroll bar match the height of the widget it is attached to - ns = north south 

List1.bind('<<ListboxSelect>>', get_selected_row)   #This line here pairs with the selected_row function that allows us to select a row in the ListBox. It is called everytime the user clicks on the listbox

List1.configure(yscrollcommand = sb1.set)
sb1.configure(command = List1.yview)

b1 = Button(window, text = "View All", width = 12, command = view_command)
b1.grid(row =2, column = 5)

b2 = Button(window, text = "Search Entry", width = 12, command = search_command)
b2.grid(row =3, column = 5)

b3 = Button(window, text = "Add Entry", width = 12, command = add_command)
b3.grid(row =4, column = 5)

b4 = Button(window, text = "Update Entry", width = 12, command = update_command)
b4.grid(row =5, column = 5)

b5 = Button(window, text = "Delete Entry", width = 12, command = delete_command)
b5.grid(row =6, column = 5)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row =7, column = 5)

window.mainloop()