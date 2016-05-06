from flask import Flask, render_template, g, request
import os
import json

import sqlite3

DATABASE = 'submissions.db'

app = Flask(__name__)

app.debug = True



def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        
        with db:
            db.execute('CREATE TABLE IF NOT EXISTS sellers (seller_id integer primary key,title text,name text,email text,telephone text,make text,model text,registration text,date text,comment text)')
        
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



@app.route('/')
@app.route('/index.html')
def homepage():
    return render_template('index.html')




@app.route('/Stock.html')
def stock():
    return render_template('Stock.html')



@app.route('/SellMyCar.html', methods=["GET", "POST"])
def sellmycar():
    
    if request.method == "POST":
        
        
        title = request.form['title']
        name = request.form['name']
        email = request.form['email']
        telephone = request.form['telephone']
        make = request.form['make']
        model = request.form['model']
        registration = request.form['registration']
        date = request.form['date']
        comment = request.form['comment']
        
        conn = get_db()
        
        with conn:
            query = 'INSERT INTO sellers (title,name,email,telephone,make,model,registration,date,comment) VALUES(?,?,?,?,?,?,?,?,?)'
            conn.execute(query, (title, name, email, telephone, make, model, registration, date, comment))
        
        
        response = {"message": "Success"}
        
        return json.dumps(response)
        
        
        
    else:
        return render_template('SellMyCar.html')



@app.route('/Finance.html')
def finance():
    return render_template('Finance.html')
@app.route('/AboutUs.html')
def aboutus():
    return render_template('AboutUs.html')
@app.route('/ContactUs.html')
def contactus():
    return render_template('ContactUs.html')


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))



