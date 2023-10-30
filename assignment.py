#!python

"""
Create a program that will store the database for a veterinary
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.
"""

import sqlite3
def create():

    file = 'dbase.db'
    connection = sqlite3.connect(file)
    cursor = connection.cursor()

    query = """
    create table if not exists pets (
        id integer primary key autoincrement,
        petname tinytext,
        species tinytext,
        breed tinytext,
        owner tinytext,
        phonenum int,
        email tinytext,
        balance smallint,
        lastdate date);
    """
    cursor.execute(query)
    cursor.execute('PRAGMA table_info(pets);')
    result = cursor.fetchall()
    for i in result:
        print(i)

def insert():
    file = 'dbase.db'
    connection = sqlite3.connect(file)
    cursor = connection.cursor()
    petname = input("Pet's name:")
    species = input("Pet's species:")
    breed = input("Pet's breed:")
    owner = input("Owner's name:")
    phonenum = input("Phone number:")
    email = input("Email:")

    data = [[petname,species,breed,owner,phonenum,email,"0","0"]]
    
    for i in data:
        query = f"insert into pets (petname,species,breed,owner,phonenum,email,balance,lastdate) values ('{i[0]}','{i[1]}',{i[2]},{i[3]},{i[4]},{i[5]},{i[6]},{i[7]});"
        print(query)
        cursor.execute(query)

create()
insert()
