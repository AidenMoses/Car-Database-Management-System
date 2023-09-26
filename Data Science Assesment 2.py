# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 20:27:08 2020
@author: aiden
"""

# Import necessary libraries
import sqlite3
import pandas as pd
from pandas import DataFrame

# Connect to the SQLite database
db = sqlite3.connect('Cars.db')
cursor = db.cursor()

# Create Functions for each of our operations
def setUp():  # Set up Functions
    # Sets up our DataFrame display
    pd.set_option('display.max_rows', 1000)
    pd.set_option('display.max_columns', 10)
    pd.set_option('display.width', 1500)
    pd.set_option('max_columns', 200)
    pd.set_option('max_colwidth', 500)

    cursor.execute('DROP TABLE IF EXISTS Cars')

def createTables():  # Create our starting table
    cursor = db.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Cars(
        Car_id integer,
        Car_Brand string,
        Car_Model string,
        Year integer,
        VIN,
        KmsTravelled integer,
        Price integer,
        Dealer_id integer,
        Primary Key(Car_id));
        ''')

def insertRecords():  # Insert Records - Hard Coded Examples
    cursor = db.cursor()
    
    # Inserting hard-coded examples
    sql = '''INSERT INTO Cars (Car_id,Car_Brand, Car_Model, Year, VIN, KmsTravelled, Price)
             VALUES(1,'Mercedes-Benz','S-Class', 2008, '3GYFK66N54G536254', 114873, 5322840);'''
    cursor.execute(sql)
    
    # Insert more hard-coded examples
    
    # Read a CSV file using Pandas
    read_CarList = pd.read_csv('Cars.csv')
    
    # Insert the values from the CSV file into the Cars table
    # Pandas creates all the insert statements
    read_CarList.to_sql('Cars', db, if_exists='append', index=False)
    
    db.commit()

def resetDB():  # Reset DB to starting state
    createTables()
    insertRecords()

# Mainline program begins here
# Call the DataFrame Setup
setUp()
cursor = db.cursor()

# Resets DB for the first time use each time the app is executed
resetDB()

# Simple starting SQL
sql = 'SELECT * FROM Cars Order by Car_id'
cursor.execute(sql)
result = cursor.fetchall()

# Display Result Set in a Pandas DataFrame
df = pd.DataFrame(result, columns=['Car_id', 'Car_Brand', 'Car_Model', 'Year', 'VIN', 'KmsTravelled', 'Price', 'Dealer_id'])
print(df)

print("***Title***")
print("1) Add a new car to the database")
print("2) Delete a Car from the database")
print("3) Update an existing database record")
print("4) View all cars in the database")
print("5) Search for a car or set of cars that meet certain criteria")
print("6) Delete all data from the database")
print("7) Quit the Program")

# Ask the user for their choice
Choice = int(input("Enter your Choice: "))

# If choice is 1, add a new car to the database
if Choice == 1:
    Selection1 = input("Car Brand: ")
    Selection2 = input("Car Model: ")
    Selection3 = int(input("Enter car year: "))
    Selection4 = input("Enter VIN: ")
    Selection5 = int(input("Enter Odometer: "))
    Selection6 = float(input("Enter Car value: "))
    sql = '''
        INSERT INTO Cars (Car_id,Car_Brand, Car_Model, Year, VIN, KmsTravelled, Price)
        VALUES(?,?,?,?,?,?,?);'''
    VALUES = (None, Selection1, Selection2, Selection3, Selection4, Selection5, Selection6)
    cursor.execute(sql, VALUES)
    print("Thank you for your input")

# If choice is 2, delete a car from the database
if Choice == 2:
    sql = "DELETE FROM Cars WHERE Car_Model = 'Toyota'"
    cursor.execute(sql)
    print("Thank you")

# If choice is 3, update an existing database record
if Choice == 3:
    sql = "UPDATE Cars SET Car_Model = 'Toyota' WHERE Car_Model = 'Chevy'"
    cursor.execute(sql)
    db.commit()

# If choice is 4, view all cars in the database
# This part is commented out, but you can uncomment it if needed.
# if Choice == 4:
#     cursor.execute("SELECT * FROM Cars")
#     myresult = cursor.fetchall()
#     for x in myresult:
#         print(x)

# If choice is 5, search for a car or set of cars that meet certain criteria
if Choice == 5:
    cursor.execute("SELECT * FROM Cars")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)

# Cleans up DB for the next trial run.
cursor.execute('DROP TABLE IF EXISTS Cars')
db.close()
