from flask import Flask, render_template
import sqlite3
from flaskr.db import read_db
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/simple-page")
def simple_page():
    fruits = ['orange', 'banane', 'fraise']
    return render_template('simple_page.html', fruits=fruits)

@app.route('/table/<name>')
def sql_table(name):
    db_con = sqlite3.connect("flaskr/data.db")
    cur = db_con.cursor()
    sql_request = f"SELECT * FROM {name} LIMIT 50"
    res = cur.execute(sql_request)
    resultat = res.fetchall()
    return render_template('tables.html', tables=resultat, name=name)