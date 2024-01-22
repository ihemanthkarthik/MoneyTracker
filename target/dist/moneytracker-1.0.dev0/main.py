# Importing Libraries and Modules
import connection
import controller

class MoneyTracker:
    def __init__(self):
        try:
            print("Welcome to Money Tracker Application! Easy way to track money")

            # Connecting to database
            conn, cur = connection.getConnection()

            controller.controller.authentication(conn=conn, cur=cur)

        except Exception as e:
            print(f"An error occurred while initializing the application: {e}")

if __name__ == "__main__":
    MoneyTracker()