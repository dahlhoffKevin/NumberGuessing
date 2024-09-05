from flask import Flask
from flask import render_template
from flask import request
# from markupsafe import escape

app = Flask(__name__)
count = 0

@app.route("/", methods=['POST'])
def hello_world():
    if 'playGameBtn' in request.form:
        return render_template('index.html')
    return render_template('start.html')

@app.route("/doguess", methods=['POST'])
def test():
    if request.method == 'POST':
        if 'randomNumberSubmitBtn' in request.form:
            count += 1
    return render_template("index.html")