from flask import Flask 

# create an instance of the now import module Class Flask (name variable) instance variable  
app = Flask(__name__) 

# this object doesn't exist yet | we are trying to transcend circular/cyclical dependency 
from app import routes
