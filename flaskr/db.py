import sqlite3

import click
from flask import current_app, g

DATABASE = 'flaskr/data.db'


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config[DATABASE],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
    

def init_app(app):
    app.teardown_appcontext(close_db)

def read_db(query, one=False):
    cur = get_db().execute(query)
    rv = cur.fetchall()
    return (rv[0] if rv else None) if one else rv
