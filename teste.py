import sqlite3

connection = sqlite3.connect('tutorial.db')
c= connection.cursor()

#sql
def create_table():
    c.execute('CREATE TABLE dados (id integer,unix real)')

    
    create_table()
