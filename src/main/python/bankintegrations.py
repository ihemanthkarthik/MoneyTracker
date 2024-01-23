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

    # Adding New Bank Account
    @staticmethod
    def addBankAccount(conn, cur, userID):
        try:
            # Fetching number of bank accounts registered under a user
            cur.execute("SELECT COUNT(1) FROM BankDetails WHERE userID = ?", (userID,))
            accountCount = cur.fetchone()

            # Checking if the user is premium user or not
            cur.execute("SELECT PremiumUser FROM Users WHERE UserID = ?", (userID,))
            premiumUser = cur.fetchone()

            if accountCount[0] > 0 and premiumUser[0] == "N":
                raise Exception("Only one bank account can be added for a standard user")
            else:
                BankIntegration.addBankDetails(conn=conn, cur=cur, userID=userID)

        except Exception as e:
            print(e)

    # Adding Bank Account Details
    @staticmethod
    def addBankDetails(conn, cur, userID):
        try:
            while True:
                accNumber = str(input("Account Number (Last 4 Digits): "))
                if len(accNumber) == 4:
                    break
                else:
                    print("Please provide last four digits of your account number.")
                    continue

            bankName = input("Bank Name: ")

            cur.execute("SELECT COUNT(1) FROM BankDetails WHERE UserID = ? AND AccountNumber = ? AND BankName = ?",
                        (userID, int(accNumber), bankName))
            accExists = cur.fetchone()

            if accExists[0] > 0:
                raise Exception("The mentioned bank account already exists!")
            else:
                cur.execute("INSERT INTO BankDetails (AccountNumber, BankName, UserID) VALUES (?, ?, ?)",
                            (accNumber, bankName, userID))
                accAdded = cur.rowcount

                if accAdded > 0:
                    log.Logger.insertlog(cur=cur, userID=userID, transID=0, message="Bank Account Added "
                                                                                    "successfully")
                    conn.commit()
                    print("The Mentioned Bank Account added successfully!")
                else:
                    raise dbe.OperationalError("Bank Account Addition Failed!")

        except Exception as e:
            print(e)
