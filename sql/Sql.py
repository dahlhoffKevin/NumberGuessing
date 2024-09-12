import sqlite3
import os

class SQL:
    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.Connection
        self.cursor = sqlite3.Cursor

    def open_conn(self):
        try:
            self.conn = sqlite3.connect(self.db, check_same_thread=False)
            self.cursor = self.conn.cursor()
            return self.conn
        except:
            return "SQL.open_conn: Error while opening database connection"
    
    def create_game(self, connection, gameId, playerId, numberOfAttempts):
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Game (GameId, PlayerId, NumberOfAttempts) VALUES (?, ?, ?)', 
                            (gameId, playerId, numberOfAttempts))
        connection.commit()

    def createDatabaseFromFile(self):
        print(f'Working in: {os.getcwd()}')
        try:
            print('Creating database...')
            self.conn = sqlite3.connect(f'{os.getcwd()}/sql/{self.db}')
            self.cursor = self.conn.cursor()

            #sql script lesen
            print('Creating tables in database...')
            with open(f'{os.getcwd()}/sql/main.sql', 'r') as sql_file:
                sql_script = sql_file.read()
            
            #sql script ausführen
            self.cursor.executescript(sql_script)
            self.conn.commit()
            self.conn.close()
            print('Database created successfully!')
        except Exception as ex:
            print(f'Error while creating database: {ex}')

    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass