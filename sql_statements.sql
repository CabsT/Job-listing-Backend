CREATE TABLE job_applications (
  id SERIAL PRIMARY KEY,
  jobId INTEGER,
  fullName VARCHAR(255) ,
  email VARCHAR(255),
  coverLetter VARCHAR(3000),
  cvFile BYTEA
);