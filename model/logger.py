#  docs : https://www.w3schools.com/python/python_mysql_select.asp
from utils import db

sqlcmd = db.conn()

def log():

    sql = "INSERT INTO logger (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    sqlcmd.execute(sql, val)

    db.conn.commit()

    return {"rowcount" : sqlcmd.rowcount}

def logs():

    sqlcmd.execute("SELECT * FROM logger")

    return sqlcmd.fetchall()