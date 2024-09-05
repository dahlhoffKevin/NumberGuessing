import sqlite3

class SQL:
    def __init__(self, db):
        self.db = db
        self.con = ''

    def open_conn(self):
        try:
            self.con = sqlite3.connect(self.db)
            self.cursor = self.con.cursor
            return self.con
        except:
            return "SQL.open_conn: Error while opening database connection"