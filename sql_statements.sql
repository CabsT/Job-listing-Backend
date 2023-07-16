CREATE TABLE job_applications (
  id SERIAL PRIMARY KEY,
  jobId INTEGER,
  full_name VARCHAR(255) ,
  email VARCHAR(255),
  cover_letter VARCHAR(3000),
  cv_file BYTEA
);