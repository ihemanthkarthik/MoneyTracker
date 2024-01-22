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

