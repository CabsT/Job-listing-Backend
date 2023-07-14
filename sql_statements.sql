CREATE TABLE jobs (
  id SERIAL PRIMARY KEY,
  jobtitle VARCHAR(255),
  companyname TEXT,
  description TEXT,
  qualification TEXT,
  employmentstatus TEXT,
  location VARCHAR(255),
  contact VARCHAR(255),
  closingdate VARCHAR(255)
);