from flask import Flask, render_template
app = Flask(__name__)



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
