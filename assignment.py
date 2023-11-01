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
class database:
    def __init__(self):
        self.create()
        while True:
            choice = input("\n1: Enter a record\n2: Retrieve info\n3: Print Data\nYour choice:")

            if choice == "1":
                database.insert()
                                                                        
            elif choice == "2":
                database.getinfo()

            elif choice == "3":
                database.printall()

    def create(self):

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

    def insert():
        from datetime import date
        connection = sqlite3.connect('dbase.db')
        cursor = connection.cursor()
        petname = input("\nPet's name:")
        species = input("Pet's species:")
        breed = input("Pet's breed:")
        owner = input("Owner's name:")

        while True:
            try:
                phonenum = int(input("Phone number:"))
                break
            except:
                print("That is not a valid input")
                
        email = input("Email:")

        query = f"insert into pets (petname,species,breed,owner,phonenum,email,balance,lastdate) values ('{petname}','{species}','{breed}','{owner}','{phonenum}','{email}','0','{date.today()}');"
        cursor.execute(query)
        connection.commit()

    def getinfo():
        connection = sqlite3.connect('dbase.db')
        cursor = connection.cursor()

        while True:
            choice = input("\n1: Find account with id\n2: Find account with email\n3: Find account with phone number\nYour choice:")
            if choice == "1":
                try:
                    x = int(input("ID: "))
                    query = f"select * from pets where id = '{x}'"
                    break
                except:
                    print("None found")
                
            elif choice == "2":
                try:
                    x = str(input("Email: "))
                    query = f"select * from pets where email = '{x}'"
                    break
                except:
                    print("None found")

            elif choice == "3":
                try:
                    x = int(input("Phone number: "))
                    query = f"select * from pets where phonenum = '{x}'"
                    break
                except:
                    print("None found")

        cursor.execute(query)
        result = cursor.fetchall()
        
        if result == []:
            print("None found")

        for i in result:
            print(i)

    def printall():

        connection = sqlite3.connect('dbase.db')
        
        cursor = connection.cursor()
        query = "select * from pets"
        cursor.execute(query)
        result = cursor.fetchall()
        
        for i in result:
            print(i)

database()
