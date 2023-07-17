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
  jobtitle VARCHAR(255),
  companyname VARCHAR(255), 
  description TEXT ,
  qualification VARCHAR(255),
  employmentstatus VARCHAR(255),
  location VARCHAR(255),
  contact VARCHAR(255),
  closingdate VARCHAR(255)
);
