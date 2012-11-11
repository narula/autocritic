from flask import Flask, url_for, request, render_template
from parse import parse_sample

# python server.py
# Super hacky lightweight server which outputs data

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/3")
def index():
    return render_template('index.html')

@app.route("/2")
def index2():
    return render_template('index-narrow.html')

@app.route("/")
def index2():
    return render_template('index-flip-arg.html', results=parse_sample())
    
if __name__ == "__main__":
    app.run(debug=True)
