-- Check if the database exists first
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Check if the user exists
SELECT COUNT(*)
FROM mysql.user
WHERE user = 'user_0d_2';

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'%' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on hbtn_0d_2 to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'%';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
