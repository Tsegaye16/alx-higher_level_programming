-- Displaying the all rows that has not null value from second_table
SELECT name, score FROM second_table WHERE name != '' ORDER BY score DESC;
