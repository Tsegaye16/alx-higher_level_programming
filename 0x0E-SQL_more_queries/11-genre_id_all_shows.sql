-- joining two or more table using left join
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_shos_genre.show_id
ORDER tv_shows.title  ASC, tv_show_genres.genre_id ASC;
