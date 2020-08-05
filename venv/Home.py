# Simple Web App using Flask Framework
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# In default, the app will run local machine in http://127.0.0.1:5000/
# app.run()

# If you want host the application in the network using a IP & Port
app.run(port=5000,host='0.0.0.0')