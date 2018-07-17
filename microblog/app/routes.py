from app import app

@app.route('/') # this is a decorator
@app.route('/index')
def index():
    return 'Hello, Aeon!' 
