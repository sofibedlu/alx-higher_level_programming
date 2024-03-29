-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record display: tv_shows.title - tv_genres.name
-- Results are sorted in ascending order by the show title and genre name
-- The database name will be passed as an argument of the mysql command

SELECT tv_shows.title, tv_genres.name
 FROM tv_shows
	LEFT JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id

	LEFT JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
 ORDER BY tv_shows.title, tv_genres.name ASC;
