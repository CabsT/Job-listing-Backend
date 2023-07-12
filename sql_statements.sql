CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    jobtitle VARCHAR(255),
    description TEXT,
    qualification VARCHAR(255),
    employmentstatus VARCHAR(255),
    location VARCHAR(255),
    contact VARCHAR(255)
);
