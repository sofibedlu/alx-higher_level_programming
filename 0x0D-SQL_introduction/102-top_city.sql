-- a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- first import dump file temperatures.sql into 'hbtn_0c_0' database

SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
