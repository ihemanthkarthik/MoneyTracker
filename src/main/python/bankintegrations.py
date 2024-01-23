# Importing Libraries and Modules
import pyodbc as dbe
import logger as log
from tabulate import tabulate as table


class bankIntegration:

    # View All Registered Bank Account Details
    def getBankAccount(conn, cur, userID):
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