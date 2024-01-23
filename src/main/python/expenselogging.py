# Importing Libraries and Modules
import pyodbc as dbe
from tabulate import tabulate as table
import src.main.python.logger as log
import src.main.python.bankintegrations as bank
import src.main.python.expensecategories as expense

class ExpenseLogging:
    # View All Expense Categories
    @staticmethod
    def getExpenseTransactions(cur, userID):
        try:
            # Fetching Number of Bank Accounts associated with User Profile
            cur.execute("SELECT COUNT(*) FROM BankDetails WHERE UserID = ?", (userID,))
            bnkNum = cur.fetchone()

            if int(bnkNum[0]) > 1:
                bankID = bank.BankIntegration.getBankID(cur, userID)
            elif int(bnkNum[0]) == 1:
                cur.execute("SELECT BankID FROM BankDetails WHERE UserID = ?", (userID,))
                values = cur.fetchone()
                bankID = values[0]
            else:
                print("\nNo Bank Account Found!")

            cur.execute("SELECT COUNT(*) FROM Statement WHERE UserID = ? ANd BankID = ?", (userID, bankID))
            tranCount = cur.fetchone()

            if tranCount[0] <= 0:
                print("\nNo Expense Transaction Found!\n")
            else:
                # Fetching number of expense categories associated with the user account
                cur.execute(
                    "SELECT ROW_NUMBER() OVER (ORDER BY b.BankName, b.AccountNumber, s.Payee, s.Description, "
                    "s.TransactionDate) AS RowNum,"
                    "(b.BankName||'-'||b.AccountNumber) AS BankAccount, "
                    "s.Amount as Amount, "
                    "s.PaymentType as PaymentType, "
                    "s.Payee as Payee, "
                    "s.Description as Description, "
                    "s.TransactionDate as DateTime "
                    "FROM Statement s "
                    "LEFT JOIN BankDetails b ON s.BankID = b.BankID "
                    "WHERE s.PaymentType = 'DB' AND s.UserID = ? and s.BankID = ?", (userID, bankID))

                rows = cur.fetchall()

                columns = list(map(lambda x: x[0], cur.description))

                print(f"Expense Details:\n\n{table(rows, columns)}")

            return bankID

        except Exception as e:
            print(e)

    # Get ExpCatID from for the Selected Expense Category
    @staticmethod
    def getTransID(cur, userID):
        try:
            # Printing all expense categories for the user to select an expense category
            bankID = ExpenseLogging.getExpenseTransactions(cur=cur, userID=userID)

            if bankID > 0:
                # Fetching number of Transactions associated with the user account
                cur.execute("SELECT COUNT(*) from Statement WHERE PaymentType = 'DB' AND UserID = ? AND BankID = ?",
                            (userID, bankID))
                rows = cur.fetchone()

                if rows[0] > 0:
                    while True:
                        rowNum = int(input("\nPlease enter the row number of the transaction: "))
                        if rowNum <= rows[0]:
                            break
                        else:
                            print("Invalid input! Please enter a valid row number from the displayed transactions.")
                            continue

                    cur.execute(
                        "WITH W AS (SELECT ROW_NUMBER() OVER (ORDER BY b.BankName, b.AccountNumber, s.Payee, "
                        "s.Description,"
                        "s.TransactionDate) AS RowNum,"
                        "s.TransID AS TransID "
                        "FROM Statement s "
                        "LEFT JOIN BankDetails b ON s.BankID = b.BankID "
                        "WHERE s.PaymentType = 'DB' AND s.UserID = ? AND s.BankID = ?) "
                        "SELECT TransID FROM W WHERE RowNum = ?", (userID, bankID, rowNum))

                    transID = cur.fetchone()

                    return transID[0]
                else:
                    return 0
            else:
                print("No Bank Accounts Found!")
                return 0

        except Exception as e:
            print(e)

    # Adding New Expense
    @staticmethod
    def addExpenseTransaction(conn, cur, userID):
        try:
            # Fetching number of bank accounts associated with the user account
            cur.execute("SELECT COUNT(*) from BankDetails WHERE UserID = ?", (userID,))
            rows = cur.fetchone()

            if rows[0] == 1:
                cur.execute("SELECT BankID from BankDetails WHERE UserID = ?", (userID,))
                bankDet = cur.fetchone()
                bankID = bankDet[0]
            elif rows[0] <= 0:
                print("Please add a bank account to proceed!")
                return
            elif rows[0] > 1:
                bankID = bank.BankIntegration.getBankID(cur=cur, userID=userID)

            amount = float(input("Please enter the amount: "))
            payee = input("Please enter the payee: ")
            expCatID = expense.ExpenseCategories.getExpCatID(cur=cur, userID=userID)
            desc = input("Please enter the description: ")
            date = input("Please enter the date(YYYY-MM-DD): ")

            cur.execute(
                "INSERT INTO Statement (UserID, BankID, Amount, PaymentType, ExpCatID, Payee, Description, "
                "TransactionDate) VALUES (?, ?, ?, 'DB', ?, ?, ?, ?)",
                (userID, bankID, amount, expCatID, payee, desc, date))
            transAdded = cur.rowcount

            transID = cur.lastrowid

            if transAdded > 0:
                log.Logger.insertlog(cur=cur, userID=userID, transID=transID,
                                     message="Expense Transaction Added successfully")
                conn.commit()
                print("The Mentioned Expense is added successfully!")
            else:
                raise dbe.OperationalError("Expense Addition Failed!")

        except Exception as e:
            print(e)