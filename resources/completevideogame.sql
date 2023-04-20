CREATE TABLE video_game_info (
    uniqueid INT,
    name VARCHAR,
    yearreleased INT,
    genre VARCHAR,
    publisher VARCHAR,
    developer VARCHAR,
    rating VARCHAR,
    CONSTRAINT pk_video_game_info PRIMARY KEY (
        uniqueid
     )
);

CREATE TABLE video_game_sales (
    uniqueid INT,
    name VARCHAR,
    nasales FLOAT,
    eusales FLOAT,
    jpsales FLOAT,
    othersales FLOAT,
    globalsales FLOAT,
    CONSTRAINT pk_video_game_sales PRIMARY KEY (
        uniqueid
     )
);

CREATE TABLE video_game_scores (
    uniqueid INT,
    name VARCHAR,
    criticscore INT,
    criticcount INT,
    userscore FLOAT,
    usercount INT,
    CONSTRAINT pk_video_game_scores PRIMARY KEY (
        uniqueid
     )
);

ALTER TABLE video_game_sales ADD CONSTRAINT fk_video_game_sales_uniqueid FOREIGN KEY("uniqueid")
REFERENCES video_game_info ("uniqueid");

ALTER TABLE video_game_scores ADD CONSTRAINT fk_video_game_scores_uniqueid FOREIGN KEY("uniqueid")
REFERENCES video_game_info ("uniqueid");

CREATE TABLE  completevideogamedata AS
SELECT vgi.uniqueid,vgi.name, vgi.yearreleased, vgi.genre, vgi.publisher, vgi.developer, vgi.rating,
       vgs.nasales, vgs.eusales, vgs.jpsales, vgs.othersales, vgs.globalsales,vgsc.criticscore, vgsc.criticcount, vgsc.userscore, vgsc.usercount
FROM video_game_sales AS vgs JOIN video_game_info AS vgi
ON vgs.uniqueid = vgi.uniqueid
JOIN video_game_scores AS vgsc
ON vgsc.uniqueid= vgi.uniqueid

SELECT * FROM completedata

CREATE TABLE jsondata2 AS
SELECT vgi.uniqueid AS game.uniqueid, vgi.name AS game.name, vgi.yearreleased AS game.yearreleased, vgi.genre AS game.genre, vgi.publisher AS game.publisher, vgi.developer AS game.developer, 
	vgi.rating AS game.rating,vgs.nasales AS game.nasales, vgs.eusales AS game.eusales, vgs.jpsales AS game.jpsales, 
	vgs.othersales AS game.othersales, vgs.globalsales AS game.globalsales,
	vgsc.criticscore AS game.criticscore, vgsc.criticcount AS game.criticcount, vgsc.userscore AS game.userscore, vgsc.usercount AS game.usercount
FROM video_game_sales AS vgs JOIN video_game_info AS vgi
ON vgs.uniqueid = vgi.uniqueid
JOIN video_game_scores AS vgsc
ON vgsc.uniqueid= vgi.uniqueid
FOR JSON PATH, ROOT(game);

CREATE TABLE jsondata AS
SELECT row_to_json(completedata)from completedata;

SELECT * FROM jsondata

SELECT * FROM completedata

CREATE TABLE json3 AS
SELECT json_agg(row_to_json(completedata)) :: text
FROM completedata

SELECT * FROM json3


CREATE TABLE json4 AS
SELECT json_object_agg(each.genre, each.names, each.globalsales) FROM (
    SELECT genre, array_agg(name) as names FROM completedata GROUP BY genre
) AS each;