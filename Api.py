from flask import Flask, request
from flask_cors import CORS
#Import the db class from the db.py file 
from db import db
import config 
#The 'app' object is an instance of the Flask class
# Uing __name__ as the argument to use the current module as the name of the application package.
app = Flask(__name__) 
CORS(app)  # Allow Cross-Origin Resource Sharing

db_instance = db('jobs')

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
    db_instance.insert(job_data)
    return {'message': 'Job submitted successfully!'}, 200

@app.route('/jobs', methods=['GET'])
def get_jobs():
    job_data = db_instance.select()
    jobs = []
    for row in job_data:
            job = {
                'id': row[0],
                'jobtitle': row[1],
                'description': row[2],
                'qualification': row[3],
                'employmentstatus': row[4],
                'location': row[5],
                'contact': row[6]
            }
            jobs.append(job)

        
    return ({'jobs': jobs})
        

if __name__ == '__main__':
    app.run()
