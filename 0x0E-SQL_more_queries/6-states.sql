-- creating the database hbtn_0d_usa with table states
-- the table state hast two columns with some constraint
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(id INT NOT NULL AUTO_INCEREMENT primary key, name VARCHAR(256) NOT NULL);
