from flask import Flask, session, render_template, request, redirect, url_for
import json 

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)