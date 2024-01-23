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

    # Modifying Expense Transaction
    @staticmethod
    def updExpenseTransaction(conn, cur, userID):
        try:
            # Fetching TransID based User Selection
            transID = ExpenseLogging.getTransID(cur=cur, userID=userID)

            if transID <= 0:
                print("\nNo transaction found!")
            else:
                cur.execute("SELECT s.BankID AS BankID, "
                            "s.Amount as Amount, "
                            "s.PaymentType as PaymentType, "
                            "s.Payee as Payee, "
                            "s.ExpCatID as ExpCatID, "
                            "s.Description as Description, "
                            "s.TransactionDate as DateTime "
                            "FROM Statement s "
                            "WHERE TransID = ?", (transID,))

                values = cur.fetchone()

                values = [values[0], values[1], values[2], values[3], values[4], values[5], values[6]]

                # Print the update options
                print(
                    "\n1. Update Bank Account"
                    "\n2. Update Amount"
                    "\n3. Update Payment Type"
                    "\n4. Update Payee"
                    "\n5. Update Expense Category"
                    "\n6. Update Description"
                    "\n7. Update Transaction Date"
                    "\n8. Confirm Changes"
                    "\n9. Cancel Expense Category updation\n"
                )

                # Menu Selection Check based on the above message
                while True:
                    menu = int(
                        input("Please enter (1-7) to Modify and 8 to confirm the changes (or) 9 to cancel: "))
                    if menu in range(8, 10):
                        break
                    elif menu in range(1, 8):
                        # Get the updated information
                        if menu == 1:
                            bankID = bank.BankIntegration.getBankID(cur=cur, userID=userID)
                            values = (bankID,) + values[1:]  # Update BankID
                        elif menu == 2:
                            amount = float(input("Enter the amount you want to update: "))
                            values = (values[0], values[1], amount) + values[3:]  # Update Amount
                        elif menu == 3:
                            while True:
                                print(
                                    "Note: Changing an expense to credit will automatically change the Expense "
                                    "Category to Income. \nThis will not be changeable until the transaction is "
                                    "changed to expense(DB)")
                                pmtType = input(
                                    "Enter the type of Transaction: CR -> Credit or DB -> Debit: ").upper()
                                if pmtType[:2] == "CR":
                                    cur.execute("SELECT ExpCatID FROM ExpenseCategories WHERE Name = 'Income'")
                                    expID = cur.fetchone()
                                    expCatID = expID[0]
                                    values = (values[0], values[1], pmtType[:2], values[3], expCatID) + values[5:]
                                    # Update Payment Type
                                    break
                                elif pmtType[:2] == "DB":
                                    values = (values[0], values[1], pmtType[:2]) + values[3:]  # Update Payment Type
                                    break
                                else:
                                    print("Invalid Input. Please input CR for Credit or DB for Debit")
                                    continue
                        elif menu == 4:
                            payee = input("Enter the payee you want to update: ")
                            values = (values[0], values[1], values[2], payee) + values[4:]
                        elif menu == 5:
                            if values[2] == "CR":
                                print(
                                    "The transaction is changed as Credit(CR). You will not be able to select an "
                                    "expense category")
                            else:
                                expCatID = expense.ExpenseCategories.getExpCatID(cur=cur, userID=userID)

                            values = (values[0], values[1], values[2], values[3], expCatID) + values[5:]
                        elif menu == 6:
                            desc = input("Enter the description you want to update: ")
                            values = (values[0], values[1], values[2], values[3], values[4], desc) + values[6:]
                        elif menu == 7:
                            date = input("Enter the transaction date you want to update: ")
                            values = (values[0], values[1], values[2], values[3], values[4], values[5], date)
                        continue
                    else:
                        print(
                            "\nInvalid choice. Please enter (1-7) to Modify and 8 to confirm the changes (or) 9 to "
                            "cancel")
                        continue

                # Get the updated information
                if menu == 8:
                    if values[3] == "CR":
                        cur.execute("SELECT ExpCatID FROM ExpenseCategories WHERE Name = 'Income'")
                        exp = cur.fetchone()
                        values[5] = exp[0]

                    # Update the bank account
                    cur.execute(
                        "UPDATE Statement SET BankID = ?, Amount = ?, PaymentType = ?, Payee = ?, ExpCatID = ?, "
                        "Description = ?, TransactionDate = ? WHERE TransID = ?",
                        (values[0], values[1], values[2], values[3], values[4], values[5], values[6], transID))
                    # Check if the bank account was updated
                    if cur.rowcount > 0:
                        # Log the update
                        log.Logger.insertlog(cur=cur, userID=userID, transID=transID,
                                             message="Expense Transaction Updated Successfully")
                        conn.commit()
                        print("\nYour Transaction Details has been updated successfully!")
                    else:
                        raise dbe.OperationalError("Unexpected Error Encountered! Sorry for the inconvenience")
                if menu == 9:
                    return

        except Exception as e:
            print(e)

    # Deleting Expense Transaction
    @staticmethod
    def delExpenseTransaction(conn, cur, userID):
        try:
            # Fetching TransID based User Selection
            transID = ExpenseLogging.getTransID(cur=cur, userID=userID)

            if transID <= 0:
                print("\nNo transaction found!")
            else:
                while True:
                    # Getting confirmation from the user for deleting the expense category
                    confirm = input(
                        "\nWARNING: This will delete your transaction permanently. Would you like to proceed (Y/N)?")[
                        0].upper()

                    if confirm[0] == "Y" or confirm[0] == "N":
                        break
                    else:
                        print("\nInvalid choice! Please enter Y  or N ")
                        continue

                if confirm[0] == "Y":
                    cur.execute("DELETE FROM Statement WHERE TransID = ?", (transID,))
                    expCatDel = cur.rowcount

                    if expCatDel > 0:
                        log.Logger.insertlog(cur=cur, userID=userID, transID=transID,
                                             message="Expense Transaction Deleted Successfully")
                        conn.commit()
                        print("\nYour Transaction has been deleted successfully!")
                    else:
                        raise dbe.OperationalError("Expense Transaction Deletion Failed")
                else:
                    print("\nAction Cancelled!")

        except Exception as e:
            print(e)