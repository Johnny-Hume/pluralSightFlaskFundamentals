from flask import Flask, render_template
from datetime import datetime

from model import db

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        message="Here's a message from the view"
        )


@app.route("/date")
def date():
    return "This page was served at "+str(datetime.now())


numberOfTimes = 0


@app.route("/stalker")
def stalker():
    global numberOfTimes
    numberOfTimes += 1
    return "This page has been viewed " + str(numberOfTimes) + " times!"


@app.route("/card")
def card_view():
    card = db[0]
    return render_template("card.html", card=card)
