-- script that displays the average temperatures (fahrenheit) by city ordered by temperature descending
-- first import temperature.sql dump file in to 'hbtn_0c_0'
-- the database name will be passed as an argument to the mysql command

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
