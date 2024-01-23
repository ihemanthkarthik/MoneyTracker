# Importing Libraries and Modules
import pyodbc as dbe
import src.main.python.logger as log

##### Login Module #####
class Authorization:

    ### User Login for MoneyTracker
    @staticmethod
    def login(conn, cur):
        try:
            while True:
                username = input("Username: ").lower()
                if len(username) >= 5:
                    break
                else:
                    print("Username is minimum 5 characters long")
                    continue

            cur.execute("SELECT COUNT(*) FROM Users WHERE UserName = ?", (username,))

            usrCount = cur.fetchone()

            if usrCount[0] > 0:
                while True:
                    password = input("Password: ")
                    if len(password) >= 8:
                        break
                    else:
                        print("Password is minimum 8 characters long")
                        continue

                if password != '':
                    cur.execute("SELECT UserID FROM Users WHERE UserName = ? AND Password = ?", (username, password))

                    values = cur.fetchone()
                    if values is not None:
                        userID = values[0]
                        log.Logger.insertlog(cur=cur, userID=userID, transID=0, message="User Logged in "
                                                                                        "Successfully")
                        print("You are now logged in!")
                        conn.commit()
                        return userID
                    else:
                        raise Exception("Username/Password incorrect")
                else:
                    raise ValueError("Please fill the password to login")
            else:
                raise Exception("No Account associated for the mentioned Username")
        except Exception as e:
            print(f"{e}")
            return -1

    ### New User Registration for MoneyTracker
    @staticmethod
    def register(conn, cur):
        try:
            email = input("Email: ").lower()

            cur.execute("SELECT COUNT(*) FROM Users WHERE Email = ?", (email,))

            usr_count = cur.fetchone()

            if usr_count is not None and usr_count[0] == 0:
                name = input("Name: ")
                gender = input("Gender: ")[0].upper()
                dob = input("Date of Birth(YYYY-MM-DD): ")

                while True:
                    username = input("Username: ").lower()
                    if len(username) >= 5:
                        break
                    else:
                        print("Username should be at least 5 characters long.")
                        continue

                while True:
                    password = input("Password: ")
                    if len(password) >= 8:
                        break
                    else:
                        print("Password should be minimum 8 characters long.")
                        continue

                cur.execute(
                    "INSERT INTO Users (Name, Gender, DOB, Email, UserName, Password, PremiumUser) VALUES (?, ?, ?, "
                    "?, ?, ?, 'N')",
                    (name, gender, dob, email, username, password))

                user_reg = cur.rowcount
                userID = cur.lastrowid

                if user_reg > 0:
                    log.Logger.insertlog(cur=cur, userID=userID, transID=0,
                                         message="User Created Successfully")
                    conn.commit()
                    print("You have been registered successfully!")
                    return 0
                else:
                    raise dbe.OperationalError("User Registration Failed")
            else:
                raise Exception("The mentioned email is already associated with an account")
        except Exception as e:
            print(f"{e}")
            return -1

    ### Reset Password for the User - Forgot Password Functionality
    @staticmethod
    def frgtPwd(conn, cur):
        try:
            username = input("Please enter your Username: ").lower()
            dob = input("please enter your Date of Birth(YYYY-MM-DD): ")

            cur.execute("SELECT UserID FROM Users WHERE UserName = ? AND DOB = ?", (username, dob))

            values = cur.fetchone()

            if values is not None:
                userID = values[0]

                while True:
                    password = input("Please enter the new password: ")
                    if len(password) >= 8:
                        break
                    else:
                        print("Password should be at least 8 characters long.")
                        continue

                cur.execute("UPDATE Users SET Password = ? WHERE UserID = ?", (password, userID))

                pwd_rst = cur.rowcount

                if pwd_rst > 0:
                    log.Logger.insertlog(cur=cur, userID=userID, transID=0,
                                         message="User Password Reset done successfully")
                    conn.commit()
                    print("Password has been reset successfully.")
                    return 0
                else:
                    raise dbe.OperationalError("Password was not updated successfully")
            else:
                raise Exception("No Data found for the mentioned Username and Date of Birth")

        except Exception as e:
            print(f"{e}")
            return -1

    ### Forgot UserName for login
    @staticmethod
    def frgtUsn(cur):
        try:
            email = input("Please enter your email: ").lower()

            cur.execute("SELECT Username from Users WHERE Email = ?", (email,))

            username = cur.fetchone()

            if username is not None and len(username) > 0:
                print(f"Your Username is {username[0]}")
                return 0
            else:
                raise Exception("No Account found for the mentioned email address")
        except Exception as e:
            print(f"{e}")
            return -1
