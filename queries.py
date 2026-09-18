## Required libraries (install from terminal before running this script!)
## pip install sqlalchemy pandas pymysql

## Note, this example should work for diverse DBMS.
## If you're working with MySQL specifically, you can also use:
## Terminal
## pip install mysql-connector-python

# db_connection.py
import sqlalchemy ###Or: #### import mysql.connector
import pandas as pd
import pymysql # Driver to connect to MySQL, alternatives: mysqlclient, mysql-connector-python.

from sqlalchemy import create_engine, text 
from sqlalchemy.engine import URL

# --- CONNECTION SETUP ---
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy.exc import OperationalError

# 1. Load environment variables
load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_port = int(os.getenv("DB_PORT", 3306))
db_name = os.getenv("DB_NAME", "MockdataGood")

# 2. Connect to MySQL server root to ensure the database exists
server_url = URL.create(
    drivername="mysql+pymysql",
    username=db_user,
    password=db_password,
    host=db_host,
    port=db_port,
    database   = db_name           # replace with your database name
)

connection_url = URL.create(
    drivername = "mysql+pymysql",   # change for different DBMS
    username   = "root",            # replace with your username
    password   = "Almos55%",    # replace with your password
    host       = "localhost",       # replace with your host
    port       = 3306,              # replace with your port, example port for MySQL and MariaDB.
    database   = "sakila"           # replace with your database name
)

engine = create_engine(connection_url)

##Other ports for different DBMS; check documnetation of the DBMS as well!:
## PostgreSQL: 5432 
## SQL Server: 1433
## Oracle: 1521
## MariaDB: 3306 (same as MySQL)
## SQLite: No port needed (file-based database)

# %%
# --- BASIC QUERY + DISPLAY ---
df = pd.read_sql("SELECT * FROM Bicycle LIMIT 10;", engine)
print(df)

# %%
# --- DML EXAMPLE (INSERT/UPDATE/DELETE) ---
# For write operations, use execute() instead of pd.read_sql()
# connection.execute() in SQLAlchemy expects an executable SQLAlchemy object. Therefore, wrap the string with text():
with engine.connect() as connection:
    connection.execute(text("UPDATE actor SET first_name = 'PENNY' WHERE actor_id = 1;"))
    connection.commit()

# %%
# --- CLOSE CONNECTION ---
engine.dispose()
