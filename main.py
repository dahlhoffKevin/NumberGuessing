import sqlite3
from flask import Flask, flash, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
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
app.secret_key = 'LctYxG3mcQGhZ6DeVLdkxD0cEWe2Ye3axJ3vecg5emE='

# generating unique game id
gameId = str(uuid.uuid4())

@app.route('/')
def hello_world():
    print(f'gameId: {gameId}')
    print(randomGameInt)
    return render_template('login.html')

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


# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        playername = request.form['playername']
        mailaddress = request.form['mailaddress']
        password = request.form['password']

        # Create a unique player ID
        player_id = str(uuid.uuid4())
        # Hash the password
        hashed_password = generate_password_hash(password)

        # Insert player into the database
        conn.execute('INSERT INTO Player (PlayerId, Playername, MailAdress, Password) VALUES (?, ?, ?, ?)',
                     (player_id, playername, mailaddress, hashed_password))
        conn.commit()

        # Flash a success alert message
        flash('Welcome to the Guessing Number Game!', 'success')
        session['playername'] = playername;
        return redirect(url_for('success'))

    return render_template('register.html')


# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mailaddress = request.form['mailaddress']
        password = request.form['password']

        try:
            # Open a new connection using the SQL object
            conn = sql.open_conn()

            # Retrieve the player from the database by mail address
            player = conn.execute('SELECT * FROM Player WHERE MailAdress = ?', (mailaddress,)).fetchone()
            print(player);

            if player is None:
                flash('Invalid email address or password.', 'error')
                return redirect(url_for('login'))

            db_password = player[3]
            print(db_password)
            # Check the password
            if check_password_hash(db_password, password):
                flash(f'Welcome {player[1]}! You can play now.', 'success')
                session['playername'] = player[0];
                session['playername'] = player[1];
                return redirect(url_for('success'))
            else:
                flash('Invalid email address or password.', 'error')

        except sqlite3.Error as e:
            flash(f"Database error: {str(e)}", 'error')

        finally:
            if conn:
                conn.close()

    return render_template('login.html')

@app.route('/success')
def success():
    #playername = session.get('playername')
    playername = session.get('playername')
    if not playername:
        return redirect(url_for('login'))
    return render_template('index.html', playername=playername)


if __name__ == '__main__':
    app.run(debug=True)