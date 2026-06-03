from flask import Flask, session, render_template, request, redirect, url_for, jsonify
import json
import os
import random

app = Flask(__name__)

app.secret_key = 'your_secret_key'

# ----------------------------------------------------
# page links
@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/basic')
def basic():
    return render_template('basic.html')

@app.route('/pro')
def pro():
    return render_template('pro.html')
   
@app.route('/rare')
def rare():
    return render_template('rare.html')

@app.route('/care')
def care():
    return render_template('care.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/terms_and_conditions')
def terms_and_conditions():
    return render_template('terms_and_conditions.html')

@app.route('/cart')
def cart():
    
    cart = session.get('cart', {})

    for product_id in cart:
        cart[product_id]['price'] +=(random.random()*2)
        cart[product_id]['price'] = round(cart[product_id]['price'],2)
        cart[product_id]['quantity'] +=1
    session['cart'] = cart

    return render_template('cart.html')


# ----------------------------------------------------
# python-json functions
def load_products():
    base_path = os.path.dirname(os.path.abspath(__file__))   # Location of the script
    file_path = os.path.join(base_path, 'static', 'data', 'products.json')
    with open(file_path, 'r') as f:
        return json.load(f)

def get_product(product_id):
    return products.get(product_id)

# ----------------------------------------------------
# html linkage functions
user_tracker = 0
def updateUserTracker():
    global user_tracker
    user_tracker +=1
    return user_tracker


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    
    
    user_id = session.get('id')
    if (user_id == None):
        user_id = updateUserTracker()
        session['id'] = user_id

    product_id = request.get_json().get('product_id') #product_id from the request
    product = get_product(product_id)

    if not product:
        return jsonify({'status': 'error', 'message': 'Product not found'}), 404

    cart = session.get('cart', {}) #the current session's cart object or create a blank object {}

    #increase quantity if in the cart alreeady, otherwise, make the quantity 1
    if product_id in cart: #if it is already on the list, increase the quantity
        cart[product_id]['quantity'] += 1
    else: #if it is not on the cart list, add it to the object with quantity 1
        cart[product_id] = {
            'name': product['name'],
            'price': product['price'],
            'quantity': 1
        }
    session['cart'] = cart #update the cart object

    print(f"User: {user_id} added {product['name']} to cart")
    print(f"Current User Cart: {session['cart']}")
    
    return jsonify({'status': 'success'})

@app.route('/get_cart', methods=['GET'])
def get_cart():
    cart = session.get('cart', {})
    return jsonify(cart)


products = load_products()
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)