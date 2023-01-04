from tkinter import *
#from PIL import ImageTk,Image
import mysql.connector

root = Tk()
root.title("arvin")
root.geometry("600x500") 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "1122",
    database = "crm",
)


# print(mydb)

# Creat a cursor and initialize it
my_cursor = mydb.cursor()

# Create a Database
# my_cursor.execute("CREATE DATABASE crm")


# Test to see if database was created
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)

#Drop the table 
#my_cursor.execute("DROP TABLE customers")
# my_cursor.execute("DROP TABLE test2")


# creat a table
my_cursor.execute("CREATE TABLE IF NOT EXISTS customers(first_name VARCHAR(255), \
    last_name VARCHAR(255), \
    zipcode INT(10), \
    price_paid DECIMAL(10,2), \
    User_id INT AUTO_INCREMENT PRIMARY KEY)")

# my_cursor.execute("CREATE TABLE test2(اسم VARCHAR(255), \
#     شماره VARCHAR(255), \
#         user_id INT AUTO_INCREMENT PRIMARY KEY)")



#Alter table 
'''
my_cursor.execute("ALTER TABLE customers ADD (\
    email VARCHAR(255),\
    address_1 VARCHAR(255),\
    city VARCHAR(255),\
    state VARCHAR(255),\
    phone VARCHAR(255))")
'''

# show  table
# my_cursor.execute("SELECT * FROM customers")
#print(my_cursor.description)

# for thing in my_cursor.description:
#     print(thing)

#Clear Text Fields
def clear_fields():
    first_name_Box.delete(0, END)
    last_name_Box.delete(0,END)
    address_1_Box.delete(0,END)
    city_Box.delete(0,END)
    state_Box.delete(0,END)
    zipcode_Box.delete(0,END)
    phone_Box.delete(0,END)
    email_Box.delete(0,END)
    price_paid_Box.delete(0,END)

# Summit customer to Database

def add_customer():
    sql_command = "INSERT INTO customers(first_name, last_name, address_1, city, state, zipcode, phone, email, price_paid) VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)"
    values = (first_name_Box.get(), last_name_Box.get(), address_1_Box.get(), city_Box.get(), state_Box.get(), zipcode_Box.get(), phone_Box.get(), email_Box.get(), price_paid_Box.get())
    my_cursor.execute(sql_command, values)
    # Commit the changes to the database
    mydb.commit()
    #clear the fields
    clear_fields()

# Create a lable 
title_label = Label(root, text= "Nilab Database", font = ("Helvetica", 16))
title_label.grid(row=0 , column=0, columnspan=2 , pady="10")

#Create Main Form To Enter Customer Data

first_name_label = Label(root, text="First Name").grid(row=1 , column=0, sticky=W, padx=10)
last_name_label = Label(root, text="Last Name").grid(row=2 , column=0, sticky=W, padx=10)
address_1_label = Label(root, text="Address").grid(row=3 , column=0, sticky=W, padx=10)
city_label = Label(root, text="City").grid(row=4 , column=0, sticky=W, padx=10)
state_label = Label(root, text="State").grid(row=5 , column=0, sticky=W, padx=10)
zipcode_label = Label(root, text="Zipcode").grid(row=6 , column=0, sticky=W, padx=10)
phone_label = Label(root, text="Phone").grid(row=7 , column=0, sticky=W, padx=10)
email_label = Label(root, text="Email Address").grid(row=8 , column=0, sticky=W, padx=10)
price_paid_label = Label(root, text="Price Paid").grid(row=9 , column=0, sticky=W, padx=10)


#Create Entry Box

first_name_Box = Entry(root)
first_name_Box.grid(row=1, column=1)

last_name_Box = Entry(root)
last_name_Box.grid(row=2, column=1, pady=5)

address_1_Box = Entry(root)
address_1_Box.grid(row=3, column=1, pady=5)

city_Box = Entry(root)
city_Box.grid(row=4, column=1, pady=5)

state_Box = Entry(root)
state_Box.grid(row=5, column=1, pady=5)

zipcode_Box = Entry(root)
zipcode_Box.grid(row=6, column=1, pady=5)

phone_Box = Entry(root)
phone_Box.grid(row=7, column=1, pady=5)

email_Box = Entry(root)
email_Box.grid(row=8, column=1, pady=5)

price_paid_Box = Entry(root)
price_paid_Box.grid(row=9, column=1, pady=5)


#create buttons

add_customer_button = Button(root, text="Add Customer To Database", command=add_customer)
add_customer_button.grid(row=14, column=0, padx=10, pady=10)

clear_fields_button = Button(root, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=14, column=1, padx=10, pady=10)

root.mainloop()