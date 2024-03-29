# Importing Libraries and Modules
import pyodbc as dbe
import src.main.python.logger as log


class UserProfile:

    # View User Profile
    @staticmethod
    def getProfile(cur, userID):
        try:
            cur.execute("SELECT Name, Gender, DOB, Email, UserName, PremiumUser from Users WHERE UserID = ?", (userID,))

            row = cur.fetchone()

            if not row:
                raise Exception("No profile found for the given UserID")

            columns = list(map(lambda x: x[0], cur.description))

            # Display the result with columns as headers
            for column, value in zip(columns, row):
                print(f"{column}: {value[0] if isinstance(value, tuple) else value}")

        except Exception as e:
            print(e)

        # Updating User Profile

    @staticmethod
    def updProfile(conn, cur, userID):
        try:
            # Fetching User info for the UserID in the database
            cur.execute("SELECT Name, Gender, DOB, Email from Users WHERE UserID = ?", (userID,))
            values = cur.fetchone()

            # Menu Selection Check based on the above message
            while True:
                # Print the update options
                print(
                    "\nPlease update a particular using the Number: "
                    "\n1. Name"
                    "\n2. Gender"
                    "\n3. DOB"
                    "\n4. Email"
                    "\n5. Confirm Changes"
                    "\n6. Cancel Update"
                )

                menu = int(input(
                    "Please enter a number between (1-4) to make changes and 5 to confirm changes and 6 to cancel: "))
                if menu in range(5, 7):
                    break
                elif menu in range(1, 5):
                    # Get the updated information
                    if menu == 1:
                        name = input("Enter the name you want to update: ")
                        values = (name,) + values[1:]  # Update name
                    elif menu == 2:
                        gender = input("Enter the gender you want to update: ").upper()
                        values = (values[0], gender[0]) + values[2:]  # Update gender
                    elif menu == 3:
                        dob = input("Enter the DOB(YYYY-MM-DD) you want to update: ")
                        values = (values[0], values[1], dob) + values[3:]  # Update DOB
                    elif menu == 4:
                        email = input("Enter the email you want to update: ")
                        values = (values[0], values[1], values[2], email)  # Update email
                    continue
                else:
                    print("Invalid choice. Please enter a number between (1-4) to make changes and 5 to confirm "
                          "changes and 6 to cancel: ")
                    continue

            # Update the Changes
            if menu == 5:
                # Update the user profile
                cur.execute("UPDATE Users SET Name = ?, Gender = ?, DOB = ?, Email = ? WHERE UserID = ?",
                            (values[0], values[1], values[2], values[3], userID))

                # Check if the user was updated
                if cur.rowcount > 0:
                    # Log the update
                    log.Logger.insertlog(cur=cur, userID=userID, transID=0,
                                         message="User Profile updated "
                                                 "successfully")
                    conn.commit()
                    print("Your profile has been updated successfully!")
                else:
                    raise dbe.OperationalError("User Profile Updation Failed")
            else:
                print("Profile Updation Cancelled!")
                return

        except Exception as e:
            print(e)

    # Delete Account
    @staticmethod
    def delAccount(conn, cur, userID):
        try:
            while True:

                confirm = \
                    input("WARNING: This will delete your account permanently. Would you like to proceed (Y/N)?")[
                        0].upper()

                if confirm[0] == "Y" or confirm[0] == "N":
                    break
                else:
                    print("Invalid choice! Please enter Y  or N ")
                    continue

            if confirm[0] == "Y":
                cur.execute("DELETE FROM Users WHERE UserID = ?", (userID,))

                usrDel = cur.rowcount

                if usrDel > 0:
                    cur.execute("DELETE FROM BankDetails WHERE UserID = ?", (userID,))
                    cur.execute("DELETE FROM Statement WHERE UserID = ?", (userID,))
                    cur.execute("DELETE FROM ExpenseCategories WHERE UserID = ?", (userID,))
                    log.Logger.insertlog(cur=cur, userID=userID, transID=0,
                                         message="User Account deleted successfully")
                    conn.commit()
                    print("Your profile has been deleted successfully!")
                    exit()
                else:
                    raise dbe.OperationalError("User Profile Deletion Failed")
            else:
                print("Action Cancelled!")

        except Exception as e:
            print(e)

    # Change Password
    @staticmethod
    def updPassword(conn, cur, userID):
        try:
            while True:
                password = input("Please enter the new password: ")
                if len(password) >= 8:
                    break
                else:
                    print("Password should be at least 8 characters long.")
                    continue

            cur.execute("UPDATE Users SET Password = ? WHERE UserID = ?", (password, userID,))

            pwd_upd = cur.rowcount

            if pwd_upd > 0:
                log.Logger.insertlog(cur=cur, userID=userID, transID=0,
                                     message="User password updated successfully")
                conn.commit()
                print("Your password has been updated successfully!")
            else:
                raise dbe.OperationalError("User Password Updation Failed")

        except Exception as e:
            print(e)

    # Upgrade Account
    @staticmethod
    def upgradeAccount(conn, cur, userID):
        try:
            # Get the license key to Upgrade to Premium Account
            license = int(input("Enter the license code to upgrade: "))

            if license == 12345:
                cur.execute("UPDATE Users SET PremiumUser = 'Y' WHERE UserID = ?", (userID,))
                upgrade = cur.rowcount

                if upgrade > 0:
                    log.Logger.insertlog(cur=cur, userID=userID, transID=0,
                                         message="User upgraded to premium user!")
                    conn.commit()
                    print("Congratulations! You now have been upgraded to premium user!")
                else:
                    raise dbe.OperationalError("User Profile Deletion Failed")
            else:
                raise Exception("Your License Code is Invalid!")

        except Exception as e:
            print(e)
