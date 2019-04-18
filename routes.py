from flask import Flask, render_template

app = Flask(__name__) #Flask initialize

@app.route("/")
def hello():
    return render_template('index.html')
