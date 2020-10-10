import sqlite3
from time import sleep

############### Settings ####################
#DB Name
DB_NAME = "app/app.db"

#SQL File with Table Schema and Initialization Data
SQL_File_Name = "table_schema.sql"
##############################################

def db_init(db,schema):
    #Read Table Schema into a Variable and remove all New Line Chars
    TableSchema=""
    with open(schema, 'r') as SchemaFile:
        TableSchema=SchemaFile.read().replace('\n', '')

    #Connect or Create DB File
    conn = sqlite3.connect(db)
    curs = conn.cursor()

    #Create Tables
    if sqlite3.complete_statement(TableSchema):
        curs.executescript(TableSchema)
    else:
        print("Schema is not valid")

    #Close DB
    curs.close()
    conn.close()

    return

print("Creating tables")
db_init(db="app/app.db",schema="table_schema.sql")
print("Tables created")
print("Adding test data")
db_init(db="app/app.db",schema="test_data_db.sql")
print("Done")