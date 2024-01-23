# Importing Libraries and Modules
import src.main.python.authentication as auth
import src.main.python.userprofile as profile
import src.main.python.bankintegrations as bank
import src.main.python.expensecategories as expcat
import src.main.python.incometracking as income
import src.main.python.expenselogging as expense

class Controller:
    def __init__(self) -> None:
        self.userID = 0
        pass

    # Application Entry Controller Function for Authentication
    @staticmethod
    def authentication(conn, cur):
        try:
            # Initializing userID
            userID = 0

            # Entry Selection
            print(
                "\n1. Login"
                "\n2. Register"
                "\n3. Forgot Password"
                "\n4. Forgot Username"
                "\n5. Exit Application"
            )

            # Input Selection Check based on the above message
            while True:
                option = int(input("\nChoose an option (1-5): "))
                if option in range(1, 6):
                    break
                else:
                    print("Invalid option. Please enter a number from 1 to 5")
                    continue

            # Function call based on the Input
            if option == 1:  # Logging In
                userID = auth.Authorization.login(conn=conn, cur=cur)
            elif option == 2:  # New User Registration
                userID = auth.Authorization.register(conn=conn, cur=cur)
            elif option == 3:  # Forgot Password
                userID = auth.Authorization.frgtPwd(conn=conn, cur=cur)
            elif option == 4:  # Forgot Username
                userID = auth.Authorization.frgtUsn(cur=cur)
            elif option == 5:  # Exit the application
                exit()

            # Check for userID and if not logged in redirects back to authentication page
            if userID <= 0:
                Controller.authentication(conn=conn, cur=cur)
            else:
                Controller.application(conn=conn, cur=cur, userID=userID)

        except Exception as e:
            print(f"\n{e}\nPlease try again later.")

    @staticmethod
    def application(conn, cur, userID):
        try:
            # Module Selection
            print(
                "\n1. User Profile"
                "\n2. Bank Integrations"
                "\n3. Expense Category Management"
                "\n4. Income Tracking"
                "\n5. Expense Logging"
                "\n6. Transaction History"
                "\n7. Expense Analysis"
                "\n8. Data Export"
                "\n9. Exit Application"
            )

            # Module Selection Check based on the above message
            while True:
                module = int(input("\nChoose an option (1-9): "))
                if module in range(1, 10):
                    break
                else:
                    print("Invalid choice. Please enter a number from 1 to 9.")

            # Function call based on the Module Selection
            if module == 1:  # User Profile Section
                Controller.usrProfileController(conn=conn, cur=cur, userID=userID)
            elif module == 2:  # Bank Integration Section
                Controller.bankIntegrationAction(conn=conn, cur=cur, userID=userID)
            elif module == 3:  # Expense Category Management Section
                Controller.expenseCategoryAction(conn=conn, cur=cur, userID=userID)
            elif module == 4:  # Income Tracking Section
                Controller.incomeTrackingAction(conn=conn, cur=cur, userID=userID)
            elif module == 5:  # Expense Logging Section
                Controller.expenseLoggingAction(conn=conn, cur=cur, userID=userID)
            elif module == 6:  # Transaction History Section
                print("Transaction History")
            elif module == 7:  # Expense Analysis Section
                print("Expense Analysis")
            elif module == 8:  # Data Export Section
                print("Data Export")
            elif module == 9:  # Exit Application
                exit()

        except Exception as e:
            print(f"\nError in Application: {e}\nPlease try again later.")

    @staticmethod
    def usrProfileController(conn, cur, userID):
        try:
            # User Profile Module Selection
            print(
                "\nUser Profile:"
                "\n1. Get User Account Details"
                "\n2. Update User Account Details"
                "\n3. Change Password"
                "\n4. Delete User Account Details"
                "\n5. Upgrade to Premium Account"
                "\n6. Log Out"
                "\n7. Back to Module Selection"
            )

            # Menu Selection Check based on the above message
            while True:
                menu = int(input("\nChoose an option (1-7): "))

                if menu in range(1, 8):
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 to 7.")
                    continue

            # Function call based on the Menu Selection
            if menu == 1:
                profile.UserProfile.getProfile(cur=cur, userID=userID)
            elif menu == 2:
                profile.UserProfile.updProfile(conn=conn, cur=cur, userID=userID)
            elif menu == 3:
                profile.UserProfile.updPassword(conn=conn, cur=cur, userID=userID)
            elif menu == 4:
                profile.UserProfile.delAccount(conn=conn, cur=cur, userID=userID)
            elif menu == 5:
                profile.UserProfile.upgradeAccount(conn=conn, cur=cur, userID=userID)
            elif menu == 6:
                print("You are successfully logged out!")
                Controller.authentication(conn=conn, cur=cur)
            elif menu == 7:
                Controller.application(conn=conn, cur=cur, userID=userID)
                return

            Controller.usrProfileController(conn=conn, cur=cur, userID=userID)

        except Exception as e:
            print(f"\nError in User Profile Module: {e}\nPlease try again later.")

    @staticmethod
    def bankIntegrationAction(conn, cur, userID):
        try:
            # Bank Integrations Module Selection
            print(
                "\nBank Integrations:"
                "\n1. Get Bank Account Details"
                "\n2. Add Bank Account"
                "\n3. Update Bank Account Details"
                "\n4. Delete Bank Account"
                "\n5. Back to Module Selection"
            )

            # Menu Selection Check based on the above message
            while True:
                menu = int(input("\nChoose an option (1-5): "))

                if menu in range(1, 6):
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 to 5.")
                    continue

            # Function call based on the Menu Selection
            if menu == 1:
                bank.BankIntegration.getBankAccount(cur=cur, userID=userID)
            elif menu == 2:
                bank.BankIntegration.addBankAccount(conn=conn, cur=cur, userID=userID)
            elif menu == 3:
                bank.BankIntegration.updBankAccount(conn=conn, cur=cur, userID=userID)
            elif menu == 4:
                bank.BankIntegration.delBankAccount(conn=conn, cur=cur, userID=userID)
            elif menu == 5:
                Controller.application(conn=conn, cur=cur, userID=userID)
                return

            Controller.bankIntegrationAction(conn=conn, cur=cur, userID=userID)

        except Exception as e:
            print(f"\nError in Bank Integrations Module: {e}\nPlease try again later.")

    @staticmethod
    def expenseCategoryAction(conn, cur, userID):
        try:
            # Expense Categories Module Selection
            print(
                "\nExpense Categories:"
                "\n1. Get Expense Categories"
                "\n2. Add Expense Category"
                "\n3. Update Expense Category"
                "\n4. Delete Expense Category"
                "\n5. Back to Module Selection"
            )

            # Menu Selection Check based on the above message
            while True:
                menu = int(input("\nChoose an option (1-5): "))

                if menu in range(1, 6):
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 to 5.")
                    continue

            if menu == 1:
                expcat.ExpenseCategories.getExpenseCategories(cur=cur, userID=userID)
            elif menu == 2:
                expcat.ExpenseCategories.addExpenseCategory(conn=conn, cur=cur, userID=userID)
            elif menu == 3:
                expcat.ExpenseCategories.updExpenseCategory(conn=conn, cur=cur, userID=userID)
            elif menu == 4:
                expcat.ExpenseCategories.delExpenseCategory(conn=conn, cur=cur, userID=userID)
            elif menu == 5:
                Controller.application(conn=conn, cur=cur, userID=userID)
                return

            Controller.expenseCategoryAction(conn=conn, cur=cur, userID=userID)

        except Exception as e:
            print(f"\nError in Expense Categories Module: {e}\nPlease try again later.")

    @staticmethod
    def incomeTrackingAction(conn, cur, userID):
        try:
            # Income Tracking Module Selection
            print(
                "\nIncome Tracking:"
                "\n1. Get All Income Transactions"
                "\n2. Add an Income Transaction"
                "\n3. Update an Income Transaction"
                "\n4. Delete an Income Transaction"
                "\n5. Back to Module Selection"
            )

            # Menu Selection Check based on the above message
            while True:
                menu = int(input("\nChoose an option (1-5): "))

                if menu in range(1, 6):
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 to 5.")
                    continue

            if menu == 1:
                income.IncomeTracking.getIncomeTransactions(cur=cur, userID=userID)
            elif menu == 2:
                income.IncomeTracking.addIncomeTransaction(conn=conn, cur=cur, userID=userID)
            elif menu == 3:
                income.IncomeTracking.updIncomeTransaction(conn=conn, cur=cur, userID=userID)
            elif menu == 4:
                income.IncomeTracking.delIncomeTransaction(conn=conn, cur=cur, userID=userID)
            elif menu == 5:
                Controller.application(conn=conn, cur=cur, userID=userID)
                return

            Controller.incomeTrackingAction(conn=conn, cur=cur, userID=userID)

        except Exception as e:
            print(f"\nError in Income Tracking Module: {e}\nPlease try again later.")

    def expenseLoggingAction(conn, cur, userID):
        try:
            # Expense Logging Module Selection
            print(
                "\nExpense Logging:"
                "\n1. Get All Expense Transactions"
                "\n2. Add an Expense Transaction"
                "\n3. Update an Expense Transaction"
                "\n4. Delete an Expense Transaction"
                "\n5. Back to Module Selection"
            )

            # Menu Selection Check based on the above message
            while True:
                menu = int(input("\nChoose an option (1-5): "))

                if menu in range(1, 6):
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 to 5.")
                    continue

            if menu == 1:
                expense.ExpenseLogging.getExpenseTransactions(cur=cur, userID=userID)
            elif menu == 2:
                expense.ExpenseLogging.addExpenseTransaction(conn=conn, cur=cur, userID=userID)
            elif menu == 3:
                print("Update an Expense Transaction")
            elif menu == 4:
                print("Delete an Expense Transaction")
            elif menu == 5:
                Controller.application(conn=conn, cur=cur, userID=userID)
                return

            Controller.expenseLoggingAction(conn=conn, cur=cur, userID=userID)

        except Exception as e:
            print(f"\nError in Expense Logging Module: {e}\nPlease try again later.")