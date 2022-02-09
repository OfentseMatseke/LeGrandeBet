# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 22:50:40 2022

@author: Lenovo-G50
"""

import mysql.connector


#db = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="mpsbhcup"
#)

#print(db)


def init_database(host_str, username_str, passw_str, database_name = ""):
    db = mysql.connector.connect(
      host=host_str,
      user=username_str,
      password=passw_str,
      database = database_name
    )
    
    return db


def create_database(database_obj, database_name):
    cursor = database_obj.cursor()
    
    cursor.execute("CREATE DATABASE "+ database_name)    

def show_databases(database_obj):
    cursor = database_obj.cursor()
    cursor.execute("SHOW DATABASES")
    
    print ("\nShowing Databases\n")
    for x in cursor:
      print(x)

def show_tables(database_obj):
    cursor = database_obj.cursor()
    cursor.execute("SHOW TABLES")
    
    print ("\nShowing Tables\n")
    for x in cursor:
      print(x)
      
      
def select_all(database_obj, table_name):
    cursor = database_obj.cursor()
    
    l = []
    cursor.execute("SELECT * FROM "+ table_name +"")
    
    result = cursor.fetchall()
    print ("SELECT * FROM "+ table_name +"")
    for x in result:
      print(x)
      l.append(x)
    
    return l
    
def add_column(database_obj, table_name, column_name, column_data_type):
    cursor = database_obj.cursor()    
    cursor.execute("ALTER TABLE "+table_name+" ADD COLUMN "+column_name + " "+column_data_type)
    print("\nAdding Column\n")
    print ("ALTER TABLE "+table_name+" ADD COLUMN "+column_name + " "+column_data_type)


def create_table(database_obj, table_name, column_obj):
    cursor = database_obj.cursor()
    cursor.execute("CREATE TABLE "+table_name +" (id INT AUTO_INCREMENT PRIMARY KEY)")
    print ("\nCreating Tabl\n")
    print ("CREATE TABLE "+table_name +" (id INT AUTO_INCREMENT PRIMARY KEY)")

def add_row(database_obj, table_name, column_str, num_cols, data):
    cursor = database_obj.cursor()
    sql = "INSERT INTO "+table_name+" ("+column_str+")"+" VALUES ("
    for i in range(num_cols):
        #
        if not(i==num_cols-1):
            sql += "%s, "
        else:
            sql += "%s)"
    
    print (sql)
    val = []
    for i in range(len(data)):
        val.append(str(data[i]))
    
    
    print (tuple(val))
    cursor.execute(sql, tuple(val))
    database_obj.commit()
    print (cursor.rowcount, "Record Inserted")
    #cursor.execute("INSERT INTO "+table_name+" (Date, Day, Result) VALUES (%s, %s, %s)")
    
    
#add_row(db, "lotto", "date, day, result", 3, [])

#print (tuple(["yes", "667", str([6, 7])]))
    