CREATE TABLE jobs (
  id SERIAL PRIMARY KEY,
  jobtitle VARCHAR(255),
  description VARCHAR(255),
  qualification TEXT,
  employmentstatus TEXT,
  location VARCHAR(255),
  contact VARCHAR(255)
