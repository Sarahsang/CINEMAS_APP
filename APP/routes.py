from flask import Flask, render_template, request
from APP import app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/book_ticket', methods=['POST'])
def book_ticket():
    # Invoke your Controller and Model logic here
    return render_template('confirmation.html')
