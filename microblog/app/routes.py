from flask import render_template 
from app import app

@app.route('/') # this is a decorator
@app.route('/index')
def index():
    user = {'username': 'hood'} 
    return render_template('index.html', title='Home', user=user) 
