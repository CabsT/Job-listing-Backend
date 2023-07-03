from flask import Flask
from flask_cors import CORS

#The 'app' object is an instance of the Flask class
# Uing __name__ as the argument to use the current module as the name of the application package.
app = Flask(__name__) 
CORS(app)  # Allow Cross-Origin Resource Sharing
