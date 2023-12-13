-- Replace 'your_database_name' with your actual database name
USE your_database_name;

-- Check if the table exists first
SELECT COUNT(*)
FROM information_schema.tables
WHERE table_schema = DATABASE() 
AND table_name = 'force_name';

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
