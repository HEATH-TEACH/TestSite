from flask import Flask, session, render_template, request, redirect, url_for
import json 

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)