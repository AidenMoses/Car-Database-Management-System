# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 20:27:08 2020

@author: aiden
"""
import sqlite3
import pandas as pd
from pandas import DataFrame
db = sqlite3.connect('Cars.db')
cursor = db.cursor()

#   Create Functions for each of our operations


def setUp(): # Set up Functions
    
   # Sets up our dataFrame display
    
    pd.set_option('display.max_rows', 1000)
    pd.set_option('display.max_columns', 10)
    pd.set_option('display.width', 1500)
    pd.set_option('max_columns', 200)
    pd.set_option('max_colwidth', 500)
    
    
    cursor.execute('DROP TABLE IF EXISTS Cars') 
    
def createTables(): # Create our starting table
    
   
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
            
def insertRecords(): # Insert Records - Hard Coded Examples
   
        cursor = db.cursor()
        sql = '''INSERT INTO Cars (Car_id,Car_Brand, Car_Model, Year, VIN, KmsTravelled, Price)
                VALUES(1,'Mecedes-Benz','S-Class', 2008, '3GYFK66N54G536254', 114873, 5322840);'''                
        cursor.execute(sql)
        sql = '''INSERT INTO Cars (Car_id,Car_Brand, Car_Model, Year, VIN, KmsTravelled, Price)
                VALUES(2,'Mitsubishi','Eclipse', 1998, 'WBAKF5C56DJ707452', 18175, 4236089);'''        
        cursor.execute(sql)
       
        sql = '''INSERT INTO Cars (Car_id,Car_Brand, Car_Model, Year, VIN, KmsTravelled, Price)
                VALUES(3,'Morgan','Aero 8', 2008, 'WBA3B3C5XDJ550397', 43127, 2692742);'''             
        cursor.execute(sql)
       
        sql = '''INSERT INTO Cars (Car_id,Car_Brand, Car_Model, Year, VIN, KmsTravelled, Price)
                VALUES(4,'Volvo','S40', 2004, '1YVHZ8BH1A5558917', 116473, 3877571);'''
        cursor.execute(sql)
        
        sql = '''INSERT INTO Cars (Car_id,Car_Brand, Car_Model, Year, VIN, KmsTravelled, Price)
                VALUES(5,'Toyota','Paseo', 1997, '1FMCU4K31CK129544', 13608, 3827537);'''
        cursor.execute(sql)

        
        
        # Read a csv file using Pandas
        read_CarList = pd.read_csv (r'Cars.csv')
        
#       Insert the values from the csv file into the Books table
#       Pandas creates all the intert into statements
        read_CarList.to_sql('Cars',db,if_exists = 'append',index= False)
        
        db.commit()        
        
def resetDB(): # Reset DB to starting state
    createTables()
    insertRecords()

#   Mainline program begins here
#   Call the dataFrame Setup
setUp()
cursor = db.cursor()  

#   Resets DB for first time use each time app is executed
resetDB()

# Simple starying SQL 
sql = 'SELECT * FROM Cars Order by Car_id' 


cursor.execute(sql)
result = cursor.fetchall()

#   Display Result Set in a Panda's DataFrame
df = pd.DataFrame(result, columns=['Car_id', 'Car_Brand','Car_Model','Year','VIN','KmsTravelled','Price','Dealer_id'])
print (df)



print("***Title***")
print("1) Add a new car to the database")
print("2) Delete a Car from the database")
print("3) Update an existing database record")
print("4) View all cars in the database")
print("5) Search for a car or set of cars that meet certain criteria")
print("6) Delete all data from the database")
print("7) Quit the Program")
#this would be asking the user for the add choice
Choice = int(input("Enter your Choice: "))
if Choice == 1:
    Selection1 = input("Car Brand: ")
    Selection2 = input("Car Model: ")
    Selection3 = (int(input("Enter car year: ")))
    Selection4 = input("Enter VIN")
    Selection5 = int(input("Enter Odometer"))
    Selection6 = float(input("Enter Car value: "))
    sql = '''
        INSERT INTO Cars (Car_id,Car_Brand, Car_Model, Year, VIN, KmsTravelled, Price)
        VALUES(?,?,?,?,?,?,?);'''
    VALUE = (Selection1,Selection2,Selection3,Selection4,Selection5,Selection6)
    cursor.execute(sql,val)
    print("Thankyou For you input")  
# this would be the delete  
if Choice == 2 :
    sql = "DELETE FROM Cars WHERE Car_Model = 'Toyota'"
cursor.execute(sql)
print("Thankyou")

#this would be the code to update
if Choice == 3:
    sql = "UPDATE Cars SET Car_Model = 'Toyota' WHERE Car_Model = 'Chevy'"
cursor.execute(sql)
db.commit()

#if Choice == 4:

#this would be used to search
if Choice == 5:
    cursor.execute("SELECT * FROM Cars")
myresult = cursor.fetchall()
for x in myresult:
  print(x)
  

#   Cleans up DB for next trial run.
cursor.execute('DROP TABLE IF EXISTS Cars')
db.close()
