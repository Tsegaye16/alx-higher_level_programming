-- joining the table by inner join with aggregate function
SELECT title, SUM(rate) AS rating FROM tv_shows INNER JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id GROUP BY title
ORDER BY rating DESC;
