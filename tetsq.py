from tkinter import *
#from PIL import ImageTk,Image
import mysql.connector
import csv
from tkinter import ttk

root = Tk()
root.title("arvin")
#root.iconbitmap("")
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
#      print(db)

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
# write to CSV Excel Function
def write_to_csv(result):
    with open("customer.csv", "a",newline = "") as f:
        w = csv.writer(f, dialect= "excel")
        for record in result:
            w.writerow(record)

# search customers
def search_customer():
    search_customers = Tk()
    search_customers.title("Search All Customers")
    search_customers.geometry("800x600") 
    def search_now():
        selected = drop.get()
        sql = ""
        if selected == "Search by...":
            test = Label(search_customers, text = "you picked searched by")
            test.grid(row=2 , column = 0)
        if selected == "Last Name":
            sql = "SELECT * FROM customers WHERE last_name = %s"
            test = Label(search_customers, text = "you picked Last name")
            test.grid(row=2 , column = 0)
        if selected == "Email Address":
            sql = "SELECT * FROM customers WHERE email = %s"
            test = Label(search_customers, text = "you picked Email Address")
            test.grid(row=2 , column = 0)
        if selected == "Customer ID":
            sql = "SELECT * FROM customers WHERE user_id = %s"
            test = Label(search_customers, text = "you picked Customer ID")
            test.grid(row=2 , column = 0)   

        
        searched = search_box.get()
        # sql = "SELECT * FROM customers WHERE last_name = %s"
        name = (searched, )
        result = my_cursor.execute(sql, name)
        result = my_cursor.fetchall()

        if not result:
            result = "Record Not Found..."
            searched_label = Label(search_customers, text =result)
            searched_label.grid(row=2 , column=0)
        else:
            for index, x in enumerate(result):
                 num = 0
                 index += 3
                 for y in x:
                        searched_label = Label(search_customers, text =y)
                        searched_label.grid(row=index , column=num)
                        num += 1
            csv_button = Button(search_customers, text = "Save to Excel", command= lambda: write_to_csv(result))
            csv_button.grid(row=index+1, column=0)

        #searched_label =Label(search_customers, text=result)
        #searched_label.grid(row=3, column=0, padx=10, columnspan=2)
        
    # Entry box to search for customers
    search_box = Entry(search_customers)
    search_box.grid(row=0 , column=1, padx=10, pady=10)
    # Entry box label to search for customers
    search_box_label= Label(search_customers, text="جستجو  ")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)
    # search Button for customer
    search_button =Button(search_customers, text="Search Customers", command=search_now)
    search_button.grid(row=1, column=0, padx = 10)
    # Drop Down Box
    drop = ttk.Combobox(search_customers, value=["Search by...", "Last Name", "Email Address", "Customer ID" ])
    drop.current(0)
    drop.grid(row = 0 , column=2)

#list customers
def list_customers():
    list_customer_query = Tk()
    list_customer_query.title("List All Customers")
    list_customer_query.geometry("800x600") 
    #Query the Database
    my_cursor.execute("SELECT * FROM customers")
    result = my_cursor.fetchall()
    
    for index, x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(list_customer_query, text =y)
            lookup_label.grid(row=index , column=num)
            num += 1
    csv_button = Button(list_customer_query, text = "Save to Excel", command= lambda: write_to_csv(result))
    csv_button.grid(row=index+1, column=0)
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

# list customers button
list_customers_button = Button(root, text="List Customer", command=list_customers)
list_customers_button.grid(row = 15, column = 0, sticky=W, padx=10)

# search customers 
search_customers_button = Button(root, text="Search Customers", command=search_customer)
search_customers_button.grid(row=15, column=1, sticky=W, padx=10)



root.mainloop()