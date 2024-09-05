import sqlite3
import os

class SQL:
    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.Connection

    def open_conn(self):
        try:
            self.conn = sqlite3.connect(self.db)
            self.cursor = self.conn.cursor()
            return self.conn
        except:
            return "SQL.open_conn: Error while opening database connection"
        
class SqlSetup:
    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.Connection
        self.cursor = sqlite3.Cursor
    
    def createDatabaseFromFile(self):
        print(f'Working in: {os.getcwd()}')
        try:
            self.conn = sqlite3.connect(self.db)
            self.cursor = self.conn.cursor()
            
            with open('/Users/kevindahlhoff/Documents/Schule/LF10a/Python Flask/sql/main.sql', 'r') as sql_file:
                sql_script = sql_file.read()
                
            self.cursor.executescript(sql_script)
            self.conn.commit()
            self.conn.close()
        except Exception as ex:
            print(f'Error while reading sql script: {ex}')