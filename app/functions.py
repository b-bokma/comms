import sqlite3
from sqlite3 import Error
from config import Config
from flask import session,redirect
from functools import wraps
from flask import request

####
# DB
####

# make DB connection
def db_conn(db=Config.DATABASE):
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)
    
    conn.row_factory = sqlite3.Row
    
    return conn

# make DB query
def db_query(conn,sql,values=None):
    c = conn.cursor()
    if values:
        if isinstance(values,tuple) is False:
            values = (values,)
        c.execute(sql,values)
    else: 
        c.execute(sql)
    conn.commit()
    return c


####
# Login
####

def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function