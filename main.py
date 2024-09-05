from flask import Flask
from flask import render_template
from flask import request
from sql import Sql
# from markupsafe import escape

app = Flask(__name__)
count = 0

setup = Sql.SqlSetup('test.db')
setup.createDatabaseFromFile()

@app.route("/")
def hello_world():
    if 'playGameBtn' in request.form:
        return render_template('test.html')
    return render_template('index.html')

@app.route("/doguess", methods=['POST'])
def test():
    if request.method == 'POST':
        if 'randomNumberSubmitBtn' in request.form:
            count += 1
    return render_template("index.html")