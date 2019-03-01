from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('forms/basic_form.html')
    elif request.method == 'POST':
        kwargs = {
            'title': request.form['title'],
            'isbn': request.form['isbn'],
            'submit_value': request.form['submit'],
        }
        database = kwargs["title"]
        table    = kwargs["isbn"]
        
        db  = pymysql.connect(host="localhost", port=3306, user="root", passwd="giridhar", db=database )
        cursor = db.cursor()
        
        sql = "select * from " + table
        cursor.execute(sql)
        details = [ ",".join(row) for row in cursor.fetchall()]
        
        return render_template(
            'forms/basic_form_result.html', data = details)
