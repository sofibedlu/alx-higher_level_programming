-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- Each record display: <TV Show genre> - <Number of shows linked to this genre>
-- First column called 'genre'
-- Second column called 'number_of_shows'
-- Don’t display a genre that doesn’t have any shows linked
-- Results sorted in descending order by the number of shows linked
-- The database name will be passed as an argument of the mysql command

SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC
