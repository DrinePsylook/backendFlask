from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/table/<name>')
def sql_table(name):
    db_con = sqlite3.connect("flaskr/data.db")
    cur = db_con.cursor()
    
    if name == "all":
        sql_request = '''SELECT customer.id AS numero_client, customer.country AS pays, co.id AS id_commande_client, co.invoice_nb AS numero_facture, co.invoice_date AS date_facture, od.id AS id_detail_commande, od.quantity AS quantite, product.id AS id_produit, product.description AS description, product.price As prix     
                            FROM customer 
                            LEFT JOIN customer_order as co
                                ON customer.id = co.customer_id
                            LEFT JOIN order_detail as od
                                ON co.id = od.order_id
                            LEFT JOIN product
                                ON od.product_id = product.id
                            ORDER BY customer.id
                            LIMIT 50'''
    else:
        sql_request = f"SELECT * FROM {name} LIMIT 50"

    res = cur.execute(sql_request)
    resultat = res.fetchall()

    active_onglet = {name}

    columns_name = [description[0] for description in cur.description]
    return render_template('tables_template.html', tables=resultat, name=name, col = columns_name, active_onglet=active_onglet)