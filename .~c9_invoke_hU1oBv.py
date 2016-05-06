from flask import Flask, render_template
import os

import sqlite3
from flask import g

DATABASE = '/path/to/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
    return render_template('Stock.html')


app = Flask(__name__)

app.debug = True


@app.route('/')
@app.route('/index.html')
def homepage():
    return render_template('index.html')




@app.route('/Stock.html')
def stock():
    return render_template('Stock.html')



@app.route('/SellMyCar.html')
def sellmycar():
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



