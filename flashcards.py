from flask import Flask, render_template

from model import db

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        message="Here's a message from the view"
        )


numberOfTimes = 0


@app.route("/count")
def countNumberOfViews():
    global numberOfTimes
    numberOfTimes += 1
    return "This page has been viewed " + str(numberOfTimes) + " times!"


@app.route("/card")
def card_view():
    card = db[0]
    return render_template("card.html", card=card)
