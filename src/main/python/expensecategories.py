# Importing Libraries and Modules
import pyodbc as dbe
from tabulate import tabulate as table
import src.main.python.logger as log


class ExpenseCategories:

    # View All Expense Categories
    @staticmethod
    def getExpenseCategories(cur, userID):
        try:
            # Fetching number of expense categories associated with the user account
            cur.execute("WITH W AS (SELECT ROW_NUMBER() OVER (ORDER BY ExpCatID, Name) AS RowNum, Name, (CASE WHEN "
                        "UserID = 0 THEN 'System' ELSE 'User' END) AS Type from ExpenseCategories WHERE UserID = 0 OR "
                        "UserID = ?) SELECT * FROM W", (userID,))
            rows = cur.fetchall()
            columns = list(map(lambda x: x[0], cur.description))
            print(f"\nExpense Categories:\n\n{table(rows, columns)}")

        except Exception as e:
            print(e)

    # Get ExpCatID from for the Selected Expense Category
    @staticmethod
    def getExpCatID(cur, userID):
        try:
            # Printing all expense categories for the user to select an expense category
            ExpenseCategories.getExpenseCategories(cur=cur, userID=userID)

            # Fetching number of expense categories associated with the user account
            cur.execute("SELECT COUNT(*) from ExpenseCategories WHERE UserID = 0 OR UserID = ?", (userID,))
            rows = cur.fetchone()

            while True:
                rowNum = int(input("\nPlease enter the row number of the Expense Category: "))
                if rowNum <= rows[0]:
                    break
                else:
                    print("Invalid input! Please enter a valid row number from the displayed Expense Categories.")
                    continue

            cur.execute("WITH W AS (SELECT ROW_NUMBER() OVER (ORDER BY ExpCatID, Name) AS RowNum, ExpCatID, Name from "
                        "ExpenseCategories WHERE UserID = 0 OR UserID = ?)"
                        "SELECT ExpCatID FROM W WHERE RowNum = ?", (userID, rowNum))

            expCatID = cur.fetchone()

            return expCatID[0]

        except Exception as e:
            print(e)

    # Adding New Expense Category
    @staticmethod
    def addExpenseCategory(conn, cur, userID):
        try:

            name = input("Expense Category Name: ")

            cur.execute("SELECT COUNT(1) FROM ExpenseCategories WHERE UserID = ? AND Name = ?", (userID, name))
            expExists = cur.fetchone()

            if expExists[0] > 0:
                raise Exception("The mentioned Expense Category already exists!")
            else:
                cur.execute("INSERT INTO ExpenseCategories (Name, UserID) VALUES (?, ?)", (name, userID))
                expAdded = cur.rowcount

                if expAdded > 0:
                    log.Logger.insertlog(cur=cur, userID=userID, transID=0, message="Expense Category Added "
                                                                                    "successfully")
                    conn.commit()
                    print("The Mentioned Expense Category added successfully!")
                else:
                    raise dbe.OperationalError("Expense Category Addition Failed!")

        except Exception as e:
            print(e)
