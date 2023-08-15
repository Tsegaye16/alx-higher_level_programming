--Grouping the rows fo second_table table that have the same score
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
