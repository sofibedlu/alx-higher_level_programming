-- script that lists all records of the table 'second_table' of the database 'hbtn_0c_0' in MySQL server.
-- Don’t list rows without a 'name' value
-- Results are display the score and the name (in this order)
-- Records are listed by descending 'score'
-- The database name will be passed as an argument to the mysql command

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
