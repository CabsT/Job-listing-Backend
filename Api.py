from flask import Flask, request
from flask_cors import CORS
#Import the db class from the db.py file 
from db import db
import config 
#The 'app' object is an instance of the Flask class
# Uing __name__ as the argument to use the current module as the name of the application package.
app = Flask(__name__) 
CORS(app)  # Allow Cross-Origin Resource Sharing

db_jobs = db('jobs')
db_job_applications = db('job_applications')


@app.route('/')
def main():
    return "Job Listing HomePage"

@app.route('/add-job', methods=['POST'])
def add_job():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if content_type != 'application/json':
            return {'message': 'Unsupported Media Type'}

    job_data = request.json
    db_jobs.insert(job_data)
    return {'message': 'Job submitted successfully!'}

@app.route('/jobs', methods=['GET'])
def get_jobs():
    job_data = db_jobs.select()
    jobs = []
    for row in job_data:
            job = {
                'id': row[0],
                'jobtitle': row[1],
                'companyname': row[2],
                'description': row[3],
                'qualification': row[4],
                'employmentstatus': row[5],
                'location': row[6],
                'contact': row[7],
                'closingdate': row[8]
            }
            jobs.append(job)

        
    return ({'jobs': jobs})



@app.route('/jobs/<int:id>', methods=['GET'])
def get_job_details(id):
    job_data = db_jobs.get_job_by_id(id)
    if job_data:
        job = {
            'id': job_data[0],
            'jobtitle': job_data[1],
            'companyname': job_data[2],
            'description': job_data[3],
            'qualification': job_data[4],
            'employmentstatus': job_data[5],
            'location': job_data[6],
            'contact': job_data[7],
            'closingdate': job_data[8]
        }
        return (job)
    else:
        return ({'error': 'Job not found'})
    
@app.route('/jobs/<int:id>/apply', methods=['POST'])
def apply_for_job(id):
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if content_type != 'application/json':
            return {'message': 'Unsupported Media Type'}

        application_data = request.json

      
        application_data = {
            'jobId': id,
            'full_name': application_data.get('full_name'),
            'email': application_data.get('email'),
            'cover_letter': application_data.get('cover_letter'),
            'cv_file': application_data.get('cv_file')
            
        }

        db_job_applications.insert_application(application_data)
        return {'message': 'Application submitted successfully'}

        

if __name__ == '__main__':
    app.run()