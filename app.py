from flask import Flask,render_template
import sqlite3
app = Flask(__name__)
@app.route("/hello")
def hello():
    return "<div>Hello World</div>"
@app.route("/")
def home():
    connexion = sqlite3.connect("data.db")
    cursor= connexion.cursor()
    return "Hello, Flask!"

                           

@app.route("/table/customer_order")
def sql_table4():
    connexion = sqlite3.connect("data.db")
    print(type(connexion))
    cursor = connexion.cursor()
    sql_request = f"SELECT * FROM customer_order limit 50"
    data= cursor.execute(sql_request).fetchall()
    print(data)

    return render_template("customer_order.html",data=data)

@app.route("/table/order_detail")
def sql_table3():
    connexion = sqlite3.connect("data.db")
    print(type(connexion))
    cursor = connexion.cursor()
    sql_request = f"SELECT * FROM order_detail limit 50"
    data= cursor.execute(sql_request).fetchall()
    print(data)

    return render_template("order_detail.html",data=data)


@app.route("/table/product")
def sql_table1():
    connexion = sqlite3.connect("data.db")
    print(type(connexion))
    cursor = connexion.cursor()
    sql_request = f"SELECT * FROM product limit 50"
    data= cursor.execute(sql_request).fetchall()
    print(data)
    

    return render_template("product.html",data=data)

@app.route("/table/customer")
def sql_table2():
    connexion = sqlite3.connect("data.db")
    print(type(connexion))
    cursor = connexion.cursor()
    sql_request = f"SELECT * FROM customer limit 50"
    data= cursor.execute(sql_request).fetchall()
    print(data)

    return render_template("customer.html",data=data)