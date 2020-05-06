# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import get_location


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    props = {

    }
    return render_template("index.html",props=props)

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == "POST":
        activity = request.form["activity"]
        location = get_location(activity)
        props = {
            "activity" : activity, 
            "location" : location
        }
        return render_template("results.html", props=props)
    else: 
        return "error"
