from flask import Flask
from flask import render_template
from flask import request
from sql import Sql
# from markupsafe import escape

app = Flask(__name__)
count = 0

setup = Sql.SqlSetup('numberGuessing.db')
setup.createDatabaseFromFile()

@app.route("/")
def hello_world():
    return render_template('index.html')