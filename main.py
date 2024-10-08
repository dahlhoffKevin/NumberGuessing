import sqlite3
from flask import Flask, flash, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
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
numberOfAttempts = 1
result = ''

# create flask app
app = Flask(__name__, static_folder='static')
app.secret_key = 'LctYxG3mcQGhZ6DeVLdkxD0cEWe2Ye3axJ3vecg5emE='

# generating unique game id
gameId = str(uuid.uuid4())

@app.route('/')
def home():
    print(randomGameInt);
    # Check if user is logged in
    logged_in = session.get('logged_in')
    if logged_in:
        return render_template('index.html', logged_in=True)
    else:
        return render_template('home.html', logged_in=False)

@app.route('/submit', methods=['POST'])
def submit_attempt():
    global numberOfAttempts  # Declare as global
    global randomGameInt  # Declare as global to use in comparison
    global player_id

    number = request.form.get('number')
    player_id = session.get('playerId')
    if not number or not number.strip().isdigit():
        flash('You must enter a valid number!', 'error')
        return redirect(url_for('success'))
    
    number = int(number)

    if number > randomGameInt:
        result = 'too large'
        numberOfAttempts += 1
        flash('Try Gessing again!', 'error')
    elif number < randomGameInt:
        result = 'too small'
        numberOfAttempts += 1
        flash('Try Gessing again!', 'error')
    elif number == randomGameInt:
        player_id = session.get('playerId')
        result = 'winning'
        #Store data to game table
        print(gameId, player_id, numberOfAttempts)
        sql.create_game(conn, gameId, player_id, numberOfAttempts)
        return render_template('won.html')
    # Store the result in the session
    session['result'] = result

    # Redirect to the success page
    return redirect(url_for('success'))


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
        session['playerId'] = player_id;
        session['playername'] = playername;
        session['logged_in'] = True
        print(player_id)
        return redirect(url_for('login'))
    return render_template('register.html')


# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check if player is already logged in
    if 'playername' in session:
        return redirect(url_for('success'))
    if request.method == 'POST':
        mailaddress = request.form['mailaddress']
        password = request.form['password']
        try:
            # Open a new connection using the SQL object
            conn = sql.open_conn()
            # Retrieve the player from the database by mail address
            player = conn.execute('SELECT * FROM Player WHERE MailAdress = ?', (mailaddress,)).fetchone()
            if player is None:
                flash('Invalid email address or password.', 'error')
                return redirect(url_for('login'))
            db_password = player[3]
            # Check the password
            if check_password_hash(db_password, password):
                flash(f'Welcome {player[1]}! You can play now.', 'success')
                session['playerId'] = player[0];
                session['playername'] = player[1];
                session['logged_in'] = True
                return render_template('index.html', playername=player[1], logged_in=True)
            else:
                flash('Invalid email address or password.', 'error')
        except sqlite3.Error as e:
            flash(f"Database error: {str(e)}", 'error')
        finally:
            if conn:
                conn.close()
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/success')
def success():
    playername = session.get('playername')
    result = session.get('result', '')
    logged_in = session.get('logged_in')
    if not playername:
        return redirect(url_for('login'))
    return render_template('index.html', playername=playername, result=result, logged_in=logged_in)

if __name__ == '__main__':
    app.run(debug=True)