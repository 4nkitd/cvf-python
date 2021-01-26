import mysql.connector, os

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USERNAME")
db_pass = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

conn = mysql.connector.connect(
  host= db_host,
  user= db_user,
  password= db_pass,
  database= db_name
)

db_conn = conn.cursor()

def conn():
    return db_conn

    