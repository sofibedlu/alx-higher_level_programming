-- create the table 'unique_id' on mysql server
-- unique_id description:
--	id INT with the default value 1 and must be unique
--	name VARCHAR(256)
-- database name will be passed as an argument of the mysql command

CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
