# Importing Libraries and Modules
import authentication as auth

class controller():
    def __init__(self) -> None:
        self.userID = 0
        pass

    # Application Entry Controller Function for Authentication
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
                userID = auth.authorization.login(conn=conn, cur=cur)
            elif option == 2:  # New User Registration
                userID = auth.authorization.register(conn=conn, cur=cur)
            elif option == 3:  # Forgot Password
                userID = auth.authorization.frgtPwd(conn=conn, cur=cur)
            elif option == 4:  # Forgot Username
                userID = auth.authorization.frgtUsn(conn=conn, cur=cur)
            elif option == 5:  # Exit the application
                exit()

            # Check for userID and if not logged in redirects back to authentication page
            if userID <= 0:
                controller.authentication(conn=conn, cur=cur)
            else:
                controller.application(conn=conn, cur=cur, userID=userID)

        except Exception as e:
            print(f"\n{e}\nPlease try again later.")

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
                print("User Profile")
            elif module == 2:  # Bank Integration Section
                print("Bank Integrations")
            elif module == 3:  # Expense Category Management Section
                print("Expense Category Management")
            elif module == 4:  # Income Tracking Section
                print("Income Tracking")
            elif module == 5:  # Expense Logging Section
                print("Expense Logging")
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