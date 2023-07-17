CREATE TABLE job_applications (
  id SERIAL PRIMARY KEY,
  jobId INTEGER,
  fullName VARCHAR(255) ,
  email VARCHAR(255),
  coverLetter VARCHAR(3000),
  cvFile BYTEA
);

CREATE TABLE jobs (
  id SERIAL PRIMARY KEY,
  jobtitle VARCHAR(255),,
  companyname TEXT, 
  description TEXT ,
  qualification TEXT,
  employmentstatus TEXT,
  location VARCHAR(255),
  contact VARCHAR(255),
  closingdate VARCHAR(255)
);