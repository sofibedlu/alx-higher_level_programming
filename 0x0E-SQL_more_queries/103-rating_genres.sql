-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record display: tv_genres.name - rating sum
-- Results are sorted in descending order by their rating
-- The database name will be passed as an argument of the mysql command

SELECT t.name, SUM(rate) AS rating
FROM tv_genres AS t
INNER JOIN tv_show_genres AS g
ON t.id = g.genre_id
INNER JOIN tv_show_ratings AS r
ON g.show_id = r.show_id
GROUP BY t.name
ORDER BY rating DESC;
