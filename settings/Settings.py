import os

class Settings:
    DatabaseName = "numberGuessing.db"
    DatabaseSubpath = "/sql/"
    DatabasePath = f'{os.getcwd()}{DatabaseSubpath}{DatabaseName}'
    