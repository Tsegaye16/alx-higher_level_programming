-- select two or more columns from two table by inner join
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
