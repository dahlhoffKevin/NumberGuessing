from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from settings.Settings import Settings
from sql import Sql
import os

if not os.path.exists(Settings.DatabasePath):
    sqlSetup = Sql.SqlSetup(Settings.DatabaseName)
    sqlSetup.createDatabaseFromFile()

app = Flask(__name__, static_folder='static')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_attempt():
    # implement code

    return redirect(url_for('hello_world'))

if __name__ == '__main__':
    app.run(debug=True)