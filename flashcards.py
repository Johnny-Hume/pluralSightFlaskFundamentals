from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to my flash cards application!"


@app.route("/date")
def date():
    return "This page was served at "+str(datetime.now())


numberOfTimes = 0


@app.route("/stalker")
def stalker():
    global numberOfTimes
    numberOfTimes += 1
    return "This page has been viewed " + str(numberOfTimes) + " times!"
