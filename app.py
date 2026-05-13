from flask import Flask, session, render_template, request, redirect, url_for
import json 

app = Flask(__name__)

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
    return render_template('cart.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)