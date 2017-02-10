import sqlite3

conn = sqlite3.connect('first.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS person(name VARCHAR(255), age NUMBER(5))')

def data_entry():
    c.execute("INSERT INTO person VALUES('Prabin', 22)")
    conn.commit()
    c.close()
    conn.close()

def read_data():
    c.execute("SELECT * FROM person")
    for row in c.fetchall():
        print("name ",row[0],"\nAge ",row[1])


create_table()
data_entry()
read_data()