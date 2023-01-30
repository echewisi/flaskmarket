from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


db= SQLAlchemy(app)

class Item(db.Model):
    name= db.Column(db.String(length= 30), nullable= False, unique= True)
    price= db.Column(db.Integer(), nullable= False)
    barcode= db.Column()

@app.route('/')
@app.route('/home')
def hello_page():
    return render_template('home.html')

@app.route('/market')
def marketpage():
    items=[
        {'id':1, 'name': 'phone', 'barcode':'128393827389', 'price':500},
        {'id':2, 'name':'computer', 'barcode':'23543998949', 'price': 900},
        {'id':3, 'name': 'radio', 'barcode': '234567009384', 'price': 600},
    ]
    
    return render_template('market.html', items=items)

# @app.route('/about/<username>')
# def about_page(username):
#     return f'this is the about page of {username}'
