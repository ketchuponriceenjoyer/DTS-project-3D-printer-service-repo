from flask import Flask, render_template, request, redirect
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

Database = ''

@app.route('/')
def render_homepage():
    return render_template('Home.html')

@app.route('/Session', methods=['POST','GET'])
def render_Sessionpage():
    if request.method == 'POST':
        Name = request.form.get('Name')
        Address = request.form.get('Address')
        Filament = request.form.get('Filament')
        Size = request.form.get('Size')
        Model = request.form.get('Model_File')
    return render_template('Session.html')

@app.route('/images')
def render_imagespage():
    return render_template('images.html')

if __name__ == '__main__':
    app.run()