from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from settings.Settings import Settings
from sql import Sql
import os
import uuid
from random import randint

sql = Sql.SQL(Settings.DatabasePath)
# handling database setup (db creation, table creation)
if not os.path.exists(Settings.DatabasePath):
    sql.createDatabaseFromFile()

# creating SQL object
conn = sql.open_conn()

# game variables
randomGameInt = randint(0, 101)
numberOfAttempts = 0

# create flask app
app = Flask(__name__, static_folder='static')

# generating unique game id
gameId = str(uuid.uuid4())

@app.route('/')
def hello_world():
    print(f'gameId: {gameId}')
    print(randomGameInt)
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_attempt():
    global numberOfAttempts  # Declare as global
    global randomGameInt  # Declare as global to use in comparison

    player_name = 'Testplayer' #fetch playername
    number = request.form.get('number')
    print(number)
    # get player id from player_name?
    temp_userID = str(uuid.uuid4())

    numberOfAttempts += 1

    if int(number) == int(randomGameInt):
        sql.create_game(conn, gameId, temp_userID, numberOfAttempts)
        print("you have won")
        return render_template('won.html')

    return redirect(url_for('hello_world'))

if __name__ == '__main__':
    app.run(debug=True)