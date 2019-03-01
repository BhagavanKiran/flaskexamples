import pymysql
from flask import Flask, render_template


app = Flask(__name__)

def connect_db():
    return pymysql.connect(host="localhost", port=3306, user="root", passwd="giridhar", db="schlumberger" )


@app.route('/')
def hello_world():
    db  = connect_db()
    cursor = db.cursor()
    sql = "select * from realestate"
    cursor.execute(sql)
    details = [ ",".join(row) for row in cursor.fetchall()]
    return render_template('database/authors.html', authors=details)
