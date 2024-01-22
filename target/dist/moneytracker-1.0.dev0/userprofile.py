# Importing Libraries and Modules
import pyodbc as dbe
import logger as log

class userProfile:

    # View User Profile
    def getProfile(conn, cur, userID):
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
                    log.logger.insertlog(conn=conn, cur=cur, userID=userID, transID=0,
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