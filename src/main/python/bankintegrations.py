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

    # Modifying Bank Details
    @staticmethod
    def updBankAccount(conn, cur, userID):
        try:
            bankID = BankIntegration.getBankID(cur=cur, userID=userID)

            if bankID > 0:
                cur.execute("SELECT AccountNumber, BankName from BankDetails WHERE UserID = ? AND BankID = ?",
                            (userID, bankID))

                values = cur.fetchone()

                # Menu Selection Check based on the above message
                while True:
                    # Print the update options
                    print(
                        "\n1. Account Number"
                        "\n2. Bank Name"
                        "\n3. Confirm Changes"
                        "\n4. Cancel Bank Account updation"
                    )

                    menu = int(
                        input("Please enter a number between (1-2) to make changes and 3 to confirm changes and 4 "
                              "to cancel: "))

                    if menu == 3:
                        break
                    elif menu in range(1, 3):
                        # Get the updated information
                        if menu == 1:
                            accNumber = input("Enter the last 4 digits of the account number you want to update: ")
                            values = (accNumber,) + values[1:]  # Update Account Number
                        elif menu == 2:
                            bankName = input("Enter the bank name you want to update: ")
                            values = (values[0], bankName)  # Update Bank Name
                        continue
                    else:
                        print("Invalid choice. Please enter a number between (1-2) to make changes and 3 to confirm "
                              "changes and 4 to cancel: ")
                        continue

                # Update the Changes
                if menu == 3:
                    # Update the bank account
                    cur.execute(
                        "UPDATE BankDetails SET AccountNumber = ?, BankName = ? WHERE UserID = ? AND BankID = ?",
                        (values[0], values[1], userID, bankID))
                    # Check if the bank account was updated
                    if cur.rowcount > 0:
                        # Log the update
                        log.Logger.insertlog(cur=cur, userID=userID, transID=0,
                                             message="Bank Account updated "
                                                     "successfully")
                        conn.commit()
                        print("Your bank account has been updated successfully!")
                    else:
                        raise dbe.OperationalError("Unexpected Error Encountered! Sorry for the inconvenience")
                elif menu == 4:
                    return
            else:
                print("No Bank Accounts found to update!")

        except Exception as e:
            print(e)