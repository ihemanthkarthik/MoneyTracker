# Importing Libraries and Modules
import pyodbc as dbe
from tabulate import tabulate as table
import src.main.python.logger as log

class ExpenseCategories:

    # View All Expense Categories
    @staticmethod
    def getExpenseCategories(conn, cur, userID):
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