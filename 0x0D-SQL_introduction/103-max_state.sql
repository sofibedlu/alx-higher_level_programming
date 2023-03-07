-- a script that displays the max temperature of each state (ordered by State name).
-- first import dump file temperatures.sql into 'hbtn_0c_0' database

SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
