USE hbtn_0d_usa; -- Replace with your database name

-- Find the state_id for California
SET @california_id := (SELECT id FROM states WHERE name = 'California');

-- List all cities in California
SELECT *
FROM cities
WHERE state_id = @california_id
ORDER BY cities.id ASC;
