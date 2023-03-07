-- script that lists the number of records with the same score in the table 'second_table' of the database 'hbtn_0c_0' in MySQL server.
-- the result display <score>, number of records for this 'score' with the label 'number'
-- list sorted by the number of records (descending)
-- the database name will be passed as an argument to the mysql command

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC
