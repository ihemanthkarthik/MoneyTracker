# Importing Libraries and Modules
import pyodbc as dbe
from tabulate import tabulate as table
import src.main.python.logger as log

class BankIntegration:

    # View All Registered Bank Account Details
    @staticmethod
    def getBankAccount(cur, userID):
        try:
            # Fetching number of bank accounts associated with the user account
            cur.execute("SELECT COUNT(*) from BankDetails WHERE UserID = ?", (userID,))
            rows = cur.fetchone()

            if rows[0] <= 0:
                print("No bank accounts associated with the user")
            else:

                cur.execute("SELECT ROW_NUMBER() OVER (ORDER BY AccountNumber, BankName) AS RowNum, AccountNumber, "
                            "BankName FROM BankDetails WHERE UserID = ?", (userID,))

                rows = cur.fetchall()

                columns = list(map(lambda x: x[0], cur.description))

                print(f"\nBank Accounts:\n\n{table(rows, columns)}")

        except Exception as e:
            print(e)

    # Get bankID from for the Selected Bank Account
    @staticmethod
    def getBankID(cur, userID):
        try:
            # Printing all bank account for the user to select a bank account
            BankIntegration.getBankAccount(cur=cur, userID=userID)

            # Fetching number of bank accounts associated with the user account
            cur.execute("SELECT COUNT(*) from BankDetails WHERE UserID = ?", (userID,))
            rows = cur.fetchone()

            if rows[0] > 0:
                while True:
                    rowNum = int(input("\nPlease enter the row number of the bank account: "))
                    if rowNum <= rows[0]:
                        break
                    else:
                        print("Invalid input! Please enter a valid row number from the displayed bank account.")
                        continue

                cur.execute(
                    "WITH W AS (SELECT ROW_NUMBER() OVER (ORDER BY AccountNumber, BankName) AS RowNum, BankID, "
                    "AccountNumber, BankName from BankDetails WHERE UserID = ?)"
                    "SELECT BankID FROM W WHERE RowNum = ?", (userID, rowNum))

                bankID = cur.fetchone()

                return bankID[0]
            else:
                return 0

        except Exception as e:
            print(e)