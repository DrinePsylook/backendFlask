from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home_page.html")


@app.route("/table/<table>", methods=['GET'])
def sql_table(table):
    connexion = sqlite3.connect('data.db')
    cursor = connexion.cursor()
    cursor.execute(f"SELECT * FROM {table} limit 50")
    data = cursor.fetchall()
    #liste = ['id', 'country', 'invoice_nb', 'invoice_date', 'customer_id', 'quantity', 'order_id', 'product_id', 'description', 'price']
    column_name = [description[0] for description in cursor.description]
    connexion.close()
    return render_template("data_page.html", table=table, data=data, column_name=column_name)


""" if table == 'customer':
        liste = ['Id', 'Country']
    if table == 'customer_order':
        liste = ['Id', 'Invoice number', 'Invoice date', 'Customer Id']
    if table == 'order_detail':
        liste = ['Id', 'Quantity', 'Order Id', 'Product Id']
    if table == 'product':
        liste = ['Id', 'Description', 'Price'] """

    
@app.route("/table", methods=['GET'])
def table_join():
    connexion = sqlite3.connect('data.db')
    cursor = connexion.cursor()
    cursor.execute('''SELECT customer.id as 'ID', country as 'Country', invoice_nb as 'Invoice Number', 
                   invoice_date as 'Invoice Date', customer_id as 'Customer ID', quantity as 'Quantity', 
                   order_id as 'Order ID', product_id as 'Product ID', description as 'Description', price as 'Price'
                   FROM customer 
                   LEFT JOIN customer_order 
                    ON customer.id = customer_order.customer_id
                   LEFT JOIN order_detail 
                    ON customer_order.id = order_detail.order_id
                   LEFT JOIN product 
                    ON order_detail.product_id = product.id
                   ORDER BY customer.id
                   limit 150 ''')
    data = cursor.fetchall()
    column_name = [description[0] for description in cursor.description]
    
    
    return render_template("data_page.html", data=data, column_name=column_name)


