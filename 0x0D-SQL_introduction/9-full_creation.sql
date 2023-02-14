-- creates a table 'second_table' in the database hbtn_0c_0 in my mysql server
-- and add multiple rows
-- the database name will be passed as an argument to the mysql command
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

INSERT INTO second_table
VALUES (1, "John", 10),
	(2, "Alex", 3),
	(3, "Bob", 14),
	(4, "George", 8);
