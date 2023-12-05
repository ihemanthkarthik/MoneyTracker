# Importing Libraries and Modules
import sqlite3 as db

# Connecting to the Database
connector = db.connect("Money Tracker.db")
cursor = connector.cursor()

# Creating Database Objects for Money Tracker
# Creating Users Table for User Profile
connector.execute(
    "CREATE TABLE IF NOT EXISTS Users "
    "(UserID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Name VARCHAR(50), Gender VARCHAR(1), DOB Date, "
    "Email VARCHAR(50), UserName VARCHAR(10), Password VARCHAR(50), PremiumUser VARCHAR(1))"
)

# Creating BankDetails Table for Maintaining User Bank Accounts
connector.execute(
    "CREATE TABLE IF NOT EXISTS BankDetails "
    "(BankID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, AccountNumber VARCHAR(15), BankName VARCHAR(50), "
    "UserID INTEGER)")

# Creating Statement Table for Maintaining Transactions of the User
connector.execute(
    "CREATE TABLE IF NOT EXISTS Statement "
    "(TransID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, UserID INTEGER, BankID INTEGER, Amount Float, "
    "PaymentType VARCHAR(2), ExpCatID INTEGER, Payee VARCHAR(50), Description VARCHAR(100), TransactionDate Datetime)"
)

# Creating Expense Categories Table for Maintaining Generic and Personalized Expense Categories of the User
connector.execute(
    "CREATE TABLE IF NOT EXISTS ExpenseCategories "
    "(ExpCatID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Name VARCHAR(50), UserID INTEGER)"
)

# Creating Log Table for Maintaining Logs of the Activity for Error Handling
connector.execute(
    "CREATE TABLE IF NOT EXISTS Logs (UserID INTEGER, TransID INTEGER, LogDescription VARCHAR(200), LogDateTime "
    "DateTime)"
)

connector.commit()

# Adding Basic Expense Categories
expcount = connector.execute("SELECT COUNT(*) FROM ExpenseCategories")

if expcount == 0:
    connector.execute("INSERT INTO ExpenseCategories (Name, UserID) VALUES ('Bills',0), ('Groceries',0), ('Rent',0), "
                      "('Entertainment',0), ('Debt Payment', 0), ('Tax', 0), ('Education', 0), ('Insurance',0),"
                      "('Health Care',0)")

    connector.commit()

def regUser(usr_det):
    global connector, table

    name = usr_det[0]
    gender = usr_det[1]
    dob = usr_det[2]
    email = usr_det[3]
    username = usr_det[4]
    password = usr_det[5]

    usr_count = connector.execute("SELECT COUNT(*) FROM Users WHERE Email = :email", email)

    if usr_count == 0:
        connector.execute("INSERT INTO Users VALUES (:name, :gender, :DOB, :email, :username, :password)", name,
                          gender, dob, email, username, password)

        user_reg = connector.rowcount
        userID = connector.insert_id()

        if user_reg > 0:
            connector.execute("INSERT INTO Logs VALUES(:userID, 0, 'User Created Successfully',datetime('now'))", userID)
            connector.commit()
            return 1
        else:
            return 0
    else:
        return -1

def login(login_creds):
    global connector, table
    username = login_creds[0]
    password = login_creds[1]

    userID = connector.execute("SELECT UserID FROM Users WHERE UserID = :username AND Password = :password", username,
                               password)

    if userID > 0:
        connector.execute("INSERT INTO Logs VALUES(:userID, 0, 'User Logged  in Successfully',datetime('now'))", userID)
        connector.commit()
        return 1
    else:
        return 0

def frgtPwd(pwd_rst):
    global connector, table

    username = pwd_rst[0]
    DOB = pwd_rst[1]
    newPassword = pwd_rst[2]

    userID = connector.execute("SELECT UserID FROM Users WHERE UserName = :username AND DOB = :DOB", username, DOB)

    if userID > 0:
        connector.execute("UPDATE Users SET Password = :newPassword WHERE WHERE UserID = :username AND DOB = :DOB",
                          username, DOB, newPassword)

        pwd_rst = connector.rowcount

        if pwd_rst > 0:
            connector.execute("INSERT INTO Logs VALUES(:UserID, 0, 'User reset password successfully',datetime('now'))",
                              userID)
            connector.commit()
            return 1
        else:
            return 0

def frgtUsn(email):
    global connector, table

    username = connector.execute("SELECT Username from Users WHERE Email = :email", email)

    if (len(username) > 0):
        return username
    else:
        return 0