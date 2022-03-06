import sqlite3

class GameDb:
    def __init__(self, arg):
        self.sqliteConnection = sqlite3.connect('Solitaire.db')
        self.cursor = self.sqliteConnection.cursor()

        if arg == "del":
            self.deleteTable()

        # Creating table
        tableQuery = """ CREATE TABLE IF NOT EXISTS SCORES (
                    Name VARCHAR(20) NOT NULL,
                    Moves INTEGER NOT NULL,
                    Time INTEGER NOT NULL,
                    Score INTEGER NOT NULL
                ); """

        if arg == "test":
            self.createTestData()

        self.cursor.execute(tableQuery)
        self.sqliteConnection.commit()

    def addWinner(self, winnerName, moves, time):
        print(winnerName, moves, time, self.createScore(moves,time))
        insertNewWinner = f""" INSERT INTO SCORES 
                        (Name, Moves, Time, Score)
                        VALUES ('{winnerName}', {moves}, {time}, {self.createScore(moves, time)});
                    """
        self.cursor.execute(insertNewWinner)
        self.sqliteConnection.commit()

    def createTestData(self):
        insertTestData = """ INSERT INTO SCORES 
                        (Name, Moves, Time, Score)
                        VALUES ('Bob', 45, 320, 5000);
                    """
        self.cursor.execute(insertTestData)
        self.sqliteConnection.commit()

    def getData(self):
        showData = """
                    SELECT ROWID, *
                    FROM SCORES
                    ORDER BY Score ASC
                """

        data = []
        for row in self.cursor.execute(showData):
            data.append(row)
        return data

    def deleteTable(self):
        deleteTable = """
                        DROP TABLE SCORES
                    """
        self.cursor.execute(deleteTable)
        self.sqliteConnection.commit()

    def createScore(self, moves, time):
        return moves * 4 + time