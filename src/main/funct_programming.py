import pyodbc as dbe
import src.main.python.logger as log
from typing import Callable, Optional, Tuple

def authenticate(conn: dbe.Connection, cur: dbe.Cursor) -> Callable[[str, str], Optional[int]]:
    """
    Returns a function for authenticating users. 
    
    ***** Final Data Structures *****
    This function returns a closure (login) that encapsulates the authentication logic. This closure operates on the final data structures (username and password) passed as arguments.
    
    ***** Use of Higher-Order Functions *****
    It is also an higher-order function that returns another function (login). This pattern allows for flexibility and composition.

    ***** Functions as Parameters and Return Values  *****
    This function takes conn and cur as parameters and returns the login function as the result.

    Args:
        conn (pyodbc.Connection): Database connection.
        cur (pyodbc.Cursor): Database cursor.

    Returns:
        Callable[[str, str], Optional[int]]: Function for user authentication.
    """
    def login(username: str, password: str) -> Optional[int]:
        """
        Authenticates users based on username and password.

        ***** Use of Closures/Anonymous Functions  *****
        This function is a closure that encapsulates the authentication logic and accesses the conn and cur variables from the outer scope.

        Args:
            username (str): User's username.
            password (str): User's password.

        Returns:
            Optional[int]: User ID if authentication is successful, None otherwise.
        """
        try:
            validate_username(username)
            validate_password(password)
            
            cur.execute("SELECT COUNT(*) FROM Users WHERE UserName = ?", (username,))
            usrCount = cur.fetchone()

            if usrCount[0] > 0:
                cur.execute("SELECT UserID FROM Users WHERE UserName = ? AND Password = ?", (username, password))
                values = cur.fetchone()

                if values is not None:
                    userID = values[0]
                    log.Logger.insertlog(cur=cur, userID=userID, transID=0, message="User Logged in Successfully")
                    print("You are now logged in!")
                    conn.commit()
                    return userID
                else:
                    raise ValueError("Username/Password incorrect")
            else:
                raise ValueError("No Account associated for the mentioned Username")
        except ValueError as ve:
            print(f"{ve}")
            return None

    def validate_username(username: str) -> None:
        """
        Validates the username. The functions validate_username is side-effect-free, as it performs validation without modifying external state.

        Args:
            username (str): User's username.

        Raises:
            ValueError: If the username is less than 5 characters long.
        """
        if len(username) < 5:
            raise ValueError("Username is minimum 5 characters long")

    def validate_password(password: str) -> None:
        """
        Validates the password. The functions validate_password is side-effect-free, as it performs validation without modifying external state.

        Args:
            password (str): User's password.

        Raises:
            ValueError: If the password is less than 8 characters long.
        """
        if len(password) < 8:
            raise ValueError("Password is minimum 8 characters long")

    return login

# Usage example:
def main():
    conn = dbe.connect("your_database_connection_string")
    cur = conn.cursor()

    # Create an authentication function
    authenticate_user = authenticate(conn, cur)

    # Use the authentication function
    user_id = authenticate_user("example_username", "example_password")

    if user_id:
        print("User ID:", user_id)
    else:
        print("Authentication failed.")

    conn.close()

if __name__ == "__main__":
    main()