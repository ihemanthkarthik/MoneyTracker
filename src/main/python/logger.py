import datetime

class Logger:
    @staticmethod
    def insertlog(cur, userID, transID, message):
        try:
            timestamp = datetime.datetime.now()
            cur.execute("INSERT INTO Logs (UserID, TransID, LogDescription, LogDateTime) VALUES (?, ?, ?, ?)",(userID, transID, message, timestamp))
        except Exception as e:
            print("Error in logging the transaction : ",e)