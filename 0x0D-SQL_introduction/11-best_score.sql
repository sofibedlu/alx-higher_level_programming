-- lists all records with a score >= 10 in the table 'second_table' of database hbtn_0c_0
-- in the mysql server
-- results should display both score and name (in this order)
-- records should be ordered by score (top first)
-- database name will be passed as an argument of the mysql command
SELECT score, name
	FROM second_table
	WHERE score >= 10
	ORDER BY score DESC
