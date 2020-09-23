from flask import Flask
app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "Hello, world!"

@app.route("/goodbye")
def goodbye():
    return "Goodbye, cruel world"
    
if __name__ == "__main__":
    helloWorld