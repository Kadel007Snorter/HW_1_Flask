from flask import Flask
import flask

print("# Flask is", flask.__version__)

app = Flask(__name__)


@app.route("/hello/flask/")
def hell0_flask():
    return "<p><h1>Hello from Flask application!</h1></p>"


@app.route("/")
def start():
    return "Go to <a href=\"http://localhost:5000/hello/flask\">Hello from flask</a> to see another message"


app.run()

# if you want directly go to the page:
# http://localhost:5000/hello/flask
