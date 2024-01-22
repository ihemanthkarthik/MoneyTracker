# Importing Libraries and Modules
import sqlite3 as db

# Creating function for Initial DB Setup
def setup(conn, cur):
    try:
        # Create a larger transaction to ensure Atomicity
        cur.execute("BEGIN TRANSACTION")

        # Creating Database Objects for Money Tracker
        # Creating Users Table for User Profile
        cur.execute(
            "CREATE TABLE IF NOT EXISTS Users "
            "(UserID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Name VARCHAR(50), Gender VARCHAR(1), DOB Date, "
            "Email VARCHAR(50), UserName VARCHAR(10), Password VARCHAR(50), PremiumUser VARCHAR(1))"
        )

        # Creating BankDetails Table for Maintaining User Bank Accounts
        cur.execute(
            "CREATE TABLE IF NOT EXISTS BankDetails "
            "(BankID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, AccountNumber VARCHAR(15), BankName VARCHAR(50), "
            "UserID INTEGER)")

        # Creating Statement Table for Maintaining Transactions of the User
        cur.execute(
            "CREATE TABLE IF NOT EXISTS Statement "
            "(TransID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, UserID INTEGER, BankID INTEGER, Amount Float, "
            "PaymentType VARCHAR(2), ExpCatID INTEGER, Payee VARCHAR(50), Description VARCHAR(100), TransactionDate Datetime)"
        )

        # Creating Expense Categories Table for Maintaining Generic and Personalized Expense Categories of the User
        cur.execute(
            "CREATE TABLE IF NOT EXISTS ExpenseCategories "
            "(ExpCatID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Name VARCHAR(50), UserID INTEGER)"
        )

        # Creating Log Table for Maintaining Logs of the Activity for Error Handling
        cur.execute(
            "CREATE TABLE IF NOT EXISTS Logs (UserID INTEGER, TransID INTEGER, LogDescription VARCHAR(200), LogDateTime "
            "DateTime)"
        )

        # Adding Basic Expense Categories
        cur.execute("SELECT COUNT(*) FROM ExpenseCategories")

        expcount = cur.fetchone()

        if expcount[0] == 0:
            expense_categories = [
                ('Bills', 0),
                ('Groceries', 0),
                ('Rent', 0),
                ('Entertainment', 0),
                ('Debt Payment', 0),
                ('Tax', 0),
                ('Education', 0),
                ('Insurance', 0),
                ('Health Care', 0),
                ('Income', 0)
            ]

            query = "INSERT INTO ExpenseCategories (Name, UserID) VALUES " + ', '.join(
                [f"('{name}',{user_id})" for name, user_id in expense_categories])

            cur.execute(query)

        # Commit the entire transaction
        conn.commit()

    except db.Error as e:
        print(f"Error in creating tables: {e}")
        # Rollback the transaction if any errors occur
        conn.rollback()