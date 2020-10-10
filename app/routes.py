from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
from flask import current_app as app

from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

from config import Config
from app.functions import db_conn, db_query, login_required
from app.queries import table_overview, question_page

from time import sleep


### Index
@app.route("/")
@app.route("/index.html")
@login_required
def home():

    # home page table
    output = []
    c = db_query(conn=db_conn(), sql=table_overview)
    res = c.fetchall()
    
    for row in res:
        output.append(dict(row))

    # details popup
    question_details = []
    c = db_query(conn=db_conn(), sql=question_page)
    res = c.fetchall()

    for row in res:
        question_details.append(dict(row))

    return render_template("home.html",table=output, details=question_details)


### Login screens

@app.route("/login", methods=["GET","POST"])
def login():
    error=None
    if request.method == "POST":
        
        # make query to DB to retrieve user information
        conn = db_conn()        
        c = db_query(conn=conn,sql = "SELECT * FROM users")
        result = c.fetchall()
        
        # check entered values with DB entries, if correct login
        for r in result:
            if request.form['email'] == r['email'] and check_password_hash(password=request.form['password'], pwhash=r['hash']):
                session['user_id'] = r['id']
                return redirect(url_for("home"))                
        #else return error
        error = "error"
                
    return render_template("login.html", alert=error)


@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('user_id', None)
   return redirect(url_for('home'))
   

@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']

        if password != confirm: #check if passwords are the same
            print("reached if statement")
            return render_template("register.html", alert="error")
        else: #check if the email address is already in use
            c = db_query(conn=db_conn(),sql="SELECT * FROM users WHERE email=?",values=(email))
            res = c.fetchone()
            if res:
                return render_template("register.html", alert="known")
            else: # add to db
                db_query(conn=db_conn(), sql="INSERT INTO users(email,hash) VALUES(?,?)",values=(email,generate_password_hash(password) ))
            return render_template("login.html", alert="success")

    return render_template("register.html")


#Default Navigation Items 
@app.route("/journalists")
@login_required
def journalists():
    return render_template("journalists.html")

@app.route("/media")
@login_required
def media():
    return render_template("media.html")

@app.route('/questions', methods=['GET','POST'])
@app.route('/questions/', methods=['GET','POST'])
@login_required
def questions():
    c = None
    # extract list of priorities to send to select fields
    statusses = []
    c = db_query(conn=db_conn(),sql = "SELECT * FROM status;")
    result = c.fetchall()
    
    for r in result:
        statusses.append(dict(r))


    # extract list of journalists to send to select fields
    journalists = []
    c = db_query(conn=db_conn(),sql = "SELECT * FROM journalists;")
    result = c.fetchall()
    
    for r in result:
        journalists.append(dict(r))

    # extract list of journalists to send to select fields
    spokespersons = []
    c = db_query(conn=db_conn(),sql = "SELECT * FROM spokespersons;")
    result = c.fetchall()
    
    for r in result:
        spokespersons.append(dict(r))

    return render_template("questions.html", questions=questions, journalists=journalists, spokespersons=spokespersons, statusses=statusses)

@app.route('/questions_add', methods=['GET','POST'])
@app.route('/questions_add/', methods=['GET','POST'])
@login_required
def questions_add():
    
    if request.method == "POST":
        subject = request.form['subject']
        question = request.form['question']
        status_id = request.form['status']
        journalist_id = request.form['journalist']
        deadline = request.form['deadline']
        spokesperson_id = request.form['spokesperson']

        c = db_query( #query to update table questions
            conn=db_conn(), 
            sql = "INSERT INTO questions(subject,question,status_id,deadline,spokesperson_id) VALUES(?,?,?,?,?)", 
            values = (subject,question,status_id,deadline,spokesperson_id)
            )
        lastrowid = c.lastrowid

        c = db_query( # query to update mapping journalists
            conn=db_conn(), 
            sql = "INSERT INTO QuestionJournalistMap(question_id,journalist_id) VALUES(?,?)", 
            values = (lastrowid,journalist_id)
            )
        if c:
            return redirect( url_for('home'))

        


@app.route("/themes")
@login_required
def themes():

    return render_template("themes.html")

# User Profile
@app.route("/profile")
@login_required
def profile():

    return render_template("profile.html")