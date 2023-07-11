from flask import Flask, request
from flask_cors import CORS
#Import the db class from the db.py file 
from db import db

#The 'app' object is an instance of the Flask class
# Uing __name__ as the argument to use the current module as the name of the application package.
app = Flask(__name__) 
CORS(app)  # Allow Cross-Origin Resource Sharing


@app.route('/')
def main():
    return "Job Listing HomePage"

@app.route('/jobs')
def get_jobs():
    db_instance = db('jobs')
    job_data = db_instance.select()
    return (job_data)
