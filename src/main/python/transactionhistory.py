# Importing Libraries and Modules
from tabulate import tabulate as table
import src.main.python.bankintegrations as bank

class TransactionHistory:
    # View All Transactions
    @staticmethod
    def getTransactionHistory(cur, userID):
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
                return

            cur.execute("SELECT COUNT(*) FROM Statement WHERE UserID = ? ANd BankID = ?", (userID, bankID))
            tranCount = cur.fetchone()

            if tranCount[0] <= 0:
                print("\nNo Transaction History Found!\n")
            else:
                # Fetching number of expense categories associated with the user account
                cur.execute(
                    "SELECT ROW_NUMBER() OVER (ORDER BY b.BankName, b.AccountNumber, s.Payee, s.Description, "
                    "s.TransactionDate) AS RowNum,"
                    "(b.BankName||'-'||b.AccountNumber) AS BankAccount, "
                    "s.Amount as Amount, "
                    "s.PaymentType as PaymentType, "
                    "s.Payee as Payee, "
                    "e.Name as ExpenseCategory, "
                    "s.Description as Description, "
                    "s.TransactionDate as DateTime "
                    "FROM Statement s "
                    "LEFT JOIN BankDetails b ON s.BankID = b.BankID "
                    "LEFT JOIN ExpenseCategories e ON s.ExpCatID = e.ExpCatID "
                    "WHERE s.UserID = ? and s.BankID = ?", (userID, bankID))

                rows = cur.fetchall()

                columns = list(map(lambda x: x[0], cur.description))

                print(f"\Transaction History:\n\n{table(rows, columns)}")

        except Exception as e:
            print(e)