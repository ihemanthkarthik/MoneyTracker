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

    # Modifying Expense Category
    @staticmethod
    def updExpenseCategory(conn, cur, userID):
        try:
            # Note Message for the User
            print("\n NOTE: You will be able to modify/delete only the expense categories you added!")
            # Fetching ExpCatID based USer Selection
            while True:
                expCatID = ExpenseCategories.getExpCatID(cur=cur, userID=userID)

                cur.execute("SELECT UserID FROM ExpenseCategories WHERE ExpCatID = ?", (expCatID,))
                usrChk = cur.fetchone()

                if usrChk[0] > 0:
                    break
                else:
                    print("\nInvalid Choice! This is a system added Expense Category!\nYou will be able to "
                          "modify/delete only the expense categories you added!")
                    continue

            # Print the update options
            print(
                "\n1. Name"
                "\n2. Cancel Expense Category updation\n"
            )

            # Menu Selection Check based on the above message
            while True:
                menu = int(input("Please enter 1 to update (or) 2 to cancel: "))
                if menu in range(1, 3):
                    break
                else:
                    print("Invalid choice. Please enter 1 to update (or) 2 to cancel: ")
                    continue

            # Get the updated information
            if menu == 1:

                # Update the expense category
                name = input("Enter the name you want to update: ")
                cur.execute("UPDATE ExpenseCategories SET Name = ? WHERE ExpCatID = ?", (name, expCatID))

                # Check if the expense category was updated
                if cur.rowcount > 0:
                    # Log the update
                    log.Logger.insertlog(cur=cur, userID=userID, transID=0, message="Expense Category updated "
                                                                                    "successfully")
                    conn.commit()
                    print("Your Expense Category has been updated successfully!")
                else:
                    raise dbe.OperationalError("Unexpected Error Encountered! Sorry for the inconvenience")
            # Cancel the update
            elif menu == 2:
                return

        except Exception as e:
            print(e)

    # Delete Expense Category
    @staticmethod
    def delExpenseCategory(conn, cur, userID):
        try:
            # Note Message for the User
            print("\n NOTE: You will be able to modify/delete only the expense categories you added!")

            # Fetching ExpCatID based USer Selection
            while True:
                expCatID = ExpenseCategories.getExpCatID(cur=cur, userID=userID)

                cur.execute("SELECT UserID FROM ExpenseCategories WHERE ExpCatID = ?", (expCatID,))
                usrChk = cur.fetchone()

                if usrChk[0] > 0:
                    break
                else:
                    print("\nInvalid Choice! This is a system added Expense Category!\nYou will only be able to "
                          "modify/delete the expense categories you added!")
                    continue

            # Checking if there are any transactions under the Expense Categories
            cur.execute("SELECT COUNT(1) FROM Statement WHERE UserID = ? AND ExpCatID = ?", (userID, expCatID))

            tranCount = cur.fetchone()

            if tranCount[0] <= 0:
                # User Input Validation Check
                while True:
                    # Getting confirmation from the user for deleting the expense category
                    confirm = input("WARNING: This will delete your expense category permanently. Would you like to "
                                    "proceed (Y/N)?")[0].upper()

                    if confirm[0] == "Y" or confirm[0] == "N":
                        break
                    else:
                        print("Invalid choice! Please enter Y  or N ")
                        continue

                if confirm[0] == "Y":
                    cur.execute("DELETE FROM ExpenseCategories WHERE ExpCatID = ?", (expCatID,))
                    expCatDel = cur.rowcount

                    if expCatDel > 0:
                        log.Logger.insertlog(cur=cur, userID=userID, transID=0, message="Expense Category "
                                                                                        "Deleted successfully")
                        conn.commit()
                        print("Your Expense Category has been deleted successfully!")
                    else:
                        raise dbe.OperationalError("Expense Category Deletion Failed")
                else:
                    print("Action Cancelled!")
            else:
                raise Exception(f"You have {tranCount} transactions under the expense category you are trying to "
                                f"delete.\nPlease modify the transaction's expense category!")
        except Exception as e:
            print(e)
