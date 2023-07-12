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

@app.route('/add-job', methods=['POST'])
def add_job():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if content_type != 'application/json':
            return {'message': 'Unsupported Media Type'}, 415

        job_data = request.json
        # Process the job_data and save it to the database or perform any required operations

        return {'message': 'Job submitted successfully!'}, 200

if __name__ == '__main__':
    app.run()