import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        connection = sqlite3.connect(db_file)
 # To-Do add a connection for the database
    except Error as e:
        print(e)

    #To-Do return the connection 
    finally:
        return connection

def close_connection(conn):
    """ closes a connection to a database """
    conn.close()


def select_all(conn):
    """select all rows from our table using the conn we already created """
    cur = conn.cursor()
    #query = "SELECT * FROM longley" # To-Do write the query to retrive all data from the longley table 
    cur.execute("SELECT * FROM longley")
    rows = cur.fetchall() 
    return rows


def print_rows(rows):
    """ Loop through the retrived rows of a table and print them"""
    # All of the function body is a todo task
    for row in rows:
        print(row)
