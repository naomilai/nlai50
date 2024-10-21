#peaches & mangoes: Anastasia Lee, Nia Lam, Naomi Lai
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")     # create courses table
with open("courses.csv", "r") as file:
    dict = csv.DictReader(file)
    for row in dict:
        command = "INSERT INTO courses (code, mark, id) VALUES " 
        command += "('" + row['code'] + "', '" + row['mark'] + "', '" + row['id'] + "');"  # adding data to db
        # print(command)
        c.execute(command)      # run SQL statement

c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)")     # create students table
with open("students.csv", "r") as file:
    dict = csv.DictReader(file)
    for row in dict:
        command = "INSERT INTO students (name, age, id) VALUES " 
        command += "('" + row['name'] + "', '" + row['age'] + "', '" + row['id'] + "');"  # adding data to db
        # print(command)
        c.execute(command)      # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database