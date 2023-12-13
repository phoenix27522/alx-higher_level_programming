-- Check if the database exists first
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Check if the table exists
SELECT COUNT(*)
FROM information_schema.tables
WHERE table_schema = 'hbtn_0d_usa' 
AND table_name = 'states';

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id), UNIQUE (id));
