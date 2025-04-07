/* Check that the table doesn't already exist in the database. If it does,remove it from the database */
DROP TABLE IF EXISTS high_pop;

/* Create the table in the database & give it a name */
CREATE TABLE high_pop (

/* Tell the database which data to import, what its name in the database should be, & the type of data to import */
	energy float,
    tempo float,
	danceability float,
    loudness float,
    liveness float,
    valence float,
    track_artist text,
    time_signature int,
    speechiness float,
    track_album_name text,
    track_id text UNIQUE,
    track_name text,
    track_album_release_date date,
    instrumentalness float,
    mode boolean,
    track_key int,
    duration_ms int,
    acousticness float
);