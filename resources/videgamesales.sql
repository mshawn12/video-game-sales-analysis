-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


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

SELECT * FROM video_game_scores