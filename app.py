from flask import Flask
app = Flask(__name__)

@app.route("/")from flask import Flask


from flask import current_app, g
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello,oui!"




def home():
    return "Hello, Flask !"