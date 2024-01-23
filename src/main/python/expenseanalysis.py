import seaborn as sns
import bankintegrations as bank
import pandas as pd
import matplotlib.pyplot as plt

class ExpenseAnalysis:
    # View All Transactions
    @staticmethod
    def getExpenseAnalysis(cur, userID):
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
                    "SELECT e.Name AS ExpenseCategory, SUM(Amount) AS CatSpent FROM Statement s LEFT JOIN "
                    "ExpenseCategories e ON s.ExpCatID = e.ExpCatID WHERE s.PaymentType = 'DB' AND s.UserID = ? AND "
                    "s.BankID = ? GROUP BY e.Name",
                    (userID, bankID))

                df = pd.DataFrame(cur.fetchall(), columns=['Expense Category', 'Category Spent'])

                # Fetching number of expense categories associated with the user account
                cur.execute(
                    "SELECT SUM(Amount) AS TotalIncome FROM Statement WHERE PaymentType = 'CR' AND UserID = ? AND "
                    "BankID = ?",
                    (userID, bankID))

                totalIncome = cur.fetchone()

                # Fetching number of expense categories associated with the user account
                cur.execute(
                    "SELECT SUM(Amount) AS TotalSpent FROM Statement WHERE PaymentType = 'DB' AND UserID = ? AND "
                    "BankID = ?",
                    (userID, bankID))

                totalSpent = cur.fetchone()

                remainingAmount = totalIncome[0] - totalSpent[0]

                if remainingAmount > 0:
                    remaining = {"Expense Category": "Remaining Amount", "Category Spent": remainingAmount}
                    df = df._append(remaining, ignore_index=True)

                df["Total Income"] = totalIncome[0]

                df["Percentage"] = (df["Category Spent"] / df["Total Income"]) * 100

                sns.set_style("whitegrid")
                plt.figure(figsize=(6, 6))
                plt.pie(df['Percentage'], labels=df['Expense Category'], autopct='%1.1f%%')
                plt.title('My Pie Chart')
                plt.show()

        except Exception as e:
            print(e)