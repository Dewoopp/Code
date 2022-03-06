import sqlite3

class GameDb:
    def __init__(self, arg):
        # Creates the connection
        self.sqliteConnection = sqlite3.connect('Solitaire.db')
        # Creates the cursor which is used to hold the data after running the query
        self.cursor = self.sqliteConnection.cursor()

        # Checks the argument for a delete command
        if arg == "del":
            self.deleteTable()

        # Checks the argument for a test case command
        if arg == "test":
            self.createTestData()

        # Query to create table if it doesnt exist
        tableQuery = """ CREATE TABLE IF NOT EXISTS SCORES (
                    Name VARCHAR(20) NOT NULL,
                    Moves INTEGER NOT NULL,
                    Time INTEGER NOT NULL,
                    Score INTEGER NOT NULL
                ); """

        # Executes the create table query
        self.cursor.execute(tableQuery)
        self.sqliteConnection.commit()

    # Inserts a new user into the database
    def addWinner(self, winnerName, moves, time):
        # print(winnerName, moves, time, self.createScore(moves,time))
        # Runs an insert query using the parameters passed into the function and creating the score
        insertNewWinner = f""" INSERT INTO SCORES 
                        (Name, Moves, Time, Score)
                        VALUES ('{winnerName}', {moves}, {time}, {self.createScore(moves, time)});
                    """
        self.cursor.execute(insertNewWinner)
        self.sqliteConnection.commit()

    # Creates the test data, ths is used when running a test argument
    def createTestData(self):
        # Inserts a simple test case into the scores table
        insertTestData = """ INSERT INTO SCORES 
                        (Name, Moves, Time, Score)
                        VALUES ('Bob', 45, 320, 5000);
                    """
        self.cursor.execute(insertTestData)
        self.sqliteConnection.commit()

    # Gets the data, which is displayed on the home screen
    def getData(self):
        # Simply selects all the data, which is sorted by score
        showData = """
                    SELECT ROWID, *
                    FROM SCORES
                    ORDER BY Score ASC
                """

        data = []
        for row in self.cursor.execute(showData):
            data.append(row)
        return data

    # Deletes the table
    def deleteTable(self):
        deleteTable = """
                        DROP TABLE SCORES
                    """
        self.cursor.execute(deleteTable)
        self.sqliteConnection.commit()

    # Generates the score from the moves and the time
    def createScore(self, moves, time):
        return moves * 4 + time