from flask import Flask
from flask import render_template
from flask import request
from sql import Sql
from settings.Settings import Settings
import os
# from markupsafe import escape

app = Flask(__name__)
count = 0

if not os.path.exists(Settings.DatabasePath):
    setup = Sql.SqlSetup(Settings.DatabasePath)
    setup.createDatabaseFromFile()

@app.route("/")
def hello_world():
    return render_template('index.html')