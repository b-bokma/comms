# OPEN TODOS

* user test the pages. Find places what can be improved and write this down. Having a to-do list is also good for the results
* clear database from test data
* create production ready pages

# CS50 Final Project

For the Final Project I have created a web app aimed at PR and Communication teams, where they can keep track of requests that have come in from journalists.

## Challenges
I have build the register and login pages myself, using parts of the CS50 library.
All online tutorials use SQLAlchemy, database models and classes for this, but I wanted to do this in raw SQL to get a better understanding of what is happening under the hood.

### Database
* This project is database heavy. I have designed the database following database normalization, the "Toxi method" http://howto.philippkeller.com/2005/04/24/Tags-Database-schemas/ 
* I have created the tables and SQL Query via this online tool: https://ondras.zarovi.cz/sql/demo/
* The query is MySQL, this is transformed to SQLite using: https://ww9.github.io/mysql2sqlite/
* The queries are stored in this repo under table_schema.sql and the database is created by running init.db. (and the schema file is invalid when comments are used ..)
* With the file test_data_db.sql the database is populated with dummy data.

### Login and Register
Flask-login gives a method to use a plugin for registration, login and logout, however this makes use of the SQLAlchemy ORM, and I decided to build the app without.
With a little help of the CS50 library (login_required decorator) I was able to build the pages myself using flask-session.

## Installation

* install all dependencies using `pip install -r requirements.txt`
* setup your database credentials by creating a `.env` file that contains 
SECRET_KEY=''
DATABASE="sqlite:///"
FLASK_ENV=development
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=
* initiate the database using `python init_db.py`
* This fills the database with some dummy data from `python test_data_db.sql`. If you want an empty DB, comment out this function
* run `flask run` to start the application 

## Improvements

* Add edit forms for journalists and media outlets
* Add possibility to label and group questions
* add possibility to add multiple journalists to one question
* add page to view all questions one journalists has asked