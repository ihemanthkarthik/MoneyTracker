# Importing Libraries and Modules
import sqlite3 as database
import setupDB as dbSetup

# Creating function for DB Connection
def getConnection():
    try:
        # Connecting to the Application DB File - (database.db)
        conn = database.connect("database.db")
        cur = conn.cursor()
        print("Started database connection")

        # Executing setup function to check and create necessary tables
        # for the application if tables not present in DB.
        dbSetup.setup(conn=conn, cur=cur)
        print("Initial DB Setup Done!")
        return conn, cur
    except Exception as e:
        print(f"dbConnect Error: {e}")
        conn.close()
        exit()

def closeConnection(conn, cur):
    """Function to close Database Connection"""
    try:
        # Committing all the unsaved transactions in the database
        cur.commit()
        # Closing both Cursor and Connection objects
        conn.close()
    except Exception as e:
        print(f"dbClose Error: {e}")
        exit()