import sqlite3

class GameDb:
    def __init__(self):
        self.sqliteConnection = sqlite3.connect('Solitaire.db')
        self.cursor = self.sqliteConnection.cursor()

        # Creating table
        tableQuery = """ CREATE TABLE IF NOT EXISTS SCORES (
                    Name VARCHAR(20) NOT NULL,
                    Moves INTEGER NOT NULL,
                    Time INTEGER NOT NULL,
                    Score INTEGER NOT NULL
                ); """
 
        self.cursor.execute(tableQuery)
        self.sqliteConnection.commit()

    def createTestData(self):
        insertTestData = """ INSERT INTO SCORES 
                        (Name, Moves, Time, Score)
                        VALUES ('Bob', 45, 320, 2000);
                    """
        self.cursor.execute(insertTestData)
        self.sqliteConnection.commit()

    def getData(self):
        showData = """
                    SELECT ROWID, *
                    FROM SCORES
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