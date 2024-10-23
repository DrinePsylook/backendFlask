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

@app.route("/table/customer")
def customer_page():
    db_con = sqlite3.connect("flaskr/data.db")
    cur = db_con.cursor()
    sql_request = "SELECT * FROM customer LIMIT 50" 
    res = cur.execute(sql_request)
    resultat = res.fetchall()
    column_names = [description[0] for description in cur.description]
    db_con.close()  
    return render_template('customer.html', customers=resultat, column_names=column_names)

@app.route("/table/product")
def product_page():
    db_con = sqlite3.connect("flaskr/data.db")
    cur = db_con.cursor()
    sql_request = "SELECT * FROM product LIMIT 50" 
    res = cur.execute(sql_request)
    resultat = res.fetchall()
    column_names = [description[0] for description in cur.description]
    db_con.close()  
    return render_template('product.html', products=resultat, column_names=column_names)

@app.route("/table/customer_order")
def customer_order_page():
    db_con = sqlite3.connect("flaskr/data.db")
    cur = db_con.cursor()
    sql_request = "SELECT * FROM customer_order LIMIT 50" 
    res = cur.execute(sql_request)
    resultat = res.fetchall()
    column_names = [description[0] for description in cur.description]
    db_con.close()  
    return render_template('customer_order.html', customer_orders=resultat, column_names=column_names)

@app.route("/table/order_detail")
def order_detail_page():
    db_con = sqlite3.connect("flaskr/data.db")
    cur = db_con.cursor()
    sql_request = "SELECT * FROM order_detail LIMIT 50" 
    res = cur.execute(sql_request)
    resultat = res.fetchall()
    column_names = [description[0] for description in cur.description]
    db_con.close()  
    return render_template('order_detail.html', order_details=resultat, column_names=column_names)