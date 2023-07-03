from flask import Flask
from flask_cors import CORS

#The 'app' object is an instance of the Flask class
# Uing __name__ as the argument to use the current module as the name of the application package.
app = Flask(__name__) 
CORS(app)  # Allow Cross-Origin Resource Sharing

##HomePage -> In Progress
@app.route('/')
def main():
    return "Job Listing HomePage"

#Route and function to render the 'Job Form' -> In progress
@app.route('/add-job')
def add_job():
    return "Job Form"


