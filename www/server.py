from flask import Flask, url_for, request, render_template
from parse import *

# python server.py
# Super hacky lightweight server which outputs data

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/")
def index():
    return render_template('index-flip-arg.html', results=get_results())
    
if __name__ == "__main__":
    app.run(debug=True)
