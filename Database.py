import sqlite3
import InsertionSort
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
                """
        # I decided to use an insertion sort to sort my data
        data = []
        for row in self.cursor.execute(showData):
            data.append(row)

        # Creates a list of the scores of the people in the leaderboard
        scoreData = [row[3] for row in data]
        # Use the insertion sort to sort the score
        InsertionSort.insertionSort(scoreData)

        # The insertion sort sorts a single column, the score
        # as we need the whole data set to change with the position of the score changing
        # we need to move the data from data to a sorted list called sortedData
        sortedData = []
        for i in range(len(scoreData)):
            for row in data:
                # If the score we are checking is the same as the score of the row we are checking
                if scoreData[i] == row[3]:
                    # Add it to the sortedData list
                    sortedData.append(row)
                    # Removes it from the data list, which is necessary if two scores are the same, there wont be duplicate entries in the sortedData
                    data.remove(row)
                    break
                    
        return sortedData

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