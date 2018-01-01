import sqlite3

expenses_table_name = "expense_data"
categories_table_name = "categories_data"
db_location = "../expenses360.db"

create_expenses_table_sql = "CREATE TABLE IF NOT EXISTS " + expenses_table_name + "(tx_id INTEGER PRIMARY KEY AUTOINCREMENT, tx_date DATE, tx_description TEXT NOT NULL, tx_amount TEXT, tx_category TEXT, tx_source TEXT, tx_comments TEXT);"
create_categories_table_sql = "CREATE TABLE IF NOT EXISTS " + categories_table_name + "(category_id INTEGER PRIMARY KEY AUTOINCREMENT, parent_category_name TEXT NOT NULL, sub_category_name TEXT NOT NULL);"

def create_expenses_database():
    global conn
    global c
    conn = sqlite3.connect(db_location)
    c = conn.cursor()
    c.execute(create_expenses_table_sql)
    c.execute(create_categories_table_sql)
    conn.commit()
    c.close()
    conn.close()

def insert_records(recordList):
    conn = sqlite3.connect(db_location)
    #c = conn.cursor()
    conn.executemany('insert into ' + expenses_table_name + ' (tx_date, tx_description, tx_amount, tx_source) values (?, ?, ?, ?)', recordList)
    #sql = 'insert into ' + expenses_table_name + ' values (1)'
    #c.execute(sql)
    conn.commit()
    #c.close()
    conn.close()

def view_records():
    conn = sqlite3.connect(db_location)
    c = conn.cursor();
    c.execute('select * from ' + expenses_table_name);
    print c.fetchone();
    c.close()
    conn.close()

def insert_cateogory_records():
    conn = sqlite3.connect(db_location)
    categoriesList = [
    ("Home","Rent"),("Home","Utilities"),("Home","Groceries"),("Home","Internet"),("Home","Supplies"),("Home","Other"),
    ("Personal","Shopping"),("Personal","Dining"),("Personal","Other"),
    ("Transportation","Fuel"),("Transportation","Repairs"),("Transportation","Car"),("Transportation","Others"),
    ("Charity&Gifts","Dharmado"),("Charity&Gifts","Akshardham"),("Charity&Gifts","Mandir_Activities"),("Charity&Gifts","Gifts_Fam"),("Charity&Gifts","Gifts_Frd"),("Charity&Gifts","Other"),
    ("Travel&Leisure","Transportation"),("Travel&Leisure","Lodging_Food"),("Travel&Leisure","Recreation"),("Travel&Leisure","Other"),
    ("Miscellaneous","Fees"),("Miscellaneous","Career"),("Miscellaneous","Other")
    ]

    conn.executemany('insert into ' + categories_table_name + ' (parent_category_name, sub_category_name) values (?, ?)', categoriesList)
    conn.commit()
    conn.close()
